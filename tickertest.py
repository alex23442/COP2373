#TODO add docstring, add a lot of comments, before turning it in.
#finished the logic
total_tickets = 20
tickets_left = 20
tickets_bought = 0
ticket_limit = 4
buyers=0
while tickets_left > 0:

    user_tickets=int(input("how many tickets do you want?"))


    if user_tickets <= ticket_limit and tickets_left - user_tickets >= 0:
        tickets_left -= user_tickets
        buyers += 1
        print(buyers)
        print(tickets_left)

    elif user_tickets <= ticket_limit and user_tickets > tickets_left:
        print(f"too much we only have{tickets_left} tickets left")

    else:
        print("yo tried to buy too much limit is four buddy")

print(buyers)
print("sorry sold out come back next time")