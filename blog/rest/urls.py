from django.urls import path
from rest.views import DecorationCartView
from rest.views import ArticleAPIView
from rest.views import CommentAPIView
from rest.views import LoginView
from rest.views import RegisterAPIView

urlpatterns = [
    path('cart/', DecorationCartView.as_view()),
    path('article/', ArticleAPIView.as_view()),
    path('comment/', CommentAPIView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterAPIView.as_view()),
]
