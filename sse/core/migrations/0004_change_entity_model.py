# Generated by Django 2.1.3 on 2018-11-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='concept_code',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='entity',
            name='omop_id',
            field=models.IntegerField(),
        ),
    ]
