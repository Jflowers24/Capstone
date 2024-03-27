# Generated by Django 5.0.2 on 2024-03-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_picture_source_beforeandafterpicture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=300)),
                ('hidden', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='beforeandafterpicture',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]