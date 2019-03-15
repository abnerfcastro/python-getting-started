import urllib.request
import json

cep = input("Qual o seu CEP? ")
request = urllib.request.Request(f"http://viacep.com.br/ws/{cep}/json/")

try:
    response = urllib.request.urlopen(request)
    data = response.read().decode('utf-8')
    json_data = json.loads(data)
    print(f"CEP {json_data['cep']} corresponde a {json_data['logradouro']}, {json_data['bairro']}, {json_data['localidade']}-{json_data['uf']}")
except Exception as e:
    print(f"There has been an error while fetching data for CEP={cep} --> {e}")