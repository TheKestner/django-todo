from rest_framework import serializers
from .models import Todo, Event, Category

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
























# class TodoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     label = serializers.CharField(max_length=500)
#     description = serializers.CharField(max_length=500)
#     due_date = serializers.DateTimeField('date due')
#     status = serializers.BooleanField(True, False)
#     priority = serializers.ChoiceField(choices=PRIORITY_CHOICES, default=MED)

#     def create(self, validated_data):
#         """
#         Create and return a new `todo` instance, given the validated data.
#         """
#         return Todo.objects.create(*validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `todo` instance, given the validated data.
#         """
#         instance.label = validated_data.get('label', instance.label)
#         instance.description = validated_data.get('description', instance.description)
#         instance.due_date = validated_data.get('due_date', instance.due_date)
#         instance.status = serializers.BooleanField('status', instance.status)
#         return instance