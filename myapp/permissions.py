# myapp/permissions.py
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import migrations

def create_permissions(apps, schema_editor):
    # ค้นหา ContentType ของแอปพลิเคชันของคุณ
    content_type = ContentType.objects.get_for_model(apps.get_model('myapp', 'ModelName'))

    # สร้าง Permission ใหม่
    permission = Permission.objects.create(
        codename='can_view_page',
        name='Can view page',
        content_type=content_type,
    )

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', 'previous_migration'),
    ]
    operations = [
        migrations.RunPython(create_permissions),
    ]
