from django.db import models
from django.contrib.auth.models import Permission

class MyModel(models.Model):
    # กำหนดฟิลด์ที่ต้องการให้มี Permissions
    can_do_something = models.BooleanField(default=False)

# สร้าง Permission ใหม่
permission = Permission.objects.create(
    codename='can_do_something',
    name='Can do something',
)
