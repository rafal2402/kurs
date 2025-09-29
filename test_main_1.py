from main_1 import dodawanie, odejmowanie, dzielenie, mnozenie

def test_dodawanie():
    assert dodawanie(2, 4) == 6
    assert dodawanie(0, 4) == 4
    assert dodawanie(0, 0) == 0
    assert dodawanie(-5, 2) == -3
    assert dodawanie(-4, -2) == -6


def test_odejmowanie():
    assert odejmowanie(6, 4) == 2
    assert odejmowanie(0, -4) == 4
    assert odejmowanie(5, 5) == 0

def test_dzielenie():
    assert dzielenie(4, 2) == 2
    assert dzielenie(-4, 2) == -2
    assert dzielenie(-9, -3) == 3

def test_mnozenie():
    assert mnozenie(1, 7) == 7
    assert mnozenie(0, 100) == 0
    assert mnozenie(-4, -7) == 28
    assert mnozenie(-6, 5) == -30