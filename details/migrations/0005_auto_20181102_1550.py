# Generated by Django 2.1.3 on 2018-11-02 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_auto_20181102_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artifactdetail',
            old_name='artifact_desc',
            new_name='artifact_description',
        ),
    ]
