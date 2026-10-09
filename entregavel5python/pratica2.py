import re

def validar_email(email: str) -> bool:
    """
    Valida e-mails no formato: usuario@dominio.com ou .com.br
    \w+ -> letras, números e underline
    [\w.-]+ -> aceita pontos e hífens no nome ou domínio
    """
    padrao = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
    return bool(re.match(padrao, email.strip()))

def validar_cpf(cpf: str) -> bool:
    """
    Valida CPF no formato pontuado: 000.000.000-00
    \d{3} -> exatamente 3 dígitos
    \. e \- -> caracteres literais de ponto e hífen
    """
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return bool(re.match(padrao, cpf.strip()))

def validar_telefone(telefone: str) -> bool:
    """
    Valida telefone com DDD e 8 ou 9 dígitos: (11)98765-4321 ou (11)8765-4321
    \( e \) -> caracteres literais de parênteses
    \d{4,5} -> 4 ou 5 dígitos no primeiro bloco
    """
    padrao = r'^\(\d{2}\)\d{4,5}-\d{4}$'
    return bool(re.match(padrao, telefone.strip()))

def validar_data(data: str) -> bool:
    """
    Valida data no formato: DD/MM/AAAA
    \d{2} -> 2 dígitos para dia/mês
    \d{4} -> 4 dígitos para o ano
    """
    padrao = r'^\d{2}/\d{2}/\d{4}$'
    return bool(re.match(padrao, data.strip()))


# --- DEMONSTRAÇÃO E TESTES ---
if __name__ == "__main__":
    dados_teste = [
        {"email": "joao@email.com", "cpf": "123.456.789-00", "telefone": "(11)98765-4321", "data": "15/03/2024"},
        {"email": "email_invalido", "cpf": "12345678900", "telefone": "11987654321", "data": "2024-03-15"}
    ]

    print("=== TESTE DE VALIDAÇÃO COM REGEX ===\n")
    
    for idx, d in enumerate(dados_teste, 1):
        print(f"--- Registro {idx} ---")
        print(f"E-mail ({d['email']}): {'VÁLIDO' if validar_email(d['email']) else 'INVÁLIDO'}")
        print(f"CPF ({d['cpf']}): {'VÁLIDO' if validar_cpf(d['cpf']) else 'INVÁLIDO'}")
        print(f"Telefone ({d['telefone']}): {'VÁLIDO' if validar_telefone(d['telefone']) else 'INVÁLIDO'}")
        print(f"Data ({d['data']}): {'VÁLIDO' if validar_data(d['data']) else 'INVÁLIDO'}\n")

#programa
#{
#	inclua biblioteca Texto --> txt
#
#	funcao logico validarCpf(cadeia cpf)
#	{
#		// CPF no formato 000.000.000-00 deve ter exatamente 14 caracteres
#		se (txt.numero_caracteres(cpf) != 14) {
#			retorne falso
#		}
#
#		// Verifica se os pontos e o hífen estão nas posições corretas
#		se (txt.obter_caracter(cpf, 3) != '.' ou txt.obter_caracter(cpf, 7) != '.' ou txt.obter_caracter(cpf, 11) != '-') {
#			retorne falso
#		}
#
#		retorne verdadeiro
#	}
#
#	funcao inicio()
#	{
#		cadeia cpfTeste = "123.456.789-00"
#		
#		escreva("=== VALIDAÇÃO DE FORMATO (PORTUGOL) ===\n")
#		se (validarCpf(cpfTeste)) {
#			escreva("CPF '", cpfTeste, "' está no formato correto!\n")
#		} senao {
#			escreva("CPF '", cpfTeste, "' é inválido.\n")
#		}
#	}
#}