# Generated by Django 5.0.2 on 2024-04-26 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lh_app', '0014_alter_admission_admission_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgQr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_pic', models.FileField(default='', upload_to='lh_app/qr_images')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lh_app.organization')),
            ],
        ),
    ]
