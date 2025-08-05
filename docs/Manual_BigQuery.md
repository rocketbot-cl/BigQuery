



# BigQuery
  
Este módulo permite la integración y manipulación de datos en Google BigQuery.  

*Read this in other languages: [English](Manual_BigQuery.md), [Português](Manual_BigQuery.pr.md), [Español](Manual_BigQuery.es.md)*
  
![banner](imgs/Banner_BigQuery.png o jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Cómo usar este módulo

Antes de usar este módulo, debe tener una cuenta de Gmail para acceder a Google Cloud:

1. **Acceda al portal de Google Cloud**
- Ve a https://console.cloud.google.com/
- Inicie sesión en la consola de Google Cloud.
- Si es la primera vez que accede, se le solicitará que acepte los términos y condiciones.

2. **Crear un nuevo proyecto**
- En la parte superior de la consola, haga clic en el selector de proyectos.
- Haga clic en "Nuevo proyecto".
- Asigne un nombre al proyecto.
- Seleccione una organización (si corresponde) o deje la opción predeterminada.
- Haga clic en "Crear".

3. **Habilite la API de Google Cloud Storage**
- En la barra de búsqueda de la consola de Google Cloud, escriba "API y servicios" y acceda a esa sección:
- Haga clic en "Habilitar API y servicios".
- Busque "API de BigQuery" y habilítela.

4. **Crear una cuenta de servicio**

- En la consola de Google Cloud, busque y seleccione "IAM y administración" → "Cuentas de servicio".
- Haga 
clic en "Crear cuenta de servicio".
- Especifique un nombre y una descripción para la cuenta de servicio.
- Asignar el rol requerido:
- En "Seleccionar un rol", busque "Administrador de BigQuery".
- Administrador de BigQuery.
- Este rol otorga permisos para administrar todos los recursos y datos de BigQuery.
- Continúe y haga clic en "Crear".

5. **Generar una clave de cuenta de servicio**
- En la cuenta de servicio creada, vaya a la pestaña "Claves".
- Haga clic en "Agregar clave" -> "Crear nueva clave".
- Seleccione el formato JSON (recomendado).
- Descargue el archivo JSON generado y guárdelo en un lugar seguro.


## Descripción de los comandos

### Configurar credenciales Google Cloud BigQuery
  
Configura credenciales de Cloud BigQuery
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta archivo de credenciales|Ruta del archivo de credenciales de Google Cloud BigQuery|C:\Usuario\Desktop\credentials.json|

### Leer datos de BigQuery
  
Ejecutar una consulta SQL y obtener resultados 
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Consulta|Query SQL|SELECT producto_id FROM proyecto_id.store.sell|
|ID del Proyecto|Project ID|bigquery-467823|
|Asignar resultado a Variable|Resultado|Variable|

### Cargar datos
  
Cargar datos desde un archivo CSV
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dataset ID|Dataset ID|dataset_id|
|Table ID|table_id|table_id|
|Ruta del archivo CSV|Ruta del archivo csv|C:\Usuario\Desktop\file.csv|
|Tiene Cabeceras|Marcar si el archivo .csv tiene encabezados|True|
|Disposicion de escritura|Forma en que se cargaran los datos|WRITE_APPEND|
|Cadena JSON del esquema|Ruta del archivo json (opcional)|C:\Usuario\Desktop\schema.json|
|ID del Proyecto|Project ID|bigquery-467823|
|Asignar resultado a Variable|Resultado|Variable|
