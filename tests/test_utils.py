import unittest
from pathlib import Path
from unittest import TestCase
from src.mecture_late import utils

if __name__ == '__main__':
    unittest.main()

class Test_get_pdf_paths_from_folder(TestCase):
    folder_path = Path("rsc/test_slides")
    names = utils.get_pdf_paths_from_folder(folder_path)
    def test_got_all_pdfs(self):
        self.assertEqual(16, len(self.names))
    def test_all_pdfs_exist_and_real(self):
        for filepath in self.names:
            self.assertTrue(filepath.exists())
            self.assertTrue(filepath.is_file())

# class Test_get_response(TestCase):
#     test_lecture = Path("rsc/test_slides/iads2526-lecture4.pdf")
#     response = utils.get_response(test_lecture)
#     print(response)
#     def test_response_exist(self):
#         self.assertTrue(self.response is not None)
#         self.assertGreater(len(self.response), 50) # Just to make sure its not a one liner or anything