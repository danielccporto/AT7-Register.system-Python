<p align="center">
    <img src="assets/logo_infnet.png" width="70" height="70" />
</p>

# *Assessment*

## Exercício 7

**Atenção:**
- É importante que você desenvolva o programa totalmente, do início ao fim, na IDE do Replit (**AQUI MESMO!!**⚠️**NÃO crie um repl no seu perfil do Replit para fazer o Assessment**⚠️). Você **NÃO** deve escrever o código em outra IDE e depois copiá-lo para cá.
- **NÃO** é permitido usar nenhum recurso que não faça parte do conteúdo desta disciplina, a menos que explicitamente autorizado no enunciado.
- Use comentários para explicar o que cada parte do código faz.
- Após concluir as tarefas, submeta suas soluções aqui e no Moodle (postando lá os links para seus projetos do Replit).

Neste exercício, você deverá criar um sistema de cadastro de dados pessoais combinando todas as funcionalidades implementadas nos exercícios anteriores conforme a descrição a seguir.

## Interação com o usuário

A interação entre o sistema e o usuário se dará através de um menu com as seguintes opções:
1. Inserir novo cadastro
2. Alterar CPF
3. Trocar sobrenomes
4. Remover cadastro
5. Listar todos os cadastros
6. Encerrar

Quando o usuário digitar o nº da opção desejada, a funcionalidade correspondente deverá ser executada (solicitando mais informações do usuário, se for o caso).

Ao concluir com sucesso uma funcionalidade de atualização dos cadastros, o programa deve apresentar uma confirmação para o usuário.

Após a conclusão da execução de cada funcionalidade solicitada pelo usuário, o menu deve ser apresentado novamente para que o usuário possa fazer uma nova seleção, até que ele selecione a opção "Encerrar", cujo efeito deve ser o encerramento do programa.

Se a entrada do usuário no menu não corresponder a nenhuma das opções apresentadas, o programa deve notificar o usuário sobre isto (e, novamente, apresentar o menu).

*Observações:*

- Mesmo que você não tenha conseguido implementar alguma das funcionalidades especificadas, o menu deverá apresentar todas as opções listadas acima.
- Se o usuário selcionar uma funcionalidade não implementada, o programa deve exibir a seguinte mensagem: 'Desculpe! A funcionalidade "X" ainda não foi implementada.', onde o X deverá ser substituído pelo nome da funcionalidade selecionada.