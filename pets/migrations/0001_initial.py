# Generated by Django 3.2.16 on 2022-10-21 14:59

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
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('cat', 'Cat'), ('dog', 'Dog'), ('bird', 'Bird'), ('horse', 'Horse'), ('wildanimal', 'Wild animal'), ('exoticanimal', 'Exotic animal'), ('mammal', 'Mammal'), ('fish', 'Fish'), ('reptile', 'Reptile'), ('insecs', 'Insect'), ('other', 'Other')], default='other', max_length=50)),
                ('description', models.TextField(blank=True, max_length=365)),
                ('image', models.ImageField(default='../petprofile_svixn2', upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_of_birth', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddConstraint(
            model_name='pet',
            constraint=models.UniqueConstraint(fields=('owner', 'name', 'date_of_birth'), name='pet_naming_constraint'),
        ),
    ]
