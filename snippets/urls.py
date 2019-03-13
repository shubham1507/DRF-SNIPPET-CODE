from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework.schemas import get_schema_view # new


schema_view = get_schema_view(title='Pastebin API') # new



urlpatterns = [
    path('schema/', schema_view), # new
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/',
         views.SnippetHighlight.as_view(), name='snippet-highlight'), 
]

urlpatterns = format_suffix_patterns(urlpatterns)
