from django.contrib import admin
from MyApp.models import *

admin.site.register(CourseDetails)
admin.site.register(Instructor)
admin.site.register(UserDetails)
admin.site.register(Course_users)
admin.site.register(LecturesModel)

# Register your models here.
