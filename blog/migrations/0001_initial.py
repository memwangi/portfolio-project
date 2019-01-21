# Generated by Django 2.1.5 on 2019-01-20 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(upload_to='images/')),
                ('post', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=150)),
            ],
        ),
    ]
