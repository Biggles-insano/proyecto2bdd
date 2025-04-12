#  Proyecto 2: Base de Datos - Simulación de Reservación de Asientos

Este proyecto tiene como objetivo visualizar el rendimiento en el manejo de diferentes **niveles de aislamiento** en una base de datos. Para ello, se simula el comportamiento de **5 hasta 30 usuarios** distintos intentando reservar asientos en un evento, evaluando así el manejo de concurrencia, conflictos y consistencia de los datos en situaciones de estrés controlado.

[ Ir a Documentación Completa](https://uvggt-my.sharepoint.com/:w:/g/personal/cat23401_uvg_edu_gt/EUeVzj7o8u1Moxz7kai8V1wB_1SvORc8sTz8S4cENGnaDw?e=p1fcgk)

---

##  Requisitos del Proyecto

Antes de ejecutar el programa, asegúrate de contar con lo siguiente:

- **PostgreSQL** (recomendado: v12 o superior)
- **pgAdmin** (u otra herramienta compatible con PostgreSQL)
- **Python 3.x**
- Librería `psycopg2` instalada:
  ```bash
  pip install psycopg2

## Como ejecutar el programa

```bash
1. ¿Cómo ejecutar el programa?

git clone https://github.com/tu_usuario/tu_repositorio.git

-cd tu_repositorio

2. Crear la base de datos e importar el script

-Abre pgAdmin o cualquier herramienta SQL.
-Crea una base de datos nueva llamada, por ejemplo: cine_db.
-Abre el archivo db.sql que está dentro de la carpeta www.
-Copia y ejecuta todo el contenido en el panel de consultas SQL de pgAdmin o tu cliente SQL.

##3. Modificar credenciales en hilos.py
-Abre el archivo hilos.py en la carpeta www y localiza el siguiente bloque de conexión:
conn = psycopg2.connect(
    dbname="cine_db",
    user="TU_USUARIO",
    password="TU_CONTRASEÑA",
    host="localhost",
    port="5432"
)

-Cambia "TU_USUARIO" y "TU_CONTRASEÑA" por tus credenciales reales de PostgreSQL.

4. Corre el programa con el comando
-python hilos.py

