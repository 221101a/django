# Generated by Django 4.2.5 on 2024-01-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_test", "0002_test_paper"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="test_paper",
            name="id",
        ),
        migrations.AlterField(
            model_name="test_paper",
            name="q_id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
