# Generated by Django 5.0.6 on 2024-07-31 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_language_language_supported_only_en_or_es'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quote',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
