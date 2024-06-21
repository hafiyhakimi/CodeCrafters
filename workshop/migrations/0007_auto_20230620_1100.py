# Generated by Django 3.2.9 on 2023-06-20 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshop', '0006_inbox'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbox',
            name='WorkshopFk',
        ),
        migrations.AlterField(
            model_name='inbox',
            name='Participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
