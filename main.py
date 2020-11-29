import tkinter as tk
from Alg import newtons_method


def run_calculation():
    global answer
    s1 = eq1_text.get()
    s2 = eq2_text.get()
    print('Пробуем ньютона со значениями:')
    print(s1)
    print(s2)
    answer_text = newtons_method(s1, s2)
    print(answer_text)
    answer.config(text=answer_text)
    print('\n\n')


# Создание окна
window = tk.Tk()
window.resizable(False, False)
window.title('Метод Ньютона, Кирюшкин 6314')

# Элементы интерфейса
eq1_label = tk.Label(text='Первое уравнение:')
eq1_text = tk.Entry(bg='gray90', width=30)
eq1_0 = tk.Label(text='= 0')
eq2_label = tk.Label(text='Второе уравнение:')
eq2_text = tk.Entry(bg='gray90', width=30)
eq2_0 = tk.Label(text='= 0')
run = tk.Button(text='Посчитать', command=run_calculation)
answer = tk.Label(height=5, width=50, bg='gray90', anchor='nw')

# Расположение элементов интерфейса
eq1_label.grid(row=1, column=0, sticky=tk.NW)
eq1_text.grid(row=1, column=1, sticky=tk.W + tk.E + tk.N)
eq1_0.grid(row=1, column=2, sticky=tk.N)
eq2_label.grid(row=3, column=0, sticky=tk.W + tk.N)
eq2_text.grid(row=3, column=1, sticky=tk.W + tk.E + tk.N)
eq2_0.grid(row=3, column=2, sticky=tk.N)
run.grid(row=5, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
answer.grid(row=6, column=1, columnspan=1, sticky=tk.W + tk.E + tk.N + tk.S)

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

window.mainloop()
