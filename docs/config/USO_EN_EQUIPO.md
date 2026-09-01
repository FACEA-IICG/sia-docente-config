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
