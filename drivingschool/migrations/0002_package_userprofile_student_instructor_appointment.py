from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("drivingschool", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Package",
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
                ("name", models.CharField(max_length=100)),
                ("title", models.TextField()),
                ("text", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("hours", models.IntegerField()),
                ("cover", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "user_type",
                    models.CharField(
                        choices=[
                            ("STUDENT", "Student"),
                            ("INSTRUCTOR", "Instructor"),
                            ("SECRETARY", "Secretary"),
                            ("ADMIN", "Admin"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("remaining_hours", models.PositiveIntegerField(default=0)),
                ("purchased_hours", models.PositiveIntegerField(default=0)),
                ("packages", models.ManyToManyField(to="drivingschool.package")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="drivingschool.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Instructor",
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
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="drivingschool.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
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
                ("date", models.DateTimeField()),
                ("duration", models.PositiveIntegerField(default=0)),
                (
                    "lesson_type",
                    models.CharField(
                        choices=[
                            ("autoroute", "Autoroute"),
                            ("parking", "Parking"),
                            ("ville", "Conduite en ville"),
                        ],
                        default="ville",
                        max_length=100,
                    ),
                ),
                ("location", models.CharField(max_length=100)),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="drivingschool.instructor",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="drivingschool.student",
                    ),
                ),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
