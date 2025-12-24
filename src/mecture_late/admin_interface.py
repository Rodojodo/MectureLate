import streamlit as st
import os
import shutil
from pathlib import Path
from database_manager import DatabaseManager
from utils import get_response, get_lecture_name, get_lecture_number, write_string_to_md


def save_uploaded_file(uploaded_file, save_dir):
    """Saves uploaded file from RAM to disk so Gemini can read it."""
    file_path = os.path.join(save_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path


def run_admin_interface():
    st.title("🚀 AI Note Generator")

    db = DatabaseManager()

    # --- 1. COURSE SELECTION / CREATION ---
    st.subheader("1. Target Course")

    col1, col2 = st.columns([1, 2])
    with col1:
        course_code = st.text_input("Course Code", value="", placeholder="e.g. CS101").strip().upper()

    # Logic: Check if course exists
    course_exists = False
    if course_code:
        # Fetch all courses to check existence (You could optimize this with a specific DB query later)
        all_courses = db.list_all_entries("courses")
        # Find if any course matches the code
        matching_course = next((c for c in all_courses if c['course_code'] == course_code), None)

        if matching_course:
            course_exists = True
            with col2:
                st.success(f"✅ Found: **{matching_course['course_name']}**")
        else:
            with col2:
                st.warning(f"⚠️ Course '{course_code}' not found.")

            # Show creation form immediately
            with st.expander(f"➕ Create Course: {course_code}", expanded=True):
                new_course_name = st.text_input("Course Name", placeholder="e.g. Intro to Computer Science")
                if st.button("Create Course"):
                    if new_course_name:
                        success = db.create_course(course_code, new_course_name)
                        if success:
                            st.success(f"Created {course_code}!")
                            st.rerun()  # Refresh so the check passes
                        else:
                            st.error("Failed to create course.")
                    else:
                        st.error("Please enter a course name.")

    st.divider()

    # --- 2. UPLOAD & PROCESS ---
    st.subheader("2. Upload Slides")

    # Disable the rest of the interface if course is invalid
    if not course_exists:
        st.info("👆 Please select or create a valid course above to continue.")
        return

    col1, col2 = st.columns(2)
    with col1:
        uploaded_files = st.file_uploader("Upload PDF Slides", type=["pdf"], accept_multiple_files=True)
    with col2:
        overwrite = st.checkbox("Overwrite existing notes?", value=False,
                                help="If checked, AI will regenerate notes even if they already exist in the DB.")

    if st.button("Generate & Save", type="primary", disabled=(not uploaded_files)):

        # Setup temp storage
        temp_dir = "temp_processing"
        os.makedirs(temp_dir, exist_ok=True)

        # UI Container for live updates
        status_box = st.status("Starting processing...", expanded=True)
        progress_bar = status_box.progress(0)

        try:
            total_files = len(uploaded_files)
            for i, up_file in enumerate(uploaded_files):

                # A. Save to temp disk
                status_box.write(f"📂 Reading **{up_file.name}**...")
                file_path = save_uploaded_file(up_file, temp_dir)

                # B. Extract Metadata
                lecture_name = get_lecture_name(file_path)
                lecture_num = get_lecture_number(lecture_name)

                # C. Check DB for existing note
                existing_id = db.check_lecture_exists(course_code, lecture_name)

                if existing_id and not overwrite:
                    status_box.warning(f"⚠️ Skipped **{lecture_name}** (Exists in DB)")
                else:
                    status_box.write(f"🤖 Generating AI notes for: {lecture_name}...")
                    try:
                        # D. AI Generation
                        markdown_content = get_response(file_path)

                        # E. Save to Supabase
                        if existing_id:
                            db.update_lecture_note(existing_id, markdown_content)
                            status_box.success(f"✅ Updated **{lecture_name}**")
                        else:
                            db.create_lecture_note(course_code, lecture_name, lecture_num, markdown_content)
                            status_box.success(f"✅ Created **{lecture_name}**")

                        # Optional: Local Backup
                        write_string_to_md(lecture_name, markdown_content)

                    except Exception as e:
                        status_box.error(f"❌ Error processing {lecture_name}: {e}")

                # Update Progress
                progress_bar.progress((i + 1) / total_files)

            status_box.update(label="All tasks completed!", state="complete", expanded=False)

        finally:
            # Cleanup temp files
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)


if __name__ == "__main__":
    run_admin_interface()