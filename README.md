# SIA · Configuración docente

Configuración oficial de infraestructura para **Desarrollo de SIA 2026**. Este repositorio contiene una base reproducible; no contiene la solución del proyecto ni credenciales.

## Versión del Encuentro 3

- Referencia vigente: `config-v0.2`
- Contenido: Docker, PostgreSQL, dependencias Django, variables de ejemplo y guías de incorporación.
- Distribución: cada equipo incorpora esta versión desde una rama `setup/config-v0.2` y abre un Pull Request.

## Regla de seguridad

Nunca suba `.env`, contraseñas, tokens, claves privadas ni datos reales. Use `.env.example` como plantilla y genere una copia `.env` local mediante el script de arranque; `.env` permanece ignorado por Git.

## Estructura

```text
docker/
django-base/
scripts/
docs/config/
.env.example
requirements.txt
```

Consulte `docs/config/USO_EN_EQUIPO.md` antes de copiar una versión al repositorio grupal.
