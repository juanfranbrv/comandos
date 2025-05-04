#!/usr/bin/env python3
"""
Creador de proyectos Python con UV
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

def check_uv():
    """Verifica si UV está instalado."""
    try:
        subprocess.run(["uv", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        console.print("[red]❌ UV no está instalado[/red]")
        console.print("\n[yellow]Instálalo con:[/yellow]")
        console.print("  Windows:  [cyan]powershell -c \"irm https://astral.sh/uv/install.ps1 | iex\"[/cyan]")
        console.print("  Linux/Mac: [cyan]curl -LsSf https://astral.sh/uv/install.sh | sh[/cyan]")
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
    """Crea un proyecto con UV."""
    try:
        subprocess.run(["uv", "init", name], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def add_dependencies(project_path):
    """Agrega dependencias al proyecto."""
    console.print("\n[bold cyan]📦 Escribe las dependencias que deseas instalar:[/bold cyan]")
    console.print("[dim]Ejemplo: requests fastapi pytest rich[/dim]")
    
    dependencies = Prompt.ask(
        "\n[cyan]Dependencias (separadas por espacios)[/cyan]",
        default=""
    )
    
    if dependencies.strip():
        packages = dependencies.strip().split()
        
        with console.status("[bold green]Instalando dependencias...") as status:
            for pkg in packages:
                status.update(f"[bold green]Instalando {pkg}...")
                try:
                    subprocess.run(["uv", "add", pkg], cwd=project_path, check=True)
                    console.print(f"[green]✓[/green] {pkg} instalado")
                except subprocess.CalledProcessError:
                    console.print(f"[red]✗[/red] Error instalando {pkg}")

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
        subprocess.run(["git", "add", "."], cwd=project_path, check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=project_path, check=True)
        
        # Crear el repositorio en GitHub
        console.print("[dim]Creando repositorio en GitHub...[/dim]")
        subprocess.run(
            ["gh", "repo", "create", project_name, "--private", "--source", ".", "--remote", "origin", "--push"],
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
        "[bold blue]Creador de Proyectos Python con UV[/bold blue]\n[dim]Crea proyectos Python modernos con facilidad[/dim]",
        border_style="blue"
    ))
    
    # Verificar UV
    if not check_uv():
        return
    
    # Nombre del proyecto
    project_name = Prompt.ask("\n[bold cyan]📝 Nombre del proyecto[/bold cyan]")
    
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
    with console.status(f"[bold green]Creando proyecto '{project_name}'...") as status:
        if create_project(project_name):
            console.print(f"[green]✓[/green] Proyecto '{project_name}' creado")
        else:
            console.print(f"[red]✗[/red] Error al crear el proyecto '{project_name}'")
            return
    
    # Agregar dependencias si el usuario quiere
    if Confirm.ask("\n[cyan]¿Deseas agregar dependencias?[/cyan]", default=False):
        add_dependencies(project_path)
    
    # Crear entorno virtual y sincronizar
    with console.status("[bold green]Creando entorno virtual y sincronizando..."):
        try:
            # UV sync automáticamente crea el entorno virtual si no existe
            subprocess.run(["uv", "sync"], cwd=project_path, check=True)
            console.print("[green]✓[/green] Entorno virtual creado y dependencias instaladas")
        except subprocess.CalledProcessError:
            console.print("[red]✗[/red] Error al crear entorno virtual")
    
    # Inicializar Git automáticamente
    with console.status("[bold green]Inicializando Git..."):
        try:
            subprocess.run(["git", "init"], cwd=project_path, check=True)
            # Crear .gitignore
            gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
.Python
env/
venv/
.env
.venv/

# UV
.uv/
uv.lock

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
            with open(gitignore_path, "w", encoding="utf-8") as f:
                f.write(gitignore_content)
            console.print("[green]✓[/green] Repositorio Git inicializado")
        except subprocess.CalledProcessError:
            console.print("[yellow]⚠️[/yellow] Git no está instalado o no se pudo inicializar")
    
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
    console.print("\n[bold green]✨ ¡Proyecto listo![/bold green]\n")
    
    instructions = Table(show_header=False, box=None, padding=(0, 2))
    instructions.add_column("Paso", style="yellow")
    instructions.add_column("Comando", style="cyan")
    
    instructions.add_row("1.", f"cd {project_name}")
    instructions.add_row("2.", "uv run main.py")
    
    console.print(Panel(instructions, title="[bold]Próximos pasos[/bold]", border_style="green"))
    
    # Comandos útiles
    tips = Table(show_header=False, box=None, padding=(0, 2))
    tips.add_column("Comando", style="cyan")
    tips.add_column("Descripción", style="white")
    
    tips.add_row("uv add <paquete>", "Agregar dependencias")
    tips.add_row("uv sync", "Sincronizar entorno")
    tips.add_row("uv run <script>", "Ejecutar scripts")
    
    console.print(Panel(tips, title="[bold]Comandos útiles de UV[/bold]", border_style="blue"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]👋 ¡Hasta luego![/yellow]")
    except Exception as e:
        console.print(f"\n[red]❌ Error: {e}[/red]")
