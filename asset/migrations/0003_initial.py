# Generated by Django 5.1.2 on 2024-10-18 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0002_delete_asset'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssetSector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10, unique=True)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.assetclassification')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.assetsector')),
            ],
        ),
    ]
