# 🧠 Exercício Relâmpago Surpresa Nº π  

---

## 📚 Tema: Orientação a Objetos  
### Edição Especial — Herança e Relacionamentos  

---

## 1️⃣ Considere o Diagrama  

O diagrama abaixo representa a hierarquia e os relacionamentos entre as classes:

<br/>
<img width="491" height="463" alt="image" src="https://github.com/user-attachments/assets/bc71f88a-3f22-4f6c-83ea-c7b1466498ca" />


---

## 2️⃣ Escreva código para responder:

a) Qual a escolaridade de um professor?  
b) Qual a escolaridade do coordenador de um curso?  
c) Qual a escolaridade do diretor de uma escola?  
d) Qual o estado de naturalidade de um aluno?  
e) Qual a cidade de nascimento de um professor?  
f) Qual o estado em que um aluno estuda?  
g) Qual o tipo de ensino (fundamental, médio, superior) que um professor foi contratado para lecionar?  
h) Quem é o coordenador do curso de um aluno?  
i) Quem é o diretor de um professor?  
j) Quem é o coordenador de um professor?

---

## 3️⃣ Orientações  

🧩 **a)** Observe que há **herança** neste diagrama!  
🔁 **b)** Herança não tem multiplicidade.  
⚙️ **c)** Defina, para cada relacionamento, as **multiplicidades** (1, n, 0..1 etc).  
🧠 **d)** Escreva **casos de teste** demonstrando o funcionamento.  
🔥 **e)** E claro... se vire com o restante! 😈  

---

## 4️⃣ Faça o exercício e deixe seu professor feliz!! 😄  

---

### 🎯 Dica de Estrutura

Você pode organizar suas classes assim:

- **Classe `Pessoa`** → atributos: `nome`, `naturalidade`  
- **Classe `Professor`** → herda de `Pessoa`  
- **Classe `Aluno`** → herda de `Pessoa`  
- **Classe `Curso`** → relaciona-se com `Professor` (coordenação) e `Aluno` (matrícula)  
- **Classe `TipoEnsino`** → usada por `Curso` e `Professor`  
- **Classe `Escola`** → tem um `diretor` (Professor) e vários `Cursos`  
- **Classe `Cidade`** e **Classe `Estado`** → para representar localizações  

---

💬 “Herança é o doce da Orientação a Objetos. Só cuidado pra não exagerar no açúcar!” 🍬
