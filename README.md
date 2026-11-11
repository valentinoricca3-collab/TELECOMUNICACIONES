# Carrera en la Ruta 🚗

Un juego 2D de autos hecho en Python con Pygame. Controlás un auto, esquivás el tránsito y tratás de conseguir el puntaje más alto posible.

## Requisitos

- Python 3.10 o superior
- pip

## Cómo instalarlo

1. Descargá o cloná este repositorio.
2. Abrí una terminal dentro de la carpeta del proyecto.
3. Instalá la dependencia:

```bash
python -m pip install -r requirements.txt
```

## Cómo jugar

Ejecutá:

```bash
python main.py
```

Controles:
- Flecha izquierda o A: mover el auto a la izquierda.
- Flecha derecha o D: mover el auto a la derecha.
- ENTER: volver a jugar después de chocar.
- ESC: salir.

## Archivos

- `main.py`: inicia el juego y controla el ciclo principal.
- `settings.py`: configuración de pantalla, colores y velocidad.
- `player.py`: comportamiento y dibujo del auto del jugador.
- `traffic.py`: autos del tránsito.
- `requirements.txt`: librerías necesarias.

## Objetivo

Evitá chocar con los otros autos. El puntaje aumenta con el tiempo y la velocidad se incrementa progresivamente.

## Tecnologías

- Python
- Pygame
