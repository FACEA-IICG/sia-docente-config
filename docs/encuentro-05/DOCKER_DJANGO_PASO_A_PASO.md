# Docker para una aplicación Django · Paso a paso

## ¿Qué es cada elemento?

- **Imagen:** plantilla inmutable que contiene Python, dependencias y configuración.
- **Contenedor:** instancia en ejecución de una imagen.
- **Dockerfile:** instrucciones para construir la imagen de Django.
- **Docker Compose:** archivo que coordina los servicios `web` y `db`.
- **Volumen:** almacenamiento persistente de PostgreSQL.

## 1. Preparar Docker

En un computador personal con Windows, instale Docker Desktop siguiendo la documentación oficial y use el backend WSL 2. En un computador institucional o compartido, no instale ni cambie WSL, virtualización o permisos sin autorización docente.

Verifique en PowerShell o Git Bash:

```bash
docker --version
docker compose version
docker run --rm hello-world
```

## 2. Clonar el repositorio docente

```bash
git clone https://github.com/FACEA-IICG/sia-docente-config.git
cd sia-docente-config
git remote -v
```

## 3. Crear el archivo local de variables

PowerShell:

```powershell
Copy-Item .env.example .env
```

Git Bash, macOS o Linux:

```bash
cp .env.example .env
```

Cambie solamente valores locales de desarrollo. Nunca publique `.env`.

## 4. Validar y construir

```bash
docker compose -f docker/docker-compose.yml config
docker compose -f docker/docker-compose.yml build
```

## 5. Iniciar Django y PostgreSQL

```bash
docker compose -f docker/docker-compose.yml up -d
docker compose -f docker/docker-compose.yml ps
```

## 6. Preparar la base de datos

```bash
docker compose -f docker/docker-compose.yml exec web python manage.py migrate
docker compose -f docker/docker-compose.yml exec web python manage.py check
```

Abra:

- `http://localhost:8000/`
- `http://localhost:8000/health/`

El segundo enlace debe informar `django: ok` y `postgresql: ok`.

## 7. Revisar errores

```bash
docker compose -f docker/docker-compose.yml logs --tail=100 web
docker compose -f docker/docker-compose.yml logs --tail=100 db
```

## 8. Detener el ambiente

```bash
docker compose -f docker/docker-compose.yml down
```

No utilice `down -v` salvo instrucción docente: elimina el volumen y los datos locales de PostgreSQL.

## 9. Comprobar seguridad

```bash
git status --short
```

El archivo `.env` no debe aparecer. En computadores públicos, cierre Docker Desktop, GitHub, VS Code y elimine únicamente su clon local al terminar.
