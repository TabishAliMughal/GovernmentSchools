# Generated by Django 3.0.5 on 2020-05-05 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('documenttype', models.CharField(max_length=250)),
            ],
        ),
    ]
