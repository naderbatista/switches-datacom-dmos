Este script realiza backups automatizados da configuração de switches Datacom com sistema DMOS via SSH.

Características principais:
1. Conexão automatizada via SSH usando a biblioteca `paramiko`.
2. Leitura de uma lista de hosts (endereço IP ou hostname) a partir do arquivo `hosts.txt`.
3. Execução de comandos definidos no arquivo `comandos.txt` para coletar a configuração do switch.
4. Salvamento das saídas em arquivos organizados no diretório `backup`, com um arquivo para cada host.
5. Uso de variáveis de ambiente (gerenciadas pelo `dotenv`) para armazenar credenciais de forma segura.
6. Sistema de logging para monitorar o progresso e registrar erros durante a execução.

O fluxo principal do script é o seguinte:
- Carregar variáveis de ambiente para credenciais SSH.
- Ler os arquivos `hosts.txt` e `comandos.txt` para determinar os alvos e os comandos.
- Para cada host, conectar via SSH, executar os comandos e salvar a saída no diretório `backup`.
- Registrar eventos e erros usando o sistema de logging.

Este script é útil para administradores de rede que precisam de uma solução automatizada para gerenciar backups de configuração de switches Datacom com o sistema DMOS.

Dependências:
- `paramiko`: Para gerenciar conexões SSH.
- `dotenv`: Para carregar variáveis de ambiente de um arquivo `.env`.
- Python 3.6 ou superior.

Cuidados:
- Verifique se as credenciais no arquivo `.env` estão corretas.
- Certifique-se de que os switches estejam acessíveis pela rede e aceitando conexões SSH.
- Garanta permissões adequadas para criar e escrever no diretório `backup`.

Siga as instruções no código para configurar o ambiente e executar o script.
