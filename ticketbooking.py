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
