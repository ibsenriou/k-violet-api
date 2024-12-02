from src.accounting.models import Account


class AccountingFactory:
    """
    This class is a container for helper functions that create "Accounting" objects for testing purposes
    """

    @staticmethod
    def create_account(
        nature_of_operation: int,
        type: int,
        description: str,
        is_global: bool,
        code: str,
        fk_account: Account,
    ) -> Account:

        account = Account.objects.create(
            nature_of_operation=nature_of_operation,
            type=type,
            description=description,
            is_global=is_global,
            code=code,
            fk_account=fk_account,
        )

        return account

    def create_accounting_all() -> str:
        """
        Create accounting.
        """

        despesas = AccountingFactory.create_account(
            nature_of_operation=2,
            type=1,
            description='Despesas',
            is_global=True,
            code='4',
            fk_account=None,
        )

        despesasOrdinarias = AccountingFactory.create_account(
            nature_of_operation=2,
            type=1,
            description='Despesas Ordinárias',
            is_global=True,
            code='4.1',
            fk_account=despesas,
        )

        administracao = AccountingFactory.create_account(
            nature_of_operation=2,
            type=1,
            description='Com a Administração',
            is_global=True,
            code='4.1.1',
            fk_account=despesasOrdinarias,
        )

        pessoas = AccountingFactory.create_account(
            nature_of_operation=2,
            type=1,
            description='Com Pessoal',
            is_global=True,
            code='4.1.1.1',
            fk_account=administracao,
        )

        salario = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Salários com Pessoal',
            is_global=True,
            code='4.1.1.1.1',
            fk_account=pessoas,
        )

        INSS = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Encargos com INSS',
            is_global=True,
            code='4.1.1.1.2',
            fk_account=pessoas,
        )

        FGTS = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Encargos com FGTS',
            is_global=True,
            code='4.1.1.1.3',
            fk_account=pessoas,
        )

        rescisao = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Rescisão Contrato Trabalho',
            is_global=True,
            code='4.1.1.1.4',
            fk_account=pessoas,
        )

        materiais = AccountingFactory.create_account(
            nature_of_operation=2,
            type=1,
            description='Com Materiais',
            is_global=True,
            code='4.1.1.2',
            fk_account=administracao,
        )

        escritorio = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Despesas C/ Materiais de Escritório/Informática',
            is_global=True,
            code='4.1.1.2.1',
            fk_account=materiais,
        )

        limpeza = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Despesas C/ Materiais de Limpeza e Conservação',
            is_global=True,
            code='4.1.1.2.2',
            fk_account=materiais,
        )

        hidraulico = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Despesas C/ Materiais Hidráulicos',
            is_global=True,
            code='4.1.1.2.3',
            fk_account=materiais,
        )

        sanitario = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Despesas C/ Materiais Sanitários',
            is_global=True,
            code='4.1.1.2.4',
            fk_account=materiais,
        )

        eletrico = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Despesas C/ Materiais Elétricos',
            is_global=True,
            code='4.1.1.2.5',
            fk_account=materiais,
        )

        manutencao = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Despesas C/ Manutenção do Prédio',
            is_global=True,
            code='4.1.1.2.6',
            fk_account=materiais,
        )

        contrucao = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Despesas C/ Construção e Melhorias',
            is_global=True,
            code='4.1.1.2.7',
            fk_account=materiais,
        )

        servicos = AccountingFactory.create_account(
            nature_of_operation=2,
            type=1,
            description='Com Serviços',
            is_global=True,
            code='4.1.1.3',
            fk_account=administracao,
        )

        juridico = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Assessoria Jurídica',
            is_global=True,
            code='4.1.1.3.1',
            fk_account=servicos,
        )

        terceiros = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Serviços Prestados por Terceiros',
            is_global=True,
            code='4.1.1.3.2',
            fk_account=servicos,
        )

        financeira = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Assessoria Técnica e Financeira',
            is_global=True,
            code='4.1.1.3.3',
            fk_account=servicos,
        )

        seguranca = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Serviços de Sistemas de Segurança',
            is_global=True,
            code='4.1.1.3.4',
            fk_account=servicos,
        )

        tributarias = AccountingFactory.create_account(
            nature_of_operation=2,
            type=1,
            description='Tributárias',
            is_global=True,
            code='4.1.2',
            fk_account=despesasOrdinarias,
        )

        impostos = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Impostos - ISS',
            is_global=True,
            code='4.1.2.1',
            fk_account=tributarias,
        )

        contribuicoes = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Contribuições PIS',
            is_global=True,
            code='4.1.2.2',
            fk_account=tributarias,
        )

        cofins = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Contribuições COFINS',
            is_global=True,
            code='4.1.2.3',
            fk_account=tributarias,
        )

        financeiras = AccountingFactory.create_account(
            nature_of_operation=2,
            type=1,
            description='Financeiras',
            is_global=True,
            code='4.1.3',
            fk_account=despesasOrdinarias,
        )

        juros = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Despesas com Juros',
            is_global=True,
            code='4.1.3.1',
            fk_account=financeiras,
        )

        multas = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Despesas com Multas',
            is_global=True,
            code='4.1.3.2',
            fk_account=financeiras,
        )

        tarifas = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Tarifas Bancárias',
            is_global=True,
            code='4.1.3.3',
            fk_account=financeiras,
        )

        despesasExtraordinarias = AccountingFactory.create_account(
            nature_of_operation=2,
            type=1,
            description='Despesas Extraordinárias',
            is_global=True,
            code='4.2',
            fk_account=despesas,
        )

        salaoFestas = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Gastos Salão de Festas',
            is_global=True,
            code='4.2.1',
            fk_account=despesasExtraordinarias,
        )

        quadras = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Gastos Quadras',
            is_global=True,
            code='4.2.2',
            fk_account=despesasExtraordinarias,
        )

        piscina = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Gastos Piscina',
            is_global=True,
            code='4.2.3',
            fk_account=despesasExtraordinarias,
        )

        playground = AccountingFactory.create_account(
            nature_of_operation=2,
            type=2,
            description='Gastos Playground',
            is_global=True,
            code='4.2.4',
            fk_account=despesasExtraordinarias,
        )

        receitas = AccountingFactory.create_account(
            nature_of_operation=1,
            type=1,
            description='Receitas',
            is_global=True,
            code='3',
            fk_account=None,
        )

        receitasOrdinarias = AccountingFactory.create_account(
            nature_of_operation=1,
            type=1,
            description='Receitas Ordinárias',
            is_global=True,
            code='3.1',
            fk_account=receitas,
        )

        taxaCondominio = AccountingFactory.create_account(
            nature_of_operation=1,
            type=2,
            description='Taxa de Condomínio',
            is_global=True,
            code='3.1.1',
            fk_account=receitasOrdinarias,
        )

        quotas = AccountingFactory.create_account(
            nature_of_operation=1,
            type=2,
            description='Quotas de Construção e Melhorias',
            is_global=True,
            code='3.1.2',
            fk_account=receitasOrdinarias,
        )

        receitasExtraordinarias = AccountingFactory.create_account(
            nature_of_operation=1,
            type=1,
            description='Receitas Extraordinárias',
            is_global=True,
            code='3.2',
            fk_account=receitas,
        )

        taxaSalaoFestas = AccountingFactory.create_account(
            nature_of_operation=1,
            type=2,
            description='Taxa de Salão de Festas',
            is_global=True,
            code='3.2.1',
            fk_account=receitasExtraordinarias,
        )

        taxaQuadras = AccountingFactory.create_account(
            nature_of_operation=1,
            type=2,
            description='Taxa de Atividades Esportivas',
            is_global=True,
            code='3.2.2',
            fk_account=receitasExtraordinarias,
        )

        vendaBens = AccountingFactory.create_account(
            nature_of_operation=1,
            type=2,
            description='Venda de Bens do Condomínio',
            is_global=True,
            code='3.2.3',
            fk_account=receitasExtraordinarias,
        )

        outraTaxa = AccountingFactory.create_account(
            nature_of_operation=1,
            type=2,
            description='Outras Taxas',
            is_global=True,
            code='3.2.4',
            fk_account=receitasExtraordinarias,
        )

        receitasFinanceiras = AccountingFactory.create_account(
            nature_of_operation=1,
            type=1,
            description='Receitas Financeiras',
            is_global=True,
            code='3.3',
            fk_account=receitas,
        )

        rendimentos = AccountingFactory.create_account(
            nature_of_operation=1,
            type=2,
            description='Rendimentos de Aplicações Financeiras',
            is_global=True,
            code='3.3.1',
            fk_account=receitasFinanceiras,
        )

        return [
            despesas,
            despesasOrdinarias,
            administracao,
            pessoas,
            salario,
            INSS,
            FGTS,
            rescisao,
            materiais,
            escritorio,
            limpeza,
            hidraulico,
            sanitario,
            eletrico,
            manutencao,
            contrucao,
            servicos,
            juridico,
            terceiros,
            financeira,
            seguranca,
            tributarias,
            impostos,
            contribuicoes,
            cofins,
            financeiras,
            juros,
            multas,
            tarifas,
            despesasExtraordinarias,
            salaoFestas,
            quadras,
            piscina,
            playground,
            receitas,
            receitasOrdinarias,
            taxaCondominio,
            quotas,
            receitasExtraordinarias,
            taxaSalaoFestas,
            taxaQuadras,
            vendaBens,
            outraTaxa,
            receitasFinanceiras,
            rendimentos,
        ]
