from django.contrib.auth.models import User, Group
from django.test import TestCase, Client
from django.urls import reverse
from Proyectos.views import *

"""
test para los views.py de Proyectos
"""

class Test_proyecto_views(TestCase):

    def test_crear_Proyecto(self):
        path = reverse('crearProyecto')
        response = self.client.get(path)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Proyectos/crearProyecto.html')

#    def test_listar_proyectos(self):
#        path = reverse('')
#        response = self.client.get(path)
#        self.assertEqual(response.status_code, 200)
#        self.assertTemplateUsed(response, 'Proyectos/listarProyectos.html')
