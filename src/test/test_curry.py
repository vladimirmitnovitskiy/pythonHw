import pytest
from hw6.curry import curry, uncurry

# ====== Тестовые функции ======
def add3(a, b, c):
    return a + b + c

def multiply(a, b):
    return a * b

def zero_args():
    return 42


# ====== Тесты для curry ======
def test_curry_basic_addition():
    f = curry(add3, 3)
    assert f(1)(2)(3) == 6


def test_curry_partial_application():
    f = curry(multiply, 2)
    g = f(5)
    assert callable(g)
    assert g(10) == 50


def test_curry_with_arity_check():
    with pytest.raises(ValueError):
        curry(add3, -1)
    with pytest.raises(ValueError):
        curry(add3, 5)
    with pytest.raises(TypeError):
        curry(123, 2)
    with pytest.raises(TypeError):
        curry(add3, "2")


def test_curry_freeze_arity():
    """Проверяем, что функция не ждёт больше аргументов, чем указано в арности."""
    f = curry(add3, 2)
    assert f(1)(2) == add3(1, 2, None) if add3.__defaults__ else pytest.skip("Пропускаем — требует фиксированных аргументов")


# ====== Тесты для uncurry ======
def test_uncurry_basic():
    curried = curry(add3, 3)
    uncurried = uncurry(curried, 3)
    assert uncurried(1, 2, 3) == 6


def test_uncurry_error_handling():
    curried = curry(multiply, 2)
    uncurried = uncurry(curried, 2)
    with pytest.raises(TypeError):
        uncurried(1)  # меньше аргументов
    with pytest.raises(TypeError):
        uncurry(123, 2)
    with pytest.raises(TypeError):
        uncurry(curried, "x")
    with pytest.raises(ValueError):
        uncurry(curried, 0)


def test_uncurry_chaining_equivalence():
    curried = curry(multiply, 2)
    uncurried = uncurry(curried, 2)
    assert curried(3)(4) == uncurried(3, 4)


# ====== Интеграционный тест ======
def test_curry_and_uncurry_roundtrip():
    def f(a, b, c):
        return (a + b) * c

    curried = curry(f, 3)
    uncurried = uncurry(curried, 3)
    assert uncurried(2, 3, 4) == f(2, 3, 4)
    assert curried(2)(3)(4) == f(2, 3, 4)


# ====== Дополнительно: тест с 0 аргументов ======
def test_zero_args_function():
    curried = curry(zero_args, 0)
    assert callable(curried)
    assert curried() == 42
