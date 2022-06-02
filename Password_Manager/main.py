import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.showerror(title="Website", message="Please don't leave any fields empty!")
        return

    if len(password) == 0:
        messagebox.showerror(title="Password", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                  f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as save_data:
            save_data.write(f"{website} | {email} | {password} |\n")
            website_entry.delete(0, "end")
            email_entry.delete(0, "end")
            email_entry.insert(0, "EMAIL HERE")
            password_entry.delete(0, "end")





# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = tk.Canvas(width=200,height=200, bg="white", highlightthickness=0)
password_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:", bg="white", font=("arial", 10, "bold"))
website_label.grid(row=1, column=0)

email_label = tk.Label(text="Email/Username:", bg="white", font=("arial", 10, "bold"))
email_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:", bg="white", font=("arial", 10, "bold"))
password_label.grid(row=3, column=0)

add_button = tk.Button(text="Add", highlightthickness=0, width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

website_entry = tk.Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()


email_entry = tk.Entry(width=50)
email_entry.grid(row=2, columnspan=2, column=1)
email_entry.insert(0,"EMAIL HERE")

password_entry = tk.Entry(width=32)
password_entry.grid(row=3, column=1)

generate_password_button = tk.Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_button.grid(row=3, column=2)





window.mainloop()

