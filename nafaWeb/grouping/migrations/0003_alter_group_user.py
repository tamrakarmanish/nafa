# Generated by Django 4.0.4 on 2022-05-03 13:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grouping', '0002_group_delete_grouping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='group_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
