# Generated by Django 5.1.2 on 2024-10-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
