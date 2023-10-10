from src.ejercicio13 import division

def test_division():
    resultado = division(13, 2)
    assert resultado == (6, 1)