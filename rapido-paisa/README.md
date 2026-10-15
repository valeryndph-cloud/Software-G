# Rápido Paisa

Actividad de simulación de entregas. El código se versiona; los archivos de
pedidos de entrada y los resultados generados se mantienen fuera de Git.

## Estructura

```text
rapido-paisa/
├── organizar.py       # Programa principal
├── sedes.py           # Reconocimiento de la sede
├── lectores.py        # Lectura de archivos .txt, .csv y .json
├── config.json        # Configuración de la Parte 3
├── generar_pedidos.py # Script del cliente; se incorpora cuando se entregue
├── README.md
├── .gitignore
└── docs/
    └── bitacora/
```

Los módulos y archivos de configuración se completarán según los
requerimientos de cada parte de la actividad. No se debe modificar
`generar_pedidos.py` cuando se incorpore.

## Parte 0: organización

- Crear en GitHub el proyecto de tipo Board y vincularlo con este repositorio.
- Invitar a los integrantes con permiso Write y configurar la visibilidad
  solicitada para el tablero.
- Crear la etiqueta `R1` y el campo de fecha `Fecha límite`.
- Mantener los tickets asignados en el tablero, moverlos a In Progress al
  comenzar y relacionar cada Pull Request con su ticket usando `Closes #N`.

Cada integrante debe tener al menos un ticket propio y revisar al menos un
Pull Request de un compañero por requerimiento.

## Reglas de archivos

El `.gitignore` de esta carpeta excluye los datos y resultados generados,
`__pycache__/` y `.venv/`. Para comprobarlo, ejecuta `git status` desde esta
carpeta después de generar los datos.
