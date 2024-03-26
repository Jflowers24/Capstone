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
    name = models.CharField(max_length=50)
    source = models.ImageField(null=True, blank=True)
    owner = models.OneToOneField(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Picture  Name: {self.name}, Owned by: {self.owner}."


class BeforeAndAfterPicture(models.Model):
    name = models.CharField(max_length=50)
    source_1 = models.ImageField(null=True, blank=True)
    source_2 = models.ImageField(null=True, blank=True)
    owner = models.OneToOneField(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Picture  Name: {self.name}, Owned by: {self.owner}."
