# Generated by Django 5.1.3 on 2024-11-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='dean',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
