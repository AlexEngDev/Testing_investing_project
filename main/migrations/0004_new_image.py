# Generated by Django 4.1.5 on 2023-02-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_new_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="new",
            name="image",
            field=models.ImageField(default="", upload_to="main/images/"),
            preserve_default=False,
        ),
    ]