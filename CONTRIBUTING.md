# Cómo trabajamos en Software-G

## Ramas

Usamos nombres en minúsculas, sin espacios y separados por guiones. Cada rama comienza con el tipo de tarea:

- `feat/`: nuevas funcionalidades.
- `fix/`: correcciones de errores.
- `docs/`: documentación.
- `chore/`: configuración y mantenimiento.

Ejemplo: `docs/actualizar-readme`.

## Commits

Los commits se escriben en minúscula, en presente y con el formato `tipo: descripción`.

- `feat: agregar formulario de registro`
- `fix: corregir validación`
- `docs: completar README`
- `chore: configurar estructura inicial`

## Revisión de Pull Requests

Cada integrante revisa el trabajo de otro compañero. Nadie debe aprobar su propio Pull Request. Para esta actividad, la revisión se organiza en cadena:

| Autor del Pull Request | Persona que revisa |
|---|---|
| Alejandro Varela Chacón | Valeryn Perea Higuita |
| Ximena Jiménez | Alejandro Varela Chacón |
| Juliana Betancur | Ximena Jiménez |
| Valeryn Perea Higuita | Juliana Betancur |

La persona revisora compara el cambio con el Issue, revisa la organización, la claridad, la ortografía y la convención de los commits. Debe dejar al menos un comentario concreto de mejora sobre una línea del cambio. El autor corrige en la misma rama y responde al comentario. Después, quien revisa resuelve la conversación y aprueba.

## Cuándo se aprueba un Pull Request

Se puede aprobar cuando:

- El cambio cumple los criterios del Issue.
- Los archivos están bien ubicados y la documentación o el código son claros.
- Los commits siguen la convención acordada.
- No se incluyen contraseñas, claves, archivos generados ni información innecesaria.
- Las observaciones de revisión fueron atendidas.
- La revisión fue realizada y aprobada por otro integrante.

Después de la aprobación, el autor puede fusionar el Pull Request con `main`. No se deben hacer cambios directos en `main`; se trabaja mediante Issues, ramas y Pull Requests.
