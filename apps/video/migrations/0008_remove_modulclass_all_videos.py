# Generated by Django 4.2.7 on 2023-11-26 03:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0007_videoapp_marked_view"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="modulclass",
            name="all_videos",
        ),
    ]