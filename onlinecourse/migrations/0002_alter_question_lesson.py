# Generated by Django 4.2.5 on 2023-09-14 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("onlinecourse", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="lesson",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.lesson"
            ),
        ),
    ]
