import unittest

from utils import extract_title

class TestUtils(unittest.TestCase):
  def test_extract_title_oneline(self):
    markdown = """
# This is a title
"""
    self.assertEqual("This is a title", extract_title(markdown))

def test_extract_title_multiline(self):
    markdown = """
# This is a title

This is a subtitle
This is some content.
"""
    self.assertEqual("This is a title", extract_title(markdown))

def test_extract_title_no_title(self):
    markdown = """
This is some content.
"""
    self.assertIsNone(extract_title(markdown))

def test_extract_title_empty(self):
    markdown = ""
    self.assertIsNone(extract_title(markdown))

def test_extract_title_multiple_titles(self):
    markdown = """
# This is a title

# This is another title
This is some content.
"""
    self.assertEqual("This is a title", extract_title(markdown))