import tkinter as tk


class MyCalc:
    def __init__(self, root: tk.Tk):
        self.window = root
        self.window.title('Калькулятор')
        self.window.resizable(False, False)

        self.window.bind('<Return>', self.handle_return_press)
        self.window.bind('<Key>', self.hanlde_key_press)

        self.temp_num = None
        self.temp_res = None
        self.oper = None

        self.initUI()

    def initUI(self):
        self.init_display()
        self.init_buttons_operations()
        self.init_buttons_numbers()
        self.settings_grid()

    def init_display(self):
        self.frame_display = tk.Frame(self.window)
        self.dial_numbers = tk.StringVar()
        self.label_display = tk.Label(self.frame_display, textvariable=self.dial_numbers, width=30, height=3)

    def init_buttons_operations(self):
        self.frame_operations_1 = tk.Frame(self.window)
        self.btn_AC = tk.Button(self.frame_operations_1, text='C', font=('Arial', 14, 'bold'), width=4, height=2, command=self.clear)
        self.btn_AB = tk.Button(self.frame_operations_1, text='n\u00B2', font=('Arial', 14, 'bold'), width=4, height=2, command=self.square)
        self.btn_AE = tk.Button(self.frame_operations_1, text='\u03C0', font=('Arial', 14, 'bold'), width=4, height=2, command=self.pi)

        self.frame_operations_2 = tk.Frame(self.window)
        self.btn_div = tk.Button(self.frame_operations_2, text='\u00F7', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.operations_add_sub_mul_div('/'))
        self.btn_mul = tk.Button(self.frame_operations_2, text='*', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.operations_add_sub_mul_div('*'))
        self.btn_sub = tk.Button(self.frame_operations_2, text='-', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.operations_add_sub_mul_div('-'))
        self.btn_add = tk.Button(self.frame_operations_2, text='+', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.operations_add_sub_mul_div('+'))
        self.btn_equals = tk.Button(self.frame_operations_2, text='=', font=('Arial', 14, 'bold'), width=4, height=2, command=self.oper_eq)

    def init_buttons_numbers(self):
        self.frame_buttons = tk.Frame(self.window)
        self.btn_1 = tk.Button(self.frame_buttons, text='1', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('1'))
        self.btn_2 = tk.Button(self.frame_buttons, text='2', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('2'))
        self.btn_3 = tk.Button(self.frame_buttons, text='3', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('3'))
        self.btn_4 = tk.Button(self.frame_buttons, text='4', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('4'))
        self.btn_5 = tk.Button(self.frame_buttons, text='5', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('5'))
        self.btn_6 = tk.Button(self.frame_buttons, text='6', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('6'))
        self.btn_7 = tk.Button(self.frame_buttons, text='7', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('7'))
        self.btn_8 = tk.Button(self.frame_buttons, text='8', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('8'))
        self.btn_9 = tk.Button(self.frame_buttons, text='9', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('9'))
        self.btn_0 = tk.Button(self.frame_buttons, text='0', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('0'))
        self.btn_dot = tk.Button(self.frame_buttons, text='.', font=('Arial', 14, 'bold'), width=4, height=2, command=lambda: self.display('.'))

    def settings_grid(self):
        self.frame_display.grid(row=0, column=0, sticky='ew', columnspan=2)
        self.label_display.grid(row=0, column=0, sticky='ew')

        self.frame_operations_1.grid(row=1, column=0)
        self.btn_AC.grid(row=0, column=0)
        self.btn_AB.grid(row=0, column=1)
        self.btn_AE.grid(row=0, column=2)

        self.frame_operations_2.grid(row=1, column=1, rowspan=2)
        self.btn_div.grid(row=0, column=0)
        self.btn_mul.grid(row=1, column=0)
        self.btn_sub.grid(row=2, column=0)
        self.btn_add.grid(row=3, column=0)
        self.btn_equals.grid(row=4, column=0)

        self.frame_buttons.grid(row=2, column=0)
        self.btn_1.grid(row=0, column=0)
        self.btn_2.grid(row=0, column=1)
        self.btn_3.grid(row=0, column=2)
        self.btn_4.grid(row=1, column=0)
        self.btn_5.grid(row=1, column=1)
        self.btn_6.grid(row=1, column=2)
        self.btn_7.grid(row=2, column=0)
        self.btn_8.grid(row=2, column=1)
        self.btn_9.grid(row=2, column=2)
        self.btn_0.grid(row=3, column=0, columnspan=2, sticky='ew')
        self.btn_dot.grid(row=3, column=2)

    def handle_return_press(self, event):
        self.oper_eq()

    def hanlde_key_press(self, event: tk.Event):
        if event.char.isdigit():
            self.display(event.char)
        elif event.char in ['+', '-', '*', '/']:
            self.operations_add_sub_mul_div(event.char)
        elif event.keysym == 'BackSpace':
            self.dial_numbers.set(self.dial_numbers.get()[:-1])

    def clear(self):
        self.temp_num = None
        self.temp_res = None
        self.oper = None
        self.dial_numbers.set('')

    def square(self):
        num = float(self.dial_numbers.get()) if '.' in self.dial_numbers.get() else int(self.dial_numbers.get())
        self.dial_numbers.set(str(num ** 2))

    def pi(self):
        self.dial_numbers.set('3.141592653589793')

    def display(self, number):
        self.dial_numbers.set(self.dial_numbers.get() + number)

    def oper_eq(self):
        if self.oper is None:
            return None

        second_num = float(self.dial_numbers.get()) if '.' in self.dial_numbers.get() else int(self.dial_numbers.get())

        if self.oper == '+':
            if self.temp_num:
                self.temp_num += second_num
                result = self.temp_num
            else:
                self.temp_res += second_num
                self.temp_num = self.temp_res
                result = self.temp_res
        elif self.oper == '-':
            if self.temp_num:
                self.temp_num -= second_num
                result = self.temp_num
            else:
                self.temp_res -= second_num
                self.temp_num = self.temp_res
                result = self.temp_res
        elif self.oper == '*':
            if self.temp_num:
                self.temp_num *= second_num
                result = self.temp_num
            else:
                self.temp_res *= second_num
                self.temp_num = self.temp_res
                result = self.temp_res
        else:
            if self.temp_num:
                try:
                    self.temp_num /= second_num
                except ZeroDivisionError:
                    result = 'Делить на 0 нельзя'
                else:
                    result = self.temp_num
            else:
                try:
                    self.temp_res /= second_num
                except ZeroDivisionError:
                    result = 'Делить на 0 нельзя'
                else:
                    self.temp_num = self.temp_res
                    result = self.temp_res

        self.dial_numbers.set(str(result))
        self.oper = '='

    def operations_add_sub_mul_div(self, operation):
        if self.oper == '=':
            self.dial_numbers.set('')
            self.temp_res = self.temp_num
            self.temp_num = None
            self.oper = operation
            return None

        try:
            second_num = float(self.dial_numbers.get()) if '.' in self.dial_numbers.get() else int(self.dial_numbers.get())
            self.dial_numbers.set('')
        except ValueError:
            return None

        if self.oper == '+':
            if self.temp_num:
                self.temp_res = self.temp_num + second_num
            else:
                self.temp_res = self.temp_res + second_num
            self.temp_num = None
            self.oper = operation
            return None

        if self.oper == '-':
            if self.temp_num:
                self.temp_res = self.temp_num - second_num
            else:
                self.temp_res = self.temp_res - second_num
            self.temp_num = None
            self.oper = operation
            return None

        if self.oper == '*':
            if self.temp_num:
                self.temp_res = self.temp_num * second_num
            else:
                self.temp_res = self.temp_res * second_num
            self.temp_num = None
            self.oper = operation
            return None

        if self.oper == '/':
            if self.temp_num:
                try:
                    self.temp_res = self.temp_num / second_num
                except ZeroDivisionError:
                    self.dial_numbers.set('Делить на 0 нельзя')
            else:
                try:
                    self.temp_res = self.temp_res / second_num
                except ZeroDivisionError:
                    self.dial_numbers.set('Делить на 0 нельзя')
            self.temp_num = None
            self.oper = operation
            return None

        self.oper = operation

        if self.temp_num is None and self.temp_res is None:
            self.temp_num = second_num
        else:
            if operation == '+':
                if self.temp_num:
                    self.temp_num = self.temp_num + second_num
                else:
                    self.temp_res = self.temp_res + second_num
            elif operation == '-':
                if self.temp_num:
                    self.temp_num = self.temp_num - second_num
                else:
                    self.temp_res = self.temp_res - second_num
            elif operation == '*':
                if self.temp_num:
                    self.temp_num = self.temp_num * second_num
                else:
                    self.temp_res = self.temp_res * second_num
            elif operation == '/':
                if self.temp_num:
                    self.temp_num = self.temp_num * second_num
                else:
                    self.temp_res = self.temp_res * second_num


if __name__ == '__main__':
    root = tk.Tk()
    application = MyCalc(root)
    root.mainloop()
