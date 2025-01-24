trains = [
    ("101", "Express Train", 100),
    ("102", "Local Train", 200),
]

# Booking data
bookings = {train[0]: 0 for train in trains} 
#doremon
def find_train(train_number):
    return next((train for train in trains if train[0] == train_number), None)

def check_availability(train_number):
    train = find_train(train_number)
    if train:
        total_seats = train[2]
        booked_seats = bookings[train_number]
        return total_seats - booked_seats
    return -1
#ch
def book_ticket(train_number, num_tickets):
    available = check_availability(train_number)
    if available == -1:
        print("Invalid Train Number.")
    elif num_tickets <= available:
        bookings[train_number] += num_tickets
        print(f"Successfully booked {num_tickets} ticket(s) on {find_train(train_number)[1]}.")
    else:
        print("Sorry, not enough seats available.")

def cancel_ticket(train_number, num_tickets):
    if train_number not in bookings:
        print("Invalid Train Number.")
    elif num_tickets <= bookings[train_number]:
        bookings[train_number] -= num_tickets
        print(f"Successfully canceled {num_tickets} ticket(s).")
    else:
        print("Cancellation failed. You cannot cancel more tickets than booked.")

# Main functionality
def main():
    while True:
        print("\nRailway Booking System")
        print("1. View Train Info")
        print("2. Check Seat Availability")
        print("3. Book Tickets")
        print("4. Cancel Tickets")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            for train in trains:
                train_number, train_name, total_seats = train
                available_seats = check_availability(train_number)
                print(f"Train Number: {train_number}, Train Name: {train_name}, Available Seats: {available_seats}")

        elif choice == "2":
            train_number = input("Enter Train Number: ")
            available = check_availability(train_number)
            if available >= 0:
                print(f"Available Seats: {available}")
            else:
                print("Invalid Train Number.")

        elif choice == "3":
            train_number = input("Enter Train Number: ")
            num_tickets = int(input("Enter number of tickets to book: "))
            book_ticket(train_number, num_tickets)

        elif choice == "4":
            train_number = input("Enter Train Number: ")
            num_tickets = int(input("Enter number of tickets to cancel: "))
            cancel_ticket(train_number, num_tickets)

        elif choice == "5":
            print("Exiting Railway Booking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
