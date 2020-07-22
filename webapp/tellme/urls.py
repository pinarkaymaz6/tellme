from django.urls import path
from . import views  # from current folder


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/add_answer', views.add_answer, name="add_answer"),
    path('add_question', views.add_question, name="add_question"),

]