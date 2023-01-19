# Generated by Django 4.1.3 on 2023-01-19 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll_app', '0009_alter_poll_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='user_id',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
