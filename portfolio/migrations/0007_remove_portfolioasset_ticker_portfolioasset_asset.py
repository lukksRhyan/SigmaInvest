# Generated by Django 5.1.2 on 2024-10-28 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_rename_assets_asset'),
        ('portfolio', '0006_alter_portfolio_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioasset',
            name='ticker',
        ),
        migrations.AddField(
            model_name='portfolioasset',
            name='asset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='asset.asset'),
        ),
    ]