# Generated by Django 4.1.3 on 2023-11-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EPCR",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("incident_number", models.CharField(max_length=50, unique=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("dob", models.DateField()),
                ("gender", models.CharField(max_length=10)),
                ("medical_history", models.TextField(blank=True)),
                ("incident_details", models.TextField()),
                ("responding_unit", models.CharField(max_length=100)),
                ("personnel", models.TextField()),
                ("assessment_findings", models.TextField(blank=True)),
                ("treatments", models.TextField(blank=True)),
                ("outcome", models.TextField(blank=True)),
                ("alcohol_involved", models.BooleanField(default=False)),
                ("overdose_type", models.CharField(max_length=100)),
                ("signature", models.TextField()),
            ],
        ),
    ]
