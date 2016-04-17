from hsg.models import Group
from hsg.models import RegInfo
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Frame, Paragraph
from reportlab.lib.units import cm
from datetime import datetime
width, height = A4


def generate_confirmation(response, reg_id):
    # Query Name and Abbreviation of the Group
    registration = RegInfo.objects.get(id=reg_id)
    group_name = registration.group.name
    group_abbrev = registration.group.abbrev
    year = registration.date.year

    styles = getSampleStyleSheet()
    # Set up page and layout
    p = canvas.Canvas(response, pagesize=A4)
    p.setFont("Helvetica", 11)
    p = _generate_heading(p, styles)
    p = _generate_fromfield(p, styles,'Andrej Rode','Inneres','innen@asta-kit.de','test')
    p = _generate_addressfield(p, styles, 'Andrej Rode', 'Teststr. 1',
                               '76523 Teststadt')
    p = _generate_textfield(p, styles, 'Testtext')
    p.showPage()
    p.save()
    return response

def _generate_heading(c, styles):
    heading = []
    heading.append(Paragraph("<a name='Test'/> <a fontSize=7>AStA am Karlsruher Institut für Technologie</a>", styles['Heading3']))
    f = Frame(2*cm, height-(1+1.7)*cm, 10.5*cm, 1.7*cm, showBoundary=1)
    f.addFromList(heading,c)
    return c


def _generate_fromfield(c, styles, name, referat, email, logo):
    addressbox = []
    addressbox.append(Paragraph("Allgemeiner Studierendenausschuss", styles['Normal']))
    addressbox.append(Paragraph("Adenauerring 7\n76131 Karlsruhe",styles['Normal']))
    addressbox.append(Paragraph("<a href='Test'>Test</a>", styles['Normal']))
    f = Frame(width - (5+1)*cm, height - (3.2+7.5)*cm, 5*cm, 7.5*cm, showBoundary=1)
    f.addFromList(addressbox, c)
    return c


def _generate_addressfield(c, styles, name, address, city):
    addressfield = []
    backaddress = [Paragraph("AStA KIT Adenauerring 7, 76131 Karlsruhe", styles['Bullet'])]
    addressfield.append(Paragraph("Test", styles['Normal']))
    f1 = Frame(2.5*cm, height-(2.7+0.5)*cm, 8*cm, 0.5*cm, showBoundary=1)
    f2 = Frame(2.5*cm, height-(2.7+0.5+4)*cm, 8*cm, (2.73+1.27)*cm, showBoundary=1)
    f1.addFromList(backaddress,c)
    f2.addFromList(addressfield,c)
    return c

def _generate_textfield(c, styles, text):
    textfield = []
    textfield.append(Paragraph(text, styles['Normal']))
    f = Frame(2.5*cm, 5*cm, width-(2+2.5)*cm, 15*cm, showBoundary=1)
    f.addFromList(textfield, c)
    return c
