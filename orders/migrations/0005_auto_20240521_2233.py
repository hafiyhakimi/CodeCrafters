# Generated by Django 3.2.9 on 2024-05-21 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='creditnumber',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cvv',
        ),
        migrations.RemoveField(
            model_name='order',
            name='expiration',
        ),
        migrations.RemoveField(
            model_name='order',
            name='namecard',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping',
        ),
    ]