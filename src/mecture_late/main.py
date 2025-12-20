import os
from pathlib import Path

from src.mecture_late.utils import get_pdf_paths_from_folder, get_response, write_string_to_md, get_lecture_name


def generate_notes_for_all_lectures(folder_path):
    lecture_paths = get_pdf_paths_from_folder(folder_path)
    for lecture_path in lecture_paths:
        lecture_name = get_lecture_name(lecture_path)
        output_path = Path("output/" + lecture_name + ".md")
        if output_path.exists():
            preference = input(
            f"""
            {lecture_name} " already has lecture notes. Would you like to skip it? (Y/n)""")
            if preference in ["n", "N", "no", "No"]:
                lecture_notes = get_response(lecture_path)
                os.remove(output_path)
                write_string_to_md(lecture_name, lecture_notes)
        else:
            lecture_notes = get_response(lecture_path)
            write_string_to_md(lecture_name, lecture_notes)
