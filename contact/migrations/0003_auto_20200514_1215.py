# Generated by Django 3.0.5 on 2020-05-14 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0002_contact_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AddField(
            model_name='contact',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
