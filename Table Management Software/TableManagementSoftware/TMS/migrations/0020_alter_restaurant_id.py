# Generated by Django 5.1.1 on 2024-11-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0019_alter_table_guests_alter_table_shape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
