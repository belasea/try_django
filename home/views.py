from django.shortcuts import render, HttpResponse
from .forms import ImageUploadForm
from .models import UploadedImage
from PIL import Image
import pytesseract
import os


# Create your views here.

def home(request):
    return HttpResponse("Hello World !")



def extract_text_from_image(image_path):
    # Optionally use image_to_data for table-like structure
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def upload_image_view(request):
    context = {}
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = form.save()
            img_path = uploaded.image.path
            extracted_text = extract_text_from_image(img_path)
            context['text'] = extracted_text
            context['image'] = uploaded.image.url
    else:
        form = ImageUploadForm()

    context['form'] = form
    return render(request, 'upload.html', context)
