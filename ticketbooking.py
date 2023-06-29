# TICKET BOOKING IN GUI #

import tkinter as tk

class TicketBookingGUI:
    def __init__(self, master):
        self.master = master
        master.title("Ticket Booking")

        # Create GUI elements
        self.seat_labels = []
        self.seat_buttons = []
        self.total_price_label = tk.Label(master, text="Total price: $0")
        self.book_button = tk.Button(master, text="Book", command=self.book)

        # CREATE SEATS
        self.seats = []
        for i in range(10):
            row = []
            for j in range(10):
                row.append(False)
            self.seats.append(row)

   # GRID LAYOUT
        for i in range(10):
            for j in range(10):
                seat_label = tk.Label(master, text="Seat {}:{}".format(i+1, j+1))
                seat_button = tk.Button(master, text="Available", command=lambda i=i, j=j: self.select_seat(i, j))

                seat_label.grid(row=i, column=j*2)
                seat_button.grid(row=i, column=j*2+1)

                self.seat_labels.append(seat_label)
                self.seat_buttons.append(seat_button)

        self.total_price_label.grid(row=10, column=0, columnspan=10)
        self.book_button.grid(row=11, column=0, columnspan=10)

    def select_seat(self, row, col):
        if not self.seats[row][col]:
            self.seats[row][col] = True
            self.seat_buttons[row*10 + col]["text"] = "Selected"
        else:
            self.seats[row][col] = False
            self.seat_buttons[row*10 + col]["text"] = "Available"
