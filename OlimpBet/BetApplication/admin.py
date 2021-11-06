from django.contrib import admin

from .models import *

admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Category)
admin.site.register(CustomUser)

# Register your models here.
