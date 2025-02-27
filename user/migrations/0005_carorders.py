# Generated by Django 4.1.7 on 2024-04-17 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_delete_carorders'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Hubli', max_length=400)),
                ('email', models.CharField(default='Hubli', max_length=400)),
                ('phone_no', models.CharField(default='Hubli', max_length=400)),
                ('address', models.CharField(default='Hubli', max_length=400)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
