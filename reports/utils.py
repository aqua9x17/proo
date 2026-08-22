from io import BytesIO

from django.http import HttpResponse
from openpyxl import Workbook
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def export_simple_pdf(title, rows):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle(title)
    y = 800
    pdf.drawString(40, y, title)
    y -= 30
    for row in rows:
        if y < 40:
            pdf.showPage()
            y = 800
        pdf.drawString(40, y, " | ".join(str(v) for v in row))
        y -= 20
    pdf.save()
    buffer.seek(0)
    return HttpResponse(buffer.read(), content_type="application/pdf")


def export_simple_excel(sheet_name, headers, rows):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = sheet_name[:31]
    sheet.append(headers)
    for row in rows:
        sheet.append(list(row))
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    workbook.save(response)
    return response
