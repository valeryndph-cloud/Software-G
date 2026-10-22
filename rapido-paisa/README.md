# Rápido Paisa

Programa de práctica para organizar pedidos de domicilios de las sedes de Itagüí, Envigado y Sabaneta.

## Archivos principales

- `generar_pedidos.py`: script entregado por el cliente para generar los pedidos de prueba. Cuando esté disponible, no se debe modificar.
- `organizar.py`: programa principal que ejecuta la organización de pedidos.
- `sedes.py`: reconoce a qué sede pertenece un pedido.
- `lectores.py`: permite leer pedidos en archivos TXT, CSV y JSON.
- `.gitignore`: evita que los datos y resultados generados se suban al repositorio.

## Requisitos

- Python 3 instalado.
- Abrir una terminal dentro de la carpeta `rapido-paisa`.

## Cómo ejecutar

Cuando el cliente haya entregado `generar_pedidos.py`, ejecuta primero:

```bash
python generar_pedidos.py
```

Después ejecuta el programa principal:

```bash
python organizar.py
```

En algunos equipos de Windows, puede ser necesario usar `py` en lugar de `python`.

> Nota: los scripts deben estar implementados y el archivo `generar_pedidos.py` debe estar disponible para que estos comandos funcionen. El archivo del cliente no debe modificarse.

## Cómo funciona

1. Se generan o reciben los pedidos de entrada.
2. Se leen los datos de cada pedido según su formato.
3. Se identifica la sede correspondiente: Itagüí, Envigado o Sabaneta.
4. El programa principal organiza los pedidos y separa los casos que necesiten revisión, según las reglas de la actividad.

## Archivos generados y Git

Los directorios `bandeja_entrada/`, `pedidos_ordenados/`, `revisar/`, `datos/` y `resultados/` están en `.gitignore` porque contienen datos de entrada o resultados creados al ejecutar el programa. No deben entregarse como archivos versionados.

Para revisar qué archivos Git detecta, ejecuta desde la carpeta del repositorio:

```bash
git status --short
```

Después de generar pedidos y resultados, vuelve a ejecutar `git status --short`. Los archivos guardados en las carpetas ignoradas no deben aparecer como archivos nuevos para subir. No agregues datos generados manualmente con `git add`.

## Comprobación rápida de la función de sedes

La función `reconocer_sede(pedido)` recibe un texto o un diccionario. Devuelve `"Itagüí"`, `"Envigado"` o `"Sabaneta"`. Si no puede identificar la sede, devuelve `None` para que el pedido pueda revisarse.

## Flujo de trabajo del equipo

Trabaja en una rama por tarea y abre un Pull Request hacia `main`. Incluye `Closes #número` en la descripción, solicita la revisión de un compañero y espera la aprobación antes de integrar los cambios.
