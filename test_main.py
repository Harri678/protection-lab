import unittest
from io import StringIO
from contextlib import redirect_stdout
from main import Hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        output = StringIO()
        with redirect_stdout(output):
            Hello()
        self.assertEqual(output.getvalue(), "Hello world\n")

if __name__ == "__main__":
    unittest.main()
