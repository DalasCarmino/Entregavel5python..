import re

# 1. Definição da Exceção Personalizada de Regra de Negócio
class FormatoInvalidoError(Exception):
    """Exceção lançada quando um campo não atende ao formato esperado (Regex)."""
    def __init__(self, campo: str, valor: str, mensagem: str = "Formato inválido"):
        self.campo = campo
        self.valor = valor
        self.mensagem = f"[{campo.upper()}] Erro no valor '{valor}': {mensagem}"
        super().__init__(self.mensagem)


# 2. Funções de validação que utilizam a exceção personalizada
def validar_cpf(cpf: str):
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    if not re.match(padrao, cpf.strip()):
        raise FormatoInvalidoError("CPF", cpf, "Deve estar no formato 000.000.000-00")

def validar_email(email: str):
    padrao = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    if not re.match(padrao, email.strip()):
        raise FormatoInvalidoError("E-mail", email, "Deve ser um e-mail válido (ex: nome@dominio.com)")


# 3. Teste do fluxo com tratamento da exceção personalizada
def cadastrar_usuario(email: str, cpf: str):
    try:
        print(f"Tentando cadastrar: {email} | {cpf}")
        validar_email(email)
        validar_cpf(cpf)
        
    except FormatoInvalidoError as erro:
        # Captura especificamente a nossa exceção de regra de negócio
        print(f"-> [FALHA DE VALIDAÇÃO] {erro.mensagem}")
        
    except Exception as erro_inesperado:
        print(f"-> [ERRO INESPERADO] {erro_inesperado}")
        
    else:
        print("-> [SUCESSO] Usuário cadastrado com sucesso!\n")


# --- DEMONSTRAÇÃO ---
if __name__ == "__main__":
    print("=== TESTE DE EXCEÇÃO PERSONALIZADA ===\n")
    
    # Caso 1: Dados Válidos
    cadastrar_usuario("joao@email.com", "123.456.789-00")
    
    # Caso 2: CPF Inválido (dispara FormatoInvalidoError)
    cadastrar_usuario("maria@email.com", "12345678900")
    
    # Caso 3: E-mail Inválido (dispara FormatoInvalidoError)
    cadastrar_usuario("email_errado", "987.654.321-11")

#programa
#{
#	inclua biblioteca Texto --> txt
#
#	// Função que simula a validação lançando uma mensagem de erro
#	funcao logico validarFormatoCpf(cadeia cpf, cadeia &mensagemErro)
#	{
#		se (txt.numero_caracteres(cpf) != 14)
#		{
#			mensagemErro = "[ERRO DE NEGÓCIO] CPF deve conter exatamente 14 caracteres (000.000.000-00)."
#			retorne falso
#		}
#		retorne verdadeiro
#	}
#
#	funcao inicio()
#	{
#		cadeia cpfEntrada = "12345678900"
#		cadeia mensagem
#
#		escreva("=== VALIDAÇÃO DE REGRA DE NEGÓCIO (PORTUGOL) ===\n\n")
#
#		se (nao validarFormatoCpf(cpfEntrada, mensagem))
#		{
#			escreva(mensagem, "\n")
#		}
#		senao
#		{
#			escreva("CPF Válido!\n")
#		}
#	}
#}