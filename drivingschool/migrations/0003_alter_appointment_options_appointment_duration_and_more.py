from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("drivingschool", "0002_package_userprofile_student_instructor_appointment"),
    ]
    operations = [
        migrations.AlterModelOptions(
            name="appointment",
            options={"ordering": ["-date"]},
        ),
        migrations.AddField(
            model_name="appointment",
            name="duration",
            field=models.PositiveIntegerField(default=0, help_text="Durée de la leçon"),
        ),
        migrations.AddField(
            model_name="appointment",
            name="lesson_type",
            field=models.CharField(
                choices=[
                    ("autoroute", "Autoroute"),
                    ("parking", "Parking"),
                    ("ville", "Conduite en ville"),
                ],
                default="ville",
                max_length=100,
            ),
        ),
    ]
