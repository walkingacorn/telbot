import requests


def getPokemonStats(name):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/'+name)
    if r.status_code == 200:
        a = r.json()
        b = a['stats']
        output = ''
        for i in b:
           output = output + i['stat']['name']+':'+str(i['base_stat'])+'\n'
        return output
    else:
        return 'Pokemon not found'
#print(getPokemonStats('squirtle'))