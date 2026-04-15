from simple_math import SimpleMath
import pytest


@pytest.fixture
def simple_math():
    return SimpleMath()


def test_square_positive_numbers(simple_math):
    assert simple_math.square(2) == 4

def test_square_negative_numbers(simple_math):
    assert simple_math.square(-2) == 4

def test_square_zero_numbers(simple_math):
    assert simple_math.square(0) == 0

def test_cube_positive_numbers(simple_math):
    assert simple_math.cube(2) == 8

def test_cube_negative_numbers(simple_math):
    assert simple_math.cube(-2) == -8

def test_zero_negative_numbers(simple_math):
    assert simple_math.cube(0) == 0