import datetime
import os
import requests
import subprocess

# Fecha actual para nombrar archivos
fecha = datetime.datetime.now().strftime("%Y-%m-%d")

# Hojas públicas (sin autenticación)
sheet_urls = {
    f"hoja1_{fecha}.csv": "https://docs.google.com/spreadsheets/d/17W6xwFXqmpcyG5y_2o3faXydPFQ_5H0yeTOrLfQz2jg/export?format=csv",
    f"hoja2_{fecha}.csv": "https://docs.google.com/spreadsheets/d/16h_ysa9Yde7ALrr4gFusl6gMhLcopVa23r_2I1_6MzI/export?format=csv"
}

# Crear carpeta si no existe
os.makedirs("hojas", exist_ok=True)

# Descargar y guardar cada hoja
for nombre_archivo, url in sheet_urls.items():
    r = requests.get(url)
    if r.status_code == 200:
        with open(f"hojas/{nombre_archivo}", "wb") as f:
            f.write(r.content)
        print(f"✅ Guardado: hojas/{nombre_archivo}")
    else:
        print(f"❌ Error al descargar {nombre_archivo}: {r.status_code}")

# Copiar CSVs a la raíz si quieres que estén en el nivel superior del repo
for archivo in os.listdir("hojas"):
    os.replace(f"hojas/{archivo}", archivo)

# Git commands
subprocess.run(["git", "config", "--global", "user.name", "jsgaston"])
subprocess.run(["git", "config", "--global", "user.email", "jsgastoniriartecabrera@gmail.com"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Actualización automática {fecha}"], check=False)
subprocess.run(["git", "push"])
