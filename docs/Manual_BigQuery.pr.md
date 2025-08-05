



# BigQuery
  
Este módulo permite a integração e manipulação de dados no Google BigQuery.  

*Read this in other languages: [English](Manual_BigQuery.md), [Português](Manual_BigQuery.pr.md), [Español](Manual_BigQuery.es.md)*
  
![banner](imgs/Banner_BigQuery.png o jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Como usar este módulo

Antes de usar este módulo, você precisa ter uma conta do Gmail para acessar o Google Cloud:

1. **Acesse o portal do Google Cloud**
- Acesse https://console.cloud.google.com/
- Faça login no Google Cloud Console.
- Se for a primeira vez, você será solicitado a aceitar os termos e condições.

2. **Crie um novo projeto**
- Na parte superior do console, clique no seletor de projetos.
- Clique em "Novo projeto".
- Dê um nome ao projeto.
- Selecione uma organização (se aplicável) ou deixe a opção padrão.
- Clique em "Criar".

3. **Habilite a API do Google Cloud Storage**
- Na barra de pesquisa do Google Cloud Console, digite "APIs e serviços" e entre nessa seção:
- Clique em "Habilitar APIs e serviços".
- Pesquise por "API do BigQuery" e habilite-a.

4. **Criar uma conta de serviço**

- No console do Google Cloud, pesquise e selecione "IAM e Admin" → "Contas de serviço"
- Clique em "Criar conta de serviço".
- Especifique um nome e uma descrição para a conta de 
serviço.
- Atribua a função necessária:
- Em "Selecionar uma função", pesquise por "Administrador de BigQuery".
- Administrador de BigQuery.
- Esta função concede permissões para gerenciar todos os recursos e dados do BigQuery.
- Continue e clique em "Criar".

5. **Gerar uma chave de conta de serviço**
- Na conta de serviço criada, vá para a aba "Chaves".
- Clique em "Adicionar chave" -> "Criar nova chave".
- Selecione o formato JSON (recomendado).
- Baixe o arquivo JSON gerado e salve-o em um local seguro.
## Descrição do comando

### 
  

|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Credentials file path|Google Cloud BigQuery credentials file path|C:\Usuario\Desktop\credentials.json|

### Read data from BigQuery
  
Run an SQL query and get results
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Query String|Consulta SQL|SELECT producto_id FROM proyecto_id.store.sell|
|Project ID|Project ID|bigquery-467823|
|Atribuir resultado à variável|Resultado|Variável|

### Load data
  
Load data from CSV file
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dataset ID|Dataset ID|dataset_id|
|Table ID|table_id|table_id|
|File path CSV|File path csv|C:\Usuario\Desktop\file.csv|
|tem cabeçalhos|Marcar se o arquivo .csv tem cabeçalhos|True|
|Organizar por|Classifique os emails listados pelo parâmetro desejado|WRITE_APPEND|
|Schema JSON|File path json (optional)|C:\Usuario\Desktop\schema.json|
|Project ID|Project ID|bigquery-467823|
|Atribuir resultado à variável|Resultado|Variável|
