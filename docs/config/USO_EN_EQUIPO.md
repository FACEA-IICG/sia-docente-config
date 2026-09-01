# Incorporación segura en el repositorio del equipo

Solo una persona actúa como **integrador de configuración**. El resto del equipo conserva sus ramas personales y revisa el Pull Request.

1. Actualice `main` y cree `setup/config-v0.1`.
2. Agregue el remoto docente y descargue sus referencias.
3. Incorpore la etiqueta `config-v0.1` sin copiar el historial ni los secretos.
4. Verifique que `.env` siga ignorado y que solo exista `.env.example`.
5. Ejecute `docker compose -f docker/docker-compose.yml config`.
6. Publique la rama y abra un Pull Request.
7. Solicite revisión de dos integrantes antes de integrar.

```bash
git switch main
git pull --ff-only
git switch -c setup/config-v0.1
git remote add docente https://github.com/FACEA-IICG/sia-docente-config.git
git fetch docente --tags
git checkout config-v0.1 -- docker django-base scripts docs/config .env.example requirements.txt
git status
git add docker django-base scripts docs/config .env.example requirements.txt
git commit -m "Incorpora configuración docente v0.1"
git push -u origin setup/config-v0.1
```

Si `docente` ya existe, use `git remote set-url docente URL`. No use `force-push` y no trabaje directamente en `main`.
