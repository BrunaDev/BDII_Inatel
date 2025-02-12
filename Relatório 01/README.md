## Exercício de Orientação a Objetos - Professor, Aluno e Aula

Criando uma classe Professor
Crie uma classe chamada Professor com as seguintes propriedades:
nome
E os seguintes métodos:
init: Construtor da classe, que inicializa a propriedade nome.
ministrar_aula: Método que recebe um argumento assunto e retorna uma string com a frase "O professor NOME está ministrando uma aula sobre ASSUNTO.".
<p>
Criando uma classe Aluno
Crie uma classe chamada Aluno com as seguintes propriedades:
nome
E os seguintes métodos:
init: Construtor da classe, que inicializa a propriedade nome.
presenca: Método que retorna uma string com a frase "O aluno NOME está presente.".
<p>
Criando uma classe Aula
Crie uma classe chamada Aula com as seguintes propriedades:
professor
assunto
alunos
E os seguintes métodos:
init: Construtor da classe, que inicializa as propriedades professor, assunto e alunos.
adicionar_aluno: Método que recebe um argumento aluno e adiciona esse objeto Aluno à lista alunos.
listar_presenca: Método que retorna uma string com a frase "Presença na aula sobre ASSUNTO, ministrada pelo professor NOME:", seguido da lista de todos os alunos presentes, usando o método ‘presenca’ do aluno.
<p>
Exemplo de uso:
professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())

# Presença na aula sobre Programação Orientada a Objetos, ministrada pelo professor Lucas:
# O aluno Maria está presente.
# O aluno Pedro está presente.