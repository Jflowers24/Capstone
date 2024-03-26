from django.contrib import admin
from app.models import Client, Picture, BeforeAndAfterPicture

# Register your models here.
admin.site.register([Client, Picture, BeforeAndAfterPicture])
