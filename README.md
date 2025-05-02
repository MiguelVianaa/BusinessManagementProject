# Projeto Gestão De Empresas
Gestão de Empresas é um projeto desenvolvido como parte da aprendizagem do framework Django. O objetivo é facilitar a administração de empresas, permitindo o cadastro e a gestão de empresas, colaboradores, setores e cargos de forma organizada.

### Gestão de Empresas:

| Relações                     | Descrição                                                 |
|------------------------------|-----------------------------------------------------------|
| (1:N) Empresa <- Colaborador | Uma empresa pode ter muitos colaboradores.                |
| (N:1) Colaborador -> Empresa | Muitos colaboradores podem trabalhar em uma empresa.      |
| (1:N) Cargo <- Colaborador   | Um cargo pode pertencer a muitos colaboradores.           |
| (N:1) Colaborador -> Cargo   | Muitos colaboradores podem ter somente um cargo.          |
| (N:1) Colaborador -> Setor   | Muitos colaboradores podem trabalhar em somente um setor. |
| (1:N) Setor <- Colaborador   | Um setor pode ser composto por vários colaboradores.      |

## Descrição:

### **Home**
Na página inicial, você pode navegar para realizar os seguintes cadastros:
- **Empresas**
- **Colaboradores**
- **Setores**
- **Cargos**

### **Empresas**
No cadastro de empresas, além de todos os campos que o copoe, a listagem, edição e exclusão das empresas,
também é gerenciado o vínculo de cada coisa, quais setores vão ter naquela empresa, estando disponivel todos
os que foram cadastrados no fluxo de setores, quais colaboradores vao trabalhar naquele setor dentro daquela
empresa, e que cargos aqueles colaboradores vão ter,um colaborador pode ter um cargo por exemplo de um Gestor do setor,
ou ser um colaborador de um outro cargo mais abaixo disso dentro daquele setor. tudo isso será gerenciavel no 
fluxo de empresas,

### **Colaboradores**
Colaboradores é o fluxo onde os mesmos são cadastrados e exibidos na listagem, posso gerencia-los
com edição e exclusão, eles são utilizados na empresas, lá onde será vinculado o mesmo a um setor
e também a um cargo.

### **Setores**
Os setores conta com o cadastro listagem e podem ser gerenciados com edição e exclusão, são
utilizados nas empresas como uma opção de multi-seleção para várias empresas, serve para
ser vinculados a várias empresas, e como um grupo de vários colaboradores, colaboradores estes
que só podem trabalhar em um grupo de setores, com determinado cargo e em  uma determinada empresa.

### **Cargos**
Os cargos da mesma forma, utilizados no cadastro e edição de empresas, para serem atribuídos a um
colaborador, o mesmo só pode ser atribuído se o colaborador já estiver vinculádo a uma empresa e a um
setor, ou seja, dentro daquela empresa, e dentro daquele setor, aquele colaborador vai ter aquele cargo,
por exemplo, o "Marcos", que trabalha na empresa "Mateus Borges Auto Peças LTDA" com o cargo de "Gestor da 
equipe de mecânicos elétricistas"

**Empresas:**
* id
* nome
* razao_social
* cnpj
* inscricao_estadual
* created_at
* updated_at
* deleted_at

**Pivot Empresas Setores:**
* id
* empresa_id
* setor_id

**Colaboradores:**
* id
* nome
* email
* empresa_id
* cargo_id
* created_at
* updated_at
* deleted_at

**Cargos:**
* id
* nome
* descricao
* created_at
* updated_at
* deleted_at

**Setores:**
* id
* nome
* descricao
* created_at
* updated_at
* deleted_at

### Bibliotecas e Pacotes

Instale as dependências: Execute o seguinte comando para instalar as bibliotecas necessárias para o projeto:
```bash
pip install -r requirements.txt
```

O arquivo requirements.txt contém todas as bibliotecas necessárias para rodar este projeto.
Aqui está uma lista das principais dependências instaladas:

### Dependências do Projeto
| Pacote        | Versão  | Descrição                                     |
|---------------|---------|-----------------------------------------------|
| Django        | 5.2     | Framework principal para desenvolvimento web. |
| psycopg2      | 2.9.10  | Conector para banco de dados PostgreSQL.      |
| Jinja2        | 3.1.2   | Motor de templates usado pelo Django.         |
| pillow        | 10.2.0  | Manipulação de imagens.                       |
| bcrypt        | 3.2.2   | Gerador de hashes seguros para senhas.        |
| cryptography  | 41.0.7  | Para funcionalidades avançadas de segurança.  |