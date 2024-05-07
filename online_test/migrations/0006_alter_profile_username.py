# Generated by Django 4.2.5 on 2024-02-28 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("online_test", "0005_profile_address_alter_profile_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="username",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="online_test.user",
            ),
        ),
    ]
