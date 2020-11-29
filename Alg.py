import numpy as np
from sympy import sympify, Symbol, diff

max_steps = 1000  # Максимум шагов приближения
converging_amount = 1e-5  # Достаточная близость к нулю
x = Symbol('x')
y = Symbol('y')


# Считает Jn
def Jacobian(jacobian, guess):
    jn00 = float(jacobian[0][0].evalf(subs={x: guess[0], y: guess[1]}))
    jn01 = float(jacobian[0][1].evalf(subs={x: guess[0], y: guess[1]}))
    jn10 = float(jacobian[1][0].evalf(subs={x: guess[0], y: guess[1]}))
    jn11 = float(jacobian[1][1].evalf(subs={x: guess[0], y: guess[1]}))
    return [[jn00, jn01], [jn10, jn11]]


# Считает Fn
def Function(functions, x, y):
    function1 = float(functions[0].evalf(subs={'x': x, 'y': y}))
    function2 = float(functions[1].evalf(subs={'x': x, 'y': y}))
    return [function1, function2]


# Метод Ньютона
def newtons_method(s1, s2):
    try:
        steps = 0
        # Перевод строк в функции библиотеки SymPy
        f1 = sympify(s1)
        f2 = sympify(s2)
        functions = [f1, f2]
        jac = [[diff(functions[0], x), diff(functions[0], y)],
               [diff(functions[1], x), diff(functions[1], y)]]  # Нахождение якобиана
        guess = [1, 2]  # Первоначальное предположение
        while steps <= max_steps:  # Цикл приближения
            Y = np.array(Function(functions, guess[0], guess[1]))  # Значение функций в точке
            J = np.array(Jacobian(jac, guess))  # Якобиан в точке
            dx = np.linalg.solve(J, -Y)
            guess += dx
            if np.linalg.norm(dx) < converging_amount:  # break если достаточно близко
                break
            steps += 1
        return 'Приближение корня уравнения:\nx={x}\ny={y}'.format(x=guess[0], y=guess[1])
    except:
        return 'Невозможно выполнить операцию\nПроверьте правильность введения уравнений'
