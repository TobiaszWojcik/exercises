from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(BodyPart)
admin.site.register(Exercises)
admin.site.register(ExerciseType)
admin.site.register(Workout)
admin.site.register(Series)