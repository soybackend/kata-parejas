from unittest import TestCase
from StringProcessor import StringProcessor

class TestStringProcessor(TestCase):
    def test_process_string_empty(self):
        self.assertEqual(StringProcessor().process(""), [0], "String Empty")
