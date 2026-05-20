# Full Stack Assessment

Este proyecto contiene una aplicación full stack para la gestión de reservas utilizando:

- Django
- Django Ninja
- React
- TypeScript
- Docker
- Docker Compose

---

# Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Docker
- Git
- Python


---

# Clonar el repositorio

```bash
git clone <tu-repositorio>
```

---

# Entrar en la carpeta del proyecto

```bash
cd prueba-tecnica-leasy
```

---

# Ejecutar la aplicación

Construir e iniciar todos los servicios:

```bash
docker compose up --build
```

---

# URLs de la aplicación

## Frontend

```text
http://localhost:5173
```

---

## Backend

```text
http://localhost:8000
```

---

## Documentación de la API

```text
http://localhost:8000/api/docs
```

---

## Django Back Office

```text
http://localhost:8000/
```

---

# Credenciales de demostración

## Usuario administrador

```text
username: manager
password: demo1234
```

---

## Usuario cliente

```text
email: alice@example.com
password: demo1234
```

---

# Funcionalidades

## Backend

- API con Django Ninja
- Autenticación JWT
- Endpoint para listar reservas
- Endpoint para cancelar reservas
- Respuestas de error estables
- Arquitectura basada en capa de servicios
- Validaciones de dominio
- Validación de propiedad de reservas
- Validación de estados permitidos

---

## Frontend

- React + TypeScript
- Inicio de sesión
- Lista de reservas
- Flujo de cancelación de reservas
- Manejo de errores de la API
- Mensajes de éxito
- Persistencia de sesión
- Logout
- Visualización del perfil del cliente

---

## Docker

- Backend dockerizado
- Frontend dockerizado
- Gunicorn como servidor WSGI
- Nginx para servir el frontend
- Docker Compose para orquestación
- WhiteNoise para archivos estáticos

---

# Detener la aplicación

```bash
docker compose down
```

---

# Notas

- El proyecto utiliza SQLite para simplificar la ejecución.
- Los datos demo se crean automáticamente al iniciar los contenedores.
- Los archivos estáticos son servidos utilizando WhiteNoise.