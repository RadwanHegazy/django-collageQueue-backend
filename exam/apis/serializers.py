from rest_framework import serializers
from ..models import Exam, Section


class ExamSerializer (serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id','name','date','is_start','level']

    def to_representation(self, instance:Exam):
        data = super().to_representation(instance)
        data['level'] = instance.level.name
        return data
    

class SectionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id','number','state']
