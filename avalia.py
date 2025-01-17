# Descrição:
# Desenvolver um programa que avalie o desempenho de funcionários com base em notas atribuídas a diferentes critérios (ex.: pontualidade, qualidade do trabalho, etc.).

# Etapas:
# Entrada de Dados:

# Solicitar ao usuário o número de funcionários (entre 1 e 100), com validação da entrada.
# Para cada funcionário, pedir notas de 0 a 10 em diversas áreas de desempenho.
# Cálculos:

# Calcular a média das notas de cada funcionário.
# Calcular a média geral da equipe.
# Identificar o melhor e o pior desempenho, com base nas médias individuais.
# Resultados:

# Exibir a média de cada funcionário, a média geral da equipe, e os funcionários com o melhor e pior desempenho.
# Requisitos:
# Validar as entradas numéricas.
# Utilizar estruturas de dados para armazenar as informações.
# Apresentar resultados de forma clara.
# Objetivos:
# Aprender a validar entradas e calcular médias.
# Analisar dados de forma simples.
# Armazenar e apresentar informações de maneira estruturada.


dadoFunc = {

}

qualidaFunc = {

}

while True:
    try:
        qtdFuncionario = int(input('Informe a quantidade de funcionários do estabelecimento: '))

        if qtdFuncionario <= 0:
            print('A quantidade de funcionários não pode ser menor ou igual a 0.')
            print('Informe a quantidade novamente.')
        elif qtdFuncionario > 100:
            print('Uma área não pode conter 100 funcionários.')
            print('Informe a quantidade novamente.')
        elif  qtdFuncionario > 0 and qtdFuncionario <= 100:
            break

    except ValueError:
        print('Digite uma numeração. Exemplo: 25, 67, 89...')


for i in range(qtdFuncionario):
    nomeFunc = input(f'Informe o nome do {i + 1}° funcionário que deseja avaliar: ').capitalize().strip()

    if nomeFunc.isalpha():
        
        while True:
            try:
                print('Responda todas as perguntas em uma escala de 1  a 10, sendo 10 excelente e 1 muito ruim.')

                qualidaFunc['qualidade'] = int(input(f'O funcionário {nomeFunc} entrega tarefas de alta qualidade de forma consistente, atendendo ou superando as expectativas em sua função? '))
                qualidaFunc['adaptação'] = int(input(f'O funcionário {nomeFunc} se adapta bem a mudanças, aprende rapidamente novas habilidades e se desenvolve constantemente para assumir novos desafios? '))
                qualidaFunc['crescimento'] = int(input(f'O funcionário {nomeFunc} possui potencial de crescimento na empresa? '))
                qualidaFunc['valores'] = int(input(f'Os valores do funcionários {nomeFunc} estão alinhados com o da empresa? '))

                if all(0 < qualidaFunc[key] <= 10 for key in ['qualidade', 'adaptação', 'crescimento', 'valores']):
                    notaMedFunc = sum(qualidaFunc.values()) / 4 # O '4' seria referente ao número de qualidades que um funcionário pode ter.
                    
                    dadoFunc[nomeFunc] = notaMedFunc 
                    break
                elif not all(0 < qualidaFunc[key] <= 10 for key in ['qualidade', 'adaptação', 'crescimento', 'valores']):
                    print('Uma das perguntas foi respondida de forma incorreta.')
                    print('Informe apenas números de 1 a 10.')
                    
            except ValueError:
                print('Informe apenas números de 1 a 10.')


    elif nomeFunc.isalpha() == False:

        print('O nome do funcionário precisa ser composto de apenas letras.')


print('Nota média de cada funcionário: ')
for k, v in dadoFunc.items():
    print(f'{k}: {v}')

print(f'Nota média da equipe: {sum(dadoFunc.values()) / qtdFuncionario:.2f}')




