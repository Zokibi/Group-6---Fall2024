# Generated by Django 5.1.1 on 2024-09-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0004_employees_delete_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='employeeSelection',
            field=models.CharField(choices=[('server', 'Isaiah Dillard'), ('manager', 'Anthony Gilliam')], default='Anthony Gilliam', max_length=7),
            preserve_default=False,
        ),
    ]
