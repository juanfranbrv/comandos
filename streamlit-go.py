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

# Instalar Streamlit en el entorno virtual
print(Fore.CYAN + "📦 Instalando Streamlit en el entorno virtual... (esto puede tardar unos momentos)")
print(Fore.BLUE + f"  {pip_path} install streamlit")
subprocess.run([pip_path, "install", "streamlit"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

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

# Crear app.py con importación de Streamlit
print(Fore.GREEN + "✅ Creando archivo app.py...")
print(Fore.BLUE + "  echo 'import streamlit as st' > app.py")
with open("app.py", "w", encoding="utf-8") as app_file:
    app_file.write("import streamlit as st\n")
    app_file.write('''

st.set_page_config(
    page_title="Titulo de la app",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="auto"
)

st.header("Titulo de la app")
''')

# Crear el fichero de secrets
print(Fore.GREEN + "✅ Creando carpeta y archivo de configuración para secrets...")
print(Fore.BLUE + "  mkdir .streamlit && echo '_API_KEY=' > .streamlit/secrets.toml")
os.makedirs(".streamlit", exist_ok=True)
with open(".streamlit/secrets.toml", "w", encoding="utf-8") as tom_file:
    tom_file.write("_API_KEY=''\n")

# Generar requirements.txt usando el pip del entorno virtual
print(Fore.CYAN + "📋 Generando archivo requirements.txt...")
print(Fore.BLUE + f"  {pip_path} freeze > requirements.txt")
with open("requirements.txt", "w") as req_file:
    subprocess.run([pip_path, "freeze"], stdout=req_file)

# Hacer commit inicial
print(Fore.GREEN + "✅ Haciendo commit inicial...")
print(Fore.BLUE + "  git add . && git commit -m 'Init commit'")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Init commit"])

# Crear repositorio remoto en GitHub con el mismo nombre del proyecto
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
print(Fore.BLUE + "  code .")
subprocess.run("code .", shell=True)

# Mensaje final
print(Fore.MAGENTA + f"🎉 Proyecto '{project_name}' creado con éxito.")
print(Fore.MAGENTA + "➡️ Recuerda activar el entorno virtual antes de trabajar ejecutando:")
print(Fore.CYAN + "   .venv\\Scripts\\activate")
