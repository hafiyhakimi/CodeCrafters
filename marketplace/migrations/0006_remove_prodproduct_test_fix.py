# Generated by Django 3.2.9 on 2024-06-13 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_prodproduct_test_fix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prodproduct',
            name='test_fix',
        ),
    ]
