# Práctica técnica guiada · Git, Docker, Django, PostgreSQL y /health/

## 1. Propósito

Esta práctica permite comprobar, paso a paso, que el computador puede ejecutar la aplicación mínima docente formada por dos servicios:

- `web`: aplicación Django;
- `db`: base de datos PostgreSQL.

La práctica utiliza **dos repositorios diferentes**:

| Repositorio | Uso durante el Encuentro 5 | ¿Se modifica? |
|---|---|---|
| Repositorio del equipo | Conservar productos de requisitos y evidencias mediante Pull Request | Sí, solo en `student/<username>` |
| `sia-docente-config` | Ejecutar localmente la demostración Docker–Django | No se hace push ni se copia al equipo |

La configuración docente se incorporará al proyecto del equipo únicamente en el encuentro que indique la planificación.

## 2. Resultado esperado

Al terminar debe poder demostrar:

1. Git reconoce ambos repositorios y sus remotos correctos.
2. Docker Engine está ejecutándose.
3. Docker Compose interpreta correctamente el archivo de configuración.
4. El contenedor `db` inicia PostgreSQL y queda saludable.
5. El contenedor `web` inicia Django y queda saludable.
6. Django puede ejecutar sus migraciones.
7. `http://localhost:8000/` responde.
8. `http://localhost:8000/health/` devuelve:
   `{"django": "ok", "postgresql": "ok"}`.
9. `.env` no aparece en Git ni se publica.
10. La evidencia se registra sin datos personales o secretos.

## 3. Conceptos antes de ejecutar

- **Git** controla versiones de archivos.
- **GitHub** aloja los repositorios y Pull Requests.
- **Imagen** es la plantilla desde la cual Docker crea un contenedor.
- **Contenedor** es un proceso aislado creado desde una imagen.
- **Dockerfile** describe cómo construir la imagen de Django.
- **Docker Compose** coordina varios servicios mediante `docker-compose.yml`.
- **Volumen** conserva los datos de PostgreSQL aunque el contenedor se detenga.
- **Migración** crea o actualiza tablas según los modelos de Django.
- **Endpoint** es una dirección de la aplicación.
- **Health check** verifica automáticamente si un servicio puede responder.
- **`/health/`** comprueba Django y ejecuta `SELECT 1` contra PostgreSQL.

## 4. Requisitos del computador

### Windows personal

- Windows 10 u 11 de 64 bits.
- Virtualización habilitada.
- WSL 2 disponible.
- Docker Desktop instalado y abierto.
- Git instalado.
- Un navegador.
- PowerShell o Git Bash.

### macOS o Linux

- Git instalado.
- Docker Engine o Docker Desktop.
- Docker Compose v2, ejecutado como `docker compose`.

### Computador institucional o compartido

No instale Docker, no active virtualización, no cambie WSL y no solicite permisos administrativos sin autorización. Si falta un requisito, registre el bloqueo y observe la demostración docente.

## 5. Verificación previa

Abra PowerShell o Git Bash y ejecute un comando por vez:

```bash
git --version
docker --version
docker compose version
docker info
```

### Resultado esperado

- Git muestra un número de versión.
- Docker muestra la versión del cliente.
- Compose muestra `Docker Compose version v2...`.
- `docker info` muestra información del servidor.

Si `docker --version` funciona, pero `docker info` falla, Docker Desktop probablemente está cerrado o el motor aún no termina de iniciar. Abra Docker Desktop, espere y vuelva a ejecutar solo `docker info`.

En Windows también puede revisar:

```powershell
wsl --version
wsl --status
```

## 6. Prueba mínima de Docker

```bash
docker run --rm hello-world
```

Docker descargará una imagen pequeña si no existe localmente, creará un contenedor, mostrará un mensaje y lo eliminará por `--rm`.

Si la red institucional impide descargar imágenes, registre el mensaje exacto. No desactive el antivirus, firewall o controles de seguridad.

## 7. Preparar una carpeta de trabajo

Elija una ruta fácil de identificar. Ejemplo en Windows:

```powershell
cd $HOME
New-Item -ItemType Directory -Force sia-practica
Set-Location sia-practica
```

En Git Bash, macOS o Linux:

```bash
cd
mkdir -p sia-practica
cd sia-practica
```

Compruebe la ubicación:

```bash
pwd
```

No ejecute los comandos desde una carpeta que ya contenga otro proyecto.

## 8. Clonar el repositorio del equipo

Copie la URL real del repositorio del equipo desde GitHub:

```bash
git clone URL_DEL_REPOSITORIO_DEL_EQUIPO
cd NOMBRE_DEL_REPOSITORIO_DEL_EQUIPO
git remote -v
git branch --show-current
git status
```

