# Generated by Django 3.1.4 on 2020-12-18 16:10

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('str_schl', models.CharField(blank=True, max_length=5, null=True)),
                ('baumgruppe', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'trees_data',
                'managed': False,
            },
        ),
    ]