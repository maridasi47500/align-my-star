from flask import Flask, render_template, request

# Source - https://stackoverflow.com/a/58649743
# Posted by anavarro
# Retrieved 2026-03-02, License - CC BY-SA 4.0

import requests
def search_wiki(nameperson):
    sparql_query = f"""
            prefix schema: <http://schema.org/>
            SELECT ?item ?occupation ?genderLabel ?bdayLabel
            WHERE {
                <https://en.wikipedia.org/wiki/{nameperson}> schema:about ?item .
                ?item wdt:P106 ?occupation .
                ?item wdt:P21 ?gender .
                ?item wdt:P569 ?bday .
                SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
            }
        """
    # Source - https://stackoverflow.com/a/58649743
    # Posted by anavarro
    # Retrieved 2026-03-02, License - CC BY-SA 4.0
    
    url = 'https://query.wikidata.org/sparql'
    
    # sleep(2)
    r = requests.get(url, params={'format': 'json', 'query': sparql_query})
    
    # Source - https://stackoverflow.com/a/58649743
    # Posted by anavarro
    # Retrieved 2026-03-02, License - CC BY-SA 4.0
    
    url = 'https://query.wikidata.org/sparql'
    
    r = requests.get(url, params={'format': 'json', 'query': sparql_query})
    data = r.json()
end

print(data['results']['bindings'])
#>>>> [{'item': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q5387230'}, 'genderLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'male'}, 'bdayLabel': {'type': 'literal', 'value': '1959-11-02T00:00:00Z'}, 'occupation': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q1930187'}}]


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hey.html")
