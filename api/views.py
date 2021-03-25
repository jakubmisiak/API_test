from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from api.models import Task


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Task':'/task/<pk:id>',
        'Create':'/task-create',
        'Delete':'/task-delete/<pk:id>',
        'Update':'/task-update/<pk:id>',
        }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, id):
	task = Task.objects.get(id=id)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, id):
	task = Task.objects.get(id=id)
	task.delete()

	return Response('Item delete!')

