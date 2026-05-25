# Examen Técnico - Backend (Django REST Framework)

API simplificada para evaluar candidatos a pasantes.

## Instalación Rápida

1. **Crear y activar entorno virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows
   source venv/bin/activate     # Linux/macOS
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Preparar base de datos:**
    ```bash
    python manage.py makemigrations movies
    python manage.py migrate
    ```

4. **Correr servidor:**
    ```bash
    python manage.py runserver
    ```
    API disponible en: http://127.0.0.1:8000/api/movies/

---

## Estructura del Examen

* **Teoría:** Preguntas en los comentarios superiores de `models.py`, `serializers.py` y `views.py`.
* **Práctica (Live Coding):** Completar el método `post` en `movies/views.py` para permitir la creación de películas.