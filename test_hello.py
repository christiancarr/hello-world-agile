import sys
from io import StringIO
import hello

def test_main():
    captured_output = StringIO()
    sys.stdout = captured_output
    hello.main()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Hello, World!"
