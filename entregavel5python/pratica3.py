import csv
import os

def processar_arquivo_dados(caminho_arquivo: str) -> list[dict]:
    """
    Lê e valida um arquivo CSV/TXT contendo informações de e-mail, CPF, telefone e data.
    Utiliza tratamento estruturado de exceções para capturar falhas de leitura, campos ou conversão.
    """
    registros = []
    arquivo_referencia = None

    print(f"\n--- Iniciando leitura do arquivo: '{caminho_arquivo}' ---")

    try:
        # Tenta abrir e processar o arquivo CSV
        arquivo_referencia = open(caminho_arquivo, mode='r', encoding='utf-8')
        leitor = csv.DictReader(arquivo_referencia)

        # Colunas obrigatórias esperadas no cabeçalho
        colunas_esperadas = {'email', 'cpf', 'telefone', 'data'}
        
        # Verifica se o arquivo está vazio ou sem cabeçalho
        if leitor.fieldnames is None:
            raise ValueError("O arquivo está completamente vazio ou corrompido.")

        # Sanitiza os nomes das colunas lidas (remove espaços)
        colunas_encontradas = {col.strip() for col in leitor.fieldnames}

        # Valida se todas as colunas necessárias estão presentes (Gera KeyError se faltar alguma)
        colunas_faltantes = colunas_esperadas - colunas_encontradas
        if colunas_faltantes:
            raise KeyError(f"Colunas ausentes no cabeçalho: {', '.join(colunas_faltantes)}")

        # Processa cada linha do arquivo
        for numero_linha, linha in enumerate(leitor, start=2):
            try:
                # Limpa espaços das chaves e valores
                registro = {chave.strip(): valor.strip() for chave, valor in linha.items()}
                
                # Exemplo de conversão/validação que pode disparar ValueError se o dado estiver inconsistente
                if not registro['email'] or not registro['cpf']:
                    raise ValueError(f"Linha {numero_linha}: Campos essenciais (email ou CPF) estão em branco.")
                
                registros.append(registro)

            except ValueError as erro_linha:
                print(f"[Aviso de Processamento] {erro_linha}")

    except FileNotFoundError:
        print(f"[ERRO CRÍTICO] O arquivo '{caminho_arquivo}' não foi encontrado.")
        print("Verifique se o nome do arquivo e o caminho estão corretos.")

    except KeyError as erro_chave:
        print(f"[ERRO ESTRUTURAL] {erro_chave}")
        print("Certifique-se de que o cabeçalho do CSV contém: email, cpf, telefone, data.")

    except ValueError as erro_valor:
        print(f"[ERRO DE CONTEÚDO] {erro_valor}")

    except Exception as erro_generico:
        print(f"[ERRO INESPERADO] Ocorreu uma falha não mapeada: {erro_generico}")

    else:
        # Executado APENAS se o bloco 'try' for concluído sem NENHUMA exceção
        print(f"[SUCESSO] Arquivo lido perfeitamente! {len(registros)} registro(s) carregado(s).")
        return registros

    finally:
        # Executado SEMPRE, ocorrendo erro ou não (ideal para fechar arquivos e limpar conexões)
        if arquivo_referencia and not arquivo_referencia.closed:
            arquivo_referencia.close()
            print("[SISTEMA] Conexão com o arquivo fechada com segurança no bloco 'finally'.")

    return []


# --- TESTES PRÁTICOS DOS CENÁRIOS DE ERRO ---
if __name__ == "__main__":
    print("=== DEMONSTRAÇÃO DE TRATAMENTO DE EXCEÇÕES ===")

    # Teste 1: Arquivo Inexistente (FileNotFoundError)
    print("\n>>> Cenario 1: Testando arquivo inexistente")
    processar_arquivo_dados("arquivo_fantasma.csv")

#programa
#{
#	funcao inicio()
#	{
#		// Simulação de verificação do "arquivo"
#		logico arquivoExiste = falso
#		logico cabecalhoValido = verdadeiro
#
#		escreva("=== TRATAMENTO DE ERROS SIMULADO (PORTUGOL) ===\n\n")
#
#		// Simula 'try / except FileNotFoundError'
#		se (nao arquivoExiste)
#		{
#			escreva("[ERRO] Arquivo de dados não foi encontrado!\n")
#		}
#		senao
#		{
#			// Simula 'try / except KeyError'
#			se (nao cabecalhoValido)
#			{
#				escreva("[ERRO] Colunas obrigatórias ausentes na estrutura do arquivo.\n")
#			}
#			senao
#			{
#				// Equivalente ao bloco 'else'
#				escreva("[SUCESSO] Dados lidos com sucesso!\n")
#			}
#		}
#
#		// Equivalente ao bloco 'finally'
#		escreva("\n[FINALLY] Finalizando rotina e liberando recursos de memória.\n")
#	}
#}