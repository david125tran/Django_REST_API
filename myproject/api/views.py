from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
from django.http.response import JsonResponse
from rest_framework import status

@api_view(['GET', 'DELETE'])
def getData(request):
    # http://127.0.0.1:8000/
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        count = Item.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def addItem(request):
    # http://127.0.0.1:8000/add/
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# JSON format for data addtion:
# {
# "name":"David"
# }
