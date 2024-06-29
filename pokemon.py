import requests


def getPokemonStats(name):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/'+name)
    if r.status_code == 200:
        a = r.json()
        c = a['stats']
        output = ''
        for i in c:
           output = output + i['stat']['name']+':'+str(i['base_stat'])+'\n'
        return output
    else:
        return 'Pokemon illa'
#print(getPokemonStats('squirtle'))