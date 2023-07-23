import tkinter as tk
from tkinter import messagebox
import datetime

class UserInformation:
    def __init__(self, ussnm, pssd):
        self.window = tk.Tk()
        self.window.title("User Information")

        self.ussnm_ = ussnm + " task.txt"
        self.pssd = pssd

        self.name_label = tk.Label(self.window, text="Enter your name:")
        self.name_entry = tk.Entry(self.window)

        self.address_label = tk.Label(self.window, text="Enter your address:")
        self.address_entry = tk.Entry(self.window)

        self.age_label = tk.Label(self.window, text="Enter your age:")
        self.age_entry = tk.Entry(self.window)

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit)

        self.name_label.pack()
        self.name_entry.pack()
        self.address_label.pack()
        self.address_entry.pack()
        self.age_label.pack()
        self.age_entry.pack()
        self.submit_button.pack()

        self.window.mainloop()

    def submit(self):
        with open(self.ussnm_, 'a') as f:
            f.write(self.pssd + '\n')
            f.write(f"Name: {self.name_entry.get()}\n")
            f.write(f"Address: {self.address_entry.get()}\n")
            f.write(f"Age: {self.age_entry.get()}\n")

        self.window.destroy()
        Login()

class Signup:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Signup")

        self.username_label = tk.Label(self.window, text="Enter a username:")
        self.username_entry = tk.Entry(self.window)

        self.password_label = tk.Label(self.window, text="Enter a password:")
        self.password_entry = tk.Entry(self.window)

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.submit_button.pack()

        self.window.mainloop()

    def submit(self):
        UserInformation(self.username_entry.get(), self.password_entry.get())
        self.window.destroy()

class Login:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")

        self.username_label = tk.Label(self.window, text="Enter your username:")
        self.username_entry = tk.Entry(self.window)

        self.password_label = tk.Label(self.window, text="Enter your password:")
        self.password_entry = tk.Entry(self.window)

        self.login_button = tk.Button(self.window, text="Login", command=self.login)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()

        self.window.mainloop()

    def login(self):
        try:
            with open(self.username_entry.get() + " task.txt", 'r') as f:
                password = f.readline().strip()
                if password == self.password_entry.get():
                    messagebox.showinfo("Success", "You are successfully logged in")
                    self.window.destroy()
                else:
                    messagebox.showerror("Error", "Incorrect username or password")
        except FileNotFoundError:
            messagebox.showerror("Error", "No account associated with this username")

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Console Task Manager")

        self.welcome_label = tk.Label(self.window, text="WELCOME TO YOUR CONSOLE TASK MANAGER")
        self.welcome_label.pack()

        self.login_button = tk.Button(self.window, text="Login", command=self.login)
        self.login_button.pack()

        self.signup_button = tk.Button(self.window, text="Signup", command=self.signup)
        self.signup_button.pack()

        self.window.mainloop()

    def login(self):
        Login()
        self.window.destroy()

    def signup(self):
        Signup()
        self.window.destroy()

if __name__ == "__main__":
    App()
