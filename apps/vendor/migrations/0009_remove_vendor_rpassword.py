# Generated by Django 3.0.14 on 2021-07-12 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_vendor_rpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='rpassword',
        ),
    ]
