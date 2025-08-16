from my_project.calculator import Calculator

def test_addition():
    calculator: Calculator = Calculator(10,5)
    assert calculator.addition() == 13, 'The sum is wrong'

def test_subtraction():
    calculator: Calculator = Calculator(10,5)
    assert calculator.subtraction() == 5, 'The subtraction is wrong'

def test_multiplication():
    calculator: Calculator = Calculator(10,5)
    assert calculator.multiplication() == 50, 'The multiplication is wrong'

def test_division():
    calculator: Calculator = Calculator(10,5)
    assert calculator.division() == 2.00, 'The quotient is wrong'