from supabase import create_client, Client
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

class DatabaseManager:
    def __init__(self, url: str, key: str):
        # Initializes the connection to Supabase.
        self.__supabase: Client = create_client(url, key)

    def get_lecture_note(self, lecture_id):
        # Fetches the md context for a specific record.
        result = self.__supabase.table("lectures") \
            .select("content") \
            .eq("id", lecture_id) \
            .single() \
            .execute()
        return result.data.get("content")


    def create_lecture_note(self, course_code, lecture_name, lecture_number, content):
        """Creates a lecture note linked to a course."""
        try:
            data = {
                "course_code": course_code,
                "name": lecture_name,
                "lecture_number": lecture_number,
                "content": content
            }
            self.__supabase.table("lectures").insert(data).execute()
            return True
        except Exception as e:
            print(f"Error creating note: {e}")
            return False

    def create_course(self, course_code, course_name):
        """Creates a course."""
        try:
            data = {
                "course_code": course_code,
                "course_name": course_name,
                "year": datetime.now().year
            }
            self.__supabase.table("courses").insert(data).execute()
            return True
        except Exception as e:
            print(f"Error creating note: {e}")
            return False

    def list_all_entries(self, table):
        """Returns all rows from a specified table."""
        result = self.__supabase.table(table).select("*").execute()
        return result.data
