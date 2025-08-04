



# CloudStorage
  
Este modulo permite subir archivos a CloudStorage.  

*Read this in other languages: [English](Manual_CloudStorage.md), [Português](Manual_CloudStorage.pr.md), [Español](Manual_CloudStorage.es.md)*
  
![banner](imgs\Banner_CloudStorage.png)
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
- Busque "API de Cloud Storage" y habilítela.

4. **Crear una cuenta de servicio**

- En la consola de Google Cloud, busque y seleccione "IAM y administración" → "Cuentas de servicio".
- Haga clic en "Crear cuenta de servicio".
- Especifique un nombre y una descripción para la cuenta de servicio.
- Asignar el rol requerido:
- En "Seleccionar un rol", busque "Administrador de almacenamiento".
- Administrador de almacenamiento.
- Este rol otorga permisos para administrar los archivos y la configuración de Cloud Storage.
- Continúe y haga clic en "Crear".

5. **Generar una clave de cuenta de servicio**
- En la cuenta de servicio creada, vaya a la pestaña "Claves".
- Haga clic en "Agregar clave" -> "Crear nueva clave".
- Seleccione el formato JSON (recomendado).
- Descargue el archivo JSON generado y guárdelo en un lugar seguro.


## Descripción de los comandos

### Configurar credenciales Google Cloud Storage
  
Configura credenciales de Cloud Storage
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta archivo de credenciales|Ruta del archivo de credenciales de Google Cloud Storage|C:\Usuario\Desktop\credentials.json|

### Subir archivo
  
Sube un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo|Ruta del archivo a subir|C:\Usuario\Desktop\file.png|
|Bucket name|El nombre del bucket donde se subira el archivo|your-bucket-name|
|Blob name|El nombre del blob donde se subira el archivo|your destination blob name|
|Timeout|Timeout de la peticion. Si se deja vacio, por defecto es 1000|1000|
