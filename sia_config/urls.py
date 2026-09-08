from django.contrib import admin
from django.db import connection
from django.http import JsonResponse
from django.urls import path


def inicio(request):
    return JsonResponse(
        {
            "aplicacion": "Desarrollo de SIA",
            "mensaje": "Django funciona dentro de Docker",
        }
    )


def salud(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        return JsonResponse({"django": "ok", "postgresql": "ok"})
    except Exception:
        return JsonResponse(
            {"django": "ok", "postgresql": "sin conexion"}, status=503
        )


urlpatterns = [
    path("", inicio, name="inicio"),
    path("health/", salud, name="salud"),
    path("admin/", admin.site.urls),
]
