import os
import webbrowser
from fpdf import FPDF
from house import Housemate
from filestack import Client

class PdfReport:
    """
    Creates a PDF file which contains data relating to the  housemates,
    including their names and their portion of rent due for a particular
    period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, rent, entered_housemates: []):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon and resize it to 30x30
        pdf.image(name="files/house.png", w=30, h=30)

        # Insert title
        #   Set font, B for bold
        pdf.set_font(family='Arial', size=20, style='B')
        #   Cell is the rectangle we're going to draw on the PDF
        #   0 means take whole row length and 80 will be in pt units defined in FPDF
        pdf.cell(w=0, h=80, txt="Housemates Bill", border=0, align="C", ln=1)  # Align Center

        # Set the font for Period and period name (size 18 instead of 20)
        pdf.set_font(family='Arial', size=18, style='B')

        # Insert Period label and value
        pdf.cell(w=125, h=40, txt="Period:", border=0)  # Align Left (can exclude, as it's L by default)
        pdf.cell(w=150, h=40, txt=rent.period, border=0, ln=1)  # Align Left (can exclude, as it's L by default)

        # Taking all housemates from our argument and adding them to a list so we can use that list
        #   when printing the names and amounts due
        final_housemates = []
        for housemate in entered_housemates:
            final_housemates.append(housemate)
        # Since our max will be 5 housemates, add empty housemates until we reach 5, if needed
        while len(final_housemates)<5:
            final_housemates.append(Housemate(name="None", room_size=0))

        # Set the font for everything after subtitles (size 14 instead of 18, not bold)
        pdf.set_font(family='Arial', size=14)

        # Housemate 1
        pdf.cell(w=125, h=25, txt=final_housemates[0].name, border=0)
        pdf.cell(w=150, h=25, txt="$" + str(final_housemates[0].pays(rent,
                 [x for x in final_housemates if x != final_housemates[0]])), border=0, ln=1)
        # Housemate 2
        pdf.cell(w=125, h=25, txt=final_housemates[1].name, border=0)
        pdf.cell(w=150, h=25, txt="$" + str(final_housemates[1].pays(rent,
                 [x for x in final_housemates if x != final_housemates[1]])), border=0, ln=1)
        # Housemate 3
        pdf.cell(w=125, h=25, txt=final_housemates[2].name, border=0)
        pdf.cell(w=150, h=25, txt="$" + str(final_housemates[2].pays(rent,
                 [x for x in final_housemates if x != final_housemates[2]])), border=0, ln=1)
        # Housemate 4
        pdf.cell(w=125, h=25, txt=final_housemates[3].name, border=0)
        pdf.cell(w=150, h=25, txt="$" + str(final_housemates[3].pays(rent,
                 [x for x in final_housemates if x != final_housemates[3]])), border=0, ln=1)
        # Housemate 5
        pdf.cell(w=125, h=25, txt=final_housemates[4].name, border=0)
        pdf.cell(w=150, h=25, txt="$" + str(final_housemates[4].pays(rent,
                 [x for x in final_housemates if x != final_housemates[4]])), border=0, ln=1)

        # Change the directory from "housemates-rent" to "files".
        # Then, output PDF and open from "files"
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open("file://" + os.path.realpath(self.filename))


# For use in Repl.it:
class FileSharer:
    def __init__(self, filepath, api_key="INSERT_API_KEY_HERE"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url