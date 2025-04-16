import os
import subprocess
from colorama import init, Fore

# Inicializar colorama con autoreset
init(autoreset=True)

# Solicitar el nombre del proyecto al usuario
project_name = input("📂 " + Fore.YELLOW + "Introduce el nombre del proyecto: ")

# Crear carpeta del proyecto
print(Fore.GREEN + "✅ Creando carpeta del proyecto...")
print(Fore.BLUE + f"  mkdir {project_name}")
os.makedirs(project_name, exist_ok=True)
os.chdir(project_name)

# Crear y configurar el entorno virtual (solo para Windows)
print(Fore.GREEN + "✅ Creando entorno virtual...")
print(Fore.BLUE + "  python -m venv .venv")
subprocess.run(["python", "-m", "venv", ".venv"])

# Definir la ruta del pip del entorno virtual (para Windows)
pip_path = os.path.join(".venv", "Scripts", "pip")

# Inicializar repositorio Git
print(Fore.GREEN + "✅ Inicializando repositorio Git...")
print(Fore.BLUE + "  git init")
subprocess.run(["git", "init"])

# Crear README.md
print(Fore.GREEN + "✅ Creando archivo README.md...")
print(Fore.BLUE + f"  echo '# {project_name}' > README.md")
with open("README.md", "w", encoding="utf-8") as readme:
    readme.write(f"# {project_name}\n")

# Crear .gitignore
print(Fore.GREEN + "✅ Creando archivo .gitignore...")
print(Fore.BLUE + "  echo '.venv/\\n__pycache__/\\n' > .gitignore")
with open(".gitignore", "w", encoding="utf-8") as gitignore:
    gitignore.write(".venv/\n__pycache__/\n")

# Crear el archivo principal del proyecto con un docstring
print(Fore.GREEN + f"✅ Creando archivo {project_name}.py con docstring...")
print(Fore.BLUE + f"  echo '\"\"\"\\nArchivo principal del proyecto {project_name}.\\n\"\"\"' > {project_name}.py")
with open(f"{project_name}.py", "w", encoding="utf-8") as main_file:
    main_file.write(f'"""\nArchivo principal del proyecto {project_name}.\n"""\n')

# Hacer commit inicial
print(Fore.GREEN + "✅ Haciendo commit inicial...")
print(Fore.BLUE + "  git add . && git commit -m 'Init commit'")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Init commit"])

# Preguntar si se desea crear un repositorio remoto en GitHub
create_repo = input(Fore.YELLOW + "¿Desea crear un repositorio en GitHub? (y/N): ").strip().lower()
if create_repo == "y":
    print(Fore.GREEN + "✅ Creando repositorio remoto en GitHub...")
    print(Fore.BLUE + f"  gh repo create {project_name} --public --source=. --remote=origin --push --confirm")
    subprocess.run([
        "gh", "repo", "create", project_name,
        "--public",
        "--source=.",
        "--remote=origin",
        "--push",
        "--confirm"
    ])

# Abrir Visual Studio Code
print(Fore.GREEN + "✅ Abriendo IDE...")
print(Fore.BLUE + "  cursor .")
subprocess.run("cursor .", shell=True)

# Mensaje final
print(Fore.MAGENTA + f"🎉 Proyecto '{project_name}' creado con éxito.")
print(Fore.MAGENTA + "➡️ Recuerda activar el entorno virtual antes de trabajar ejecutando:")
print(Fore.CYAN + "   .venv\\Scripts\\activate")
