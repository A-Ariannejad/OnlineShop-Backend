# Generated by Django 3.2.19 on 2023-06-20 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RateStore', '0001_initial'),
        ('Stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratestore',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stores.store'),
        ),
    ]
