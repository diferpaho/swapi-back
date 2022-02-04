# Generated by Django 2.2.13 on 2022-02-04 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220202_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='home_world',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='inhabitants', to='app.Planet'),
        ),
    ]
