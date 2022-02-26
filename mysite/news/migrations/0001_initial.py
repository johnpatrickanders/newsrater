# Generated by Django 4.0 on 2021-12-18 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('length', models.IntegerField()),
                ('source', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=300)),
                ('pub_date',
                 models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('article',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='news.article')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='auth.user')),
            ],
        ),
    ]
