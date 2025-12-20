import unittest
from pathlib import Path
from unittest.mock import patch

from src.mecture_late.main import generate_notes_for_all_lectures


class TestMain(unittest.TestCase):
    # Use setUpClass to prepare data once for all tests in this class
    @classmethod
    def setUpClass(cls):
        cls.folder_path = Path("rsc/test_files/test_slides")
        cls.output_path = Path("output/")

    @patch('src.mecture_late.main.get_response')
    def test_generate_notes_flow(self, mock_get):
        """This is the main test that handles the API mocking"""
        # 1. Setup the mock response
        mock_get.return_value = """# Mock Lecture Notes\n## Summary\nComplexity is $O(n)$..."""

        # 2. Run the function
        generate_notes_for_all_lectures(self.folder_path)

        # 3. Collect produced files
        files = list(self.output_path.glob("*.md"))

        # 4. Run Assertions
        self.assertTrue(len(files) > 0, "No markdown files were created.")
        self.assertEqual(len(files), 16, f"Expected 16 files, but found {len(files)}")

        for file in files:
            self.assertTrue(file.is_file())
            with open(file) as f:
                content = f.readlines()
                # Check that the file isn't just a header
                self.assertTrue(len(content) > 0, f"File {file.name} is empty")


if __name__ == '__main__':
    unittest.main()