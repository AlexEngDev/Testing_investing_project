# Generated by Django 4.1.5 on 2023-02-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_rename_news_new"),
    ]

    operations = [
        migrations.AlterField(
            model_name="new", name="date", field=models.DateTimeField(null=True),
        ),
    ]