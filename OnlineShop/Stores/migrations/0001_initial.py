# Generated by Django 3.2.19 on 2023-06-21 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('image', models.ImageField(upload_to='store_images/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=100)),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('rate_number', models.IntegerField(default=0)),
            ],
        ),
    ]
