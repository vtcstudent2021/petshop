# Generated by Django 4.2 on 2024-04-27 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
    ]