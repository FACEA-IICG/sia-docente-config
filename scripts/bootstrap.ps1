$ErrorActionPreference = "Stop"

if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "Se creó .env desde el ejemplo. Reemplace los valores locales antes de iniciar."
}

docker compose -f docker/docker-compose.yml config | Out-Null
Write-Host "Configuración Docker válida."
