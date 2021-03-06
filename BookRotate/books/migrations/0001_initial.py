# Generated by Django 2.1.3 on 2020-01-09 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=100, null=True)),
                ('isbn', models.CharField(max_length=100, null=True)),
                ('publisher', models.TextField(max_length=100)),
                ('categories', models.TextField(max_length=500)),
                ('language', models.TextField(max_length=30)),
                ('genre', models.TextField(max_length=200)),
                ('pub_year', models.DateTimeField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bookshelf',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_status', models.TextField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('ff', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('current_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_reader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_user_2', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_user_1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField(blank=True, max_length=520)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('bookshelf', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='library', to='books.Bookshelf')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_languages', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.TextField(max_length=500)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
