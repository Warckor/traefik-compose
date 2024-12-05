# 🔧 DevOps Local Environment for Full-Stack Projects

Este proyecto esta planteado para realizar unas prácticas de DevOps para crear un entorno completo de desarrollo local para proyectos full-stack, incorporando balanceo de carga, monitoreo y un pipeline de CI/CD. Es ideal como base para futuros proyectos o para aprender prácticas de DevOps.


## Descripción

El entorno contiene los siguientes servicios:

- Traefik: Balanceador de carga y gestor de rutas.
- Frontend: Una aplicación simple de frontend.
- Backend: Un backend básico con conexión a una base de datos PostgreSQL.
- Prometheus & Grafana: Sistema de monitoreo con dashboards.
- GitHub Actions: Pipeline para validación, construcción y despliegue de imágenes Docker.
- Pre-Commit: Una configuración de diversos lints para garantizar un grado de robusted en lo desarrollado antes de realizar el commit.

Incluye ejemplos de configuración de Docker Compose y pipelines de CI/CD para garantizar la calidad del proyecto.


## 🌐 Arquitectura

Diagrama de cómo interactúan los servicios:

```rust
Traefik  <--->  Frontend  <---> Backend
                              |---> PostgreSQL
                              |---> Prometheus <---> Grafana
```


## 🛠️ Tecnologías Utilizadas

- Docker y Docker Compose
- Traefik (v2.11.14)
- Grafana
- Prometheus
- PostgreSQL
- GitHub Actions (para CI/CD)
- pre-commit hooks


## ⚙️ Requisitos Previos

Antes de empezar, asegúrate de tener instalado:

1. Docker y Docker Compose.
2. Crear un archivo .env basado en el ejemplo proporcionado (.env.example).
3. Un editor de texto para personalizar configuraciones (VSCode recomendado).


## 📂 Configuración del Entorno

1. Clona este repositorio:
>> ```bash
>> git clone https://github.com/Warckor/traefik-compose.git
>> cd traefik-compose
>> ```

2. Configura las variables de entorno en `services` y `monitoring` segun las variables de `.env.example`.

3. Levanta los servicios:
>> ```bash
>> docker compose -f ./services/compose.yaml up --build
>> docker compose -f ./monitoring/compose.yaml up --build
>> ```

## 🚀 Servicios y Puertos
| Servicio   | URL                        | Puerto |
| ---------- | -------------------------- | ------ |
| Frontend   | https://frontend.localhost | 4000   |
| Backend    | https://backend.localhost  | 3001   |
| Traefik    | http://localhost:8080      | 8080   |
| Grafana    | http://localhost:3001      | 3000   |
| Prometheus | http://localhost:9090      | 9090   |


## 🔄 CI/CD Pipeline

El proyecto utiliza GitHub Actions para la integración y despliegue continuo. El pipeline se ejecuta en cada push a `master` y pull request.

### Proceso del Pipeline

1. **Validación de Dockerfiles**
   - Utiliza Hadolint para validar la sintaxis de los Dockerfiles del frontend y backend
   - Verifica las mejores prácticas en la construcción de imágenes

2. **Validación de Docker Compose**
   - Comprueba la configuración de los archivos compose.yaml
   - Verifica la sintaxis y estructura de los servicios

3. **Construcción y Publicación**
   - Construye las imágenes de Docker para frontend y backend
   - Publica las imágenes en GitHub Container Registry (ghcr.io)

4. **Pruebas de Integración**
   - Despliega los servicios en un entorno de prueba
   - Verifica el estado de salud de los contenedores
   - Valida la comunicación entre servicios

### Variables de Entorno Requeridas

El pipeline requiere las siguientes variables en GitHub Secrets:

| Variable             | Descripción                                       |
| -------------------- | ------------------------------------------------- |
| `ACTIONS_TOKEN`      | Token de GitHub para acceso al Container Registry |
| `TRAEFIK_HTTP_PORT`  | Puerto HTTP para Traefik                          |
| `TRAEFIK_HTTPS_PORT` | Puerto HTTPS para Traefik                         |
| `BACKEND_PORT`       | Puerto para el servicio backend                   |
| `PROMETHEUS_PORT`    | Puerto para Prometheus                            |
| `CADVISOR_PORT`      | Puerto para cAdvisor                              |
| `GRAFANA_PORT`       | Puerto para Grafana                               |
| `POSTGRES_USER`      | Usuario de PostgreSQL                             |
| `POSTGRES_PASSWORD`  | Contraseña de PostgreSQL                          |
| `POSTGRES_DB`        | Nombre de la base de datos                        |


## 📊 Monitoreo con Grafana y Prometheus

1. Accede a Grafana: http://localhost:3000.

2. Configura Prometheus como Data Source:
    - URL: http://prometheus:9090.

3. Importa los dashboards para:
    - Traefik Metrics: Importa el dashboard ID 8588 desde Grafana Dashboards.


## 🛠️ Próximos Pasos

- Añadir más tests automatizados para el backend y el frontend.
- Implementar seguridad con Oauth2 en Traefik.
- Migrar la configuración a un entorno de producción.
