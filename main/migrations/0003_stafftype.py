# Generated by Django 3.0.3 on 2020-05-06 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_documenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffType',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(max_length=250)),
            ],
        ),
    ]
