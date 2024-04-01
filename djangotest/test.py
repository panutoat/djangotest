import os
from django.conf import settings

# กำหนดค่า DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangotest.settings')

# เรียกใช้งาน settings.configure() เพื่อกำหนดค่า
settings.configure()

# โหลดแอปพลิเคชันของ Django
import django
django.setup()

# เรียกใช้งานโมดูล Django
from django.contrib.auth.models import User, Group, Permission

# ทำสิ่งที่คุณต้องการกับโมดูล Django ต่อไปนี้
