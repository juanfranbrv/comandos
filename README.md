# Generadores de Proyectos Python

Una colección de herramientas para crear proyectos Python estructurados de forma rápida y elegante, con soporte para diferentes gestores de paquetes y entornos virtuales.

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

Este proyecto proporciona scripts para automatizar la creación de proyectos Python estructurados, con soporte para dos sistemas diferentes de gestión de dependencias:

- **UV**: Una alternativa ultrarrápida a pip y venv, escrita en Rust.
- **pip + venv**: El sistema tradicional de Python para gestionar paquetes y entornos virtuales.

Los scripts te permiten crear un nuevo proyecto con toda la estructura necesaria, un entorno virtual configurado, repositorio Git inicializado, y más, todo con una interfaz visual elegante en la terminal.

## 🛠️ Herramientas incluidas

### Generadores con UV

1. **python-uv.py**: Crea proyectos Python genéricos con UV, ideal para cualquier tipo de desarrollo en Python.
2. **streamlit-uv.py**: Crea aplicaciones web con Streamlit utilizando UV como gestor de paquetes.

### Generadores con pip + venv

3. **python-pip.py**: Crea proyectos Python genéricos con pip y venv, siguiendo el enfoque tradicional.
4. **streamlit-pip.py**: Crea aplicaciones web con Streamlit utilizando pip y venv.

## 📋 Requisitos

- Python 3.8 o superior
- Para los scripts con UV: [UV](https://github.com/astral-sh/uv) instalado
- Para los scripts con pip: pip actualizado
- Paquete `rich` para Python (`pip install rich`)
- Git (opcional, para inicializar repositorios)
- GitHub CLI (opcional, para crear repositorios remotos)
- Cursor IDE (opcional, para abrir proyectos)

## ⚙️ Instalación

1. Clona o descarga este repositorio en tu sistema:
   ```bash
   git clone https://github.com/juanfranbrv/comandos.git
   cd comandos
   ```

2. Para usar los scripts con UV, instala UV:
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

### Usando los generadores con UV:

```bash
# Crear un proyecto Python con UV
python python-uv.py
# o usando el archivo batch en Windows:
python-uv.bat

# Crear un proyecto Streamlit con UV
python streamlit-uv.py
# o usando el archivo batch en Windows:
streamlit-uv.bat
```

### Usando los generadores con pip + venv:

```bash
# Crear un proyecto Python con pip + venv
python python-pip.py
# o usando el archivo batch en Windows:
python-pip.bat

# Crear un proyecto Streamlit con pip + venv
python streamlit-pip.py
# o usando el archivo batch en Windows:
streamlit-pip.bat
```

## ✨ Características

### Todos los generadores:

- 🎨 Interfaz visual con Rich (colores, tablas, paneles)
- 🔧 Inicialización automática de Git con .gitignore
- 🌍 Creación de entorno virtual automática
- 🐙 Integración con GitHub (con `gh` CLI)
- 💻 Integración con Cursor IDE
- 📄 Generación de README.md detallado

### Específico de los generadores con UV:

- 📦 Gestión de dependencias con UV (mucho más rápido que pip)
- 🚀 Comando `uv sync` para sincronizar entorno y dependencias
- 🔄 No requiere activar el entorno virtual para ejecutar scripts

### Específico de los generadores con pip + venv:

- 📦 Gestión de dependencias con el sistema tradicional de pip
- 📋 Creación y actualización de requirements.txt
- 🔄 Requiere activar el entorno virtual antes de ejecutar

### Generadores de Streamlit:

- 🚀 Plantilla de aplicación Streamlit lista para usar
- 🔑 Configuración de secrets para Streamlit
- 📊 Ejemplos de componentes y visualizaciones

## 📋 Ejemplos

### Proyectos Python estándar:

```
# Con UV
mi-proyecto/
├── .gitignore          # Configurado para Python
├── .venv/              # Entorno virtual (creado por UV)
├── main.py             # Punto de entrada
├── pyproject.toml      # Configuración y dependencias
└── README.md           # Documentación generada

# Con pip + venv
mi-proyecto-pip/
├── .gitignore          # Configurado para Python
├── .venv/              # Entorno virtual (creado por venv)
├── main.py             # Punto de entrada
├── requirements.txt    # Lista de dependencias
└── README.md           # Documentación generada
```

### Proyectos Streamlit:

```
# Con UV
mi-app-streamlit-uv/
├── .gitignore          # Configurado para Python y Streamlit
├── .streamlit/         # Configuración de Streamlit
│   └── secrets.toml    # Archivo de secretos
├── .venv/              # Entorno virtual (creado por UV)
├── app.py              # Aplicación Streamlit de ejemplo
├── pyproject.toml      # Configuración y dependencias
└── README.md           # Documentación generada

# Con pip + venv
mi-app-streamlit-pip/
├── .gitignore          # Configurado para Python y Streamlit
├── .streamlit/         # Configuración de Streamlit
│   └── secrets.toml    # Archivo de secretos
├── .venv/              # Entorno virtual (creado por venv)
├── app.py              # Aplicación Streamlit de ejemplo
├── requirements.txt    # Lista de dependencias
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
