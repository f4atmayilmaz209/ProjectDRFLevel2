# Generated by Django 3.2.12 on 2022-02-11 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitaplar', '0002_alter_yorum_yorum_sahibi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitap',
            name='guncellenme_tarihi',
        ),
        migrations.RemoveField(
            model_name='kitap',
            name='yaratilma_tarihi',
        ),
    ]
