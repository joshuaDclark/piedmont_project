# Generated by Django 2.1.2 on 2018-10-09 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=40, null=True)),
            ],
        ),
    ]
