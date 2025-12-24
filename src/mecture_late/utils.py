from pathlib import Path
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import re
load_dotenv()
gemini_key = os.getenv("GEMINI_KEY")

# Input: folder path
# Output: array of paths from the pdf files in the folder
def get_pdf_paths_from_folder(folder_path):
    # Define the directory path
    files = [pdf_file for pdf_file in folder_path.glob("*.pdf")]
    return files


# Input: Lecture slide pdf file path
# Output: Lecture notes written in markdown as a string
def get_response(filepath):
    client = genai.Client(api_key=gemini_key)

    prompt = "Generate notes in enough detail for exam revision for university students. They should be in markdown format."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(
                data=Path(filepath).read_bytes(),
                mime_type='application/pdf',
            ),
            prompt])
    print(response.text)
    return response.text


# Input: original_file_name - .pdf, content to go in the file
# Output: Write
def write_string_to_md(lecture_name, content):
    folder_path = Path("output/")
    new_path = folder_path / (lecture_name + ".md")
    try:
        with open(new_path, "w") as f:
            f.write(content)
        print(f"Successfully created {new_path}")
        return True
    except FileExistsError:
        print(f"Error: The file '{new_path}' already exists. No data was written.")
        return False


# Input: Path to lecture pdf
# Output: Name of the lecture (e.g. iads11heaps0)
def get_lecture_name(lecture_path):
    lecture_name = Path(lecture_path).stem
    return lecture_name


def get_lecture_number(lecture_name):
    # 1. Find all sequences of digits in the string
    numbers = re.findall(r'\d+', lecture_name)

    # 2. Check each number found
    for num_str in numbers:
        value = int(num_str)
        # 3. Apply your "cap" logic
        if value <= 50:
            return value

    return None  # Return None if no valid number is found


