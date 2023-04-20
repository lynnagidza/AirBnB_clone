#!/usr/bin/python3
"""
Unittest for console.py

To run:
$ python3 -m unittest tests/test_console.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Test the console
    """

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertEqual("", f.getvalue().strip())

    def test_eof(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
            self.assertEqual("", f.getvalue().strip())

    def test_prompt(self):
        """Test prompt"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().cmdloop()
            self.assertEqual("(hbnb) ", f.getvalue()[:7])

    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual("", f.getvalue())


if __name__ == '__main__':
    unittest.main()
