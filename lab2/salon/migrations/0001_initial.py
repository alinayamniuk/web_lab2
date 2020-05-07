# Generated by Django 3.0.5 on 2020-05-05 19:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='salon.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master_price', to='salon.Master')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_price', to='salon.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(default='0639999999', max_length=20)),
                ('time', models.IntegerField()),
                ('date', models.DateField()),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='master_order', to='salon.Master')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='service_order', to='salon.Service')),
            ],
        ),
    ]
