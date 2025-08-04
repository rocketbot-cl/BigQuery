



# CloudStorage
  
Esse módulo permite fazer upload de arquivos para o CloudStorage.  

*Read this in other languages: [English](Manual_CloudStorage.md), [Português](Manual_CloudStorage.pr.md), [Español](Manual_CloudStorage.es.md)*
  
![banner](imgs\Banner_CloudStorage.png)
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
- Pesquise por "API do Cloud Storage" e habilite-a.

4. **Criar uma conta de serviço**

- No console do Google Cloud, pesquise e selecione "IAM e Admin" → "Contas de serviço"
- Clique em "Criar conta de serviço".
- Especifique um nome e uma descrição para a conta de serviço.
- Atribua a função necessária:
- Em "Selecionar uma função", pesquise por "Administrador de armazenamento".
- Administrador de armazenamento.
- Esta função concede permissões para gerenciar arquivos e configurações do Cloud Storage.
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
|Credentials file path|Google Cloud Storage credentials file path|C:\Usuario\Desktop\credentials.json|

### Upload file
  
Upload a file
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|File path|File path to upload|C:\Usuario\Desktop\file.png|
|Bucket name|The name of the bucket where the file will be uploaded|your-bucket-name|
|Blob name|The name of the blob where the file will be uploaded|your destination blob name|
|Timeout|Timeout of the request. If left empty, by default is 1000|1000|
