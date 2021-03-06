# Generated by Django 3.0.2 on 2020-01-05 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djpaddle.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('billing_type', models.CharField(choices=[('day', 'day'), ('month', 'month'), ('year', 'year')], max_length=255)),
                ('billing_period', models.IntegerField()),
                ('trial_days', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('cancel_url', models.URLField()),
                ('checkout_id', models.CharField(max_length=32)),
                ('currency', models.CharField(max_length=3)),
                ('email', models.EmailField(max_length=254)),
                ('event_time', models.DateTimeField()),
                ('marketing_consent', models.BooleanField()),
                ('next_bill_date', models.DateTimeField()),
                ('passthrough', models.TextField()),
                ('quantity', models.IntegerField()),
                ('source', models.URLField()),
                ('status', models.CharField(choices=[('active', 'active'), ('trialing', 'trialing'), ('past_due', 'past due'), ('paused', 'paused'), ('deleted', 'deleted')], max_length=16)),
                ('unit_price', models.FloatField()),
                ('update_url', models.URLField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djpaddle.Plan')),
                ('subscriber', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currency', djpaddle.fields.PaddleCurrencyCodeField(help_text='Three-letter ISO currency code', max_length=3)),
                ('quantity', models.FloatField()),
                ('recurring', models.BooleanField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='djpaddle.Plan')),
            ],
            options={
                'ordering': ['currency', 'recurring'],
                'unique_together': {('plan', 'currency', 'recurring')},
            },
        ),
    ]
