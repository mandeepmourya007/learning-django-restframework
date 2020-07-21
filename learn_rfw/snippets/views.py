
# Create your views here.

'''  these are simple  django  views '''


# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from snippets.models import snippets
# from snippets.serializers import SnippetsSerializer
# from rest_framework.decorators import api_view

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


''' functioon based view of rwf '''


# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from snippets.models import snippets
# from snippets.serializers import SnippetsSerializer



# @api_view(['GET', 'POST']) #this is  a decortor which tells about mthods which are allowed
# # def snippet_list(request):
# def snippet_list(request, format=None):
  
#     if request.method == 'GET':
#         Snippets = snippets.objects.all()
#         serializer = SnippetsSerializer(Snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnippetsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# # def snippet_detail(request, pk):
# def snippet_detail(request, pk, format=None):

#     try:
#         snippet = snippets.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetsSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetsSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)









''' class based view for rfw '''

# from snippets.models import snippets
# from snippets.serializers import SnippetsSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class SnippetList(APIView):

#     def get(self, request, format=None):
#         Snippets = snippets.objects.all()
#         serializer = SnippetsSerializer(Snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
  
#     def get_object(self, pk):
#         try:
#             return snippets.objects.get(pk=pk)
#         except snippets.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetsSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetsSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


''' using Minins '''

# from snippets.models import snippets
# from snippets.serializers import SnippetsSerializer
# from rest_framework import mixins
# from rest_framework import generics



# class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

#     queryset = snippets.objects.all()
#     serializer_class = SnippetsSerializer

#     def get(self,request,*args,**kwargs):

#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args, **kwargs)
    
# class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = snippets.objects.all()
#     serializer_class = SnippetsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


''' using generics '''


# from snippets.models import snippets
# from snippets.serializers import SnippetsSerializer
# from rest_framework import generics
# from rest_framework import permissions

# from snippets.permissions import IsOwnerOrReadOnly
# class SnippetList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = snippets.objects.all()
#     serializer_class = SnippetsSerializer
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly]
#     queryset = snippets.objects.all()
#     serializer_class = SnippetsSerializer


# t4

# from snippets.serializers import UserSerializer
# from django.contrib.auth.models import User

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# t5

from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(('GET',))
def  api_root(request,format=None):

    return Response(
      {  "user" : reverse("user-list",request=request,format=format),
          "snippets" : reverse("snippet-list",request=request,format=format)
      }
    )

# from rest_framework import renderers

# from rest_framework.response import Response

# class SnippetHighlight(generics.GenericAPIView):

#     queryset = snippets.objects.all()
#     renderer_class = [renderers.StaticHTMLRenderer ]

#     def get(self,request,*arg,**kwargs):
#         snippet = self.get_object() 
#         return Response(snippet.highlighted)


# t6

''' viewsets'''

from snippets.serializers import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework.decorators import action
from rest_framework.response import Response
from snippets.models import snippets
from snippets.serializers import SnippetsSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework import renderers 

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = snippets.objects.all()
    serializer_class = SnippetsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True,renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)