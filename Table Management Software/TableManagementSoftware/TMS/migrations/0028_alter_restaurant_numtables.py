# Generated by Django 5.1.1 on 2024-12-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0027_alter_table_employee_alter_table_shape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='numTables',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
