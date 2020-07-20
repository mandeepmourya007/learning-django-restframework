from django.urls import path
from snippets import views

# to see different formate of data
from rest_framework.urlpatterns import format_suffix_patterns 

# t1 url
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

#t2 url

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)