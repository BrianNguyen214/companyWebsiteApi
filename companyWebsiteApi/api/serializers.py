from rest_framework import serializers

from boardMembers.models import Member

#converts to JSON
#validations for data passed
class MemberSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = Member
        fields = [
            'pk',
            'name',
            'position',
            'description',
            'picture',
        ]

    def validate_title(self, value):
        qs = Member.objects.filter(title__iexact=value)
        #this is how you exclude the current pk
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The title has already been used")
        return value