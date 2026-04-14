# Consigna para el candidato

## Objetivo

Queremos evaluar cómo entiendes una base de código existente y cómo extiendes un
flujo real con buen criterio técnico.

La prueba está dividida en tres partes:

1. Backoffice Django con templates.
2. Mini app cliente en el framework frontend que prefieras.
3. Dockerización de la solución.

## Tiempo esperado

- `3.5 a 4.5 horas` en total.

## Regla sobre IA

Puedes usar herramientas externas, incluida IA, si lo declaras.

Lo que evaluaremos es:

- si entiendes tu solución
- si puedes defenderla
- si puedes modificarla en vivo

El uso de IA no compensa una falta de comprensión del código entregado.

## Parte 1: Backoffice Django

### Feature

Agregar el estado `ON_HOLD` a una reserva con motivo obligatorio.

### Requerimientos

- Una reserva puede pasar a `ON_HOLD`.
- Al pasar a `ON_HOLD`, se debe registrar `hold_reason`.
- El motivo debe verse en el detalle de la reserva.
- El listado debe reflejar el nuevo estado.
- Solo usuarios con el permiso `reservations.hold_reservation` pueden ejecutar
  esa acción.
- La validación debe estar en backend.
- Debes agregar tests relevantes de servicio y/o vista.

### Qué esperamos que mantengas

- Vistas finas.
- Lógica de negocio en servicios.
- Permisos reales en backend, no solo ocultar botones.
- Uso consistente de constantes y errores del dominio.

## Parte 2: Mini app cliente

Construye una mini app dentro de `client-app/` con el framework frontend que
prefieras.

### Feature

Permitir que un cliente cancele su propia reserva con motivo.

### API disponible hoy

- `POST /api/v1/auth/login`
- `GET /api/v1/auth/me`
- `GET /api/v1/reservations/`

### API que debes agregar

- `POST /api/v1/reservations/{reservation_id}/cancel`

### Reglas del endpoint

- Solo el dueño de la reserva puede cancelarla.
- Requiere `reason`.
- Solo se puede cancelar si la reserva está en un estado permitido.
- Si falla, debe responder con un error estable del API.

### Qué debe incluir la mini app

- Login simple.
- Pantalla “Mis reservas”.
- Acción “Cancelar reserva”.
- Formulario o modal para ingresar motivo.
- Actualización visual del estado.
- Manejo claro de errores del API.

## Parte 3: Docker

Debes dockerizar la solución completa para demostrar criterio de empaquetado,
reproducibilidad y setup de ejecución.

### Requerimientos

- Agregar un `Dockerfile` para el backend Django.
- Agregar un `Dockerfile` para la mini app cliente dentro de `client-app/`.
- Agregar un `docker-compose.yml` en la raíz del repo para levantar ambos
  servicios.
- Documentar en el `README.md` o en un `DOCKER.md` cómo construir y correr la
  solución con Docker.

### Qué esperamos del Dockerfile del backend

- Debe estar pensado para producción, no para desarrollo improvisado.
- Debe evitar correr como `root` si no es necesario.
- Debe instalar dependencias de forma reproducible.
- Debe aprovechar bien el cache de capas.
- No debe depender de `runserver` como comando principal final.
- Debe ser razonablemente pequeño y limpio.

### Qué esperamos del compose

- Debe levantar backend y cliente con un solo comando.
- Debe dejar claro cómo se pasan variables de entorno necesarias.
- Debe permitir probar el flujo principal sin pasos manuales raros.

### Restricciones

- No es obligatorio migrar el starter a PostgreSQL.
- Puedes seguir usando SQLite para la prueba si lo documentas bien.
- No se evalúa Kubernetes ni despliegue cloud.

## Entrega

Debes entregar:

- tu código completo
- tests backend relevantes
- dockerización funcional de backend y cliente
- un archivo `DECISIONS.md` con:
  - 3 decisiones técnicas que tomaste
  - 1 alternativa que descartaste y por qué
- historial de commits razonable

## Qué no queremos

- refactors masivos del starter
- cambiar la arquitectura base sin necesidad
- esconder permisos solo en UI
- meter dependencias innecesarias
- una imagen Docker que solo funcione en tu máquina sin documentación clara

