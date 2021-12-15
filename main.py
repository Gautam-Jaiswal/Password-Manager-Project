from tkinter import *
from tkinter import messagebox
from Encryption import encryption, decryption, create_new_password
import json

Main_Encrypted_Password = ''


def generate_password():
    global Main_Encrypted_Password
    if len(password_entry_box.get()) > 0:
        user_input = messagebox.askquestion(title='Password Warning',
                                            message='You have clicked Generate New Password.A new Password will be generated for you.'
                                                    'Press Yes for new Password or No if you want to continue with your own password')
        if user_input.lower() == 'yes':
            Main_Encrypted_Password = encryption(create_new_password())
        else:
            Main_Encrypted_Password = encryption(password_entry_box.get())
    else:
        Main_Encrypted_Password = encryption(create_new_password())

    password_entry_box.delete(0,END)
    password_entry_box.insert(0,Main_Encrypted_Password)
    generate_password_button.config(state='disabled')

def save_password():
    new_dict = {
        (website_entry_box.get()).lower(): {
            "email": email_entry_box.get(),
            "password": password_entry_box.get()
        }
    }

    if len(website_entry_box.get()) == 0 or len(email_entry_box.get()) == 0 or len(password_entry_box.get()) == 0:
        messagebox.showinfo(title='Error', message='Please Input all the Fields')
    else:
        if str(generate_password_button['state']) == DISABLED:
            try:
                with open('password.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('password.json', 'w') as file:
                    json.dump(new_dict,file, indent=4)
            else:
                data.update(new_dict)
                with open('password.json', 'w') as file:
                    json.dump(data,file, indent=4)
            finally:
                website_entry_box.delete(0,END)
                email_entry_box.delete(0,END)
                password_entry_box.delete(0,END)
                generate_password_button.config(state='active')
        else:
            messagebox.showwarning(title='Error', message='Please Hit Generate Button')

def search_password():
    if len(website_entry_box.get()) == 0:
        messagebox.showinfo(title="Error", message='Please Input Website Name')
    else:
        search_website = (website_entry_box.get()).lower()
        try:
            with open('password.json','r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title='Error', message='No such website Password Exsits')
        else:
            if search_website in data:
                decrypted_password = decryption(data[search_website]['password'])
                messagebox.showinfo(title='Details', message=f'Email: {data[search_website]["email"]} \n Password: {decrypted_password}')
            else:
                messagebox.showwarning(title='Error', message='No such website Password Exsits')

window = Tk()
window.title("Password Manager")
window.config(bg='white')

canvas = Canvas(master=window, height=350, width=350)
canvas.grid(row=0, column=0, columnspan=2)

Lock_Image = PhotoImage(file='lock.png')
canvas.create_image(220, 180, image=Lock_Image)

# ************** LABELS ***************#

website_name_label = Label(text='Website:', font=("Arial", 18))
website_name_label.grid(row=1, column=0, padx=0, pady=8)

email_name_label = Label(text='Email:', font=("Arial", 18))
email_name_label.grid(row=2, column=0, padx=0, pady=8)

password_name_label = Label(text='Password:', font=("Arial", 18))
password_name_label.grid(row=3, column=0, padx=0, pady=8)

# ************** ENTRY BOX ***************#

website_entry_box = Entry(width=20)
website_entry_box.grid(row=1, column=1)
website_entry_box.focus_set()

email_entry_box = Entry(width=20)
email_entry_box.grid(row=2, column=1)

password_entry_box = Entry(width=20)
password_entry_box.grid(row=3, column=1)

# ************** BUTTONS ***************#

generate_password_button = Button(text='Generate', command=generate_password, bd=5, font=("Arial", 15, 'bold'))
generate_password_button.grid(row=3, column=2, pady=8, padx=8)

save_button = Button(text='SAVE',command=save_password, bd=5, height=2, width=10, font=("Arial", 15, 'bold'))
save_button.grid(row=4, column=1, pady=8, padx=8)

search_button = Button(text='SEARCH',command=search_password, bd=5, height=2, width=10, font=("Arial", 15, 'bold'))
search_button.grid(row=5, column=1, pady=8, padx=8)

window.mainloop()
