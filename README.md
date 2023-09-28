## Um Endpoint Detection and Response (EDR) otimizado para Windows

O **Aégis Defender** é uma solução de segurança endpoint desenvolvida para proteger seu sistema contra a crescente ameaça dos ransomwares. Criado com Python e otimizado para sistemas Windows, nosso EDR incorpora algoritmos avançados de aprendizado de máquina, monitoramento em tempo real via WMI (Windows Management Instrumentation) e outras técnicas modernas de defesa em profundidade para oferecer proteção robusta e eficiente.

### Características Principais

- **Machine Learning para Detecção**: Utilizamos algoritmos de aprendizado de máquina para aprimorar a eficácia na detecção de ameaças, permitindo que o sistema se adapte às novas variantes de ransomware.
  
- **Monitoramento em Tempo Real via WMI**: O Aégis Defender faz uso do WMI para monitorar eventos de sistema em tempo real, aumentando nossa capacidade de detecção e resposta imediata a atividades maliciosas.

- **Verificação na Base de Dados JSON**: A base de dados JSON permite uma análise rápida e precisa de arquivos e processos, tornando o sistema mais abrangente que antivírus comuns.

## Pré-requisitos

Para garantir o funcionamento correto do Aégis Defender, é crucial que o ambiente onde ele será executado atenda a certas especificações. Os pré-requisitos abaixo são os mínimos recomendados, baseados em nossos ambientes de teste:

- **Memória**: 2GB de RAM (mínimo)
- **Processador**: 2 cores de CPU (mínimo)

### Sistema Operacional

- **Windows 10 x64**: A versão de 64 bits do Windows 10 é o sistema operacional suportado. É altamente recomendável manter o sistema atualizado com as últimas atualizações de segurança.


### Permissões

- **Acesso Administrativo**: O Aégis Defender requer privilégios de administrador para acessar recursos de sistema essenciais.

### Softwares Adicionais

- **Python Runtime**: É necessário ter Python instalado para executar o código.
- **Atualizações de Segurança**: Certifique-se de que todas as atualizações de segurança e patches estejam instalados.

Note que essas configurações foram as utilizadas em nossos ambientes de teste e servem como um ponto de partida. Configurações de hardware mais robustas são recomendadas para um melhor desempenho.

## Tecnologias

O Aégis Defender foi meticulosamente desenvolvido para operar no ambiente Windows 10, aproveitando as capacidades avançadas oferecidas pela linguagem de programação Python. Abaixo, você encontrará as tecnologias que compõem a espinha dorsal deste projeto:

### Sistema Operacional

- **Windows 10**: O Aégis Defender foi otimizado para operar no Windows 10, tirando vantagem das APIs e recursos nativos oferecidos por este sistema operacional.

### Linguagem de Programação

- **Python**: Linguagem escolhida por sua robustez e facilidade de integração com várias bibliotecas e APIs, permitindo uma rápida prototipagem e desenvolvimento.

### Bibliotecas

A seleção criteriosa de bibliotecas em Python amplifica as funcionalidades do Aégis Defender:

- **os, ctypes, sys**: Essas bibliotecas permitem uma integração profunda com o sistema operacional Windows.
- **psutil, wmi**: Empregadas no monitoramento em tempo real dos processos e eventos do sistema.
- **sklearn**: Implementa algoritmos de aprendizado de máquina para uma detecção de ameaças mais precisa.
- **json**: Encarregada do gerenciamento da base de dados JSON, que armazena informações cruciais.
- **webview, time**: Estas bibliotecas são utilizadas para a manipulação da interface de usuário e gerenciamento do tempo.
- **pathlib**: A biblioteca pathlib oferece uma maneira mais conveniente e orientada a objetos de trabalhar com caminhos de arquivos e diretórios no sistema de arquivos, tornando mais fácil a manipulação e navegação nos caminhos.
- **pythoncom**: A biblioteca pythoncom é usada principalmente para integração com componentes COM (Component Object Model) no Windows, permitindo a comunicação entre objetos de software através da infraestrutura COM.
- **threading**: A biblioteca threading é usada para criar e gerenciar threads em um programa Python. Isso é útil para realizar tarefas concorrentes ou paralelas, melhorando o desempenho e a eficiência em programas que exigem processamento simultâneo.
- **subprocess**: A biblioteca subprocess é usada para criar processos secundários ou subprocessos a partir de um programa Python. Ela é útil para executar comandos do sistema operacional, interagir com outros programas e capturar a saída desses programas.
- **flask**: Flask é um micro-framework web leve para Python. Ele é usado para criar aplicativos web e APIs de forma rápida e fácil. Flask é conhecido por sua simplicidade e extensibilidade, sendo uma escolha popular para o desenvolvimento web em Python.

