# Generated by Django 5.1.1 on 2024-09-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0005_employees_employeeselection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='employeeSelection',
            field=models.CharField(choices=[('1', 'Charne Robinson'), ('2', 'Jacob Sparks'), ('3', 'Daryna Kozlova'), ('4', 'Isaiah Dillard'), ('5', 'Anthony Gilliam')], max_length=10),
        ),
    ]