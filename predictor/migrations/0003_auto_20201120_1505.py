# Generated by Django 3.1.2 on 2020-11-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0002_imageupload_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
