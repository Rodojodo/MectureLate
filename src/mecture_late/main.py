import os
from pathlib import Path
from .database_manager import DatabaseManager
from .utils import get_pdf_paths_from_folder, get_response, write_string_to_md, get_lecture_name, get_lecture_number
import streamlit as st


def main():
    """CLI entry point with default paths"""
    input_dir = Path("rsc/input_slides")
    # Ensure output dir exists
    Path("output").mkdir(exist_ok=True)

    st.status(f"🚀 Starting MectureLate on folder: {input_dir}")
    generate_notes_for_all_lectures(input_dir)


def generate_notes_for_all_lectures(folder_path):
    lecture_paths = get_pdf_paths_from_folder(folder_path)
    course_code = input("Please enter the course code: ")
    course_name = input("Please enter the course name: ")
    db_manager = DatabaseManager()
    db_manager.create_course(course_code, )
    for lecture_path in lecture_paths:
        lecture_name = get_lecture_name(lecture_path)
        lecture_number = get_lecture_number(lecture_name)
        output_path = Path("output/" + lecture_name + ".md")

        # Check if lecture already exists in database, if so, get lecture_id
        lecture_id = db_manager.check_lecture_exists(course_code, lecture_name)
        if output_path.exists() or (lecture_id is not None):
            preference = input(
            f"""
            {lecture_name} " already has lecture notes. Would you like to skip it? (Y/n)""")
            if preference in ["n", "N", "no", "No"]:
                lecture_notes = get_response(lecture_path)
                os.remove(output_path)
                write_string_to_md(lecture_name, lecture_notes)
                db_manager.update_lecture_note(lecture_id, lecture_notes)
        else:
            lecture_notes = get_response(lecture_path)
            write_string_to_md(lecture_name, lecture_notes)
            db_manager.create_lecture_note(course_code, lecture_name, lecture_number, lecture_notes)




if __name__ == "__main__":
    main()