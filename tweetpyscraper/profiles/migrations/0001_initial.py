# Generated by Django 2.0.1 on 2018-01-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=255)),
                ('image', models.URLField(max_length=100)),
            ],
        ),
    ]
