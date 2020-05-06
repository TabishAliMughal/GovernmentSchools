# Generated by Django 3.0.5 on 2020-05-05 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
        ('main', '0002_documenttype'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_userdocuments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Employ',
        ),
        migrations.RenameModel(
            old_name='UserDocuments',
            new_name='EmployDocuments',
        ),
        migrations.AlterField(
            model_name='employdocuments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
