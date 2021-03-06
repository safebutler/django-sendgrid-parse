# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django_sendgrid_parse.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_sendgrid_parse', '0008_auto_20170214_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(max_length=1000, upload_to=django_sendgrid_parse.models.attachments_file_upload, verbose_name='Attached File'),
        ),
    ]
