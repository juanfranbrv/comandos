# Generadores de Proyectos Python con UV

Una colección de herramientas para crear proyectos Python estructurados de forma rápida y elegante, utilizando UV como gestor de paquetes y entornos virtuales.

## 📋 Contenido

- [Descripción](#descripción)
- [Herramientas incluidas](#herramientas-incluidas)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Ejemplos](#ejemplos)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## 📝 Descripción

Este proyecto proporciona scripts para automatizar la creación de proyectos Python estructurados, utilizando [UV](https://github.com/astral-sh/uv) como gestor de paquetes y entornos virtuales. UV es una alternativa ultrarrápida a pip y venv, escrita en Rust.

Los scripts te permiten crear un nuevo proyecto con toda la estructura necesaria, un entorno virtual configurado, repositorio Git inicializado, y más, todo con una interfaz visual elegante en la terminal.

## 🛠️ Herramientas incluidas

### 1. Generador de Proyectos Python (`python-uv.py`)

Crea proyectos Python genéricos con UV, ideal para cualquier tipo de desarrollo en Python.

### 2. Generador de Proyectos Streamlit (`streamlit-uv.py`)

Crea aplicaciones web con Streamlit, configuradas y listas para ejecutar. Incluye un app.py de ejemplo que muestra las características principales de Streamlit.

## 📋 Requisitos

- Python 3.8 o superior
- [UV](https://github.com/astral-sh/uv) instalado
- Paquete `rich` para Python (`pip install rich`)
- Git (opcional, para inicializar repositorios)
- GitHub CLI (opcional, para crear repositorios remotos)
- Cursor IDE (opcional, para abrir proyectos)

## ⚙️ Instalación

1. Clona o descarga este repositorio en tu sistema
2. Asegúrate de tener instalado UV:

```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Instala rich si no lo tienes:

```bash
pip install rich
```

## 📚 Uso

### Crear un proyecto Python con UV:

```bash
# Desde la terminal
python python-uv.py

# En Windows, también puedes hacer doble clic en:
python-uv.bat
```

### Crear un proyecto Streamlit con UV:

```bash
# Desde la terminal
python streamlit-uv.py

# En Windows, también puedes hacer doble clic en:
streamlit-uv.bat
```

## ✨ Características

### Ambos generadores:

- 🎨 Interfaz visual con Rich (colores, tablas, paneles)
- 📦 Gestión de dependencias con UV (mucho más rápido que pip)
- 🔧 Inicialización automática de Git con .gitignore
- 🌍 Creación de entorno virtual automática
- 🐙 Integración con GitHub (con `gh` CLI)
- 💻 Integración con Cursor IDE
- 📄 Generación de README.md detallado

### Generador de Streamlit:

- 🚀 Plantilla de aplicación Streamlit lista para usar
- 🔑 Configuración de secrets para Streamlit
- 📊 Ejemplos de componentes y visualizaciones

## 📋 Ejemplos

### Proyecto Python estándar:

```
mi-proyecto/
├── .gitignore          # Configurado para Python
├── .venv/              # Entorno virtual (creado por UV)
├── main.py             # Punto de entrada
├── pyproject.toml      # Configuración y dependencias
└── README.md           # Documentación generada
```

### Proyecto Streamlit:

```
mi-app-streamlit/
├── .gitignore          # Configurado para Python y Streamlit
├── .streamlit/         # Configuración de Streamlit
│   └── secrets.toml    # Archivo de secretos
├── .venv/              # Entorno virtual (creado por UV)
├── app.py              # Aplicación Streamlit de ejemplo
├── pyproject.toml      # Configuración y dependencias
└── README.md           # Documentación generada
```

## 🤝 Contribuir

Las contribuciones son bienvenidas. Puedes:

1. Abrir issues para reportar bugs o sugerir mejoras
2. Enviar pull requests con nuevas características o correcciones
3. Mejorar la documentación
4. Compartir el proyecto con otros desarrolladores

## 📜 Licencia

Este proyecto está disponible bajo la licencia MIT.
