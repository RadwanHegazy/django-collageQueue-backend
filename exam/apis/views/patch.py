from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from ...models import Section


class section_pending (APIView) : 
    permission_classes = [permissions.IsAuthenticated]

    def patch (self, request, section_id) : 
        try :
            section = Section.objects.get(id=section_id)
        except Section.DoesNotExist:
            return Response({
                'message' : 'section not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        section.state = section.SectionState.pending
        section.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class section_done (APIView) : 
    permission_classes = [permissions.IsAuthenticated]

    def patch (self, request, section_id) : 
        try :
            section = Section.objects.get(id=section_id)
        except Section.DoesNotExist:
            return Response({
                'message' : 'section not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        section.state = section.SectionState.done
        section.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

