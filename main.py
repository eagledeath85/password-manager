from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
    #TODO On click Add button do:
        # read website, email/username, password
        # create a data.txt file if not exist
        # format data to save according to expected format: website,email/username,password
        # append formatted data to file
        # save file
        # clear all fields in the app

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Creating canvas in the window
canvas = Canvas(width=200, height=200, highlightthickness=0)

# Creating the image to put in the canvas
locker_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_image)   # Placing the image approx at the center of the canvas
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)


# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()   # Put the cursor inside this entry

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

window.mainloop()
