from . models import *
from rest_framework import serializers

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ('pk', 'image', 'spam')
