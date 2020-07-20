from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import snippets
from snippets.serializers import SnippetsSerializer
from rest_framework.decorators import api_view

# Create your views here.

'''  these are simple  django  views '''

# @csrf_exempt
# @api_view(['GET', 'POST'])  #this is  a decortor which tells about mthods which are allowed
# def snippet_list(request):
  
#     if request.method == 'GET':
#         Snippets = snippets.objects.all()
#         serializer = SnippetsSerializer(Snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetsSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def snippet_detail(request, pk):
   
#     try:
#         snippet = snippets.objects.get(pk=pk)
#     except snippets.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetsSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetsSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import snippets
from snippets.serializers import SnippetsSerializer



@api_view(['GET', 'POST']) #this is  a decortor which tells about mthods which are allowed
# def snippet_list(request):
def snippet_list(request, format=None):
  
    if request.method == 'GET':
        Snippets = snippets.objects.all()
        serializer = SnippetsSerializer(Snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
def snippet_detail(request, pk, format=None):

    try:
        snippet = snippets.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetsSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)