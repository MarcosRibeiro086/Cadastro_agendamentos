# Sistema de cadastro de agendamentos médicos
Este projeto tem como objetivo o exercícios de práticas de programação full-stack em django e tem como proposta os seguintes pontos:

1. Permitir o cadastro de pacientes (inclusão, exclusão e edição);
  a. Nome, CPF, data de nascimento, sexo, altura e peso.
2. Permitir o cadastro de profissional de saúde (inclusão, exclusão e edição);
  a. Nome, CPF, data de nascimento e sexo.
3. Realizar agendamento de atendimento com data/hora, paciente e profissional de saúde;
  a. Não deve ser permitido o registro de dois ou mais atendimentos com conflito de data/hora, paciente ou profissional de saúde.

INSTALAÇAO:

Todas as bibliotecas estão instaladas localmente no repositório.
Use o comando git clone "link.do.repositorio.git" para clonar o projeto.
Conteúdo:

manage.py: Principal arquivo do projeto, responsável por diversos comandos.

PASTA"SETUP":

settings.py: Armazena informações de pacotes e aplicações instaladas.
urls.py: Gerencia o roteamento da aplicação.
Pasta "control":

models: Define os modelos das entidades para o banco de dados.
views: Contém métodos para ações como criar, atualizar, excluir ou listar objetos.
templates: Armazena templates HTML para cada opção (Agendamento, paciente, profissional).
Migrações:

Pasta "migrations": Armazena atualizações dos modelos para migração no banco de dados.
Use os comandos python manage.py makemigrations e python manage.py migrate para aplicar atualizações.
Execução:

Certifique-se de estar no diretório "novo projeto".
Ative o ambiente virtual com .\.venv\Scripts\activate.
Execute o projeto com python manage.py runserver.
Para parar a aplicação, use "CTRL + c".
Saia do ambiente virtual com o comando deactivate.
