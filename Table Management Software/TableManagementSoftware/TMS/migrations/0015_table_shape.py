# Generated by Django 5.1.1 on 2024-11-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0014_alter_orderitem_item_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='shape',
            field=models.CharField(choices=[('circle', 'circle'), ('rect', 'rect')], default=0, max_length=30),
            preserve_default=False,
        ),
    ]
