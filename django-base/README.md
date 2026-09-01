# Base Django

Esta carpeta documenta la configuración mínima esperada. El equipo crea el proyecto Django dentro de su repositorio y conserva sus propias decisiones de arquitectura.

Variables que deben leerse desde el entorno:

- `DJANGO_DEBUG`
- `DJANGO_SECRET_KEY`
- `DJANGO_ALLOWED_HOSTS`
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`

La configuración real se mantiene en `.env`, archivo que nunca se versiona.
