# Generated by Django 4.0.8 on 2023-01-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0011_rename_description_meetingtype_meeting_type_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('ongoing', 'Ongoing'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=50, null=True),
        ),
    ]