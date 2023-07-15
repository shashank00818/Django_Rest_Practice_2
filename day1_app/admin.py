from django.contrib import admin
from day1_app.models import Friends
# Register your models here.

# This will show the Friends model on url/admin
@admin.register(Friends)  # this will connect the model friends to admin
class Friends_admin(admin.ModelAdmin):
    list_display=['id','name','age','city','gender']