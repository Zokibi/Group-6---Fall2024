# Generated by Django 5.1.1 on 2024-10-14 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0006_alter_item_price_alter_table_chairs'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ManyToManyField(to='TMS.table'),
        ),
    ]
