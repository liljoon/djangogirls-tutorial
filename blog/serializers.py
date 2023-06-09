from blog.models import Post
from rest_framework import serializers
from django.contrib.auth import get_user

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'text', 'created_date', 'published_date', 'image')
