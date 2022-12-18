from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.shortcuts import get_object_or_404
from datetime import date
from .models import *



class BodyPartsList(ListView):
    model = BodyPart
    template_name = 'list_view.html'


class ExercisesList(ListView):
    model = Exercises
    template_name = 'exercise_list.html'
    print('krok3')

    def get_queryset(self):
        selection = self.kwargs.get('id')
        ordering = 'name'
        if selection:
            queryset = Exercises.objects.filter(body_part=selection)
        else:
            queryset = Exercises.objects.all()
        return queryset


class ExerciseDetile(DetailView):
    model = Exercises
    template_name = 'exercise_detile.html'


class ExerciseCreate(CreateView):
    model = Exercises
    template_name = 'exercise_detile.html'


class BodyPartsList(ListView):
    model = BodyPart
    template_name = 'bodypart_list.html'


class WorkoutList(ListView):
    model = Workout
    template_name = 'workout_list.html'
    # queryset = Workout.objects.filter(date=date.today())


class Workout(DetailView):
    model = Workout
    template_name = 'workout.html'

class AddTrening(FormView):
    form_class = Workout
    temple


