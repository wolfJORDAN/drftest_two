from rest_framework import routers
"""
from rest_framework import routers: Esta línea importa el módulo routers de Django REST Framework, que proporciona herramientas para crear enrutadores de API.
"""

from .api import ProjectViewSet

"""
from .api import ProjectViewSet: Aquí se importa el ProjectViewSet desde un archivo llamado api que está en el mismo directorio que este código. El ProjectViewSet probablemente sea una clase que contiene lógica para manejar las solicitudes HTTP relacionadas con un modelo de proyectos en tu aplicación.
"""


router = routers.DefaultRouter()
"""
router = routers.DefaultRouter(): Esta línea inicializa un enrutador utilizando la clase DefaultRouter proporcionada por Django REST Framework. Este enrutador ayudará a manejar las rutas y vistas para tus APIs.
"""

router.register('api/projects', ProjectViewSet, 'projects')
"""
router.register('api/projects', ProjectViewSet, 'projects'): Esta línea registra el ProjectViewSet en el enrutador.
"""

urlpatterns = router.urls