from tkinter import *
from tkinter import messagebox


class NewAccount:
    def __init__(self, first_name, last_name, account_type, account_number, balance):
        # assigning the input first_name to class instance first name
        self.first_name = first_name
        # assigning the input last_name to class instance last name
        self.last_name = last_name
        # assigning the input first_name & last name to class instance username
        self.username = first_name + last_name
        # assigning the input account_type to class instance acc_type
        self.acc_type = account_type
        # assigning the input account_number to class instance accountNumber
        self.accountNumber = account_number
        # assigning the input balance to class instance balance
        self.balance = balance

    # Creating a function to allow users to deposit into their account, accepts one input argument from the user
    def deposit(self, deposit):
        # Initialising a new variable total, with the value of the current balance + the deposit amount
        total = self.balance + deposit
        # Initialising a new variable rounded_total, formatting the float to two decimal places
        rounded_total = float("{:.2f}".format(total))
        # Updating the balance with the value of rounded_total
        self.balance = rounded_total

    # Creating a function to allow users to withdraw from their account
    def withdraw(self, withdraw):
        # Initialising a new variable total, with the value of the current balance - the withdrawal amount
        total = self.balance - withdraw
        # A conditional check to see if the value of total is greater than 0, so the user can't overdraw money
        if total >= 0:
            # Used to debug the condition
            print(total)
            # Formatting the variable total to two decimal places
            total = float("{:.2f}".format(total))
            # Used to debug the formatting
            print(total)
            # Updating the balance to be the value of total
            self.balance = total
            # Used to debug the updating of the balance
            print(self.balance)
            # return True, used for error handling in function call
            return True
        else:
            # return false, used for error handling in function call
            return False


def open_account(account_details):
    # minimizes root window so the new window is only visible
    root.wm_withdraw()
    # creating a easier to use variable for first name
    name = account_details.first_name
    # Creating a new window and assigning it to top
    top = Toplevel()
    # Setting the size of the new window to 400 x 400
    top.geometry("400x400")
    # Locking the minimum window size to 400 x 400 to prevent squashing
    top.minsize(400, 400)
    # Setting the name for the window, using passed in variable name
    top.title("Account Options for " + name)
    # Protocol to run when the user clicks to close the new window
    top.protocol("WM_DELETE_WINDOW", lambda: log_out())
    # Initialising and declaring the variable label, holds a string where it can set the text value and can retrieve it
    label = StringVar()
    # Using the set method to update the initial value
    label.set('Current Balance: £' + str(account_details.balance))

    # Function to update class balance and display text, accepts 1 input
    def transaction(transact):
        # Used to debug and check that argument is passed in correctly
        print(transact)
        # Condition to check argument type
        if transact == "Withdraw":
            # Get the value of the entry box withdraw and initialize a new variable withdraw_amount
            withdraw_amount = withdraw.get()
            # Used to debug that it is correctly getting the value
            print(withdraw_amount)
            # Passes in the input to check it is a valid number
            if validate(withdraw_amount):
                # Using the function within account details to update balance, using the input
                if account_details.withdraw(float(withdraw_amount)):
                    # Using the set method to update the message with new balance
                    label.set('Current Balance: £' + str(account_details.balance))
                    # Using the delete method to clear the entry box withdraw
                    withdraw.delete(0, END)
                    # Create a pop up to highlight the completion of the transaction to the user
                    messagebox.showinfo("Success", f'Successfully withdrawn £{withdraw_amount} from your account')
                # Condition to run if the withdraw method returns false
                else:
                    # Create a pop up to highlight the error with the transaction with context to the user
                    messagebox.showerror('Overdrawn', 'We cannot process this transaction!')
            # Condition to run if the validate method returns false
            else:
                # Create a pop up to highlight the error with the users input
                messagebox.showerror('Invalid input', 'Please input a valid amount')
        # Secondary condition to check argument type
        elif transact == "Deposit":
            # Get the value of the entry box deposit and initialize a new variable deposit_amount
            deposit_amount = deposit.get()
            # Used to debug that it is correctly getting the value
            print(deposit_amount)
            # Passes in the input to check it is a valid number
            if validate(deposit_amount):
                # Using the function within account details to update balance, using the input
                account_details.deposit(float(deposit_amount))
                # Using the set method to update the message with new balance
                label.set('Current Balance: £' + str(account_details.balance))
                # Using the delete method to clear the entry box deposit
                deposit.delete(0, END)
                # Create a pop up to highlight the completion of the transaction to the user
                messagebox.showinfo("Success", f'Successfully deposited £{deposit_amount} into your account')

            else:
                # Create a pop up to highlight the error with the transaction with context to the user
                messagebox.showerror('Invalid input', 'Please input a valid amount')

    # Function to check input value is a number
    def validate(value):
        # Condition to check input value is being passed in
        if value:
            # Condition to attempt the type check
            try:
                # Attempt to convert to type float
                float(value)
                # Debug conversion to type float
                print("value is ok")
                # Return True to show success of validating the input as a float
                return True
            # Exception to run if it can't convert to type float
            except ValueError:
                # Return False to show failure of validating the input as a float
                return False
        # Condition to run if no argument is provided
        else:
            # Return False to show failure of validating the input as a float, no input provided
            return False

    # Configuring option window for user interaction
    top.grid_columnconfigure(0, weight=1, uniform="foo")
    top.grid_columnconfigure(1, weight=1, uniform="foo")
    top.grid_columnconfigure(2, weight=1, uniform="foo")
    top.grid_columnconfigure(3, weight=1, uniform="foo")
    top.grid_columnconfigure(4, weight=1, uniform="foo")

    # Creating all the widgets needed for the secondary pop up (Entry, Button, Label)
    Label(top).grid(row=0, columnspan=5, sticky=EW)
    Label(top, text='Hello ' + name, font="none 20").grid(row=1, columnspan=5, sticky=EW)
    Label(top).grid(row=2, columnspan=5, sticky=EW)
    Label(top, text='What are you looking to do today?', font="none 16").grid(row=3, columnspan=5, sticky=EW)
    Label(top).grid(row=4, columnspan=5, sticky=EW)
    Label(top).grid(row=5, columnspan=5, sticky=EW)
    Label(top, textvariable=label, font="none 16").grid(row=6, columnspan=5, sticky=EW)
    Label(top).grid(row=7, columnspan=5, sticky=EW)
    withdraw = Entry(top, )
    withdraw.grid(row=8, columnspan=1, column=2, sticky=EW)
    Label(top).grid(row=9, columnspan=5, sticky=EW)
    withdraw_btn = Button(top, text='Withdraw', command=lambda: transaction("Withdraw"))
    withdraw_btn.grid(row=10, columnspan=3, column="1", sticky=NSEW)
    Label(top).grid(row=11, columnspan=5, sticky=EW)
    deposit = Entry(top,)
    deposit.grid(row=12, columnspan=1, column=2, sticky=EW)
    Label(top).grid(row=13, columnspan=5, sticky=EW)
    deposit_btn = Button(top, text='Deposit', command=lambda: transaction("Deposit"))
    deposit_btn.grid(row=14, columnspan=3, column="1", sticky=NSEW)

    # Function to run when the user closes the secondary window
    def log_out():
        # Expand the initial window again
        root.state('zoomed')
        # Destroy the new window
        top.destroy()


