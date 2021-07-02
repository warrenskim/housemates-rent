class Rent:
    """
    Object which contains data about a particular bill, including
    the amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Housemate:
    """
    Person who lives in the home and pays a share of the rent
    based on the size of their room or living quarters (in sq-ft).
    """

    def __init__(self, name, room_size):
        self.name = name
        self.room_size = room_size

    def pays(self, rent, housemates: []):
        total_size = self.room_size
        for housemate in housemates:
            total_size += housemate.room_size
        amount_due = rent.amount * (self.room_size / total_size)
        return '%.2f' %amount_due