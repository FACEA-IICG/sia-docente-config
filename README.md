# SIA · Configuración docente

Configuración oficial de infraestructura para **Desarrollo de SIA 2026**. Contiene una aplicación mínima reproducible con Django y PostgreSQL; no contiene la solución de los proyectos ni credenciales reales.

## Uso pedagógico

- **Encuentro 5:** demostración, instalación/verificación de Docker y ejecución guiada de la aplicación mínima. Los equipos todavía no incorporan esta configuración a su repositorio.
- **Encuentro 21:** incorporación controlada al repositorio de cada equipo mediante la referencia `config-v0.2`, rama `setup/config-v0.2`, Pull Request y revisión por pares.

## Inicio rápido de la demostración

PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/bootstrap.ps1
docker compose -f docker/docker-compose.yml up -d --build
docker compose -f docker/docker-compose.yml exec web python manage.py migrate
docker compose -f docker/docker-compose.yml exec web python manage.py check
```

Git Bash, macOS o Linux:

```bash
sh scripts/bootstrap.sh
docker compose -f docker/docker-compose.yml up -d --build
docker compose -f docker/docker-compose.yml exec web python manage.py migrate
docker compose -f docker/docker-compose.yml exec web python manage.py check
```

Abra `http://localhost:8000/` y `http://localhost:8000/health/`.

## Material del Encuentro 5

Consulte `docs/encuentro-05/` para utilizar el simulador de entrevista, la guía de preguntas, la plantilla de registro y el procedimiento Docker–Django.

## Regla de seguridad

Nunca publique `.env`, contraseñas, tokens, claves privadas ni datos reales. Use `.env.example` como plantilla. Antes de cualquier commit ejecute `git status --short` y compruebe que `.env` no aparezca.

## Estructura principal

```text
docker/
sia_config/
scripts/
docs/config/
docs/encuentro-05/
manage.py
.env.example
requirements.txt
```

La guía para incorporar la configuración a un repositorio de equipo permanece en `docs/config/USO_EN_EQUIPO.md` y se aplicará cuando lo indique la planificación.
