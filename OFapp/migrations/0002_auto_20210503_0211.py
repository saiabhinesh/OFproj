# Generated by Django 3.2 on 2021-05-02 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OFapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collections_table',
            name='description',
            field=models.CharField(default=23, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collections_table',
            name='title',
            field=models.CharField(default=45, max_length=50),
            preserve_default=False,
        ),
    ]
