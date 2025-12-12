import sys
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.append(str(root / 'src'))

from app import add, subtract, multiply, divide, square, square_root, percent, log, sin, cos

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_incorrect():
    assert add(2, 2) != 5
    assert add(-1, -1) != 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_subtract_incorrect():
    assert subtract(5, 2) != 4
    assert subtract(3, 1) != 1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_multiply_incorrect():
    assert multiply(2, 2) != 5
    assert multiply(-1, -1) != -1

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-4, 2) == -2

def test_divide_incorrect():
    assert divide(6, 2) != 4
    assert divide(9, 3) != 4

def test_square():
    assert square(4) == 16
    assert square(-3) == 9

def test_square_incorrect():
    assert square(5) != 20
    assert square(-2) != -4

def test_square_root():
    assert square_root(16) == 4
    assert square_root(9) == 3

def test_square_root_incorrect():
    assert square_root(25) != 6
    assert square_root(4) != -3

def test_percent():
    assert percent(50, 200) == 25
    assert percent(30, 150) == 20

def test_percent_incorrect():
    assert percent(50, 100) != 60
    assert percent(20, 80) != 30

def test_log():
    assert log(100, 10) == 2
    assert log(8, 2) == 3

def test_log_incorrect():
    assert log(100, 10) != 3
    assert log(16, 2) != 5

def test_sin():
    assert sin(math.pi / 2) == 1
    assert sin(0) == 0

def test_sin_incorrect():
    assert sin(math.pi) != 1
    assert sin(math.pi / 4) != 1

def test_cos():
    assert cos(0) == 1
    assert cos(math.pi) == -1

def test_cos_incorrect():
    assert cos(math.pi / 2) != 1
    assert cos(math.pi / 3) != 0

