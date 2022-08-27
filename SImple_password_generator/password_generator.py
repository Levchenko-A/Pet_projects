from random import randint, choice
import tkinter
import sys
import pyperclip


def copy_pass():
    '''copy created password to clipboard'''
    text = text_password.get()
    if len(text) == 0 or text == "Enter the password`s length":
        return text_password.insert(0, "You need to generate a password before copying")
    else:
        return pyperclip.copy(text)


def generate_password():
    '''generates password using ascii-codes and random module'''
    length = text_len.get()
    if len(length) == 0:
        result = "Enter the password`s length"
    else:
        length = int(length)
        result = ''
        symbols_vars = ["low", "up", "num", "sym"]
        i = 0
        while i < length:
            symbol_type = choice(symbols_vars)
            if symbol_type == "low":
                result += chr(randint(97, 122))
            elif symbol_type == "up":
                result += chr(randint(65, 90))
            elif symbol_type == "num":
                result += chr(randint(48, 57))
            else:
                result += chr(
                    choice([randint(33, 47), randint(58, 64), randint(91, 96), randint(123, 126)]))
            i += 1
    text_password.delete(0, tkinter.END)
    return text_password.insert(0, result)


def exit_app():
    '''close app'''
    return sys.exit()


tk = tkinter.Tk()
tk.title("Password generator")
tk.resizable(False, False)
tk.wm_attributes('-topmost', 1)

canvas = tkinter.Canvas(tk, width=375, height=125)
canvas.pack()

button_generate = tkinter.Button(tk, text="Generate new password", command=generate_password)
button_generate.place(x=20, y=75)

button_copy = tkinter.Button(tk, text="Copy password", command=copy_pass)
button_copy.place(x=170, y=75)

button_close = tkinter.Button(tk, text="Exit", command=exit_app, width=10)
button_close.place(x=275, y=75)

text_len = tkinter.Entry(width=15)
text_len.place(x=10, y=12.5)

text_password = tkinter.Entry(width=50)
text_password.place(x=10, y=37.5)

label = tkinter.Label(tk, text="Please, input the password`s length")
label.place(x=120, y=10)

tk.mainloop()
