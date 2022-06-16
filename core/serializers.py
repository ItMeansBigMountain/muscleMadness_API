from rest_framework import serializers
from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        # fields = ( "id" , "title" , "passage_body" , "author" , "email" , "date" )
        fields = "__all__"

