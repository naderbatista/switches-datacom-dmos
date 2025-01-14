import paramiko
import os
import logging
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Função para executar comandos e salvar resultados
def executar_comandos_e_salvar_resultados(host, username, password, comandos, caminho_saida):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        logging.info(f'Conectando ao host {host}...')
        client.connect(hostname=host, username=username, password=password)

        # Criar o diretório de backup se não existir
        if not os.path.exists('backup'):
            os.makedirs('backup')

        with open(caminho_saida, 'w') as arquivo_saida:
            comandos_concatenados = "\n".join(comandos)
            stdin, stdout, stderr = client.exec_command(comandos_concatenados)

            # Processar a saída do comando
            output = stdout.read().decode('utf-8')
            errors = stderr.read().decode('utf-8')

            if output:
                arquivo_saida.write(output)
                logging.info(f'Resultado do host {host} salvo em {caminho_saida}.')
            if errors:
                logging.warning(f'Erros ao executar comandos no host {host}: {errors}')
        logging.info(f'Backup do host {host} concluído com sucesso.')
    except paramiko.AuthenticationException:
        logging.error(f'Falha na autenticação para o host {host}. Verifique as credenciais.')
    except paramiko.SSHException as sshException:
        logging.error(f'Erro de conexão para o host {host}: {str(sshException)}')
    except Exception as e:
        logging.error(f'Ocorreu um erro inesperado para o host {host}: {str(e)}')
    finally:
        client.close()
        logging.info(f'Conexão com o host {host} encerrada.')

# Carregar hosts e comandos de arquivos
with open('hosts.txt', 'r') as arquivo_hosts:
    hosts = [linha.strip() for linha in arquivo_hosts]

with open('comandos.txt', 'r') as arquivo_comandos:
    comandos = [linha.strip() for linha in arquivo_comandos]

# Obter credenciais de variáveis de ambiente
username = os.getenv('SSH_USERNAME', 'usuario_padrao')
password = os.getenv('SSH_PASSWORD', 'senha_padrao')

# Iterar sobre os hosts e executar os comandos
for host in hosts:
    caminho_saida = os.path.join('backup', f'backup_{host}.txt')
    executar_comandos_e_salvar_resultados(host, username, password, comandos, caminho_saida)
