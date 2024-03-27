from django.contrib import admin
from app.models import UserClient, Picture, BeforeAndAfterPicture

# Register your models here.
admin.site.register([UserClient, Picture, BeforeAndAfterPicture])
