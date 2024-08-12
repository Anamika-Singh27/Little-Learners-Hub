# Generated by Django 5.0.2 on 2024-04-18 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lh_app', '0011_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=55)),
                ('mother_name', models.CharField(max_length=55)),
                ('father_name', models.CharField(max_length=55)),
                ('phone', models.IntegerField(max_length=10)),
                ('alternative_phone', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=55)),
                ('dob', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=10)),
                ('school_name', models.CharField(max_length=55)),
                ('admission_mode', models.CharField(blank=True, max_length=50)),
                ('fees', models.CharField(max_length=10)),
                ('payment_screenshot', models.FileField(default='', upload_to='lh_app/payment_images')),
                ('photo', models.FileField(default='', upload_to='lh_app/student_images')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lh_app.activity')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lh_app.organization')),
            ],
        ),
    ]
