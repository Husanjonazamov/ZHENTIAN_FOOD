# Generated by Django 5.1.3 on 2025-06-25 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_productmodel_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='table',
        ),
    ]
