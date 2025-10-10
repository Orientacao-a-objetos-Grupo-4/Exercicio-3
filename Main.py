from Models.Aluno import Aluno
from Models.Cidade import Cidade
from Models.Curso import Curso
from Models.Escola import Escola
from Models.Escolaridade import Escolaridade
from Models.Professor import Professor
from Models.TipoEnsino import TipoEnsino

print("Respostas das Perguntas do Exercicio!")

cidade_petropolis = Cidade(cidade="Petropolis", estado="Rio de Janeiro")
cidade_juiz_fora = Cidade(cidade="Juiz Fora", estado="Minas Gerais")
cidade_barbacena = Cidade(cidade="Barbacena", estado="Minas Gerais")

esc_superior = Escolaridade(escolaridade="Ensino Superior")
esc_ens_medio = Escolaridade(escolaridade="Ensino Medio Completo")
esc_pos_graduado = Escolaridade(escolaridade="Pós Graduado")
esc_mestrado = Escolaridade(escolaridade="Mestrado")

tipoEnsino_fundamental = TipoEnsino(tipoEnsino = "Ensino Fundamental")

diretorCarlos = Professor(
    nome="Carlos",
    idade=67,
    escolaridade= esc_mestrado,
    naturalidade= cidade_barbacena,
    materia="matematica"
)

profAlexandre = Professor(
    nome='Alexandre',
    idade=37,
    escolaridade= esc_superior,
    naturalidade= cidade_petropolis,
    materia="Física"
)

profMM = Professor(
    nome='MM',
    idade=45,
    escolaridade= esc_pos_graduado,
    naturalidade= cidade_juiz_fora,
    materia="Orientação a Objetos"
)

alunoVitor = Aluno(
    nome='Vitor',
    idade=25,
    escolaridade=esc_ens_medio,
    naturalidade=cidade_juiz_fora,
    matricula="0123456789"
)

escolaUni = Escola(
    nome="UniEscola",
    direcao=diretorCarlos,
    cidade=cidade_petropolis
)

cursoEng = Curso(
    nome="Curso Engenharia",
    coordenacao=profMM,
    escola = escolaUni
)



profAlexandre.setContratacao(cursoEng)
alunoVitor.setCurso(cursoEng)

print(f'a = {profAlexandre.getEscolaridade().getEscolaridade()}')
print(f'b = {cursoEng.getCoordenacao().getEscolaridade().getEscolaridade()}')
print(f'c = {escolaUni.getDirecao().getEscolaridade().getEscolaridade()}')
print(f'd = {alunoVitor.getNaturalidade().getEstado()}')
print(f'e = {profAlexandre.getNaturalidade().getCidade()}')
print(f'f = {alunoVitor.getCurso().getEscola().getCidade().getEstado()}')
cursoEng.setTipoEnsino(tipoEnsino_fundamental)
print(f'g = {profAlexandre.getContratacao().getTipoEnsino().getTipoEnsino()}')
print(f'h = {alunoVitor.getCurso().getCoordenacao().getNome()}')
print(f'i = {profAlexandre.getContratacao().getEscola().getDirecao().getNome()}')
print(f'j = {profAlexandre.getContratacao().getCoordenacao().getNome()}')
