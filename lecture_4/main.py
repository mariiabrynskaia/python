def test_positive():
    assert nod(10, 5) == 5, "nod(10, 5) should be 5"
    assert nod(10, 50) == 10, "nod(10, 50) should be 10"
    assert nod(15, 27) == 3, "nod(15, 27) should be 3"
    assert nod(6, 14) == 2, "nod(6, 14) should be 2"
    assert nod(150, 120) == 30, "nod(150, 120) should be 30"
    assert nod(17, 120) == 1, "nod(17, 120) should be 1"
    assert nod(17, 17) == 17, "nod(17, 17) should be 17"


def test_negative():
    assert nod(0, 5) == 0, "Testing 0 failed..."
    assert nod(3, 0) == 0, "Testing 0 failed..."
    assert nod(0, 0) == 0, "Testing 0 failed..."
    assert nod(1, 0) == 0, "Testing 0 failed..."
    assert nod(0, 1) == 0, "Testing 0 failed..."
    assert nod(-1, 1) == 0, "Testing negative failed..."
    assert nod(-17, 17) == 0, "Testing negative failed..."
    assert nod(-22, -25) == 0, "Testing negative failed..."
    assert nod(0.5, 0.5) == 0, "Testing not natural failed..."
    assert nod(1, 0.5) == 0, "Testing not natural failed..."
    assert nod(10, 0.5) == 0, "Testing not natural failed..."
    assert nod(10.7, 355) == 0, "Testing not natural failed..."


def nod (a: int, b: int):
    if a <= 0 or b <=0 or int(a) != a or int(b) != b:
        return 0
    else:
        while a - b != 0 or b - a != 0:
            if a >= b:
                a = a - b
            elif b >= a:
                b = b - a
    return a


if __name__ == "__main__":
    test_positive()
    test_negative()
    print("Everything passed")
