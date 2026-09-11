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
docker compose -f docker/docker-compose.yml ps
```

Git Bash, macOS o Linux:

```bash
sh scripts/bootstrap.sh
docker compose -f docker/docker-compose.yml up -d --build
docker compose -f docker/docker-compose.yml exec web python manage.py migrate
docker compose -f docker/docker-compose.yml exec web python manage.py check
docker compose -f docker/docker-compose.yml ps
```

Abra `http://localhost:8000/` y `http://localhost:8000/health/`. Los servicios `web` y `db` deben aparecer como `healthy`.

## Material del Encuentro 5

- [Práctica técnica guiada y detallada](docs/encuentro-05/PRACTICA_TECNICA_GUIADA.md)
- [Procedimiento breve Docker–Django](docs/encuentro-05/DOCKER_DJANGO_PASO_A_PASO.md)
- [Simulador, guía de preguntas y plantilla de registro](docs/encuentro-05/README.md)

## Regla de seguridad

Nunca publique `.env`, contraseñas, tokens, claves privadas ni datos reales. Use `.env.example` como plantilla. `.dockerignore` impide que `.env` y archivos locales entren en la imagen. Antes de cualquier commit ejecute `git status --short` y compruebe que `.env` no aparezca.

## Estructura principal

```text
docker/
sia_config/
scripts/
docs/config/
docs/encuentro-05/
manage.py
.env.example
.dockerignore
requirements.txt
```

La guía para incorporar la configuración a un repositorio de equipo permanece en `docs/config/USO_EN_EQUIPO.md` y se aplicará cuando lo indique la planificación.
