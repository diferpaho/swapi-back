# Generated by Django 2.2.13 on 2022-02-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220202_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(choices=[('black', 'BLACK'), ('brown', 'BROWN'), ('yellow', 'YELLOW'), ('red', 'RED'), ('green', 'GREEN'), ('purple', 'PURPLE'), ('unknow', 'UNKNOWN')], max_length=32),
        ),
    ]
