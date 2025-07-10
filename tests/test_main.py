from src.main import add, subtract

def test_add():
    assert add(10, 20) == 30
    assert add(5, 10) == 15
    assert add(25, 25) == 50
    
def test_subtract():
    assert subtract(30, 10) == 20
    assert subtract(100, 25) == 75
    