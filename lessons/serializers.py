from rest_framework import serializers

from lessons.models import Lesson, LessonsTaken


class LessonSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    lessons_taken = serializers.SerializerMethodField()

    def create(self, validated_data):
        return LessonsTaken.objects.create(**validated_data)

    def get_lessons_taken(self, obj):
        return LessonsTaken.objects.filter(user=obj.user).count()

    class Meta:
        model = Lesson
        fields = "__all__"
        # fields = ("title", "text", "user", "lessons_taken")
