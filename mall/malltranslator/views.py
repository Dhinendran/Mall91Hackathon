from django.shortcuts import render
from . serializers import *
from rest_framework import viewsets


def homepage(request):
    return render(request, 'malltranslator/mallhomepage.html', {})

class ImageUploadViewSet(viewsets.ModelViewSet):
    serializer_class = ImageUploadSerializer
    queryset = ImageUpload.objects.all()

    def get_queryset(self):
        return ImageUpload.objects.all()
