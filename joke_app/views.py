from django.shortcuts import render
import requests
# Create your views here.

def rand_joke(request):
    API_URL = 'https://v2.jokeapi.dev//joke//Any'
    try:
        response = requests.get(API_URL)
        if response.status_code==200:
            joke_data = response.json()
            context=dict(joke_data)
            return render (request, 'joke_app/index.html',{'joke_data':joke_data})
        else:
            error_message =f"ERROR: {response.status_code}-{response.text}"
            
            return render (request, 'joke_app/index.html',{'error_message':error_message})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message,
        }
        return render(request, 'jokeapp/error.html', context)