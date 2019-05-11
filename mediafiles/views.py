from django.http import HttpResponse
from django.core.files import File

import os

# Create your views here.
def index(request, image_path):
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(file_path, "uploaded_files/api_v1/images/")

    try:
        return HttpResponse(File(open(os.path.join(file_path, image_path), 'rb')), content_type="image/jpeg")
    except:
        return HttpResponse("file not found", status=404)
