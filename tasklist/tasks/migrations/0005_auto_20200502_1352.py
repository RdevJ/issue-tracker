# Generated by Django 3.0.5 on 2020-05-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200430_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
