# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

   sudo pip install <package> -t .

"""
import os
import sys
import json

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Google-BigQuery" + os.sep + "libs" + os.sep
sys.path.append(cur_path)

from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd

global credentials
module = GetParams("module")

if module == "setCredentials":
    credentials_path = GetParams("credentials_path")
    print("hhh")
    try:
        #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
        print("hhh")
        credentials = service_account.Credentials.from_service_account_file(credentials_path)
        # Prueba: listar datasets
        print("aquiiiii")
        client = bigquery.Client(credentials=credentials, project=credentials.project_id)
        datasets = list(client.list_datasets())
        if datasets:
            print(" Conexión exitosa. Datasets encontrados:")
            for dataset in datasets:
                print(f" - {dataset.dataset_id}")

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
#  Leer datos de BigQuery: Ejecutar una consulta SQL y obtener resultados    
if module == "readDataFromQuery":
    query_string = GetParams("query_string")
    project_id = GetParams("project_id") # Opcional: Si no se usa el proyecto predeterminado
    var_ = GetParams('var_')
    
    try:
        client = bigquery.Client(project=project_id)
        query_job = client.query(query_string)        
        results = query_job.result()        
        # Convierte los resultados a una lista de diccionarios
        list_ = [dict(row) for row in results]        
        SetVar(var_, list_)
        
    except Exception as e:
        print("\x1B[31;40mOcurrió un error al leer datos de BigQuery mediante consulta.\x1B[0m")
        PrintException()
        raise e
    
if module == "insertRows":
    dataset_id = GetParams("dataset_id")
    table_id = GetParams("table_id")
    rows_to_insert_json = GetParams("rows_to_insert_json")
    project_id = GetParams("project_id") 
    var_ = GetParams('var_')
    
    try:
        rows_to_insert = json.loads(rows_to_insert_json)
        
        client = bigquery.Client(project=project_id)
        table_ref = client.dataset(dataset_id).table(table_id)

        errors = client.insert_rows_json(table_ref, rows_to_insert) 
        if errors == []:
            SetVar(var_, True)
        else:
            print(f"\x1B[31;40mOcurrieron errores al insertar filas en {dataset_id}.{table_id}:\x1B[0m")
            for error in errors:
                print(error)
            raise Exception("Errores al insertar filas en BigQuery.")
            
    except Exception as e:
        SetVar(var_, False)
        PrintException()
        raise e
    
# Ejemplo: Cargar datos desde un archivo (GCS o local) a una tabla
if module == "loadDataFromCSVFile":
    dataset_id = GetParams("dataset_id")
    table_id = GetParams("table_id")
    path_file = GetParams("path_file") #'gs://bucket/file.csv' o 'file.csv'
    write_disposition = GetParams("write_disposition") # 'WRITE_TRUNCATE', 'WRITE_APPEND', 'WRITE_EMPTY'
    schema_json = GetParams("schema_json") # Opcional: Cadena JSON del esquema, si no se infiere
    project_id = GetParams("project_id") # Opcional
    has_header = GetParams("has_header")
    has_header = str(has_header) == "true" or str(has_header) == "True"
    var_ = GetParams('var_')
    
    try:
        # Validar que el archivo sea CSV
        if not (path_file.lower().endswith('.csv') or path_file.startswith("gs://") and '.csv' in path_file.lower()):
            raise ValueError("El archivo de origen debe ser de formato CSV.")

        client = bigquery.Client(project=project_id)
        table_ref = client.dataset(dataset_id).table(table_id)
        
        job_config = bigquery.LoadJobConfig()

        job_config.source_format = bigquery.SourceFormat.CSV
        
        # Configuración específica para CSV
        job_config.skip_leading_rows = 1 if has_header else 0
        job_config.autodetect = True 
        
        # Establecer la disposición de escritura
        job_config.write_disposition = getattr(bigquery.WriteDisposition, write_disposition.upper())
        
        # Si se proporciona un esquema explícito, usarlo y desactivar la autodetección
        if schema_json:
            schema_data = json.loads(schema_json)
            job_config.schema = [
                bigquery.SchemaField(field['name'], field['type'], mode=field.get('mode', 'NULLABLE'))
                for field in schema_data
            ]
            job_config.autodetect = False 

        if path_file.startswith("gs://"):
            # Cargar desde Cloud Storage
            load_job = client.load_table_from_uri(
                path_file,
                table_ref,
                job_config=job_config
            )
        else:
            # Cargar desde un archivo local
            with open(path_file, "rb") as source_file:
                load_job = client.load_table_from_file(
                    source_file,
                    table_ref,
                    job_config=job_config
                )
        
        load_job.result()  
        SetVar(var_, True)
       
    except Exception as e:
        SetVar(var_, False)
        print("\x1B[31;40mOcurrió un error al cargar datos en BigQuery desde el archivo CSV.\x1B[0m")
        PrintException()
        raise e