
def checking_tickets(ticket_limit, tickets_left,total_buyers ):
    """
    Checks the number of tickets ordered by the buyer and determines
    whether the purchase can be made or not.

    Parameters:
    ticket_limit(int): The max number of tickets a buyer can buy.
    tickets_left(int): The number of tickets left.
    buyers(int): The number of buyers that made the purchase.

    Variables:
    user_tickets(int): The number of tickets wanted by the buyer.

    Logic:
    1.Prompt the user to enter the number of tickets they want to buy.
    2.checks that the amount they requested is within the ticket limit
      and that there's enough tickets available.
    3.If purchase is valid, subtract the tickets from the
      remaining tickets  and increase the number of buyers.
    4.If not enough tickets available, display the number of tickets
      remaining.
    5.If the buyer exceeds the ticket limit, display an error message.
    6.Return the updated number of tickets and buyers.

    Return:
    Returns the updated values of tickets_left and buyers.
    """

    #this section prompts the user with a message 'how many tickets do you want'
    # and checks whether it's a valid input.
    #if they enter an invalid input it goes through the except function and
    #returns the current values(ticket_left, buyers).
    #if they enter a negative number it returns the current values(ticket_left,buyers) again.
    try:
        user_tickets = int(input("Hello there, how much tickets would you like?"))
        if user_tickets <= 0:
            print("enter a positive integer")
            return tickets_left,total_buyers


    except ValueError:
        print("Please enter a valid number")
        return tickets_left,total_buyers

    #checks for both the amount of tickets the buyer wants is available and is within ticket limit.
    #If so, subtracts the tickets bought from the tickets left, adds one to the successful buyers,
    #and displays both buyers and tickets left.
    if user_tickets <= ticket_limit and tickets_left - user_tickets >= 0:
        tickets_left -= user_tickets
        total_buyers += 1
        if tickets_left > 0:
            print(f"the number of tickets left is : {tickets_left}")

        else:
            pass

    #checks if the amount of tickets the buyers want is within the ticket limit and greater than the
    #tickets left. If so, prompt the user with a display letting them know how many tickets are left.
    elif ticket_limit >= user_tickets > tickets_left:
        print(f"Sorry, we only have {tickets_left} tickets left")


    #if they try to get more then the ticket limit they will be prompt with a messages
    #that says they're buying more the limit
    else:
        print("the limit is 4 tickets")

    #returns the updated values of tickets_left and buyers.
    return tickets_left,total_buyers


def interface():
    """
    Controls the main flow of the program.

    Parameters:
    None

    Variables:
    tickets_left(int): The number of tickets left.
    ticket_limit(int): The max number of tickets the buyer can purchase.
    buyers(int): The number of buyers that made the purchase.

    Return:
    None
    """

    tickets_left = 10
    ticket_limit = 4
    buyers = 0

    #this while loop will keep running the function(checking_tickets) until all tickets are sold out,
    #which displays two messages, total buyers, and sold out message.
    while tickets_left > 0:


        #updates the values tickets_left and buyers with the values it returned from the function
        #checking_tickets.
        tickets_left, buyers = checking_tickets(ticket_limit,
                                                tickets_left,
                                                buyers)

    print("\nsorry sold out come back next time")
    print(f"\nthe total number of buyers is: {buyers} ")


interface()