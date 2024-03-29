# Generated by Django 4.1.7 on 2024-01-28 13:57

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0003_alter_profile_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="city",
            field=models.CharField(
                default="Nariobi", max_length=180, verbose_name="city"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="country",
            field=django_countries.fields.CountryField(
                default="KE", max_length=2, verbose_name="country"
            ),
        ),
    ]
