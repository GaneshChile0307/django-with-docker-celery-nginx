# Generated by Django 4.1.7 on 2024-01-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_alter_profile_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                default="O",
                max_length=20,
                verbose_name="gender",
            ),
        ),
    ]
