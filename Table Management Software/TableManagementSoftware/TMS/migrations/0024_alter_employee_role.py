# Generated by Django 5.1.1 on 2024-12-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0023_alter_employee_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('HOST', 'HOST'), ('SERVER', 'SERVER')], default='SERVER', max_length=10),
        ),
    ]
