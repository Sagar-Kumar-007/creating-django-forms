# Generated by Django 3.1.3 on 2021-05-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_creation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedata',
            name='branch',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storedata',
            name='email',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storedata',
            name='phone',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
