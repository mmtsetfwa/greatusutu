# Generated by Django 3.1.1 on 2020-09-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20200911_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='team_member_description',
            field=models.TextField(blank=True, help_text='only for team members'),
        ),
    ]
