from src.main import add, subtract, get_date

def test_add():
    assert add(10, 20) == 30
    assert add(5, 10) == 15
    assert add(25, 25) == 50
    
def test_subtract():
    assert subtract(30, 10) == 20
    assert subtract(100, 25) == 75
    
def test_get_date():
    assert str(get_date('2025-07-10 21:08:00')) == '2025-07-10'
    assert str(get_date('2024-12-12 10:10:10')) == '2024-12-12'
    