# Generated by Django 5.1.3 on 2025-06-26 07:12

import core.apps.api.models.product
import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_productmodel_table_alter_optionsmodel_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='table',
            field=django_ckeditor_5.fields.CKEditor5Field(default=core.apps.api.models.product.load_default_description),
        ),
    ]
