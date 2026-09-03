from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_enter.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
   site =  website_enter.get()
   mail =email_enter.get()
   password = password_enter.get()
   new_data = {
       site:{
           "email" : mail,
           "password" : password,
       }
   }
   if len(mail) == 0 or len(password) ==0 :
       messagebox.showwarning(title= "Warning", message="Please enter all the details")
   else:
       try:
           with open("data.json", 'r') as f:
               # json.dump(new_data , f , indent=4)
                 data = json.load(f)
                 data.update(new_data)
       except FileNotFoundError:
           with open("data.json", "w") as f:
               json.dump(new_data , f , indent=4)
       else:
           with open("data.json", "w") as f:
               json.dump(data , f , indent=4)
       finally:
           website_enter.delete(0,END)
           password_enter.delete(0, END)

    # ---------------------------- UI SETUP ------------------------------- #
def find_password():
    try:
        site = website_enter.get()
        with open("data.json","r") as f:
            data = json.load(f)

    except FileNotFoundError:
        messagebox.showwarning(title ="WARNING",message="no password saved  in this application yet.")

    else:
        if site in data:
            email = data[site]["email"]
            pswd = data[site]["password"]
            messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {pswd}")
        else:
            messagebox.showwarning(title="Warning", message=f"no details for the {site} exist")


windows = Tk()
windows.title("Password Manager")
windows.config(padx=50 , pady=50)

canvas = Canvas(width=200 , height=200)
canvas.grid(column=1,row=0)
image1= PhotoImage(file ="logo.png")
canvas.create_image(100,100 , image=image1)

website_label= Label(text= "Website:")
website_label.grid(column=0,row=1)

email_label = Label(text= "Email/Username:")
email_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

website_enter = Entry(width=21)
website_enter.grid(column=1,row=1)
website_enter.focus()

search_button = Button(text="Search",command = find_password)
search_button.grid(column=2, row=1)


email_enter = Entry(width=35)
email_enter.grid(column=1,row=2, columnspan=2)
email_enter.insert(0, "seana29aviral@gmail.com")

password_enter = Entry(width=21)
password_enter.grid(column=1,row=3)

gen_pswd = Button(text= "Generate Password", width= 15 , command= generate_password)
gen_pswd.grid(column=2 , row=3)

add_button = Button(text= "Add", width=36,command = save)
add_button.grid(column=1,row=4, columnspan=2)









mainloop()