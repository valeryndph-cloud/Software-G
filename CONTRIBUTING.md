cat > CONTRIBUTING.md <<'EOF'
# Cómo trabajamos en nuestra empresa

## Ramas

Usamos nombres en minúsculas, sin espacios y separados por guiones.
Cada rama debe comenzar con el tipo de tarea:

- feat/: para nuevas funcionalidades.
- fix/: para corregir errores.
- docs/: para documentación.
- chore/: para configuración y mantenimiento.

Ejemplo: docs/contributing

## Commits

Los commits deben escribirse en minúsculas, en presente y con el formato:

tipo: descripción del cambio

Usamos estos tipos:

- feat: para agregar funcionalidades.
- fix: para corregir errores.
- docs: para modificar documentación.
- chore: para configuración y mantenimiento.

Ejemplos:
- docs: crear reglas del equipo
- feat: agregar estructura del proyecto
- fix: corregir error de validación
- chore: configurar archivos iniciales

## Revisión de Pull Requests

Cada integrante debe revisar el trabajo de otro compañero.
Nadie puede aprobar su propio Pull Request.

Los revisores se asignan por turnos para que todos participen.
Antes de aprobar, se debe comprobar que los cambios cumplan la tarea,
que los archivos estén bien organizados y que no existan errores evidentes.

## Cuándo se aprueba un Pull Request

Para aprobar un Pull Request se requiere:

- Que el cambio cumpla con la tarea asignada.
- Que el código o la documentación sean claros y estén organizados.
- Que no se incluyan contraseñas, claves ni archivos innecesarios.
- Que otro integrante revise los cambios y los apruebe.
- Que se solucionen las observaciones realizadas durante la revisión.

Después de cumplir estos requisitos, el Pull Request puede fusionarse
con la rama main.
EOF