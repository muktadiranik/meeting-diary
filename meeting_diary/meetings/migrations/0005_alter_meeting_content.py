# Generated by Django 4.0.8 on 2023-01-13 15:04

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0004_alter_committee_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='content',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]