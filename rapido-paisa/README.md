# Rápido Paisa

Programa de práctica para organizar pedidos de domicilios de las sedes de Itagüí, Envigado y Sabaneta.

## Archivos principales

- `generar_pedidos.py`: script entregado por el cliente para crear pedidos de prueba. No se debe modificar.
- `organizar.py`: será el programa principal que organiza los pedidos. Actualmente solo tiene el comentario inicial, así que todavía no realiza la organización.
- `sedes.py`: debe contener la función para reconocer la sede de cada pedido.
- `lectores.py`: debe contener las funciones para leer pedidos en archivos TXT, CSV y JSON.
- `.gitignore`: evita que los datos de entrada y los resultados generados se suban a GitHub.

## Requisitos

- Tener Python 3 instalado.
- Abrir una terminal dentro de la carpeta `rapido-paisa`.

## Cómo generar los pedidos de prueba

Para crear el primer lote, ejecuta:

```bash
python generar_pedidos.py
```

Para crear el segundo lote, ejecuta:

```bash
python generar_pedidos.py --lote 2
```

En algunos equipos con Windows puedes usar `py` en lugar de `python`.

**Importante:** el generador borra la carpeta `bandeja_entrada/` si ya existe y la vuelve a crear. Si tienes archivos propios allí, guárdalos antes de ejecutar el generador. No modifiques `generar_pedidos.py`, porque es el archivo entregado por el cliente.

## Cómo ejecutar el programa principal

Cuando la función de organización esté implementada en `organizar.py`, se podrá ejecutar con:

```bash
python organizar.py
```

Por ahora, ese archivo todavía no organiza los pedidos. Los módulos `sedes.py` y `lectores.py` también tienen que contar con sus funciones implementadas para completar el proceso.

## Cómo funciona el sistema

1. El generador crea archivos de pedidos de prueba en `bandeja_entrada/`, con diferentes nombres y formatos.
2. El lector debe abrir los archivos TXT, CSV y JSON y obtener los datos de cada pedido.
3. La función de reconocimiento debe identificar si el pedido corresponde a Itagüí, Envigado o Sabaneta.
4. El programa principal debe organizar las copias de los pedidos por sede y separar los que tengan datos dañados o no permitan identificar la sede.
5. Los archivos originales de `bandeja_entrada/` deben conservarse sin modificaciones.

## Archivos generados y Git

El archivo `.gitignore` excluye las carpetas `bandeja_entrada/`, `pedidos_ordenados/`, `revisar/`, `datos/` y `resultados/`, además de los archivos temporales de Python y los entornos virtuales. Estas carpetas contienen datos de entrada o resultados generados, por lo que no deben subirse al repositorio.

Para revisar qué archivos detecta Git, ejecuta desde la carpeta del repositorio:

```bash
git status --short
```

Después de generar pedidos o resultados, vuelve a ejecutar el comando. Los archivos dentro de las carpetas ignoradas no deberían aparecer como archivos nuevos para subir. No agregues manualmente los datos generados con `git add`.

## Comprobación de la función de sedes

Cuando `reconocer_sede(pedido)` esté implementada, debe aceptar el texto o los datos de un pedido, reconocer Itagüí, Envigado o Sabaneta aunque cambien las mayúsculas o las tildes, y devolver `None` cuando no pueda identificar la sede. Los casos que devuelvan `None` deben quedar pendientes de revisión.

## Flujo de trabajo del equipo

Trabaja en una rama por tarea y abre un Pull Request hacia `main`. Incluye `Closes #número` en la descripción, solicita la revisión de un compañero y espera la aprobación antes de integrar los cambios.
