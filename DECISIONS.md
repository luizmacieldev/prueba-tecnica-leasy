# Decisiones Técnicas

## 1. Validación de reglas de negocio en servicios

La lógica de cancelación de reservas fue implementada en una capa de servicios para separar reglas de negocio de los endpoints.

Se validan:

- propiedad de la reserva
- estados permitidos
- motivo obligatorio de cancelación

---

## 2. Persistencia de sesión en frontend

Decidí persistir el token JWT usando localStorage para mantener la sesión activa después de actualiza la página.

---

## 3. Integración del perfil autenticado

La mini app consume el endpoint `/auth/me` para mostrar información del cliente autenticado en la interfaz.

---

## 4. Configuración de CORS

Utilicé `django-cors-headers` para permitir la comunicación entre el frontend React y el backend Django durante el desarrollo local y la ejecución con Docker.

---

## 5. Dockerización completa

Backend y frontend fueron dockerizados usando Docker Compose para permitir ejecutar toda la solución con un solo comando.

---

## 6. WhiteNoise para archivos estáticos

Utilicé WhiteNoise para servir archivos estáticos del Django utilizando Gunicorn dentro del contenedor Docker.

---

# Alternativa descartada

## PostgreSQL

Consideré utilizar PostgreSQL, pero decidí mantener SQLite porque el assessment permitía usarlo y simplificaba la configuración del entorno.

---
## Tailwind Components o librerías UI

Consideré utilizar una librería de componentes UI, pero preferí mantener una interfaz simple utilizando TailwindCSS para enfocarme en la integración con la API y la lógica del flujo principal.

# Mejoras Futuras

- Agregar pruebas automatizadas para el frontend.
- Implementar refresh tokens para autenticación JWT.
- Agregar validaciones de fechas, por ejemplo validar que la fecha de fin no sea menor que la fecha de inicio.
- Permitir que el manager pueda cambiar nuevamente una reserva en estado "en espera" a "confirmado".
- Mejorar el manejo de estados y feedback visual del frontend.