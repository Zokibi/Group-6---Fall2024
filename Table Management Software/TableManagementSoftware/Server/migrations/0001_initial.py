# Generated by Django 5.1.1 on 2024-10-06 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeSelection', models.CharField(choices=[('100', 'Charne Robinson'), ('200', 'Jacob Sparks'), ('300', 'Daryna Kozlova'), ('400', 'Isaiah Dillard'), ('500', 'Anthony Gilliam')], max_length=10)),
            ],
        ),
    ]