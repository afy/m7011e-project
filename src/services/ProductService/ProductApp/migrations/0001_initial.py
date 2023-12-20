# Generated by Django 4.2.7 on 2023-11-22 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ProductApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Special_Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ProductApp.product')),
                ('special_sale', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ProductApp.special_sale')),
            ],
        ),
    ]