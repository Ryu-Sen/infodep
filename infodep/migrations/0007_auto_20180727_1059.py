# Generated by Django 2.0.7 on 2018-07-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infodep', '0006_kitting_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitting',
            name='job_date',
            field=models.DateTimeField(null=True, verbose_name='job date'),
        ),
    ]