# Incorporación segura en el repositorio del equipo

Solo una persona actúa como **integrador de configuración**. El resto del equipo conserva sus ramas personales y revisa el Pull Request.

1. Actualice `main` y cree `setup/config-v0.2`.
2. Agregue el remoto docente y descargue sus referencias.
3. Incorpore la etiqueta `config-v0.2` sin copiar el historial ni los secretos.
4. Verifique que `.env` esté ignorado por Git.
5. Ejecute **un solo** script según su terminal. El script crea `.env` local desde `.env.example` si falta y valida Docker:
   - Windows PowerShell: `powershell -ExecutionPolicy Bypass -File scripts/bootstrap.ps1`
   - Git Bash, macOS o Linux: `sh scripts/bootstrap.sh`
6. Confirme con `git status --short` que `.env` no aparece entre los archivos por publicar.
7. Publique la rama y abra un Pull Request.
8. Solicite revisión de dos integrantes antes de integrar.

```bash
git switch main
git pull --ff-only
git switch -c setup/config-v0.2
git remote add docente https://github.com/FACEA-IICG/sia-docente-config.git
git fetch docente --tags
git checkout config-v0.2 -- docker django-base scripts docs/config .env.example requirements.txt
git status
git add docker django-base scripts docs/config .env.example requirements.txt
git commit -m "Incorpora configuración docente v0.2"
git push -u origin setup/config-v0.2
```

Si `docente` ya existe, use `git remote set-url docente URL`. No use `force-push` y no trabaje directamente en `main`.

| Comando                                                                                            | ¿Qué hace?                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `git switch main`                                                                                  | Cambia a la rama local `main` del repositorio del equipo.                                                                                                      |
| `git pull --ff-only`                                                                               | Descarga la versión más reciente de `main`. La opción `--ff-only` evita que Git cree automáticamente un `merge`; si existen cambios incompatibles, se detiene. |
| `git switch -c setup/config-v0.2`                                                                  | Crea una nueva rama llamada `setup/config-v0.2` a partir del `main` actualizado y cambia inmediatamente a ella.                                                |
| `git remote add docente URL`                                                                       | Registra el repositorio público de la profesora con el nombre corto `docente`. No descarga ni modifica archivos todavía.                                       |
| `git fetch docente --tags`                                                                         | Descarga las referencias y etiquetas del repositorio docente, incluida la etiqueta `config-v0.2`, sin modificar los archivos actuales.                         |
| `git checkout config-v0.2 -- docker django-base scripts docs/config .env.example requirements.txt` | Copia exclusivamente esos archivos y carpetas desde la versión docente `config-v0.2` hacia la rama actual del equipo. No cambia de rama.                       |
| `git status`                                                                                       | Muestra qué archivos se incorporaron, modificaron o quedaron preparados para confirmar. Permite revisar antes de continuar.                                    |
| `git add ...`                                                                                      | Prepara únicamente los archivos de configuración indicados para incluirlos en el próximo commit.                                                               |
| `git commit -m "Incorpora configuración docente v0.2"`                                             | Registra localmente la incorporación como un nuevo cambio dentro de la rama `setup/config-v0.2`. Todavía no modifica `main`.                                   |
| `git push -u origin setup/config-v0.2`                                                             | Publica la rama en el repositorio del equipo. `-u` vincula la rama local con la rama remota para futuros `push` y `pull`.                                      |
