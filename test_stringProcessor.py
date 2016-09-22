from unittest import TestCase
from StringProcessor import StringProcessor

class TestStringProcessor(TestCase):
    def test_process_string_empty(self):
        self.assertEqual(StringProcessor().process(""), [0], "String Empty")

    def test_process_string_with_one_number(self):
        self.assertEqual(StringProcessor().process("1"), [1], "One Number Sent")

    def test_process_string_with_two_numbers(self):
        self.assertEqual(StringProcessor().process("1,2"), [2], "Two Numbers Sent")