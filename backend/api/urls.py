from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cypher/insert', views.cypher_insert, name='cypher_insert'),
    path('mssql/insert', views.mssql_insert, name='mssql_insert'),
]