# Generated by Django 4.1.2 on 2022-11-01 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodypart',
            name='icon',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
    ]