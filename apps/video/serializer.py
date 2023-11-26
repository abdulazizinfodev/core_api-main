from rest_framework import serializers
from .models import VideoApp, ModulClass, Comment
from apps.users.serializers import UserReadSerializer


# class ModulSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ModulClass
#         fields = ('id', 'name',)


# class ModulSerializer(serializers.ModelSerializer):
#     all_videos = serializers.SerializerMethodField()

#     class Meta:
#         model = ModulClass
#         fields = ('id', 'name', 'all_videos',)

#     def get_all_videos(self, obj):
#         module_videos = VideoApp.objects.filter(modul=obj)
#         return [video.name for video in module_videos]

class CommentSerializer(serializers.ModelSerializer):
    created_by = UserReadSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'created_by', 'comment',)


class VideoAppSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True)

    class Meta:
        model = VideoApp
        fields = ('id', 'name', 'video', 'description',
                  'comment', 'created_at', 'marked_view')


class ModulSerializer(serializers.ModelSerializer):
    videos = VideoAppSerializer(
        source='videoapp_set', many=True, read_only=True)

    class Meta:
        model = ModulClass
        fields = ('id', 'name', 'videos', 'created_at')


# class VideoAppSerializer(serializers.ModelSerializer):
#     modul = ModulSerializer(read_only=True)
#     comment = CommentSerializer()

#     class Meta:
#         model = VideoApp
#         fields = ('id', 'modul', 'name',
#                   'description', 'marked_view', 'comment', 'video', 'get_thumbnail',)