# Creating different instances of the class NewAccount and initializing new variables
account1 = NewAccount("John", "Jones", "Savings", 1239826738, 234.97)
account2 = NewAccount("David", "Smith", "Business", 1239826738, 10000.00)
account3 = NewAccount("Jane", "Doe", "Business", 1239826738, 5039.98)
account4 = NewAccount("Alex", "Roberts", "Savings", 1239826738, 1032.34)

# Creating a new GUI window
root = Tk()
# Naming the new GUI window
root.title("ATM service")
# Setting the new GUI window size
root.geometry("600x800")
# Restricting the new GUI minimum window size
root.minsize(600, 800)

# configuring the column width so they are equally sized
root.grid_columnconfigure(0, weight=1, uniform="foo")
root.grid_columnconfigure(1, weight=1, uniform="foo")
root.grid_columnconfigure(2, weight=1, uniform="foo")
root.grid_columnconfigure(3, weight=1, uniform="foo")
root.grid_columnconfigure(4, weight=1, uniform="foo")

# creating login display
Label(root).grid(row=0, columnspan=5, sticky=EW)
Label(root, text='Please select the account you wish to access', font="none 20").grid(row=1, columnspan=5, sticky=EW)
Label(root).grid(row=2, columnspan=5, sticky=EW)
Label(root).grid(row=3, columnspan=5, sticky=EW)
Label(root).grid(row=4, columnspan=5, sticky=EW)
user1 = Button(root, text=account1.username, font="none 16", command=lambda: open_account(account1))
user1.grid(row=5, columnspan=3, column="1", sticky=NSEW, padx=20, pady=20, ipady=20,)
Label(root).grid(row=8, columnspan=5, sticky=EW)
Label(root).grid(row=9, columnspan=5, sticky=EW)
user2 = Button(root, text=account2.username, font="none 16", command=lambda: open_account(account2))
user2.grid(row=10, columnspan=3, column="1", sticky=NSEW, padx=20, pady=20, ipady=20)

Label(root).grid(row=12, columnspan=5, sticky=EW)
Label(root).grid(row=13, columnspan=5, sticky=EW)
user3 = Button(root, text=account3.username, font="none 16", command=lambda: open_account(account3))
user3.grid(row=14, columnspan=3, column="1", sticky=NSEW, padx=20, pady=20, ipady=20)

Label(root).grid(row=15, columnspan=5, sticky=EW)
Label(root).grid(row=16, columnspan=5, sticky=EW)
user4 = Button(root, text=account4.username, font="none 16", command=lambda: open_account(account4))
user4.grid(row=17, columnspan=3, column="1", sticky=NSEW, padx=20, pady=20, ipady=20)

# The main loop to open the primary GUI window
root.mainloop()
