# Framework Django - Projeto Gestão De Empresas
Gestão de Empresas é um projeto desenvolvido como parte da aprendizagem do framework Django. Seu objetivo é aplicar na prática os conhecimentos adquiridos sobre o framework, criando um software voltado para a administração empresarial. A ferramenta permite o cadastro e a gestão de empresas, colaboradores, setores e cargos de maneira organizada, tornando a administração mais eficiente e estruturada.

<hr/>

## Descrição:

### **Home**
Na página inicial, você pode navegar para realizar os seguintes fluxos:
- **Empresas**
- **Colaboradores**
- **Setores**
- **Cargos**

### **Empresas**
O módulo de **Empresas** permite o cadastro, listagem, edição e exclusão de empresas, além de gerenciar suas interações com setores, colaboradores e cargos. Dentro de cada empresa, é possível:
- Definir quais **setores** estarão disponíveis, escolhendo entre aqueles cadastrados no fluxo de setores.
- Vincular **colaboradores** a setores específicos da empresa.
- Atribuir **cargos** aos colaboradores dentro dos setores da empresa. Um colaborador pode ocupar um cargo de liderança, como **Gestor de Setor**, ou desempenhar outra função dentro da estrutura organizacional.

Todo esse gerenciamento ocorre no fluxo de **Empresas**, garantindo uma estrutura flexível para acomodar diferentes hierarquias e organizações.

### **Colaboradores**
O módulo de **Colaboradores** permite o cadastro, listagem, edição e exclusão de colaboradores. Os colaboradores cadastrados podem ser vinculados a:
- **Empresas**, onde irão trabalhar.
- **Setores**, dentro das empresas.
- **Cargos**, que serão atribuídos a cada colaborador dentro do setor em que atuam.

Essa estrutura facilita o gerenciamento dos profissionais e a definição clara de suas responsabilidades dentro da organização.

### **Setores**
Os **Setores** contam com funcionalidades de cadastro, listagem, edição e exclusão. Eles podem ser vinculados a múltiplas empresas e servem como agrupamentos de colaboradores. Algumas características desse módulo incluem:
- **Multi-seleção**, permitindo que setores sejam utilizados em diversas empresas.
- Os colaboradores só podem atuar dentro de setores específicos, de acordo com seus cargos e a empresa à qual estão vinculados.

Isso torna o fluxo de **Setores** essencial para estruturar departamentos dentro de cada empresa.

### **Cargos**
Os **Cargos** funcionam como a peça final da estrutura organizacional. Eles são cadastrados e utilizados no módulo de **Empresas** e podem ser atribuídos a colaboradores dentro dos setores em que atuam. Um cargo só pode ser atribuído a um colaborador que:
- Já esteja vinculado a uma **empresa**.
- Já tenha sido vinculado a um **setor** dentro dessa empresa.

Isso garante que cada colaborador tenha um papel bem definido, como no caso de **Marcos**, que trabalha na empresa **Mateus Borges Auto Peças LTDA** com o cargo de **Gestor da equipe de mecânicos eletricistas**

<hr/>

## Relacionamentos e Banco de dados:

### **Empresas ↔ Setores:**
- **Relacionamento muitos-para-muitos, implementado pela tabela Empresa_Setor.**
- **Exemplo: A empresa "Mateus Borges Auto Peças LTDA" pode ter os setores "Mecânica Eletricista" e "Vendas".**

### **Colaboradores → Empresas, Setores, Cargos:**

- **A tabela Colaborador_Setor_Cargo vincula um colaborador a uma empresa, um setor e um cargo.**
- **Garante que um colaborador só possa ser associado a um setor que existe na empresa (validação via Empresa_Setor) e a um cargo válido.**
- **Exemplo: Marcos é vinculado à empresa "Mateus Borges Auto Peças LTDA", ao setor "Mecânica Eletricista" e ao cargo "Gestor da Equipe"**

<hr/>

### Colunas do banco:

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