from django.contrib import admin
from .models import Department ,Course,Major,Semester
# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Major)
admin.site.register(Semester)

