from django.apps import AppConfig


class StaffListConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff_list'
INSTALLED_APPS = [
    'staff_list.apps.StaffListConfig',
]
