# Generated by Django 4.2.7 on 2023-12-28 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0004_alter_product_discount_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_discount',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProductApp.product'),
        ),
    ]
