#TODO fix up docstring, and comment before turning it in.




def checking_tickets(ticket_limit, tickets_left,buyers ):
    """This function handles all the logic of the program."""

    #promts the user how many tickets they want
    user_tickets = int(input("how many tickets do you want?"))

    #these lines work together checks if the amount of tickets they want is in the limit
    #as well as checking if we have enough to provide it.
    #then subtracts the amount they want from the total amount left,
    #adds to the total buyer, and prints the total tickets left and buyers.
    if user_tickets <= ticket_limit and tickets_left - user_tickets >= 0:
        tickets_left -= user_tickets
        buyers += 1
        print(buyers)
        print(tickets_left)

    #this line checks is the amount fo tickets the user wants is within the limit,
    #and checks if the amount is greater than the tickets left. If so it promts the
    #with a message that says we only have many tickets left.
    elif ticket_limit >= user_tickets > tickets_left:
        print(f"too much we only have {tickets_left} tickets left")


    #these lines are the final it's the last chek if it didn't pass the other it either means
    #they tried to type a higher number or entered an invalid number.
    else:
        print("yo tried to buy too much limit is four buddy")

    #this line returns the values to proceed with the fuction
    return tickets_left,buyers


def interface():
    """these functions handle the light work holding variables and calling the first function"""

    tickets_left = 20
    ticket_limit = 4
    buyers = 0

    #this while loop is here because it will keep running
    #the first function until the number of tickets are sold out.
    while tickets_left > 0:

        tickets_left, buyers = checking_tickets(ticket_limit,
                                                tickets_left,
                                                buyers)

    #after the tickets are sold out it will print these lines.
    print(buyers)
    print("sorry sold out come back next time")

interface()