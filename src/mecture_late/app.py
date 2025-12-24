import streamlit as st
from database_manager import DatabaseManager
# from mecture_late.admin_interface import run_admin_interface
#
# --- 1. SETUP & CACHING ---
st.set_page_config(page_title="Lecture Notes", layout="wide")


# We use @st.cache_resource for the DatabaseManager because it holds
# the connection object. We don't want to recreate it on every rerun.
@st.cache_resource
def get_manager():
    return DatabaseManager()


db = get_manager()
#
# # --- 2. SIDEBAR (Navigation) ---
# st.sidebar.title("Navigation")
# # Let users filter by course immediately
# courses = db.list_all_entries("courses")
# course_options = {c['course_code']: c['course_name'] for c in courses}
#
# selected_course_code = st.sidebar.selectbox(
#     "Select Course",
#     options=list(course_options.keys()),
#     format_func=lambda x: f"{x} - {course_options[x]}"
# )
#
# # --- 3. MAIN UI ---
# tab1, tab2, tab3 = st.tabs(["Read Notes", "Manual Entry", "PDF Uploader"])
#
# # === TAB 1: READ NOTES ===
# with tab1:
#
#
# # === TAB 2: CREATE NOTE ===
# with tab2:
#     st.header("Add New Lecture Note")
#
#     with st.form("new_note_form"):
#         c_code = st.selectbox("Course", options=list(course_options.keys()))
#         l_num = st.number_input("Lecture Number", min_value=1, step=1)
#         l_name = st.text_input("Lecture Topic/Name")
#         l_content = st.text_area("Content (Markdown supported)", height=200)
#
#         submitted = st.form_submit_button("Create Note")
#
#         if submitted:
#             # Check if exists
#             if db.check_lecture_exists(c_code, l_name):
#                 st.error("A lecture with this name already exists for this course.")
#             else:
#                 success = db.create_lecture_note(c_code, l_name, l_num, l_content)
#                 if success:
#                     st.success("Note created successfully!")
#                 else:
#                     st.error("Failed to create note.")
#
# # === TAB 3: UPLOAD NOTES FOR PROCESSING ===
# with tab3:
#     run_admin_interface()



import streamlit as st
from admin_interface import run_admin_interface
# ... import other pages ...

st.set_page_config(layout="wide")

# Sidebar Navigation
page = st.sidebar.radio("Go to", ["Read Notes", "Admin Upload"])

courses = db.list_all_entries("courses")
course_options = {c['course_code']: c['course_name'] for c in courses}

selected_course_code = st.sidebar.selectbox(
    "Select Course",
    options=list(course_options.keys()),
    format_func=lambda x: f"{x} - {course_options[x]}"
)

if page == "Read Notes":

    st.header(f"Notes for {selected_course_code}")

    # 1. Get all notes (we need to filter by course in Python or add a DB method)
    # ideally, add a method: get_notes_by_course(course_code) to your class.
    # For now, we fetch all and filter here (slower, but works for starting).
    all_lectures = db.list_all_entries("lectures")
    course_lectures = [l for l in all_lectures if l['course_code'] == selected_course_code]

    if not course_lectures:
        st.info("No notes found for this course.")
    else:
        # Sort by lecture number
        course_lectures.sort(key=lambda x: x['lecture_number'])

        for lecture in course_lectures:
            with st.expander(f"Lecture {lecture['lecture_number']}: {lecture['name']}"):
                # View Mode
                st.markdown(lecture['content'])

                # Edit Button logic
                if st.button("Edit", key=f"edit_{lecture['id']}"):
                    st.session_state['edit_note_id'] = lecture['id']
                    st.session_state['edit_content'] = lecture['content']
                    st.rerun()

    # --- EDITING MODAL (Simple implementation) ---
    if 'edit_note_id' in st.session_state:
        st.markdown("---")
        st.subheader("Editing Mode")
        new_content = st.text_area("Update Content", value=st.session_state['edit_content'], height=300)

        col1, col2 = st.columns([1, 10])
        if col1.button("Save"):
            db.update_lecture_note(st.session_state['edit_note_id'], new_content)
            st.success("Updated!")
            del st.session_state['edit_note_id']  # Exit edit mode
            st.rerun()
        if col2.button("Cancel"):
            del st.session_state['edit_note_id']
            st.rerun()
elif page == "Admin Upload":
    run_admin_interface()