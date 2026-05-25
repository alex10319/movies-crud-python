# =============================================================================
# PREGUNTAS TEÓRICAS (Para responder oralmente durante la revisión del código):
# 1. ¿Qué es un 'ModelSerializer' en DRF y qué ventaja tiene sobre un 'Serializer' común?
# 2. ¿Para qué sirve el campo obligatorio 'fields' dentro de la clase 'Meta'?
# 3. Si quisieras que el campo 'created_at' se devuelva en la API pero que el cliente 
#    no pueda modificarlo al enviar un POST, ¿qué propiedad le agregarías en el serializador?
# =============================================================================

from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'created_at']