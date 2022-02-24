from itertools import product
from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# This must for using html2pdf
# Quick fix is to add reportlab==3.6.6 in requirements.txt until this commit is merged.


def home(request):
    return render(request,'invoiceapp/invoice.html')

def pdf_generator(request):
    # products = Product.objects.all()

    template_path = 'invoiceapp/pdf.html'
    products = ['altaf','hosen']
    context = {'products': products}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




