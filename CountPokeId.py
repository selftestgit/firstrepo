#Poke API
#Count the number of pokemons in poke API http://pokeapi.co/api
import requests
import simplejson as json
import pykemon
from simplejson import JSONDecodeError

#Define function count with value id
def Count(id):
    #Empty list to store the pokemns
    pokemons = []
    
    while id >= 1:
        url = 'http://pokeapi.co/api/v1/pokemon/'
        url = (url)+ str(id)
        #request to connect to url
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            d= data['name']
            #print d
            #Add the id to the list created
            pokemons.append(d)
        else:
            print " Access Denied"
        
        id += 1
    print len(pokemons)
Count(1)   
