# Generated by Django 3.0.5 on 2020-05-07 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('semis_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionArea',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionBoundaryWall',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('ifyes', models.CharField(blank=True, choices=[('C', 'Complete'), ('I', 'InComplete')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionBuildingCondition',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('condition', models.CharField(choices=[('G', 'Good'), ('R', 'Repairable'), ('D', 'Dangerous')], max_length=10)),
                ('ifrepairable', models.CharField(blank=True, choices=[('F', 'Floor'), ('R', 'Roof'), ('W', 'Walls')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionElectricityAvailiblity',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('meter', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=10, null=True)),
                ('meterno', models.IntegerField(blank=True, null=True)),
                ('consumerno', models.IntegerField(blank=True, null=True)),
                ('contactaccnp', models.IntegerField(blank=True, null=True)),
                ('kunda', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('solar', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('solarqty', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionFurniture',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('therefor', models.CharField(choices=[('S', 'Students'), ('T', 'Staff')], max_length=10)),
                ('dualdeskqty', models.IntegerField(blank=True, null=True)),
                ('chairsqty', models.IntegerField(blank=True, null=True)),
                ('tablesqty', models.IntegerField(blank=True, null=True)),
                ('shelvesqty', models.IntegerField(blank=True, null=True)),
                ('lockersqty', models.IntegerField(blank=True, null=True)),
                ('cupboardqty', models.IntegerField(blank=True, null=True)),
                ('others', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionPlantation',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('qtyoftrees', models.IntegerField(blank=True, null=True)),
                ('qtyofplants', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionPlayGround',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('type', models.CharField(blank=True, choices=[('H', 'Huge'), ('N', 'Normal'), ('S', 'Small')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionPlumbingAvailiblity',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('condition', models.CharField(choices=[('G', 'Good'), ('R', 'Repairable'), ('D', 'Dangerous')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionWiringAvailiblity',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('condition', models.CharField(choices=[('G', 'Good'), ('R', 'Repairable'), ('D', 'Dangerous')], max_length=10)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionWaterDispenserAvailiblity',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('type', models.CharField(blank=True, choices=[('E', 'Electric-Chiller'), ('C', 'Cooler')], max_length=10, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionWaterAvailiblity',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('availabletype', models.CharField(blank=True, choices=[('D', 'Drinking'), ('N', 'Non-Drinking')], max_length=10, null=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionToiletAvailiblity',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('functionalqty', models.IntegerField(blank=True, null=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionSenitaryAvailiblity',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionROPlantAvailiblity',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=10)),
                ('type', models.CharField(blank=True, choices=[('F', 'Functional'), ('N', 'Non-Functional')], max_length=10, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionRooms',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('therefor', models.CharField(choices=[('S', 'Students'), ('T', 'Staff')], max_length=10)),
                ('rooms', models.IntegerField()),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.Institution')),
            ],
        ),
    ]
