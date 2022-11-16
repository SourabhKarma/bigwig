from random import choices
from rest_framework import serializers

from .models import Poll, Choice, Vote



class votevalidateser(serializers.Serializer):
    voted_by  = serializers.CharField()
    poll = serializers.CharField()








class VoteSerializer(serializers.ModelSerializer):
    # choice = serializers.RelatedField(many=True,read_only  =True)

    # def validate(self, attrs):

    #     # poll = attrs.get('poll', self.object.poll)
    #     # voted_by = attrs.get('voted_by', self.object.voted_by)
    #     try:
    #         Vote.objects.get(poll=attrs['poll'], voted_by=attrs['voted_by'])
    #     except Vote.DoesNotExist:
    #         pass
    #     else:
    #         raise serializers.ValidationError('field1 with field2 already exists')

    #     return attrs

    class Meta:
        model = Vote
        fields = '__all__'
        # depth = 1















class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'







class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'





# without votes
class ChoiceSerializerNoVotes(serializers.ModelSerializer):
    # votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'



class PollSerializerNoVotes(serializers.ModelSerializer):
    choices = ChoiceSerializerNoVotes(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = ['id','question','choices']



#count

class VoteSerializerCount(serializers.ModelSerializer):
    # vote_count = serializers.SerializerMethodField()
    # vote_count = serializers.HiddenField()
    # vote = serializers.IntegerField(source="vote_count.count", read_only=True)
    
    class Meta:
        model = Vote
        fields = "__all__"

    # def get_vote_count(self, obj):
    #     return obj.votes.count()

class ChoiceSerializerCount(serializers.ModelSerializer):
    # votes = VoteSerializerCount(many=True, read_only=True, required=False)
    votes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Choice
        fields = ['id','votes_count','choice_text']



    def get_votes_count(self, obj):
        return obj.votes.count()






class PollSerializerCount(serializers.ModelSerializer):
    choices = ChoiceSerializerCount(many=True, read_only=True, required=False)
    
    # votes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Poll
        # fields = '__all__'

        fields = ['id','question','choices']













    # def get_votes(self, language):
    #     return language.choices.count()