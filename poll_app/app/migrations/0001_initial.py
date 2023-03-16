# Generated by Django 4.1.2 on 2023-03-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.CharField(max_length=30)),
                ('option2', models.CharField(max_length=30)),
                ('option3', models.CharField(max_length=30)),
                ('option4', models.CharField(max_length=30)),
                ('option1_count', models.IntegerField(default=0)),
                ('option2_count', models.IntegerField(default=0)),
                ('option3_count', models.IntegerField(default=0)),
                ('option4_count', models.IntegerField(default=0)),
            ],
        ),
    ]
