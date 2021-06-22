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

    def pays(self, rent, *args):
        total_size = self.room_size
        for housemate in args:
            total_size += housemate.room_size
        return round(rent.amount * (self.room_size / total_size), 2)

class PdfReport:
    """
    Creates a PDF file which contains data relating to the  housemates,
    including their names and their portion of rent due for a particular
    period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, housemate1, housemate2, rent):
        pass

rent1 = Rent(amount=2400, period="June 2021")
john = Housemate(name="John", room_size=120)
jacob = Housemate(name="Jacob", room_size=150)
josephine = Housemate(name="Josephine", room_size=140)

print(john.pays(rent1, jacob, josephine))