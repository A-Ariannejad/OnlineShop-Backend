# Generated by Django 3.2.19 on 2023-06-20 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Stores', '0001_initial'),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stores.store'),
        ),
    ]
