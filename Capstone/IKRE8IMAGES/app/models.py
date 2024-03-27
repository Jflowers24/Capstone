from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class UserClient(AbstractUser):

    def __str__(self):
        return f"UserClient  Email: {self.email}"

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

    def __str__(self):
        return f"Name: {self.name}, Owned by: {self.owner}."


class BeforeAndAfterPicture(models.Model):
    name = models.CharField(max_length=50, unique=True)
    source_1 = models.ImageField(null=True, blank=True)  # Before Picture
    source_2 = models.ImageField(null=True, blank=True)  # After Picture

    def __str__(self):
        return f"Name: {self.name}, Owned by: {self.owner}."


class Review(models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=300)
    hidden = models.BooleanField()

    def __str__(self):
        return f"Name: {self.name}, Hidden?: {self.hidden}, Comment: {self.comment[:20]}..."


# Create
def add_picture(name: str, source_1: str) -> Picture:
    return Picture.objects.create(name=name, source_1=source_1)


def add_before_after_picture(
    name: str, source_1: str, source_2: str
) -> BeforeAndAfterPicture:
    return BeforeAndAfterPicture.objects.create(
        name=name, source_1=source_1, source_2=source_2
    )


def add_review(name: str, comment: str, hidden: bool) -> Review:
    return Review.objects.create(name=name, comment=comment, hidden=hidden)


# Read
def get_all_pictures() -> list:
    return Picture.objects.all()


def get_all_before_after_pictures() -> list:
    return BeforeAndAfterPicture.objects.all()


def get_everything_pictures() -> list:
    return [Picture.objects.all(), BeforeAndAfterPicture.objects.all()]


def get_all_reviews() -> list:
    return Review.objects.all()


def get_unhidden_reviews() -> list:
    return Review.objects.filter(hidden=False)


# Update
def modify_picture_by_name(name: str, new_name=None, new_source=None) -> None:
    target = Picture.objects.get(name=name)
    if new_name:
        target.name = new_name
    if new_source:
        target.source = new_source
    target.save()


def modify_picture_by_id(id: int, new_name=None, new_source=None) -> None:
    target = Picture.objects.get(id=id)
    if new_name:
        target.name = new_name
    if new_source:
        target.source = new_source
    target.save()


def modify_review_by_id(id: int, new_name=None, new_comment=None) -> None:
    target = Review.objects.get(id=id)
    if new_name:
        target.name = new_name
    if new_comment:
        target.comment = new_comment
    target.save()


def toggle_review_visibility(id: int):
    target = Review.objects.get(id=id)
    target.hidden = not target.hidden


# Delete
def remove_picture_by_name(name: str) -> None:
    target = Picture.objects.get(name=name)
    target.delete()


def remove_picture_by_id(id: int) -> None:
    target = Picture.objects.get(id=id)
    target.delete()


def remove_before_after_picture_by_name(name: str) -> None:
    target = BeforeAndAfterPicture.objects.get(name=name)
    target.delete()


def remove_before_after_picture_by_id(id: int) -> None:
    target = BeforeAndAfterPicture.objects.get(id=id)
    target.delete()


def remove_review(id: int) -> None:
    target = Review.objects.get(id=id)
    target.delete()
