# Generated by Django 5.0.6 on 2024-10-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0007_alter_author_id_alter_language_id_alter_quote_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]