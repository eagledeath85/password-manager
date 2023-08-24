import os
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

# read website, email/username, password
# create a data.txt file if not exist
# format data to save according to expected format: website,email/username,password
# append formatted data to file
# save file
# clear all fields in the app

def read_text():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()


    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message=f"Website and/or Password information cannot be empty")

    else:
         write_text_to_file(website, username, password)


def write_text_to_file(website, username, password):
    data_file_path = os.path.join(os.path.dirname(__file__), 'data_file.json')
    # result = f'{website},{username},{password}\n'
    # if not os.path.exists(data_file_path):
    #     categories = f'website,email/username,password\n'
    # with open(data_file.json, 'w') as data_file:
    #     data_file.write(categories)
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }
    try:
        with open('data.json', 'r') as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        # Updating old data with new_data
        data.update(new_data)

        with open('data.json', 'w', encoding='utf-8', newline='') as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)    # indent param allows the json file to be human readable
    finally:
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Creating canvas in the window
canvas = Canvas(width=200, height=200, highlightthickness=0)

# Creating the image to put in the canvas
locker_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_image)  # Placing the image approx at the center of the canvas
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=read_text)
add_button.grid(row=4, column=1, columnspan=2)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # Put the cursor inside this entry

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


window.mainloop()
