# Generated by Django 5.1.1 on 2024-11-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0013_orderitem_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item_quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='numTables',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='table',
            name='seats',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
