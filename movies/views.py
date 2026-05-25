# =============================================================================
# PREGUNTAS TEÓRICAS (Para responder oralmente durante la revisión del código):
# 1. ¿Qué diferencia hay entre los métodos HTTP GET, POST, PUT y DELETE?
# 2. ¿Para qué sirve el archivo 'models.py' en Django y qué es una migración?
# 3. ¿Qué función cumple el 'Serializer' en Django REST Framework?
# =============================================================================

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer

class MovieListCreateAPIView(APIView):
    
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        # ---------------------------------------------------------------------
        # MINI EJERCICIO PRÁCTICO:
        # El candidato debe completar este método para permitir la creación 
        # de una nueva película. Debe validar los datos con el serializador
        # y guardar el registro si es válido, o retornar un error 400.
        # ---------------------------------------------------------------------
        
        # TU CÓDIGO AQUÍ:
        pass