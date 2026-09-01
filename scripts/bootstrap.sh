#!/usr/bin/env sh
set -eu

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Se creó .env desde el ejemplo. Reemplace los valores locales antes de iniciar."
fi

docker compose -f docker/docker-compose.yml config >/dev/null
echo "Configuración Docker válida."
