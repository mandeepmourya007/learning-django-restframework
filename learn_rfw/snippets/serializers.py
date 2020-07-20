from rest_framework import serializers
from django.contrib.auth.models import User
from . models import snippets,Language_CHOICES,STYLE_CHOICES

''' here Serialiser is used  there we have to rewrite fields'''

# class SnippetsSerializer(serializers.Serializer):

#Fileds for our api
    # id =serializers.IntegerField(read_only=True)
    # tille = serializers.CharField(required=False,allow_blank=True,max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=Language_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # #to create instnce
    # def create(self, validated_data):
    #     return Snippets.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #                                     #????????????????
    #     instance.title = validated_data.get('title',instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance


''' here ModelSerialiser is used no need to rewrite '''

class SnippetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = snippets
        fields =  ['id', 'title', 'code', 'linenos', 'language', 'style']

        ''' we can see representaion using below code
            serializer = SnippetsSerializer()
            print(repr(serializer)) '''



class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=snippets.objects.all())

                            # ????????????????
    # Snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=snippets.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets','owner']