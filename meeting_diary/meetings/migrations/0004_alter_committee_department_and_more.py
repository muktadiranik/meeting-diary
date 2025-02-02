# Generated by Django 4.0.8 on 2023-01-13 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meetings', '0003_meeting_department_member_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meetings.department'),
        ),
        migrations.AlterField(
            model_name='committee',
            name='description',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='description',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='committee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meetings.committee'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meetings.department'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='description',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meeting_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meetings.meetingtype'),
        ),
        migrations.AlterField(
            model_name='meetingtype',
            name='description',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]
