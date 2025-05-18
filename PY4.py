#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Questão 1 - Validação de Endereços IP

# Criação automática do arquivo de entrada
with open("entrada_ips.txt", "w") as arquivo:
    arquivo.write("""200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256""")

def validar_ip(ip):
    partes = ip.strip().split(".")
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        numero = int(parte)
        if numero < 0 or numero > 255:
            return False
    return True

with open("entrada_ips.txt", "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

ips_validos = []
ips_invalidos = []

for linha in linhas:
    ip = linha.strip()
    if validar_ip(ip):
        ips_validos.append(ip)
    else:
        ips_invalidos.append(ip)

with open("relatorio_ips.txt", "w") as arquivo_saida:
    arquivo_saida.write("[Endereços válidos:]\n")
    for ip in ips_validos:
        arquivo_saida.write(ip + "\n")
    arquivo_saida.write("\n[Endereços inválidos:]\n")
    for ip in ips_invalidos:
        arquivo_saida.write(ip + "\n")

# Impressão dos resultados no console
print("[Endereços válidos:]")
for ip in ips_validos:
    print(ip)

print("\n[Endereços inválidos:]")
for ip in ips_invalidos:
    print(ip)



# In[3]:


# Questão 2 - Conceitos de Erros

# a) Erro de sintaxe
# Ocorre quando o código está escrito de forma incorreta, impedindo a execução.

# Exemplo:
# print("Olá"  # ← erro de sintaxe (faltou fechar parêntese)

# b) Erro de tempo de execução
# Ocorre durante a execução do programa, geralmente por entrada incorreta ou operações inválidas.

# Exemplo:
# numero = int("abc")  # ← erro de tempo de execução (ValueError)

# c) Erro semântico
# Ocorre quando o código roda sem erros, mas o resultado não é o esperado logicamente.

# Exemplo:
# media = soma / 2  # ← erro semântico (talvez o correto fosse dividir pela quantidade de itens)



# In[5]:


# Questão 3 - Tratamento de Erros com try, except, else, finally

def entrada_idade():
    # Exemplo de tratamento de erro em entrada de dados
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Erro: Digite um número inteiro válido.")
    else:
        print(f"Sua idade é: {idade}")
    finally:
        print("Encerrando programa.")

entrada_idade()


# In[ ]:




