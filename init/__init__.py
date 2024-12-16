import subprocess
import sys
import os

def check_and_install_requirements(requirements_file="requirements.txt"):
    """
    Verifica e instala los paquetes del archivo requirements.txt.
    """
    try:
        # Ruta absoluta del archivo requirements.txt
        base_path = os.path.dirname(os.path.abspath(__file__))
        requirements_path = os.path.join(base_path, "..", requirements_file)

        # Leer los requisitos
        with open(requirements_path, "r") as f:
            requirements = [line.strip() for line in f if line.strip()]

        for package in requirements:
            try:
                # Si el paquete incluye una versión específica
                if "==" in package or ">=" in package or "<=" in package:
                    package_name = package.split("=")[0]
                else:
                    package_name = package

                # Verificar si está instalado
                installed = subprocess.run(
                    [sys.executable, "-m", "pip", "show", package_name],
                    capture_output=True,
                    text=True
                )
                if package_name in installed.stdout:
                    print(f"{package_name} ya está instalado.")
                else:
                    print(f"Instalando: {package}")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

            except Exception as e:
                print(f"Error al instalar {package}: {e}")
    except FileNotFoundError:
        print(f"El archivo {requirements_file} no existe.")
        sys.exit(1)

# Llamada inicial al cargar el módulo
print("Verificando dependencias...")
check_and_install_requirements()
print("Todas las dependencias están instaladas.")
