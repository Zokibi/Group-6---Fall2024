# Generated by Django 5.1.1 on 2024-09-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0003_delete_employeeclockin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
