from django.contrib import admin
from .models import Waitlist

# Register your models here.


admin.site.site_header = "fix36 Admin"
admin.site.register(Waitlist)