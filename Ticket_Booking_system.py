total_seats = int(input("Enter the total number of seats: "))
available_seats = list(range(1, total_seats + 1))
booked_seats = []
def book_seat(ticket):
    if ticket in available_seats:
        available_seats.remove(ticket)
        booked_seats.append(ticket)
        print(f"Seat {ticket} has been successfully booked.")
    else:
        print(f"Seat {ticket} is already booked or does not exist.")
def cancel_seat(ticket):
    if ticket in booked_seats:
        booked_seats.remove(ticket)
        available_seats.append(ticket)
        print(f"Booking for seat {ticket} has been successfully canceled.")
    else:
        print(f"Seat {ticket} is not booked, so it cannot be canceled.")
def display_available_seats():
    print("Available seats:", sorted(available_seats))
    print("Booked seats :",booked_seats)
def display():
    while True:
        print("\nMenu:")
        print("1. Check available seats")
        print("2. Book a ticket")
        print("3. Cancel a booking")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_available_seats()
        elif choice == 2:
            ticket_num = int(input("Enter the seat number to book: "))
            book_seat(ticket_num)
        elif choice == 3:
            ticket_num = int(input("Enter the seat number to cancel: "))
            cancel_seat(ticket_num)
        elif choice == 4:
            print("Exiting the booking system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
display()