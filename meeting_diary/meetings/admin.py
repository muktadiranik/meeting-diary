from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(Member)
admin.site.register(Committee)
admin.site.register(MeetingType)
admin.site.register(Meeting)
