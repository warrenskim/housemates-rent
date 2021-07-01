from fpdf import FPDF

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
        return round(rent.amount * (self.room_size / total_size), 2)

class PdfReport:
    """
    Creates a PDF file which contains data relating to the  housemates,
    including their names and their portion of rent due for a particular
    period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, rent, **housemates):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        #   Set font, B for bold
        pdf.set_font(family='Arial', size=20, style='B')
        #   Cell is the rectangle we're going to draw on the PDF
        #   0 means take whole row length and 80 will be in pt units defined in FPDF
        pdf.cell(w=0, h=80, txt="Housemates Bill", border=1, align="C", ln=1)  # Align Center

        # Insert Period label and value
        pdf.cell(w=125, h=40, txt="Period", border=1)  # Align Left (can exclude, as it's L by default)
        pdf.cell(w=150, h=40, txt=rent.period, border=1, ln=1)  # Align Left (can exclude, as it's L by default)

        # Taking all housemates from our argument and adding them to a list so we can use that list
        #   when printing the names and amounts due
        housemates_list = []
        for housemate in housemates.values():
            housemates_list.append(housemate)
        # Since our max will be 5 housemates, add empty housemates until we reach 5, if needed
        while len(housemates_list)<5:
            housemates_list.append(Housemate(name="None", room_size=0))

        # Housemate 1
        pdf.cell(w=125, h=40, txt=housemates_list[0].name, border=1)
        pdf.cell(w=150, h=40, txt="$" + str(housemates_list[0].pays(rent,
                 [x for x in housemates_list if x != housemates_list[0]])), border=1, ln=1)
        # Housemate 2
        pdf.cell(w=125, h=40, txt=housemates_list[1].name, border=1)
        pdf.cell(w=150, h=40, txt="$" + str(housemates_list[1].pays(rent,
                 [x for x in housemates_list if x != housemates_list[1]])), border=1, ln=1)
        # Housemate 3
        pdf.cell(w=125, h=40, txt=housemates_list[2].name, border=1)
        pdf.cell(w=150, h=40, txt="$" + str(housemates_list[2].pays(rent,
                 [x for x in housemates_list if x != housemates_list[2]])), border=1, ln=1)
        # Housemate 4
        pdf.cell(w=125, h=40, txt=housemates_list[3].name, border=1)
        pdf.cell(w=150, h=40, txt="$" + str(housemates_list[3].pays(rent,
                 [x for x in housemates_list if x != housemates_list[3]])), border=1, ln=1)
        # Housemate 5
        pdf.cell(w=125, h=40, txt=housemates_list[4].name, border=1)
        pdf.cell(w=150, h=40, txt="$" + str(housemates_list[4].pays(rent,
                 [x for x in housemates_list if x != housemates_list[4]])), border=1, ln=1)


        pdf.output(self.filename)

rent1 = Rent(amount=2400, period="July 2021")
john = Housemate(name="John", room_size=120)
jacob = Housemate(name="Jacob", room_size=150)
josephine = Housemate(name="Josephine", room_size=140)

print(john.pays(rent1, [jacob, josephine]))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(rent=rent1, housemate1=john, housemate2=jacob, housemate3=josephine)