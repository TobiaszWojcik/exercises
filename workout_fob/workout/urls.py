from django.urls import path, include
from .views import *


app_name = 'exercises'

urlpatterns = [
    path('bodyparts/', BodyPartsList.as_view(), name='body_parts_list'),
    path('exercie/', ExerciseCreate.as_view, name='exercise_add'),
    path('exercie/<int:pk>', ExerciseDetile.as_view(), name='exercise_detail'),
    path('bodypart/<int:id>', ExercisesList.as_view(), name='exercises_list'),
    path('workouts/', WorkoutList.as_view(), name='workout_list'),
    path('workout/<int:pk>', Workout.as_view(), name='workout'),
    path('', BodyPartsList.as_view(), name='exercises_list'),
]