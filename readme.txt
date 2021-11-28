Proyecto creado por Luca Citta Giordano para hackathon online de JOBMadrid.


REQUERIMIENTOS:

✅ Task 1 → Crear un base de datos (PostgreSQL, MySQL, Mongo, Firebase,etc) y guardar toda la lista de compañías.
    utilizando siguiendo el esquema del JSON

✅ Task 2 → Crear un endpoint que devuelva las compañías y este ordenadas por tamaño.

✅ Task 3 → Crear un endpoint que devuelva las compañías y este ordenadas por fecha de creación.

✅ Task 4 → Crear un endpoint que devuelva los siguientes datos: Número de empresas que hay en cada industria,
    Número de empresas que hay por cada rango de tamaños, Número de empresas que hay en cada año de creación.


# Instalacion de la api

    * Utilizar una versión de Python 3.X
    * Clonar el repositorio de https://github.com/lucacitta/JobMadrid.git
    * Crear y activar un entorno virtual (Yo utilizo virtualenv, pero no es obligatorio)
    * Instalar las dependencias de requirements.txt con pip en el entorno virtual (pip install -r requirements.txt)
    * Crear un archivo llamado 'password.py' y ubicarlo dentro de la carpeta settings, en ella crear estas variables.
        - DB_NAME: El nombre de la Base de datos PostgreSQL a utilizar.
        - PASSWORD_PASSWORD: La contraseña para acceder a la base de datos PostgreSQL.
        - PASSWORD_SECRET_KEY: Aqui deberan incluir la clave secreta del proyecto como tal.

    * Realizar las migraciones a la base de datos (python manage.py makemigrations) y (python manage.py migrate)

    *Con estos pasos el proyecto ya se encontraria funcionando, luego en 'Uso de api' se detalla como poblar la DB


#Uso de la api

    Para utilizar la api una vez realizada la instalacion, se debe poblar la base de datos.
        Para ello se debe acceder al endpoint /populate_DB/, esto creara o actualizara los registros

    Luego uno puede acceder a 3 endpoint con distinta informacion:
        * /companies/bysize/ Para obtener la informacion de las empresas ordenadas por el tamaño de las mismas.

        * /companies/bycreation/ Para obtener la informacion de las empresas ordenadas por la fecha de creacion.

        * /companies/metrics/ Para obtener las metricas requeridas, la cantidad de empresas por rubro,
            por año de creacion y por tamaño.
