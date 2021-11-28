from django.shortcuts import render
from django.db import models
from django.shortcuts import render, redirect
from .forms import UploadImageForm
from .models import Profiles
import base64


def upload_file(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_img = form.save(commit=False)
            uploaded_img.image_data = form.cleaned_data['drawing_data'].file.read()
            uploaded_img.save()
            return redirect('/')
        else:
            form = UploadImageForm()
        return render(request, 'image_process/upload.html', {'form': form})