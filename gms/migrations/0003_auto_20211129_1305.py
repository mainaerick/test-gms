# Generated by Django 3.1.8 on 2021-11-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gms', '0002_namespaces'),
    ]

    operations = [
        migrations.AddField(
            model_name='namespaces',
            name='tenantz',
            field=models.ManyToManyField(to='gms.Tenants'),
        ),
        migrations.AddField(
            model_name='tenants',
            name='regionz',
            field=models.ManyToManyField(to='gms.Regions'),
        ),
    ]
