# Generated by Django 4.0.6 on 2022-08-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='through_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='university',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profileImg/'),
        ),
    ]