# Generated by Django 5.1.1 on 2024-11-24 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0018_alter_table_table_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='guests',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='table',
            name='shape',
            field=models.CharField(choices=[('circle', 'circle'), ('rect', 'rect')], default='rect', max_length=30),
        ),
    ]