# Generated by Django 3.2.19 on 2023-06-21 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_product_store'),
        ('Baskets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketmtmproduct',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ps', to='Baskets.basket'),
        ),
        migrations.AlterField(
            model_name='basketmtmproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ps', to='Products.product'),
        ),
    ]
