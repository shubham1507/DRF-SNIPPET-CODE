from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username') # new


#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos',
#                   'language', 'style','owner', )

class SnippetSerializer(serializers.HyperlinkedModelSerializer): # new
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField( # new
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'title', 'code', 'linenos',
                  'language', 'style', 'owner',) # new



# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')


class UserSerializer(serializers.HyperlinkedModelSerializer): # new
    snippets = serializers.HyperlinkedRelatedField( # new
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets') # new
