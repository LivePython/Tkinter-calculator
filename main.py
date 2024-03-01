from tkinter import *
import ast
# Adding tkinter widget
root = Tk()

# Function to add number to entry
i = 0
def get_number(num):
    global i
    display.insert(i, num)
    i += 1


def get_operator(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def clear_all():
    display.delete(0, END)


def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode='eval')
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)

    except Exception:
        clear_all()
        display.insert(0,'Error')


def delete_num():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)

    else:
        clear_all()
        display.insert(0, '')

# Adding display
display = Entry(root)
display.grid(row=1, columnspan=6)

# Adding button
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=2, height=2,
                        command=lambda text=button_text: get_number(text))
        button.grid(row=x+2, column=y)
        counter += 1

button = Button(root, text="0", width=2, height=2, command=lambda: get_number(0))
button.grid(row=5, column=1)

# Adding operations
count = 0
operations = ['+', '-', '*', '/', '*3.14', '%', '(', '**', ')', '**2']
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count],
                            width=2, height=2,
                            command=lambda text=operations[count]: get_operator(text))
            count += 1
            button.grid(row=x + 2, column=y+3)

Button(root, text="AC", width=2, height=2, command=clear_all).grid(row=5, column=0)
Button(root, text="=", width=2, height=2, command=calculate).grid(row=5, column=2)
Button(root, text="<<", width=2, height=2, command=lambda: delete_num()).grid(row=5, column=4)


root.mainloop()
