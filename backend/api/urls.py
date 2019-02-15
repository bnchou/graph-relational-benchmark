from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cypher/reset', views.cypher_reset, name='cypher_reset'),
    path('sql/reset', views.sql_reset, name='sql_reset'),
    path('command', views.command, name='command'),
]
