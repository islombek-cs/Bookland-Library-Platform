# Generated by Django 5.0.4 on 2024-05-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Free_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_cover', models.ImageField(upload_to='books/covers/')),
                ('book_title', models.CharField(max_length=255)),
                ('book_description', models.TextField()),
                ('book_pdf', models.FileField(upload_to='books/pdfs/')),
            ],
        ),
    ]