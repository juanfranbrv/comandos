#!/usr/bin/env python3
"""
Creador de proyectos Streamlit con pip y venv
"""
import subprocess
import sys
import os
from pathlib import Path

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt, Confirm
    from rich.table import Table
    from rich import print as rprint
except ImportError:
    print("Este script necesita 'rich' para funcionar correctamente.")
    print("Instálalo con: pip install rich")
    sys.exit(1)

console = Console()

def check_pip():
    """Verifica si pip está instalado."""
    try:
        subprocess.run(["pip", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        console.print("[red]❌ pip no está instalado correctamente[/red]")
        console.print("\n[yellow]Instálalo con:[/yellow]")
        console.print("  [cyan]python -m ensurepip --upgrade[/cyan]")
        return False

def check_cursor():
    """Verifica si Cursor está instalado y disponible."""
    try:
        if sys.platform == "win32":
            subprocess.run(["where", "cursor"], capture_output=True, check=True)
        else:
            subprocess.run(["which", "cursor"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_gh():
    """Verifica si GitHub CLI está instalado y disponible."""
    try:
        subprocess.run(["gh", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def create_project(name):
    """Crea un proyecto Streamlit básico."""
    try:
        # Crear el directorio del proyecto
        project_path = Path.cwd() / name
        project_path.mkdir(exist_ok=True)
        
        # Crear archivo requirements.txt con Streamlit
        requirements_path = project_path / "requirements.txt"
        with open(requirements_path, "w") as f:
            f.write("# Dependencias del proyecto\n")
            f.write("streamlit>=1.30.0\n")
        
        # Crear README.md detallado
        readme_content = f"""# {name}

## Descripción
Una aplicación Streamlit creada con streamlit-pip.py.

## Requisitos
- Python 3.8 o superior
- Streamlit y otras dependencias listadas en requirements.txt

## Instalación

1. Clona este repositorio o descárgalo:
   ```bash
   git clone <url-del-repositorio>
   cd {name}
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv .venv
   ```

3. Activa el entorno virtual:
   ```bash
   # En Windows
   .venv\\Scripts\\activate
   
   # En Linux/Mac
   source .venv/bin/activate
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la aplicación Streamlit:
```bash
streamlit run app.py
```

## Estructura del proyecto
```
{name}/
├── app.py                # Aplicación principal de Streamlit
├── .streamlit/           # Configuración de Streamlit
│   └── secrets.toml      # Secretos (no incluidos en Git)
├── .venv/                # Entorno virtual (generado)
├── requirements.txt      # Lista de dependencias
└── README.md             # Este archivo
```

## Licencia
Este proyecto está disponible bajo la licencia MIT.
"""
        readme_path = project_path / "README.md"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
            
        return True, project_path
    except Exception as e:
        console.print(f"[red]Error al crear el proyecto: {e}[/red]")
        return False, None

def create_venv(project_path):
    """Crea un entorno virtual con venv."""
    try:
        subprocess.run([sys.executable, "-m", "venv", ".venv"], cwd=project_path, check=True)
        return True
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error al crear el entorno virtual: {e}[/red]")
        return False

def get_pip_path(project_path):
    """Obtiene la ruta al pip del entorno virtual."""
    if sys.platform == "win32":
        return project_path / ".venv" / "Scripts" / "pip"
    else:
        return project_path / ".venv" / "bin" / "pip"

def install_streamlit(project_path):
    """Instala Streamlit en el entorno virtual."""
    pip_path = get_pip_path(project_path)
    
    with console.status("[bold green]Instalando Streamlit...") as status:
        try:
            subprocess.run([str(pip_path), "install", "streamlit"], cwd=project_path, check=True)
            console.print(f"[green]✓[/green] Streamlit instalado")
            return True
        except subprocess.CalledProcessError:
            console.print(f"[red]✗[/red] Error instalando Streamlit")
            return False

def add_dependencies(project_path):
    """Agrega dependencias adicionales al proyecto."""
    console.print("\n[bold cyan]📦 ¿Deseas agregar otras dependencias además de Streamlit?[/bold cyan]")
    console.print("[dim]Ejemplo: pandas numpy matplotlib plotly altair[/dim]")
    
    dependencies = Prompt.ask(
        "\n[cyan]Dependencias adicionales (separadas por espacios)[/cyan]",
        default=""
    )
    
    if dependencies.strip():
        packages = dependencies.strip().split()
        pip_path = get_pip_path(project_path)
        
        # Actualizar requirements.txt manteniendo streamlit
        requirements_path = project_path / "requirements.txt"
        with open(requirements_path, "r") as f:
            lines = f.readlines()
        
        with open(requirements_path, "w") as f:
            for line in lines:
                f.write(line)
            for pkg in packages:
                f.write(f"{pkg}\n")
        
        with console.status("[bold green]Instalando dependencias adicionales...") as status:
            for pkg in packages:
                status.update(f"[bold green]Instalando {pkg}...")
                try:
                    subprocess.run([str(pip_path), "install", pkg], cwd=project_path, check=True)
                    console.print(f"[green]✓[/green] {pkg} instalado")
                except subprocess.CalledProcessError:
                    console.print(f"[red]✗[/red] Error instalando {pkg}")

def create_app_file(project_path):
    """Crea un archivo app.py con código básico de Streamlit."""
    app_content = """import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mi Aplicación Streamlit",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="auto"
)

# Título principal
st.title("Mi Aplicación Streamlit")

# Sidebar
with st.sidebar:
    st.header("Configuración")
    nombre = st.text_input("Tu nombre")
    color = st.color_picker("Elige un color", "#0066ff")
    
# Contenido principal
st.header("¡Bienvenido a Streamlit!")

if nombre:
    st.markdown(f"### Hola, {nombre}! 👋")
    st.write(f"Tu color elegido es: {color}")
    
    # Demostración de algunos widgets
    tab1, tab2, tab3 = st.tabs(["Datos", "Visualización", "Acerca de"])
    
    with tab1:
        st.subheader("Ejemplo de tabla de datos")
        st.dataframe({
            "Columna 1": [1, 2, 3, 4],
            "Columna 2": [10, 20, 30, 40],
            "Columna 3": ["a", "b", "c", "d"]
        })
        
    with tab2:
        st.subheader("Ejemplo de gráfico")
        st.line_chart({"datos": [1, 5, 2, 6, 2, 8, 3]})
        
    with tab3:
        st.subheader("Acerca de esta aplicación")
        st.info("Esta es una aplicación de demostración creada con Streamlit.")
        with st.expander("Ver más información"):
            st.write(\"\"\"
                Streamlit es una biblioteca de Python que facilita la creación de aplicaciones web 
                para ciencia de datos y machine learning en minutos.
                
                Esta app fue creada automáticamente con el script streamlit-pip.py.
            \"\"\")
else:
    st.info("👈 Ingresa tu nombre en la barra lateral para comenzar")

# Pie de página
st.divider()
st.caption("Creado con Streamlit y venv 🚀")
"""
    
    app_path = project_path / "app.py"
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(app_content)
    console.print(f"[green]✓[/green] Archivo app.py creado")

def create_secrets_folder(project_path):
    """Crea carpeta .streamlit con archivo secrets.toml."""
    secrets_dir = project_path / ".streamlit"
    secrets_dir.mkdir(exist_ok=True)
    
    secrets_path = secrets_dir / "secrets.toml"
    with open(secrets_path, "w", encoding="utf-8") as f:
        f.write("# Archivo de secretos para Streamlit\n")
        f.write("# Agrega tus variables secretas aquí\n\n")
        f.write("API_KEY = \"\"\n")
    
    console.print(f"[green]✓[/green] Configuración de secretos creada")

def open_in_cursor(project_path):
    """Intenta abrir el proyecto en Cursor IDE."""
    try:
        if sys.platform == "win32":
            # En Windows, usar shell=True para mejor compatibilidad
            subprocess.run(f'cursor "{str(project_path)}"', shell=True, check=True)
        else:
            # En Linux/Mac
            subprocess.run(["cursor", str(project_path)], check=True)
        return True
    except Exception as e:
        console.print(f"[yellow]Debug:[/yellow] {e}")
        # Método alternativo
        try:
            os.system(f'cursor "{str(project_path)}"')
            return True
        except Exception as e2:
            console.print(f"[red]Error:[/red] {e2}")
            return False

def create_github_repo(project_name, project_path):
    """Crea un repositorio en GitHub usando gh CLI."""
    try:
        # Primero hacer el commit inicial
        console.print("[dim]Creando commit inicial...[/dim]")
        subprocess.run(["git", "init"], cwd=project_path, check=True)
        subprocess.run(["git", "add", "."], cwd=project_path, check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=project_path, check=True)
        
        # Crear el repositorio en GitHub
        console.print("[dim]Creando repositorio en GitHub...[/dim]")
        subprocess.run(
            ["gh", "repo", "create", project_name, "--public", "--source", ".", "--remote", "origin", "--push"],
            cwd=project_path,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error creando repositorio en GitHub:[/red] {e}")
        return False

def main():
    """Función principal."""
    console.print(Panel.fit(
        "[bold blue]Creador de Proyectos Streamlit con pip y venv[/bold blue]\n[dim]Crea aplicaciones Streamlit modernas con facilidad[/dim]",
        border_style="blue"
    ))
    
    # Verificar pip
    if not check_pip():
        return
    
    # Nombre del proyecto
    project_name = Prompt.ask("\n[bold cyan]📝 Nombre del proyecto Streamlit[/bold cyan]")
    
    if not project_name.strip():
        console.print("[red]❌ El nombre no puede estar vacío[/red]")
        return
    
    project_name = project_name.strip()
    project_path = Path.cwd() / project_name
    
    # Verificar si el proyecto ya existe
    if project_path.exists():
        console.print(f"[red]❌ Ya existe un proyecto con ese nombre[/red]")
        return
    
    # Crear proyecto
    with console.status(f"[bold green]Creando proyecto Streamlit '{project_name}'...") as status:
        success, project_path = create_project(project_name)
        if success:
            console.print(f"[green]✓[/green] Proyecto '{project_name}' creado")
        else:
            console.print(f"[red]✗[/red] Error al crear el proyecto '{project_name}'")
            return
    
    # Crear entorno virtual con venv
    with console.status("[bold green]Creando entorno virtual..."):
        if create_venv(project_path):
            console.print("[green]✓[/green] Entorno virtual creado")
        else:
            console.print("[red]✗[/red] Error al crear entorno virtual")
            return
            
    # Instalar Streamlit
    with console.status("[bold green]Instalando Streamlit..."):
        if not install_streamlit(project_path):
            console.print("[red]✗[/red] No se pudo instalar Streamlit, el proyecto podría no funcionar correctamente")
    
    # Agregar dependencias adicionales si el usuario quiere
    add_dependencies(project_path)
    
    # Crear archivos específicos de Streamlit
    create_app_file(project_path)
    create_secrets_folder(project_path)

    # Crear .gitignore
    with console.status("[bold green]Creando .gitignore..."):
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
.Python
env/
venv/
.env
.venv/

# Streamlit
.streamlit/secrets.toml

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/

# Build
build/
dist/
*.egg-info/
"""
        gitignore_path = project_path / ".gitignore"
        with open(gitignore_path, "w") as f:
            f.write(gitignore_content)
        console.print("[green]✓[/green] Archivo .gitignore creado")
    
    # Preguntar si crear repositorio en GitHub
    if check_gh():
        if Confirm.ask("\n[cyan]¿Crear repositorio en GitHub?[/cyan]", default=False):
            if create_github_repo(project_name, project_path):
                console.print("[green]✓[/green] Repositorio creado en GitHub")
            else:
                console.print("[yellow]⚠️[/yellow] No se pudo crear el repositorio en GitHub")
    
    # Preguntar si abrir en Cursor (solo si está instalado)
    if check_cursor():
        if Confirm.ask("\n[cyan]¿Abrir proyecto en Cursor IDE?[/cyan]", default=False):
            if open_in_cursor(project_path):
                console.print("[green]✓[/green] Abriendo en Cursor IDE...")
            else:
                console.print("[yellow]⚠️[/yellow] No se pudo abrir Cursor IDE")
    
    # Instrucciones finales
    console.print("\n[bold green]✨ ¡Proyecto Streamlit listo![/bold green]\n")
    
    instructions = Table(show_header=False, box=None, padding=(0, 2))
    instructions.add_column("Paso", style="yellow")
    instructions.add_column("Comando", style="cyan")
    
    instructions.add_row("1.", f"cd {project_name}")
    instructions.add_row("2.", ".venv\\Scripts\\activate" if sys.platform == "win32" else "source .venv/bin/activate")
    instructions.add_row("3.", "streamlit run app.py")
    
    console.print(Panel(instructions, title="[bold]Próximos pasos[/bold]", border_style="green"))
    
    # Comandos útiles
    tips = Table(show_header=False, box=None, padding=(0, 2))
    tips.add_column("Comando", style="cyan")
    tips.add_column("Descripción", style="white")
    
    tips.add_row("pip install <paquete>", "Agregar dependencias")
    tips.add_row("pip freeze > requirements.txt", "Actualizar requirements.txt")
    tips.add_row("streamlit --help", "Ver opciones de Streamlit")
    
    console.print(Panel(tips, title="[bold]Comandos útiles[/bold]", border_style="blue"))

if __name__ == "__main__":
    main() 