### Frameworks e APIs

- **Flask**: Este micro-framework é utilizado para desenvolver uma interface web que permite uma fácil interação com o Aégis Defender.
- **MITRE ATT&CK**: Utilizamos as diretrizes e práticas recomendadas do MITRE ATT&CK para melhorar a segurança.
- **Google APIs**: Permite integrações com serviços do Google para funcionalidades adicionais.
- **Boxicons API**: Essa API é empregada para a inclusão de ícones vetoriais em aplicações web, aprimorando a experiência do usuário com elementos visuais de alta qualidade.

## Instalação

### Como baixar nosso aplicativo através do site Aégis Defender

Se você está interessado em baixar e experimentar nosso aplicativo, siga as instruções abaixo para uma experiência tranquila e descomplicada:

1. **Acesse o site**: Primeiro, visite o site do [Aégis Defender](https://aegis.avalontech.net.br). Nosso site foi otimizado para ser fácil de navegar e é compatível com todos os navegadores modernos.
2. **Navegue até o botão de download**: Em nossa página inicial, você encontrará um botão claramente marcado como "Download" ou "Baixar". Este botão foi projetado para ser visível e de fácil acesso.
3. **Inicie o download**: Uma vez que você clique no botão de download, o processo de baixar o arquivo começará automaticamente. Depende da velocidade da sua conexão com a internet, mas, geralmente, leva apenas alguns minutos.
4. **Siga as instruções de instalação**: Após o download ser concluído, abra o arquivo baixado e siga as instruções na tela para instalar nosso aplicativo em seu dispositivo.

Agradecemos por escolher nosso aplicativo e esperamos que você tenha uma excelente experiência ao usá-lo!

## Uso

### Funcionalidades:

1. **Detecção em Tempo Real**:
    - **Como usar**: Após abrir o programa, localize e clique no botão "Iniciar Detecção em Tempo Real".

        ![ off](img/off.jpeg)

    - **Descrição**: Esta função permite que o software monitore e identifique ameaças ou atividades não usuais em tempo real, garantindo maior segurança para seu sistema.

        ![ on](img/on.jpeg)

    -**Recomendação**: É aconselhável manter esta função sempre ativada para uma proteção constante.

2. **Logs**:
    - **Ainda em desenvolvimento!**

3. **Processos**:
    - **Como usar**: Selecione "Processos" no menu. Aqui, você verá uma lista de todos os processos em execução.
    - **Descrição**: Esta função permite visualizar e gerenciar todos os processos ativos no seu sistema.
    - **Dica**: Se notar algum processo desconhecido ou suspeito, investigue ou encerre-o para garantir a segurança do seu sistema.

        ![ processos](img/process.jpeg)

## Avaliações e Testes

- **Metodologia Rigorosa de Testes**: O Aégis Defender foi meticulosamente avaliado mediante metodologias padronizadas e testes rigorosos, garantindo sua capacidade de defesa e resposta.

    1. **Resiliência a Ransomwares**: Parte integral dos testes de avaliação, o Aégis Defender foi submetido a cenários adversos envolvendo alguns dos ransomwares mais notórios no cenário de ameaças cibernéticas. Esta bateria de testes incluiu ameaças como o Wannacry e o Jigsaw, dentre outros. O sucesso obtido diante dessas ameaças é um testemunho da robustez, competência e eficácia da nossa solução.

    2. **Compromisso com a Segurança**: Além dos testes específicos contra ransomwares, o Aégis Defender passa por uma série contínua de avaliações para garantir que mantém sua efetividade frente à evolução constante das ameaças. A cada atualização ou refinamento do software, novos testes são conduzidos para certificar-se de que o nível de proteção oferecido está alinhado às melhores práticas e padrões da indústria.

- **Dedicação à Excelência**: A dedicação incansável da equipe por trás do Aégis Defender é refletida na meticulosidade dos testes realizados e na constante busca por aperfeiçoamento, garantindo aos usuários uma ferramenta confiável e de alta performance.

## Autores

- **Equipe Aégis Defender**: O Aégis Defender representa um marco na segurança cibernética, fruto da colaboração e dedicação de três profissionais distintos:

    - **Júlia Barboza Brunelli**
        - [GitHub](https://github.com/Aykie)
        - [LinkedIn](https://www.linkedin.com/in/aykie/)

    - **Nicholas Calegari Sanches**
        - [GitHub](https://github.com/NCalegariS)
        - [LinkedIn](https://www.linkedin.com/in/nicholas-calegari-258823242/)
        
    - **Renan Dias da Costa Silva**
        - [GitHub](https://github.com/WHrez1ns)
        - [LinkedIn](https://www.linkedin.com/in/renan-dias-da-costa-563830264/)

Cada integrante da equipe contribuiu significativamente para a concepção, design e desenvolvimento deste projeto, consolidando sua relevância no panorama atual de segurança cibernética.

## Agradecimentos

À medida que a evolução digital avança, os desafios no campo da segurança cibernética tornam-se ainda mais intrincados. Dentro desse cenário complexo, a concepção e a realização do Aégis Defender são frutos da combinação sinérgica entre talento, dedicação e colaboração interdisciplinar. Por isso, consideramos imprescindível reconhecer e agradecer a todos que participaram dessa empreitada conosco.

- **Professores da FIAP**: Nos corredores acadêmicos e salas de aula da FIAP, encontramos um ambiente de fomento ao pensamento crítico e inovação. Agradeço aos professores que, com profundo conhecimento e vasta experiência, forneceram orientações precisas, moldando assim a base teórica e prática do Aégis Defender.

- **Pride Security**: Em um mercado tão competitivo e dinâmico, confiar em jovens talentos e desafiar os limites convencionais é uma postura louvável. A Pride Security não apenas nos propôs um desafio, mas também se tornou parte integral do nosso processo de aprendizado e desenvolvimento.

- **Avalon Tech**: A colaboração com a Avalon Tech foi de suma importância para dar vida ao Aégis Defender, e agradecemos o apoio ao projeto.

A jornada do Aégis Defender é testemunha do poder da colaboração. Assim, com humildade e respeito, agradecemos a cada indivíduo e instituição que nos apoiou, direta ou indiretamente, e confiou na nossa visão. Estamos no início de uma trajetória que, esperamos, contribuirá significativamente para a segurança digital.

## Assistência e Suporte Técnico

- **Canais de Comunicação** : Estamos comprometidos em oferecer um suporte eficiente e ágil aos usuários do Aégis. Se você encontrar dificuldades, tiver dúvidas sobre a aplicação ou precisar de orientação técnica:

    1. **Página de Contato**: A primeira opção é visitar a nossa [página de contato no site da Avalon Tech](https://avalontech.net.br/contact.php), onde disponibilizamos um formulário para dúvidas e sugestões.
    
    2. **E-mail**: Para um suporte mais direto, não hesite em nos enviar um e-mail. A nossa equipe de suporte técnico está sempre pronta para auxiliar e responderá sua mensagem o mais breve possível.
    
    3. **Documentação**: Recomendamos também a consulta à nossa documentação extensiva, onde muitas questões comuns são abordadas e esclarecidas.

Esperamos que estas vias de comunicação facilitem sua experiência com o Aégis e garantam a resolução de qualquer inquietação ou obstáculo que possa surgir.
