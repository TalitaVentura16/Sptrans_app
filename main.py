import requests 

#iniciar sessao
sessao  = requests.Session()

#configuracoes 
url = "http://api.olhovivo.sptrans.com.br/v2.1"
token = "b10dad0695188c5f9f7d010b7ca56ce3dd61d2471982be7c29ff66d9916e3271"

#autenticacao
r_aut = sessao.post(f"{url}/Login/Autenticar?token={token}")
print(r_aut.status_code)

#verificacao
if r_aut.status_code != 200:
    print("ERRO")

#numero do onibus
cod_onibus = input("Por favor, informe o número do ônibus para o qual deseja realzar a busca ")

#pesquisa por um onibus
r_busca = sessao.get(f"{url}/Linha/Buscar?termosBusca={cod_onibus}")
print(r_busca.json())

