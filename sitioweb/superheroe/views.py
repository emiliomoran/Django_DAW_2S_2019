from django.shortcuts import render
import requests

# Create your views here.
def index(request):

    list_id = ['620', '644', '70', '346', '149', '659', '332', '720', '157']
    superheroes = []

    for id in list_id:
        response = requests.get('https://superheroapi.com/api/2542779899290396/%s/image' % id)
        if response.status_code == 200:
            superheroe = response.json()    
            superheroes.append(superheroe)    

    #print(superheroes)
    return render(request, 'index.html', {
        'superheroes': superheroes,
    })

def details(request, id):
    response = requests.get('https://superheroapi.com/api/2542779899290396/%s' % id)
    if response.status_code == 200:
        superheroe = response.json()
        return render(request, 'details.html', {
            'superheroe': superheroe,
        })
    return None