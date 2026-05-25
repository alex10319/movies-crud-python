# =============================================================================
# PREGUNTAS TEÓRICAS (Para responder oralmente durante la revisión del código):
# 1. ¿Qué es un ORM y qué ventaja nos da usarlo en lugar de escribir consultas SQL puras?
# 2. ¿Qué diferencia hay entre los atributos 'auto_now_add=True' y 'auto_now=True' en un DateTimeField?
# 3. Si quisiéramos relacionar este modelo con un director (un director puede tener muchas películas), 
#    ¿qué tipo de campo deberíamos agregar y cómo se declararía?
# =============================================================================

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title