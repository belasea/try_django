import os
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from django.conf import settings

def get_pdf_file(request):
    context = {'object': "হ্যালো ওয়ার্ল্ড!"}  

    # Render HTML from template
    html_string = render_to_string('pdf/pdf_invoice.html', context)

    # Generate PDF
    pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()

    # Return as response
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    return response

