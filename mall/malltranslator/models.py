from django.db import models

def getImagePath(instance , filename):
    return 'malltranslator/images/%s' %(filename)

class ImageUpload(models.Model):
    image = models.ImageField(upload_to=getImagePath)
    spam = models.BooleanField(default=False)
