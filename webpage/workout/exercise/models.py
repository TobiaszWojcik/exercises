from django.db import models
from django.urls import reverse

class BodyPart(models.Model):
    name = models.CharField(max_length=250)
    icon = models.FileField(null=True)

    def __str__(self):
        return self.name


class ExerciseType(models.Model):
    name = models.CharField(max_length=250)
    icon = models.FileField(null=True)

    def __str__(self):
        return self.name


class Exercises(models.Model):
    name = models.CharField(max_length=250)
    body_part = models.ManyToManyField(BodyPart)
    icon = models.FileField(null=True)
    type = models.ManyToManyField(ExerciseType)

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('exercises:exercie', kwargs={'pk': self.pk})


class Workout(models.Model):
    date = models.DateField()
    exercises = models.ManyToManyField(Exercises)
    type = models.ForeignKey(ExerciseType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.date} - {self.type}'
    #
    # def get_absolut_url(self):
    #     return reverse('exercises:workout_list', kwargs={'pk': self.pk})


class Series(models.Model):
    date = models.DateField(auto_now=True)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    series1 = models.CharField(max_length=10, default='0')
    series2 = models.CharField(max_length=10, default='0')
    series3 = models.CharField(max_length=10, default='0')
    series4 = models.CharField(max_length=10, default='0')
    wage1 = models.CharField(max_length=10, default='0')
    wage2 = models.CharField(max_length=10, default='0')
    wage3 = models.CharField(max_length=10, default='0')
    wage4 = models.CharField(max_length=10, default='0')

    def __str__(self):
        return f'{self.date} - {self.exercise}'
