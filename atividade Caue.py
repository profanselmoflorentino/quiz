quiz = [
    ["Qual a montadora do carro Mustang?", "Chevrolet", "Ford", "Dodge", "Toyota", "B"],
    ["Qual país é famoso pela fabricação de carros Ferrari?", "Alemanha", "Itália", "Espanha", "França", "B"],
    ["Qual é o nome do modelo elétrico mais popular da Tesla?", "Model X", "Model 3", "Model S", "Roadster", "B"],
    ["Qual montadora fabrica o modelo Civic?", "Ford", "Honda", "Volkswagen", "Nissan", "B"],
    ["Qual o carro mais vendido da Volkswagen?", "Polo", "Golf", "Passat", "Fusca", "D"],
    ["Qual o carro mais rápido do mundo?", "Bugatti Chiron", "BMW i8", "Lamborghini Aventador", "Ferrari 812 GTS", "A"],
    ["Qual país é conhecido por fabricar o carro esportivo Koenigsegg?", "Suécia", "Alemanha", "Itália", "Japão", "A"],
    ["Qual é a função do virabrequim em um motor a combustão interna?", "Regular a temperatura do motor", "Converter o movimento linear dos pistões em movimento rotativo", "Controlar a mistura de ar e combustível", "Reduzir as emissões de gases poluentes", "B"],
    ["Qual componente do motor é responsável por controlar a abertura e fechamento das válvulas?", "Pistão", "Virabrequim", "Comando de válvulas", "Biela", "C"],
    ["O que significa a sigla 'DOHC' em motores?", "Dual Overhead Camshaft", "Direct Overhead Cylinder", "Dual Overhead Cylinder", "Direct Overhead Camshaft", "A"]
]

def run_quiz(quiz):
    score = 0
    for question in quiz:
        print(question[0])
        print(f"A) {question[1]}")
        print(f"B) {question[2]}")
        print(f"C) {question[3]}")
        print(f"D) {question[4]}")
        answer = input("Sua resposta: ").strip().upper()
        if answer == question[5]:
            print("Correto!\n")
            score += 1
        else:
            print(f"Errado! A resposta correta é {question[5]}\n")
    print(f"Você acertou {score} de {len(quiz)} perguntas.")

run_quiz(quiz)
