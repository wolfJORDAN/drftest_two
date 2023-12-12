"""
Los serializers en Django REST Framework permiten realizar validaciones, crear relaciones entre modelos, trabajar con datos anidados y mucho más, lo que hace que sea más fácil y potente construir API RESTful en Django.
"""

from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project  # Aquí se debe asignar el modelo Project sin los paréntesis
        fields = ('id', 'title', 'description', 'tecnology', 'created_at')
        read_only_fields = ('created_at', )#aqui si no le ponesmo la coma lo va a tomar como string y no tupla, habria un error