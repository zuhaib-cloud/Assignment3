import pytest  
from src.area import calculate_area_square  
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])
def test_calculate_area_square_student_id():
    # Test for correct calculation (area = 21)
    side_length = 5  # changed for failiure
    expected_area = 21
    assert calculate_area_square(side_length) == pytest.approx(expected_area)