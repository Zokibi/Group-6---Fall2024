# Generated by Django 5.1.1 on 2024-10-06 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0007_tables'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employees',
        ),
        migrations.DeleteModel(
            name='MealOrder',
        ),
        migrations.DeleteModel(
            name='Tables',
        ),
    ]