from ..serializers import Exam, ExamSerializer, Section, SectionSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class home_view (APIView) : 
    serializer_class = ExamSerializer

    def get (self, request) : 
        level = request.GET.get('level', None)
        if level:
            query = Exam.objects.filter(level__name=level)
        else:
            query = Exam.objects.all()
            
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class exam_view (APIView) : 
    serializer_class = SectionSerializer

    def get (self, request, exam_id) :
        try : 
            exam = Exam.objects.get(id=exam_id)
        except Exam.DoesNotExist:
            return Response({
                'message' : 'no exam found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        if not exam.is_start :
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        query = Section.objects.filter(exam=exam)
        serializer = self.serializer_class(query, many=True)
        data = {
            'exam_name' : exam.name,
            'total_sections' : query.count(),
            'is_done_sections' : query.filter(state=Section.SectionState.done).count(),
            'pending' : query.exclude(state=Section.SectionState.done).count(),
            'sections' : serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
