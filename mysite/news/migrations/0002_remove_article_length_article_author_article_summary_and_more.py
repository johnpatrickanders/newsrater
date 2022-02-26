# Generated by Django 4.0 on 2022-02-26 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='length',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Piper', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(default='About Piper', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.article'),
        ),
    ]
