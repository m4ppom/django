from rest_framework import serializers
from .models import Artist, Music, Comment

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id')


class ArtistDetailSerializer(ArtistSerializer):
    music_set = MusicSerializer(many=True)
    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('music_set',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id')

class MusicDetailSerializer(MusicSerializer):
    comment = CommentSerializer(source='connemt_set', many=True)
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comments',)

