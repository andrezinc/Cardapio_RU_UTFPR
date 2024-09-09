**## Cardápio RU UTFPR

O projeto **Cardápio RU UTFPR** visa automatizar o acesso ao cardápio do Restaurante Universitário (RU) da UTFPR, facilitando para os alunos obterem as informações diretamente no Telegram. Desenvolvido para sistemas com Arch Linux, o projeto utiliza dois scripts Python principais para gerenciar o cardápio semanalmente.

### Descrição

O sistema é composto por dois scripts:

1. **Download.py**:
   - **Baixa o Cardápio**: Toda segunda-feira, o script faz o download do cardápio em PDF a partir de uma pasta no Google Drive.
   - **Converte o PDF para Texto**: Após o download, o PDF é convertido em um arquivo de texto (.txt) para facilitar o processamento.
   - **Limpeza de Dados**: Remove arquivos temporários antigos para manter o sistema limpo e atualizado.

2. **BOT.py**:
   - **Envio de Informações**: De segunda a sábado, este script envia as informações do cardápio para um bot do Telegram, permitindo que os alunos consultem o cardápio facilmente através do aplicativo de mensagens.

### Funcionalidades

- **Automatização do Cardápio**: Atualização semanal automática do cardápio do RU.
- **Integração com Telegram**: Acesso ao cardápio diretamente no Telegram, facilitando a consulta por parte dos alunos.
- **Sistema Limpo e Atualizado**: Garante que apenas os dados mais recentes sejam utilizados e disponíveis.

### Instalação e Configuração

1. **Configuração do Ambiente**: Certifique-se de ter o Arch Linux e as bibliotecas Python necessárias instaladas (`gdown`, `pdftotext`).
2. **Configuração do Cron**: Ajuste o `crontab` para executar `Download.py` toda segunda-feira e `BOT.py` diariamente de segunda a sábado.
3. **Execução dos Scripts**: Assegure-se de que os scripts tenham permissões de execução adequadas e estejam no diretório correto.
