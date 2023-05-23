1º Função:

- Mapeia os processos da máquina, guarda em uma lista, sendo cada um dos processos um objeto

2º Função:

- Pergunta para o usuário se ele deseja realizar o backup dos dados (extra measure)

📦 Modo de verificação (verify mode)

- Windows API (monitorar)
- Aguarda o próximo processo a ser iniciado na máquina
- Realiza as técnicas de mitigação
- Retorna status id correspondente
- Atualiza a lista
- Notifica o usuário
- Break Windows API
- verify mode = False

📦 Modo de constância (constant mode)

- Enquanto constant mode = True
- Windows API (monitorar)
- Aguarda o próximo processo a ser iniciado na máquina
- Realiza as técnicas de mitigação
- Retorna status id correspondente
- Notifica o usuário

Status IDs + Machine Learning (genial):

- **0** - Seguro
- **1** - Suspeito
- **2** - Perigoso

Técnicas de mitigação:

1. Comparar o hash do arquivo com uma base de dados externa 
2. Chamadas de função de criptografia do sistema 
3. Manipulando muitos arquivos
4. Analisar o tráfego de rede da máquina 
