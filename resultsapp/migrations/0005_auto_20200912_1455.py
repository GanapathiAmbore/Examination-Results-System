# Generated by Django 2.2 on 2020-09-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultsapp', '0004_auto_20200911_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='halticket',
            name='htno',
        ),
        migrations.AlterField(
            model_name='halticket',
            name='id',
            field=models.CharField(blank=True, max_length=150, primary_key=True, serialize=False),
        ),
    ]
