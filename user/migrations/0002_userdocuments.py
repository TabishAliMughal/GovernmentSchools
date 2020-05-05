# Generated by Django 3.0.5 on 2020-05-05 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_documenttype'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDocuments',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('picture', models.ImageField(upload_to='static/images/user/%user')),
                ('documenttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.DocumentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
