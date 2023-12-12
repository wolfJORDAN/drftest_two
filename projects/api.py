from .models import Project

from rest_framework import viewsets, permissions
"""
permissions contiene clases que definen las reglas de autorización que se aplican a las vistas en Django REST Framework. Estas reglas permiten controlar quién tiene acceso a qué recursos dentro de la API.
"""

from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    #aqui le decimos que consultas se van a poder hacer
    queryset = Project.objects.all()#consulta todos los datos de una tabla
    permission_classes = [permissions.AllowAny]
    #los permisos son que solo de allowany, que cualquier cliente va a poder accder a los datos
    serializer_class = ProjectSerializer 
    #a partir de que serializer va a estar utilizando estos datos, como lo va aconvertir