# Generated by Django 3.2.12 on 2023-08-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploadapp', '0004_remove_uploadedfile_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='tags',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]