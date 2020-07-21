from django.urls import path
from . import views  # from current folder


urlpatterns = [
    path('', views.index, name="index"),
    #127.0.0.1/tellme
    path('<int:question_id>/', views.detail, name="detail"),
    #127.0.0.1/polls/2
    #path('<int:question_id>/results', views.results, name="results"),
    #127.0.0.1/polls/2/results
    #path('<int:question_id>/vote', views.vote, name="vote"),
    #127.0.0.1/polls/2/vote
]