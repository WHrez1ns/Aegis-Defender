1º Função:

- Mapeia os processos da máquina, guarda em um cache temporário em forma de lista, sendo cada um deles um objeto

2º Função:

- Pergunta para o usuário se ele deseja realizar o backup dos dados (extra measure)

📦 Modo de verificação (verify mode)

- Dispara evento
- Aguarda o próximo processo a ser iniciado na máquina
- Realiza as técnicas de mitigação
- Retorna status id correspondente
- Notifica o usuário
- Encerra evento
- verify mode = False

📦 Modo de constância (constant mode)

- Enquanto constant mode = True
- Dispara evento
- Aguarda o próximo processo a ser iniciado na máquina
- Realiza as técnicas de mitigação
- Retorna status id correspondente
- Notifica o usuário

Status IDs:

- **0** - Seguro
- **1** - Suspeito
- **2** - Perigoso
