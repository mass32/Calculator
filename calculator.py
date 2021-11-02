import sqlite3 as sq
import tkinter as tk
from tkinter import ttk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600+400+300')
        self.title('Calculator')
        #self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.expression = 0
        self.expression_str = ''

        self.frm_output = tk.LabelFrame(master=self, text='Output:')
        self.frm_output.rowconfigure(1, weight=1)
        self.frm_output.columnconfigure(1, weight=1)
        self.frm_output.grid(row=1, column=1, sticky='nesw', padx=2, pady=2)

        self.lbl_output = tk.Label(master=self.frm_output, text=self.expression_str, height=3, width=20)
        self.lbl_output.grid(row=1, column=1, sticky='nesw', padx=2, pady=2)

        self.frm_buttons = tk.Frame(master=self)
        self.frm_buttons.columnconfigure([1, 2, 3, 4], weight=1)
        self.frm_buttons.rowconfigure([1, 2, 3, 4, 5], weight=1)
        self.frm_buttons.grid(row=2, column=1, sticky='nesw', padx=2, pady=2)

        self.btn_plus = tk.Button(master=self.frm_buttons, text='+')
        self.btn_plus.grid(row=1, column=1, sticky='nesw', padx=2, pady=2)
        self.btn_minus = tk.Button(master=self.frm_buttons, text='-')
        self.btn_minus.grid(row=1, column=2, sticky='nesw', padx=2, pady=2)
        self.btn_times = tk.Button(master=self.frm_buttons, text='X')
        self.btn_times.grid(row=1, column=3, sticky='nesw', padx=2, pady=2)
        self.btn_divide = tk.Button(master=self.frm_buttons, text='%')    
        self.btn_divide.grid(row=1, column=4, sticky='nesw', padx=2, pady=2)

        self.btn_1 = tk.Button(master=self.frm_buttons, text='1')
        self.btn_1.grid(row=2, column=1, sticky='nesw', padx=2, pady=2)
        self.btn_2 = tk.Button(master=self.frm_buttons, text='2')
        self.btn_2.grid(row=2, column=2, sticky='nesw', padx=2, pady=2)
        self.btn_3 = tk.Button(master=self.frm_buttons, text='3')
        self.btn_3.grid(row=2, column=3, sticky='nesw', padx=2, pady=2)

        self.btn_4 = tk.Button(master=self.frm_buttons, text='4')
        self.btn_4.grid(row=3, column=1, sticky='nesw', padx=2, pady=2)
        self.btn_5 = tk.Button(master=self.frm_buttons, text='5')
        self.btn_5.grid(row=3, column=2, sticky='nesw', padx=2, pady=2)
        self.btn_6 = tk.Button(master=self.frm_buttons, text='6')
        self.btn_6.grid(row=3, column=3, sticky='nesw', padx=2, pady=2)

        self.btn_7 = tk.Button(master=self.frm_buttons, text='7')
        self.btn_7.grid(row=4, column=1, sticky='nesw', padx=2, pady=2)
        self.btn_8 = tk.Button(master=self.frm_buttons, text='8')
        self.btn_8.grid(row=4, column=2, sticky='nesw', padx=2, pady=2)
        self.btn_9 = tk.Button(master=self.frm_buttons, text='9')
        self.btn_9.grid(row=4, column=3, sticky='nesw', padx=2, pady=2)

        self.btn_clear = tk.Button(master=self.frm_buttons, text='C')
        self.btn_clear.grid(row=5, column=1, sticky='nesw', padx=2, pady=2)
        self.btn_0 = tk.Button(master=self.frm_buttons, text='0')
        self.btn_0.grid(row=5, column=2, sticky='nesw', padx=2, pady=2)
        self.btn_decimal = tk.Button(master=self.frm_buttons, text='.')
        self.btn_decimal.grid(row=5, column=3, sticky='nesw', padx=2, pady=2)

        self.btn_equals = tk.Button(master=self.frm_buttons, text='=')
        self.btn_equals.grid(row=2, column=4, rowspan=4, sticky='nesw', padx=2, pady=2)

        self.frm_history = tk.Frame(master=self, bg='purple')
        self.frm_history.rowconfigure(1, weight=1)
        self.frm_history.columnconfigure(1, weight=1)
        self.frm_history.grid(row=1, column=2, rowspan=2, sticky='nesw', padx=2, pady=2)

        self.lstbox_history = tk.Listbox(master=self.frm_history)
        self.lstbox_history.grid(row=1, column=1, sticky='nesw', padx=2, pady=2)


if __name__ == '__main__':
    calc_app = CalculatorApp()
    calc_app.mainloop()