from django.shortcuts import render

# Create your views here.
# qKok1dABf4vU1CRXaqozOw==b3iD6G5jsZPpaWuT
def Home(request):
        # use pip install requests
    import requests
    import json
    if request.method == 'POST': # checks if the incoming request is a POST request.
        query = request.POST['query'] # This line retrieves the value from the query field submitted in the POST request.
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query ,headers={'X-Api-Key': 'qKok1dABf4vU1CRXaqozOw==b3iD6G5jsZPpaWuT'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "Oops!! there an error"
            print(e)
        return render(request,'home.html',{'api':api})
    #The context dictionary ({'api':api}) is passed to the template. 
    # This dictionary contains the variable api which will hold either
    #  the parsed JSON data from the API or the error message in case of an exception.
    else:
        return render(request,'home.html',{'query':'Enter a valid query'})
