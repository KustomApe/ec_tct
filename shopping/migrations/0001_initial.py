# Generated by Django 3.2.6 on 2022-07-01 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'カテゴリ',
                'verbose_name_plural': 'カテゴリ',
                'ordering': ['-category_id'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('manufacturer', models.CharField(max_length=32)),
                ('color', models.CharField(max_length=16)),
                ('price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('recommended', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.category')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'ordering': ['-item_id'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('destination', models.CharField(max_length=256)),
                ('booked_date', models.DateTimeField(auto_now_add=True)),
                ('cancel', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'verbose_name': '購入履歴',
                'verbose_name_plural': '購入履歴',
                'ordering': ['-booked_date'],
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('purchase_detail_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('amount', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.item')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.purchase')),
            ],
            options={
                'verbose_name': '注文詳細',
                'verbose_name_plural': '注文詳細',
                'ordering': ['-purchase_detail_id'],
            },
        ),
        migrations.CreateModel(
            name='ItemsInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('booked_date', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'verbose_name': 'ショッピングカート',
                'verbose_name_plural': 'ショッピングカート',
                'ordering': ['-booked_date'],
            },
        ),
    ]
