# Generated by Django 4.0.4 on 2022-05-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='tag_name',
            field=models.ManyToManyField(to='Post.tag'),
        ),
    ]
