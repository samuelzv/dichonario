# Generated by Django 5.0.6 on 2024-07-31 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0006_alter_author_id_alter_language_id_alter_quote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quote',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
