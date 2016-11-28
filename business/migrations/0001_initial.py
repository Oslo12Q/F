# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 08:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('dead_time', models.DateTimeField()),
                ('arrived_time', models.CharField(max_length=100, null=True)),
                ('status', models.IntegerField(max_length=11)),
                ('location', models.CharField(max_length=100)),
                ('receive_mode', models.IntegerField(default=2, max_length=11)),
                ('seq', models.IntegerField(default=0, max_length=11)),
                ('card_title', models.CharField(max_length=100)),
                ('card_desc', models.CharField(max_length=255)),
                ('card_icon', models.ImageField(blank=True, upload_to='images/card_icon/%Y/%m/%d')),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BulkProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField(default=0, max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('receive_mode', models.IntegerField(default=2, max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulk_card_title_template', models.TextField(blank=True, null=True)),
                ('bulk_card_desc_template', models.TextField(blank=True, null=True)),
                ('order_card_title_template', models.TextField(blank=True, null=True)),
                ('order_card_desc_template', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('desc', models.TextField(blank=True)),
                ('status', models.IntegerField(max_length=11)),
                ('tag', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DishDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plain', models.TextField(blank=True)),
                ('seq', models.IntegerField(max_length=11)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Dish')),
            ],
            options={
                'verbose_name': 'Dish details',
                'verbose_name_plural': 'Dish details',
            },
        ),
        migrations.CreateModel(
            name='Dispatcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('tail', models.CharField(blank=True, max_length=255)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExhibitedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_2x', models.ImageField(blank=True, null=True, upload_to='images/exhibited_product/%Y/%m/%d')),
                ('cover_3x', models.ImageField(blank=True, null=True, upload_to='images/exhibited_product/%Y/%m/%d')),
                ('seq', models.IntegerField(max_length=11)),
                ('stick', models.BooleanField(default=False)),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Exhibit')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=11)),
            ],
            options={
                'verbose_name': 'Goods',
                'verbose_name_plural': 'Goods',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('md5', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/upload/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('seq', models.IntegerField(max_length=11)),
                ('quantity', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('receive_mode', models.IntegerField(default=2, max_length=11)),
                ('receive_name', models.CharField(blank=True, max_length=200, null=True)),
                ('receive_mob', models.CharField(blank=True, max_length=20, null=True)),
                ('receive_address', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(max_length=11)),
                ('freight', models.IntegerField(max_length=11)),
                ('total_fee', models.IntegerField(max_length=11)),
                ('seq', models.IntegerField(default=0, max_length=11)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('obtain_name', models.CharField(blank=True, max_length=100, null=True)),
                ('obtain_mob', models.CharField(blank=True, max_length=20, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PayRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('third_party_order_id', models.CharField(max_length=200)),
                ('third_party_fee', models.IntegerField(default=0)),
                ('balance_fee', models.IntegerField(default=0)),
                ('use_balance', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('unit_price', models.IntegerField(max_length=11)),
                ('market_price', models.IntegerField(max_length=11)),
                ('tag', models.CharField(blank=True, max_length=20, null=True)),
                ('tag_color', models.CharField(blank=True, max_length=20, null=True)),
                ('spec', models.CharField(max_length=100)),
                ('spec_desc', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='images/product/%Y/%m/%d')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('limit', models.IntegerField(max_length=11, null=True)),
                ('stock', models.IntegerField(default=0, max_length=11)),
                ('purchased', models.IntegerField(default=0, max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/product_details/%Y/%m/%d')),
                ('plain', models.TextField()),
                ('seq', models.IntegerField(max_length=11)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product details',
                'verbose_name_plural': 'Product details',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('desc', models.TextField(blank=True)),
                ('status', models.IntegerField(max_length=11)),
                ('tag', models.CharField(blank=True, max_length=200, null=True)),
                ('time', models.CharField(blank=True, max_length=200, null=True)),
                ('cover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Image')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeExhibit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reseller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('tail', models.CharField(blank=True, max_length=255)),
                ('state', models.IntegerField(default=0, max_length=11)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mob', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('key', models.IntegerField(blank=True, max_length=11, null=True)),
                ('image', models.ImageField(upload_to='images/slide/%Y/%m/%d')),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('seq', models.IntegerField(max_length=11)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plain', models.TextField(blank=True)),
                ('seq', models.IntegerField(max_length=11)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Image')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Recipe')),
            ],
            options={
                'verbose_name': 'Step details',
                'verbose_name_plural': 'Step details',
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('mob', models.CharField(blank=True, max_length=100, null=True)),
                ('opening_time', models.IntegerField(blank=True, max_length=11, null=True)),
                ('closing_time', models.IntegerField(blank=True, max_length=11, null=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('is_custom', models.BooleanField(default=False)),
                ('reseller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Reseller')),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plain', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('balance', models.IntegerField(default=0, max_length=11)),
                ('recent_obtain_name', models.CharField(blank=True, max_length=100, null=True)),
                ('recent_obtain_mob', models.CharField(blank=True, max_length=20, null=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('mob_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('recent_storage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Storage')),
            ],
        ),
        migrations.CreateModel(
            name='BulkDetails',
            fields=[
                ('bulk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.Bulk')),
                ('reseller_name', models.CharField(blank=True, max_length=100, null=True)),
                ('reseller_mob', models.CharField(blank=True, max_length=20, null=True)),
                ('bulk_title', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('dead_time', models.DateTimeField()),
                ('bulk_status', models.IntegerField(max_length=11)),
                ('bulk_receive_mode', models.IntegerField(max_length=11)),
                ('countsize', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'view_bulk_reseller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BulkSummary',
            fields=[
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.Product')),
                ('total_price', models.IntegerField(max_length=11)),
                ('quantity', models.IntegerField(max_length=11)),
                ('spec', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'view_bulk_summary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.Order')),
                ('mob', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('receive_mode', models.IntegerField(default=2, max_length=11)),
                ('total_fee', models.IntegerField(max_length=11)),
                ('status', models.IntegerField(max_length=11)),
                ('pay_status', models.IntegerField(default=0)),
                ('third_party_fee', models.IntegerField(default=0)),
                ('third_party_order_id', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField()),
                ('product', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'view_bulk_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PurchasedProductHistory',
            fields=[
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='business.Order')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(max_length=11)),
                ('spec', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'view_history_purchased_products',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.User'),
        ),
        migrations.AddField(
            model_name='reseller',
            name='mob_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recipeexhibit',
            name='slides',
            field=models.ManyToManyField(to='business.Slide'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tips',
            field=models.ManyToManyField(to='business.Tip'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.User'),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Category'),
        ),
        migrations.AddField(
            model_name='payrequest',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='business.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='bulk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Bulk'),
        ),
        migrations.AddField(
            model_name='order',
            name='storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Storage'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.User'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Recipe'),
        ),
        migrations.AddField(
            model_name='goods',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Order'),
        ),
        migrations.AddField(
            model_name='goods',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Product'),
        ),
        migrations.AddField(
            model_name='goods',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.User'),
        ),
        migrations.AddField(
            model_name='exhibitedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Product'),
        ),
        migrations.AddField(
            model_name='exhibit',
            name='hot_bulks',
            field=models.ManyToManyField(to='business.Bulk'),
        ),
        migrations.AddField(
            model_name='exhibit',
            name='hot_products',
            field=models.ManyToManyField(through='business.ExhibitedProduct', to='business.Product'),
        ),
        migrations.AddField(
            model_name='exhibit',
            name='slides',
            field=models.ManyToManyField(to='business.Slide'),
        ),
        migrations.AddField(
            model_name='dispatcher',
            name='mob_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dishdetails',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Image'),
        ),
        migrations.AddField(
            model_name='dish',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Image'),
        ),
        migrations.AddField(
            model_name='dish',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Recipe'),
        ),
        migrations.AddField(
            model_name='dish',
            name='tips',
            field=models.ManyToManyField(to='business.Tip'),
        ),
        migrations.AddField(
            model_name='dish',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.User'),
        ),
        migrations.AddField(
            model_name='bulkproduct',
            name='bulk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Bulk'),
        ),
        migrations.AddField(
            model_name='bulkproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Product'),
        ),
        migrations.AddField(
            model_name='bulk',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Category'),
        ),
        migrations.AddField(
            model_name='bulk',
            name='products',
            field=models.ManyToManyField(through='business.BulkProduct', to='business.Product'),
        ),
        migrations.AddField(
            model_name='bulk',
            name='reseller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Reseller'),
        ),
        migrations.AddField(
            model_name='bulk',
            name='storages',
            field=models.ManyToManyField(to='business.Storage'),
        ),
    ]