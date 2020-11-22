# Generated by Django 3.1.1 on 2020-09-08 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('card_type', models.CharField(choices=[('B', 'Banner Card'), ('T', 'Team Card'), ('S', 'Service Card')], default='B', max_length=200)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]