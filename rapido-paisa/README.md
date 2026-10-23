# Rápido Paisa

Programa de práctica para organizar pedidos de domicilios de las sedes de Itagüí, Envigado, Sabaneta y Bello.

## Archivos principales

- `generar_pedidos.py`: script entregado por el cliente para crear pedidos de prueba. No se debe modificar.
- `organizar.py`: programa principal que debe organizar los pedidos por sede y separar los que necesitan revisión. Verifica que sus funciones estén implementadas antes de dar por terminada la ejecución.
- `sedes.py`: contiene la función para reconocer la sede de cada pedido.
- `lectores.py`: contiene las funciones para leer pedidos en archivos TXT, CSV y JSON.
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

Cuando la organización esté implementada y sus módulos estén listos, ejecuta:

```bash
python organizar.py
```

Si todavía hay funciones pendientes en `organizar.py`, `sedes.py` o `lectores.py`, el proceso completo puede no funcionar. Comprueba el resultado con los pedidos de prueba antes de dar la tarea por validada.

## Cómo funciona el sistema

1. El generador crea archivos de pedidos de prueba en `bandeja_entrada/`, con diferentes nombres y formatos.
2. Los lectores deben abrir los archivos TXT, CSV y JSON y obtener los datos de cada pedido.
3. La función de reconocimiento debe identificar si el pedido corresponde a Itagüí, Envigado, Sabaneta o Bello.
4. El programa principal debe organizar las copias de los pedidos por sede y separar los que tengan datos dañados o no permitan identificar la sede.
5. Los archivos originales de `bandeja_entrada/` deben conservarse sin modificaciones.

## Archivos generados y Git

El archivo `.gitignore` excluye las carpetas `bandeja_entrada/`, `pedidos_ordenados/`, `revisar/`, `datos/` y `resultados/`, además de los archivos temporales de Python, los entornos virtuales y los archivos `.env` que pueden contener datos privados. Estas carpetas contienen datos de entrada o resultados generados, por lo que no deben subirse al repositorio.

Para revisar qué archivos detecta Git, ejecuta desde la carpeta del repositorio:

```bash
git status --short
```

Después de generar pedidos o resultados, vuelve a ejecutar el comando. Los archivos dentro de las carpetas ignoradas no deberían aparecer como archivos nuevos para subir. No agregues manualmente los datos generados con `git add`.

## Comprobación de la función de sedes

La función `reconocer_sede(pedido)` debe reconocer Itagüí, Envigado, Sabaneta y Bello aunque cambien las mayúsculas o las tildes, y devolver `None` cuando no pueda identificar una sede. También conviene probar pedidos con texto, diccionarios, datos vacíos (`None`) y pedidos que mencionen más de una sede, para evitar resultados incorrectos. Los casos que no permitan identificar una sede deben quedar pendientes de revisión.

## Flujo de trabajo del equipo

Trabaja en una rama por tarea y abre un Pull Request hacia `main`. Incluye `Closes #número` en la descripción, solicita la revisión de un compañero y espera la aprobación antes de integrar los cambios.
