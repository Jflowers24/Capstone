from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class Client(AbstractUser):

    def __str__(self):
        return f"Client  Email: {self.email}"

    client_permissions = models.ManyToManyField(
        Permission,
        verbose_name=("client permissions"),
        blank=True,
        related_name="clients_permissions",
    )

    client_groups = models.ManyToManyField(
        Group,
        verbose_name=("client groups"),
        blank=True,
        related_name="clients_groups",
    )


class Picture(models.Model):
    name = models.CharField(max_length=50, unique=True)
    source = models.ImageField(null=True, blank=True)
    owner = models.OneToOneField(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Picture  Name: {self.name}, Owned by: {self.owner}."


class BeforeAndAfterPicture(models.Model):
    name = models.CharField(max_length=50, unique=True)
    source_1 = models.ImageField(null=True, blank=True)  # Before Picture
    source_2 = models.ImageField(null=True, blank=True)  # After Picture
    owner = models.OneToOneField(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Picture  Name: {self.name}, Owned by: {self.owner}."


# Create
def add_picture(name: str, source_1: str, owner: object):
    return Picture.objects.create(name=name, source_1=source_1, owner=owner)


def add_before_after_picture(name: str, source_1: str, source_2: str, owner: object):
    return BeforeAndAfterPicture.objects.create(
        name=name, source_1=source_1, source_2=source_2, owner=owner
    )


# Read
def get_all_pictures():
    return Picture.objects.all()


def get_all_before_after_pictures():
    return BeforeAndAfterPicture.objects.all()


def get_everything_pictures():
    return [Picture.objects.all(), BeforeAndAfterPicture.objects.all()]


# Update
def modify_picture_by_name(name: str, new_name=None, new_source=None):
    target = Picture.objects.get(name=name)
    if new_name:
        target.name = new_name
    if new_source:
        target.source = new_source
    target.save()


def modify_picture_by_id(id: int, new_name=None, new_source=None):
    target = Picture.objects.get(id=id)
    if new_name:
        target.name = new_name
    if new_source:
        target.source = new_source
    target.save()


# Delete
def remove_picture_by_name(name: str):
    target = Picture.objects.get(name=name)
    target.delete()


def remove_picture_by_id(id: int):
    target = Picture.objects.get(id=id)
    target.delete()


def remove_before_after_picture_by_name(name: str):
    target = BeforeAndAfterPicture.objects.get(name=name)
    target.delete()


def remove_before_after_picture_by_id(id: int):
    target = BeforeAndAfterPicture.objects.get(id=id)
    target.delete()
