from supabase import create_client, Client
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

class DatabaseManager:
    def __init__(self):
        # Initializes the connection to Supabase.
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
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


    def update_lecture_note(self, lecture_id, content):
        """Deletes a lecture note linked to a course."""
        try:
            self.__supabase.table("lectures") \
                .update({"content": content}) \
                .eq("id", lecture_id) \
                .execute()
            return True
        except Exception as e:
            print(f"Error updating lecture: {e}")
            return False


    def check_lecture_exists(self, course_code, lecture_name):
        try:
            # FIX: Use limit(1) instead of maybe_single().
            # It returns a list, which is safer to check than a nullable object.
            response = self.__supabase.table("lectures") \
                .select("id") \
                .eq("course_code", course_code) \
                .eq("name", lecture_name) \
                .limit(1) \
                .execute()

            # Check if the list contains any data
            if response.data and len(response.data) > 0:
                return response.data[0]['id']
            return None

        except Exception as e:
            print(f"Error checking existence: {e}")
            return None


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
