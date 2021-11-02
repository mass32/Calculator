import sqlite3 as sq
import tkinter as tk
from tkinter import ttk
import datetime as dt

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600+400+300')
        self.title('Calculator')
        #self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.connection = sq.connect('history.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS history (execution_time DATETIME, expression TEXT, result REAL)')
        self.cursor.execute('DELETE FROM history')
        self.connection.commit()

        self.output = tk.StringVar()
        self.expression_str = ''
        self.results = ''

        self.frm_output = tk.LabelFrame(master=self, text='Output:')
        self.frm_output.rowconfigure(1, weight=1)
        self.frm_output.columnconfigure(1, weight=1)
        self.frm_output.grid(row=1, column=1, sticky='nesw', padx=2, pady=2)

        self.lbl_output = tk.Entry(master=self.frm_output, textvariable=self.output, font=('Calibri', 32), width=20)
        self.lbl_output.grid(row=1, column=1, sticky='nesw', padx=2, pady=2)

        self.frm_buttons = tk.Frame(master=self)
        self.frm_buttons.columnconfigure([1, 2, 3, 4], weight=1)
        self.frm_buttons.rowconfigure([1, 2, 3, 4, 5], weight=1)
        self.frm_buttons.grid(row=2, column=1, sticky='nesw', padx=2, pady=2)

        self.btn_plus = tk.Button(master=self.frm_buttons, text='+', font=('Calibri', 32), command=lambda: self.add_to_equation('+'))
        self.btn_plus.grid(row=1, column=1, sticky='nesw', padx=2, pady=2)
        self.btn_minus = tk.Button(master=self.frm_buttons, text='-', font=('Calibri', 32), command=lambda: self.add_to_equation('-'))
        self.btn_minus.grid(row=1, column=2, sticky='nesw', padx=2, pady=2)
        self.btn_times = tk.Button(master=self.frm_buttons, text='X', font=('Calibri', 32), command=lambda: self.add_to_equation('*'))
        self.btn_times.grid(row=1, column=3, sticky='nesw', padx=2, pady=2)
        self.btn_divide = tk.Button(master=self.frm_buttons, text='/', font=('Calibri', 32), command=lambda: self.add_to_equation('/'))    
        self.btn_divide.grid(row=1, column=4, sticky='nesw', padx=2, pady=2)

        self.btn_1 = tk.Button(master=self.frm_buttons, text='1', font=('Calibri', 32), command=lambda: self.add_to_equation(1))
        self.btn_1.grid(row=2, column=1, sticky='nesw', padx=2, pady=2)
        self.btn_2 = tk.Button(master=self.frm_buttons, text='2', font=('Calibri', 32), command=lambda: self.add_to_equation(2))
        self.btn_2.grid(row=2, column=2, sticky='nesw', padx=2, pady=2)
        self.btn_3 = tk.Button(master=self.frm_buttons, text='3', font=('Calibri', 32), command=lambda: self.add_to_equation(3))
        self.btn_3.grid(row=2, column=3, sticky='nesw', padx=2, pady=2)

        self.btn_4 = tk.Button(master=self.frm_buttons, text='4', font=('Calibri', 32), command=lambda: self.add_to_equation(4))
        self.btn_4.grid(row=3, column=1, sticky='nesw', padx=2, pady=2)
        self.btn_5 = tk.Button(master=self.frm_buttons, text='5', font=('Calibri', 32), command=lambda: self.add_to_equation(5))
        self.btn_5.grid(row=3, column=2, sticky='nesw', padx=2, pady=2)
        self.btn_6 = tk.Button(master=self.frm_buttons, text='6', font=('Calibri', 32), command=lambda: self.add_to_equation(6))
        self.btn_6.grid(row=3, column=3, sticky='nesw', padx=2, pady=2)

        self.btn_7 = tk.Button(master=self.frm_buttons, text='7', font=('Calibri', 32), command=lambda: self.add_to_equation(7))
        self.btn_7.grid(row=4, column=1, sticky='nesw', padx=2, pady=2)
        self.btn_8 = tk.Button(master=self.frm_buttons, text='8', font=('Calibri', 32), command=lambda: self.add_to_equation(8))
        self.btn_8.grid(row=4, column=2, sticky='nesw', padx=2, pady=2)
        self.btn_9 = tk.Button(master=self.frm_buttons, text='9', font=('Calibri', 32), command=lambda: self.add_to_equation(9))
        self.btn_9.grid(row=4, column=3, sticky='nesw', padx=2, pady=2)

        self.btn_clear = tk.Button(master=self.frm_buttons, text='C', font=('Calibri', 32), command=self.clear)
        self.btn_clear.grid(row=5, column=1, sticky='nesw', padx=2, pady=2)
        self.btn_0 = tk.Button(master=self.frm_buttons, text='0', font=('Calibri', 32), command=lambda: self.add_to_equation(0))
        self.btn_0.grid(row=5, column=2, sticky='nesw', padx=2, pady=2)
        self.btn_decimal = tk.Button(master=self.frm_buttons, text='.', font=('Calibri', 32), command=lambda: self.add_to_equation('.'))
        self.btn_decimal.grid(row=5, column=3, sticky='nesw', padx=2, pady=2)

        self.btn_equals = tk.Button(master=self.frm_buttons, text='=', font=('Calibri', 32), command=self.calculate)
        self.btn_equals.grid(row=2, column=4, rowspan=4, sticky='nesw', padx=2, pady=2)

        self.frm_history = tk.Frame(master=self, bg='purple')
        self.frm_history.rowconfigure(1, weight=1)
        self.frm_history.columnconfigure(1, weight=1)
        self.frm_history.grid(row=1, column=2, rowspan=2, sticky='nesw', padx=2, pady=2)

        self.lstbox_history = tk.Listbox(master=self.frm_history)
        self.lstbox_history.grid(row=1, column=1, sticky='nesw', padx=2, pady=2)
        self.populate_history()
        self.lstbox_history.bind('<<ListboxSelect>>', self.selected_history)

    def add_to_equation(self, char):
        self.expression_str += str(char)
        self.output.set(self.expression_str)

    def calculate(self):
        try:
            self.result = str(eval(self.expression_str))
            self.output.set(self.result)
            insert_time = dt.datetime.today()
            self.cursor.execute('INSERT INTO history VALUES (?, ?, ?)', (insert_time, self.expression_str, float(self.result)))
            self.connection.commit()
            self.expression_str = ''
            self.lstbox_history.delete(0, 'end')
            self.populate_history()
        except Exception as e:
            print(e)
            self.output.set('Error')
            self.expression_str = ''

    def selected_history(self, event):
        selection = self.lstbox_history.get(self.lstbox_history.curselection())
        words = selection.split(' = ')
        equation = words[0]
        result = words[1]
        self.output.set(equation)
        self.expression_str = equation
    
    def populate_history(self):
        for x in self.cursor.execute('SELECT * FROM history LIMIT 100'):
            insert = str(x[1])+' = '+str(x[2])
            self.lstbox_history.insert('end', insert)

    def clear(self):
        self.expression_str = ''
        self.output.set('')


if __name__ == '__main__':
    calc_app = CalculatorApp()
    calc_app.mainloop()