### Verifique

- `origin` apunta al repositorio correcto de `FACEA-IICG`.
- La rama inicial es `main`.
- `git status` no informa cambios.

Actualice `main` y su rama permanente:

```bash
git switch main
git pull origin main
git switch student/<username>
git merge main
git push origin student/<username>
```

Reemplace `<username>` por el usuario de GitHub. No cree una rama nueva para el Encuentro 5.

Regrese a la carpeta superior:

```bash
cd ..
```

## 9. Clonar el repositorio docente

```bash
git clone https://github.com/FACEA-IICG/sia-docente-config.git
cd sia-docente-config
git remote -v
git branch --show-current
git status
```

### Verifique

- `origin` apunta a `FACEA-IICG/sia-docente-config`.
- Está en `main`.
- El árbol de trabajo está limpio.

Los estudiantes utilizan este clon solo para la práctica local. No crean ramas, no hacen commits y no realizan push en este repositorio.

## 10. Reconocer la configuración

Revise los elementos principales:

```text
docker/Dockerfile
docker/docker-compose.yml
sia_config/settings.py
sia_config/urls.py
scripts/bootstrap.ps1
scripts/bootstrap.sh
.env.example
requirements.txt
manage.py
```

### Relación entre elementos

1. Compose inicia `db` con PostgreSQL 16.
2. El health check de `db` utiliza `pg_isready`.
3. `web` se construye con `docker/Dockerfile`.
4. El Dockerfile instala Python y `requirements.txt`.
5. Compose entrega a Django las variables de `.env`.
6. Django utiliza `POSTGRES_HOST=db`, el nombre del servicio.
7. `web` espera que `db` esté saludable.
8. `/health/` consulta PostgreSQL y devuelve el resultado.

## 11. Crear el archivo local .env

No edite `.env.example`. Cree una copia llamada `.env`.

PowerShell:

```powershell
Copy-Item .env.example .env
```

Git Bash, macOS o Linux:

```bash
cp .env.example .env
```

Compruebe que existe sin mostrar su contenido:

PowerShell:

```powershell
Test-Path .env
git status --short
```

Git Bash, macOS o Linux:

```bash
test -f .env && echo ".env existe"
git status --short
```

`git status --short` no debe mostrar `.env`, porque `.gitignore` lo excluye. No copie su contenido en capturas, mensajes o Pull Requests.

## 12. Validación automática inicial

Use solo el script correspondiente a su terminal.

PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/bootstrap.ps1
```

Git Bash, macOS o Linux:

```bash
sh scripts/bootstrap.sh
```

El script crea `.env` si falta y ejecuta la validación de Compose. El mensaje esperado es:

```text
Configuración Docker válida.
```

## 13. Validar Compose manualmente

```bash
docker compose -f docker/docker-compose.yml config
```

Este comando no levanta contenedores. Interpreta el YAML, sustituye variables y muestra la configuración final.

Revise que aparezcan los servicios `web` y `db`. No comparta la salida si contiene valores de `.env`.

Para obtener solo los nombres:

```bash
docker compose -f docker/docker-compose.yml config --services
```

Resultado esperado:

```text
db
web
```

## 14. Construir la imagen de Django

```bash
docker compose -f docker/docker-compose.yml build
```

Durante la primera ejecución Docker descarga la imagen base de Python e instala Django y el controlador PostgreSQL. Puede tardar varios minutos.

Si falla:

1. lea las últimas líneas;
2. identifique si el error corresponde a red, espacio, permisos o dependencias;
3. registre el mensaje;
4. no repita el comando indefinidamente.

Después compruebe las imágenes:

```bash
docker compose -f docker/docker-compose.yml images
```

## 15. Iniciar PostgreSQL y Django

```bash
docker compose -f docker/docker-compose.yml up -d
```

`-d` deja los servicios ejecutándose en segundo plano.

Compruebe el estado:

```bash
docker compose -f docker/docker-compose.yml ps
```

### Resultado esperado

- `db`: `Up` y `healthy`.
- `web`: `Up` y, después de unos segundos, `healthy`.
- El puerto `8000` está publicado para `web`.

Si aparece `starting`, espere unos segundos y ejecute nuevamente `ps`. Si aparece `unhealthy` o `Exited`, revise los registros.

## 16. Ejecutar migraciones y comprobaciones

```bash
docker compose -f docker/docker-compose.yml exec web python manage.py migrate
docker compose -f docker/docker-compose.yml exec web python manage.py check
```

### Resultado esperado

- `migrate` aplica las migraciones iniciales o informa que no quedan migraciones pendientes.
- `check` termina con `System check identified no issues`.

Compruebe la conexión directamente desde PostgreSQL:

```bash
docker compose -f docker/docker-compose.yml exec db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "SELECT 1;"'
```

Debe aparecer una fila con el valor `1`.

## 17. Comprobar la aplicación

Abra en el navegador:

- <http://localhost:8000/>
- <http://localhost:8000/health/>

La raíz debe indicar que Django funciona dentro de Docker. `/health/` debe responder con estado HTTP 200 y:

```json
{"django": "ok", "postgresql": "ok"}
```

PowerShell:

```powershell
Invoke-RestMethod http://localhost:8000/health/
```

Git Bash, macOS o Linux:

```bash
curl -i http://localhost:8000/health/
```

La comprobación es válida solo cuando Django y PostgreSQL aparecen como `ok`.

## 18. Revisar registros

Estado general:

```bash
docker compose -f docker/docker-compose.yml ps
```

Últimas 100 líneas:

```bash
docker compose -f docker/docker-compose.yml logs --tail=100 web
docker compose -f docker/docker-compose.yml logs --tail=100 db
```

Seguimiento en tiempo real:

```bash
docker compose -f docker/docker-compose.yml logs -f web
```

Presione `Ctrl+C` para salir de la vista. Esto no detiene el contenedor.

## 19. Diagnóstico de errores frecuentes

| Síntoma | Comprobación | Acción segura |
|---|---|---|
| `docker: command not found` | `docker --version` | Instalar Docker solo en equipo personal o registrar bloqueo |
| No puede conectar con Docker | `docker info` | Abrir Docker Desktop y esperar al motor |
| Compose no encuentra `.env` | Verificar desde la raíz del repositorio | Crear la copia desde `.env.example` |
| Puerto 8000 ocupado | Revisar el mensaje de `up` | Cerrar la aplicación propia que usa el puerto o avisar |
| `db` aparece `unhealthy` | `logs --tail=100 db` | Revisar variables y estado del volumen |
| `web` aparece `Exited` | `logs --tail=100 web` | Revisar error de Python, dependencias o conexión |
| `/health/` devuelve 503 | Revisar `db` y registros | Esperar salud de PostgreSQL y revisar credenciales locales |
| Error al descargar imágenes | Revisar conexión institucional | Registrar bloqueo; no desactivar controles de seguridad |
| Migraciones fallan | Revisar salida completa | Confirmar que `db` está saludable antes de repetir |

## 20. Detener sin borrar datos

```bash
docker compose -f docker/docker-compose.yml down
```

Compruebe:

```bash
docker compose -f docker/docker-compose.yml ps
```

No debe haber servicios en ejecución. El volumen de PostgreSQL se conserva.

No utilice:

```bash
docker compose -f docker/docker-compose.yml down -v
```

`-v` elimina el volumen y los datos locales. Solo la docente puede indicar cuándo usarlo.

## 21. Repetir la práctica

Para iniciar nuevamente:

```bash
docker compose -f docker/docker-compose.yml up -d
docker compose -f docker/docker-compose.yml ps
```

Las migraciones ya aplicadas permanecen en el volumen.

## 22. Evidencia que debe conservar el estudiante

En el Pull Request del repositorio del equipo registre:

- versión de Git;
- versión de Docker;
- versión de Compose;
- resultado resumido de `docker compose ps`;
- confirmación de `manage.py check`;
- respuesta de `/health/`;
- incidencia encontrada y cómo se resolvió, o indicación de que no hubo incidencia;
- equipo utilizado: personal, institucional o alternativo;
- declaración de que `.env` no fue versionado.

No pegue:

- contenido de `.env`;
- contraseñas;
- tokens;
- rutas que revelen datos personales;
- identificadores de personas entrevistadas;
- capturas con información sensible.

## 23. Cierre en computador compartido

1. Ejecute `docker compose ... down`.
2. Cierre VS Code, terminales y GitHub.
3. Elimine únicamente su clon local cuando la docente lo indique.
4. No elimine imágenes, volúmenes, contenedores o archivos de otra persona.
5. No borre configuraciones generales de Docker o WSL.

## 24. Lista final para la docente

- [ ] Los estudiantes distinguen repositorio del equipo y repositorio docente.
- [ ] Nadie copió la configuración al repositorio del equipo.
- [ ] `.env` permanece local e ignorado.
- [ ] Compose reconoce `web` y `db`.
- [ ] PostgreSQL queda saludable.
- [ ] Django ejecuta migraciones y `check`.
- [ ] La raíz y `/health/` responden.
- [ ] La evidencia no expone secretos.
- [ ] Los servicios se detienen sin eliminar el volumen.
