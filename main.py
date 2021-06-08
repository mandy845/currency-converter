from tkinter import *
import requests
from tkinter import messagebox

windows = Tk()
windows.title("CURRENCY CONVERTOR")
windows.geometry("500x500")
windows.config(bg='pink')

# API
url = "https://v6.exchangerate-api.com/v6/52f23c7db09d54899cbe4221/latest/USD"

req = requests.get(url)

result = req.json()
print(result)
rates = result['conversion_rates'].keys()


# function
def convertor():

    amount = float(amount_entry.get())

    new_amnt = amount * result['conversion_rates'][lst.get(ACTIVE)] # converting currency

    answer['text'] = new_amnt

def exit():
    mgbox = messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        windows.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")


def clear_entry():
        reset_btn.delete(0, 'end')
        reset_btn.delete(0, 'end')


# Labels
l1_convertor = Label(windows, text="Currency Convertion", bg="green", fg="black", font=("bold", 12))
l1_convertor.place(x = 150, y =3)

amount = Label(text="Amount:", bg="green", fg="black", font=("bold", 12))
amount.place(x = 100, y = 60)

# Entry
amount_entry = Entry(windows)
amount_entry.place(x= 180, y = 60)

# Label
crrncy1 = Label(text="To Currency:", bg="green", fg="black", font=("bold", 12))
crrncy1.place(x= 60, y =90)

# function
lst = Listbox(windows, width=20)
for i in rates:
    lst.insert(END, str(i))
    lst.place(x =180, y=85)

# button
btn = Button(windows, text="Convertor", bg='green', command=convertor, borderwidth=5)
btn.place(x = 180, y = 280)

reset_btn = Button(windows, text='clear', bg='green', command=clear_entry, borderwidth=5)
reset_btn.place(x= 300, y = 280)

exit_btn = Button(windows, text='Exit', bg='green', command=exit, borderwidth = 5)
exit_btn.place(x= 300, y= 330)


# Label
answer = Label(windows, font=('bold', 12))
answer.place(x = 180, y = 350)


windows.mainloop()