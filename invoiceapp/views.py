from itertools import product
from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Invoice




# This must for using html2pdf
# Quick fix is to add reportlab==3.6.6 in requirements.txt until this commit is merged.


def home(request):
    if request.method=="POST":
        product_name = request.POST.get('product_name')
        product_des = request.POST.get('product_des')
        rate = request.POST.get('rate')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        total = request.POST.get('total')
        amount_paid = request.POST.get('amount_paid')
        balance_due = request.POST.get('balance_due')
        notes= request.POST.get('notes')
        print(product_name,product_des,rate,quantity,price,total,amount_paid,balance_due,notes)

    return render(request,'invoiceapp/invoice_form.html')


# def pdf_generator(request):

#     return render(request,'invoiceapp/pdf.html')


def pdf_generator(request):
    products = Invoice.objects.all()
    template_path = 'invoiceapp/pdf.html'
    for data in products:
        for data in products.product_set.all:
            print(data)
            print(data.client_name)
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




