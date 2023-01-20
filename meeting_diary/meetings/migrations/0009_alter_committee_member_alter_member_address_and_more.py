# Generated by Django 4.0.8 on 2023-01-13 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0008_alter_meeting_acknowledged_member_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='member',
            field=models.ManyToManyField(blank=True, to='meetings.member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meetings.department'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
