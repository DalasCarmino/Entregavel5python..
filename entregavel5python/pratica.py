import csv
import os

def ler_arquivo_dados(caminho_arquivo):
    """
    Lê um arquivo CSV ou TXT contendo e-mail, CPF, telefone e data,
    retornando uma lista de dicionários com os registros cadastrados.
    """
    # Verifica se o arquivo realmente existe
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []

    registros = []

    try:
        # Abre o arquivo para leitura (suporta tanto .csv quanto .txt delimitado por vírgula)
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            # Usando csv.DictReader para mapear o cabeçalho automaticamente
            leitor = csv.DictReader(arquivo)
            
            for linha in leitor:
                # Remove espaços em branco extras das chaves e valores
                registro = {chave.strip(): valor.strip() for chave, valor in linha.items()}
                registros.append(registro)
                
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return []

    return registros


# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    nome_arquivo = "dados.csv"  # Pode ser um arquivo .csv ou .txt
    
    print("=== LEITURA DE ARQUIVO DE DADOS ===")
    dados = ler_arquivo_dados(nome_arquivo)

    if dados:
        print(f"\nSucesso! {len(dados)} registro(s) carregado(s):\n")
        print("-" * 65)
        print(f"{'E-MAIL':<25} | {'CPF':<14} | {'TELEFONE':<12} | {'DATA':<10}")
        print("-" * 65)
        
        for p in dados:
            email = p.get('email', 'N/A')
            cpf = p.get('cpf', 'N/A')
            telefone = p.get('telefone', 'N/A')
            data = p.get('data', 'N/A')
            
            print(f"{email:<25} | {cpf:<14} | {telefone:<12} | {data:<10}")
        print("-" * 65)

#programa
#{
#	funcao inicio()
#	{
#		// Simulação dos dados que seriam lidos de um arquivo TXT/CSV
#		cadeia emails[3] = {"joao@email.com", "maria@email.com", "carlos@email.com"}
#		cadeia cpfs[3] = {"123.456.789-00", "987.654.321-11", "456.789.123-22"}
#		cadeia telefones[3] = {"(11)98765-4321", "(21)99999-8888", "(31)97777-6666"}
#		cadeia datas[3] = {"15/03/2024", "20/04/2024", "05/05/2024"}
#
#		escreva("=== LEITURA DE DADOS DO ARQUIVO (SIMULAÇÃO) ===\n\n")
#		escreva("-------------------------------------------------------------------\n")
#		escreva("E-MAIL\t\t\t| CPF\t\t| TELEFONE\t| DATA\n")
#		escreva("-------------------------------------------------------------------\n")
#
#		para (inteiro i = 0; i < 3; i++)
#		{
#			escreva(emails[i], "\t| ", cpfs[i], "\t| ", telefones[i], "\t| ", datas[i], "\n")
#		}
#		escreva("-------------------------------------------------------------------\n")
#	}
#}