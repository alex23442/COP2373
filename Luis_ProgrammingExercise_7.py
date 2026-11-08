
class BankAcct:
    """
    Purpose:
    Represents a customer's bank account and manages account information.

    Parameters:
    name(str): The name of the account holder.
    account_number(int): The customer's account number.
    balance(float): The current amount of money in the account.
    interest_rate(float): The account's current interest rate.

    Variables:
    self.name: Stores the account holder's name.
    self.account_number: Stores the account number.
    self.balance: Stores the current account balance.
    self.interest_rate: Stores the current interest rate.
    self.interest_earned: Stores the interest earned on the account.

    Logic:
    1. Defines the information and methods belonging to a bank account.

    Return:
    None
    """

    def __init__(self, name, account_number, balance, interest_rate):
        """
        Purpose:
        Initializes a new bank account with the customer's information.

        Parameters:
        name(str): The name of the account holder.
        account_number(int): The customer's account number.
        balance(float): The starting account balance.
        interest_rate(float): The starting interest rate.

        Variables:
        self.name: Stores the account holder's name.
        self.account_number: Stores the account number.
        self.balance: Stores the starting balance.
        self.interest_rate: Stores the starting interest rate.
        self.interest_earned: Initializes the interest earned to zero.

        Logic:
        1. Assigns the customer's information to the account attributes.
        2. Initializes the interest earned to zero.

        Return:
        None
        """
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest_earned = 0

    def deposit(self, amount):
        """
        Purpose:
        Deposits money into the customer's bank account.

        Parameters:
        amount(float): The amount of money being deposited.

        Variables:
        self.balance: The customer's current account balance.

        Logic:
        1. Adds the deposited amount to the current balance.

        Return:
        None
        """
        self.balance += amount

    # Subtracts the withdrawn amount from the current balance
    def withdraw(self, amount):
        """
        Purpose:
        Withdraws money from the customer's bank account.

        Parameters:
        amount(float): The amount of money being withdrawn.

        Variables:
        self.balance: The customer's current account balance.

        Logic:
        1. Subtracts the withdrawn amount from the current balance.

        Return:
        None
        """
        self.balance -= amount

    # Sets the current interest rate to a new rate
    def interest_adjust(self, change):
        """
        Purpose:
        Sets a new interest rate on the customer's bank account.

        Parameters:
        change(float): The new interest rate that replaces the current rate.

        Variables:
        self.interest_rate: The customer's current interest rate.

        Logic:
        1. Replaces the current interest rate with the new interest rate.

        Return:
        None
        """
        self.interest_rate = change

    def interest_calculate(self, NOD):
        """
        Purpose:
        Calculates the new account balance after earning interest.

        Parameters:
        NOD(int): The number of days interest is calculated for.

        Variables:
        self.balance: The current account balance.
        self.interest_rate: The current interest rate.
        self.interest_earned: The amount of interest earned.

        Logic:
        1. Calculates interest using the current balance and interest rate.
        2. Adjusts the calculation based on the number of days.
        3. Adds the earned interest to the current account balance.

        Return:
        None
        """
        self.interest_earned = (self.balance * self.interest_rate * (NOD / 365))
        self.balance += self.interest_earned

    def __str__(self):
        """
        Purpose:
        Displays the customer's bank account information.

        Parameters:
        None.

        Variables:
        self.name: The account holder's name.
        self.balance: The current account balance.
        self.interest_earned: The interest earned on the account.

        Logic:
        1. Formats the account holder's name.
        2. Displays the current account balance.
        3. Displays the amount of interest earned.

        Return:
        Returns a formatted string containing the account information.
        """
        return (f"Account Holder: {self.name}\n"
                f"Balance: ${self.balance:.2f}\n"
                f"Interest Earned: ${self.interest_earned:.2f}")


def test():
    """
    Purpose:
    Tests the different methods in the BankAcct class.

    Parameters:
    None.

    Variables:
    luisBank(BankAcct): Luis's bank account object.
    abnerBank(BankAcct): Abner's bank account object.

    Logic:
    1. Creates two bank account objects.
    2. Tests depositing money.
    3. Tests withdrawing money.
    4. Tests adjusting the interest rate.
    5. Tests calculating interest for three days.
    6. Displays both bank account objects.

    Return:
    None
    """

    # Create two bank account objects
    luisBank = BankAcct("Luis", 100, 100, 0.02)
    abnerBank = BankAcct("Abner", 100, 1000, 0.01)

    # Test depositing money into Luis's account
    luisBank.deposit(20)

    # Test withdrawing money from Abner's account
    abnerBank.withdraw(200)

    # Test withdrawing money from Luis's account
    luisBank.withdraw(20)

    # Test depositing money into Abner's account
    abnerBank.deposit(1000)

    # Set Abner's interest rate to 6%
    abnerBank.interest_adjust(.06)

    # Calculate interest on Luis's account on the number of days
    luisBank.interest_calculate(3)

    # Calculate interest on Abner's account on the number of days
    abnerBank.interest_calculate(3)

    # Display both account objects using the __str__ method
    print(abnerBank)
    print(luisBank)


# Call the test function to run the program
test()
