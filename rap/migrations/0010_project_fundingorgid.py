# Generated by Django 2.2.11 on 2020-03-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0009_auto_20200318_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='FundingOrgId',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
