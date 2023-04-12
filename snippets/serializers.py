from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    #

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', queryset=Snippet.objects.all()
    )
    # PrimaryKeyRelatedField may be used to represent the target of the relationship using its primary key.

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


