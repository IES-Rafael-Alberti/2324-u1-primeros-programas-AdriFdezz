from src.ejercicio1 import bienvenida

def test_bienvenida():
    resultado = bienvenida("Adri")
    assert resultado == "Hola, Adri."