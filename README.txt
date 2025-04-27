Gestão de Empresas:
	Relações:
		* (N:M) Empresa <-> Setor        * Muitas empresas podem ter muitos setores.
		* (1:N) Empresa <- Colaborador   * Uma empresa pode ter muitos colaboradores.
		* (N:1) Colaborador -> Empresa   * Muitos colaboradores pode trabalhar em uma empresa.
		* (1:N) Cargo <- Colaborador     * Um cargo pode pertencer a muitos colaboradores.
		* (N:1) Colaborador -> Cargo     * Muitos colaboradores podem ter somente um cargo.
		* (N:1) Colaborador -> Setor     * Muitos colaboradores podem trabalhar em somente um setor.
		* (1:N) Setor <- Colaborador     * Um setor pode ser composto por vários colaboradores.

    Descrição:
        TODO: ### **Página Home**
        Na página inicial, você pode navegar para realizar os seguintes cadastros:
        - **Empresas**
        - **Colaboradores**
        - **Setores**
        - **Cargos**

        TODO: ### **Página de Empresas**
        Na página de empresas, é possível:
        1. Cadastrar uma nova empresa.
        2. Vincular colaboradores à empresa durante o cadastro ou edição da empresa.
        3. Associar setores à empresa cadastrada.
        4. Definir cargos para os colaboradores vinculados à empresa.

        Obs.:
            Não é obrigatório preencher imediatamente o setor ou cargo de um colaborador.
            Essa associação pode ser realizada posteriormente.

        TODO: ### **Página de Colaboradores**
        Na página de colaboradores, além de cadastrar ou editar as informações dos mesmos, é possível:
        1. Alterar ou adicionar vínculos do colaborador com **empresas, setores ou cargos**, de forma flexível, conforme necessário.

        TODO: ### **Página de Setores**
        O cadastro e a edição de setores são simples e diretos.
        Basta preencher os campos necessários para que o setor seja utilizado no fluxo.

        TODO: ### **Página de Cargos**
        Assim como na página de setores, o cadastro de cargos é prático e intuitivo.
        Permite definir os cargos que serão utilizados posteriormente no fluxo.

	Empresas:
		* id
		* nome
		* razao_social
		* cnpj
		* inscricao_estadual
		* created_at
		* updated_at
		* deleted_at

	Pivot Empresas Setores:
		* id
		* empresa_id
		* setor_id

	Colaboradores:
		* id
		* nome
		* email
		* empresa_id
		* cargo_id
		* created_at
        * updated_at
        * deleted_at

	Cargos:
		* id
		* nome
		* descricao
		* created_at
        * updated_at
        * deleted_at

	Setores:
		* id
		* nome
		* descricao
		* created_at
		* updated_at
		* deleted_at


Instale as dependências: Execute o seguinte comando para instalar as bibliotecas necessárias para o projeto:
pip install -r requirements.txt

Bibliotecas e Pacotes
O arquivo requirements.txt contém todas as bibliotecas necessárias para rodar este projeto.
Aqui está uma lista das principais dependências instaladas:

Pacote	        Versão	    Descrição
Django	        5.2         Framework principal para desenvolvimento web.
psycopg2	    2.9.10      Conector para banco de dados PostgreSQL.
Jinja2	        3.1.2       Motor de templates usado pelo Django.
pillow	        10.2.0      Manipulação de imagens.
bcrypt	        3.2.2       Gerador de hashes seguros para senhas.
cryptography    41.0.7      Para funcionalidades avançadas de segurança.

