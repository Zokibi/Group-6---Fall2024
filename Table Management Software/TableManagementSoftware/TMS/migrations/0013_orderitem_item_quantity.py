# Generated by Django 5.1.1 on 2024-11-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0012_alter_item_order_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='item_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
