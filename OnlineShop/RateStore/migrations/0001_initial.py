# Generated by Django 3.2.19 on 2023-06-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RateStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]