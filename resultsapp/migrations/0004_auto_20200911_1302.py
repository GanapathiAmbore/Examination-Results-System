# Generated by Django 2.2 on 2020-09-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultsapp', '0003_auto_20200911_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='halticket',
            name='htno',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
