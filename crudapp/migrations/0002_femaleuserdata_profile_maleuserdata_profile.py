# Generated by Django 4.1 on 2022-10-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='femaleuserdata',
            name='profile',
            field=models.ImageField(null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='maleuserdata',
            name='profile',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]
