# Generated by Django 2.2.11 on 2020-03-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rap', '0005_auto_20200317_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gtrcategory',
            options={'verbose_name': 'GtR Category', 'verbose_name_plural': 'GtR Categories'},
        ),
        migrations.AlterModelOptions(
            name='hecategory',
            options={'verbose_name': 'HE Category', 'verbose_name_plural': 'HE Categories'},
        ),
        migrations.AlterModelOptions(
            name='heresearcharea',
            options={'verbose_name': 'HE Research Area', 'verbose_name_plural': 'HE Research Areas'},
        ),
        migrations.AddField(
            model_name='hecategory',
            name='search_terms',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
