from flask import Flask, render_template
import requests, datetime,time,random
app = Flask(__name__)
RANKING_HTML = 'ranking.html'

problems = ["easy1", "oii_pangramma", "ois_constellation", "ois_tractor", "ois_candies", "ois_dream", "ois_dristor2", "ois_monopoly", "ois_panama", "ois_patrol", "ois_sumtree", "ois_tournament2", "ois_vendingmachines"]
users = ["lorenzoferrari", "Mazza", "eliasol", "eric", "FraLu", "nicolas", "pety", "barchero", "Yeah", "hoom","0xA1E", "Alan_Bovo", "leo.perretta"]

#per evitare i tempi dell'api
data_dev = [{'User': 'lorenzo ferrari (lorenzoferrari)', 'easy1': random.randint(0,100), 'oii_pangramma': random.randint(0,100), 'ois_constellation': random.randint(0,100), 'ois_tractor': random.randint(0,100), 'ois_candies': random.randint(0,100), 'ois_dream': random.randint(0,100), 'ois_dristor2': random.randint(0,100), 'ois_monopoly': random.randint(0,100), 'ois_panama': random.randint(0,100), 'ois_patrol': random.randint(0,100), 'ois_sumtree': random.randint(0,100), 'ois_tournament2': random.randint(0,100), 'ois_vendingmachines': random.randint(0,100), 'Total': 1300}, {'User': 'Simone Mazzacano (Mazza)', 'easy1': random.randint(0,100), 'oii_pangramma': random.randint(0,100), 'ois_constellation': random.randint(0,100), 'ois_tractor': 64, 'ois_candies': random.randint(0,100), 'ois_dream': random.randint(0,100), 'ois_dristor2': 0, 'ois_monopoly': random.randint(0,100), 'ois_panama': 0, 'ois_patrol': random.randint(0,100), 'ois_sumtree': 0, 'ois_tournament2': random.randint(0,100), 'ois_vendingmachines': random.randint(0,100), 'Total': 964}, {'User': 'ERIC AQUILOTTI (eric)', 'easy1': random.randint(0,100), 'oii_pangramma': 0, 'ois_constellation': random.randint(0,100), 'ois_tractor': 61, 'ois_candies': random.randint(0,100), 'ois_dream': random.randint(0,100), 'ois_dristor2': 70, 'ois_monopoly': random.randint(0,100), 'ois_panama': 0, 'ois_patrol': 10, 'ois_sumtree': 0, 'ois_tournament2': random.randint(0,100), 'ois_vendingmachines': random.randint(0,100), 'Total': 841}, {'User': 'Elia Soldati (eliasol)', 'easy1': random.randint(0,100), 'oii_pangramma': random.randint(0,100), 'ois_constellation': random.randint(0,100), 'ois_tractor': 0, 'ois_candies': random.randint(0,100), 'ois_dream': random.randint(0,100), 'ois_dristor2': 0, 'ois_monopoly': 0, 'ois_panama': 0, 'ois_patrol': 0, 'ois_sumtree': 0, 'ois_tournament2': 0, 'ois_vendingmachines': random.randint(0,100), 'Total': 600}, {'User': 'Edoardo Balistri (hoom)', 'easy1': random.randint(0,100), 'oii_pangramma': random.randint(0,100), 'ois_constellation': 0, 'ois_tractor': 0, 'ois_candies': random.randint(0,100), 'ois_dream': 70, 'ois_dristor2': 0, 'ois_monopoly': 0, 'ois_panama': 75, 'ois_patrol': 0, 'ois_sumtree': 0, 'ois_tournament2': 0, 'ois_vendingmachines': 0, 'Total': 445}, {'User': 'Alan Davide Bovo (Alan_Bovo)', 'easy1': random.randint(0,100), 'oii_pangramma': 0, 'ois_constellation': 0, 'ois_tractor': 0, 'ois_candies': random.randint(0,100), 'ois_dream': 35, 'ois_dristor2': 0, 'ois_monopoly': 0, 'ois_panama': 0, 'ois_patrol': 0, 'ois_sumtree': 0, 'ois_tournament2': random.randint(0,100), 'ois_vendingmachines': random.randint(0,100), 'Total': 435}, {'User': 'Leonardo Perretta (leo.perretta)', 'easy1': random.randint(0,100), 'oii_pangramma': 0, 'ois_constellation': 0, 'ois_tractor': 0, 'ois_candies': 0, 'ois_dream': 0, 'ois_dristor2': 0, 'ois_monopoly': 0, 'ois_panama': 0, 'ois_patrol': 0, 'ois_sumtree': 0, 'ois_tournament2': random.randint(0,100), 'ois_vendingmachines': random.randint(0,100), 'Total': 300}, {'User': 'Nicolas Benatti (nicolas)', 'easy1': random.randint(0,100), 'oii_pangramma': 0, 'ois_constellation': 0, 'ois_tractor': 0, 'ois_candies': 0, 'ois_dream': 0, 'ois_dristor2': 0, 'ois_monopoly': 0, 'ois_panama': 0, 'ois_patrol': 0, 'ois_sumtree': 0, 'ois_tournament2': 0, 'ois_vendingmachines': 0, 'Total': random.randint(0,100)}, {'User': 'Petichan Zeul (pety)', 'easy1': 0, 'oii_pangramma': 0, 'ois_constellation': 0, 'ois_tractor': 0, 'ois_candies': 0, 'ois_dream': 0, 'ois_dristor2': 0, 'ois_monopoly': 0, 'ois_panama': 0, 'ois_patrol': 0, 'ois_sumtree': random.randint(0,100), 'ois_tournament2': 0, 'ois_vendingmachines': 0, 'Total': random.randint(0,100)}, {'User': 'Francesco Barcherini (barchero)', 'easy1': random.randint(0,100), 'oii_pangramma': 0, 'ois_constellation': 0, 'ois_tractor': 0, 'ois_candies': 0, 'ois_dream': 0, 'ois_dristor2': 0, 'ois_monopoly': 0, 'ois_panama': 0, 'ois_patrol': 0, 'ois_sumtree': 0, 'ois_tournament2': 0, 'ois_vendingmachines': 0, 'Total': random.randint(0,100)}, {'User': "Thomas D'angelo (Yeah)", 'easy1': random.randint(0,100), 'oii_pangramma': 0, 'ois_constellation': 0, 'ois_tractor': 0, 'ois_candies': 0, 'ois_dream': 0, 'ois_dristor2': 0, 'ois_monopoly': 0, 'ois_panama': 0, 'ois_patrol': 0, 'ois_sumtree': 0, 'ois_tournament2': 0, 'ois_vendingmachines': 0, 'Total': random.randint(0,100)}, {'User': 'Bob Jhonny (0xA1E)', 'easy1': 0, 'oii_pangramma': 0, 'ois_constellation': 0, 'ois_tractor': 0, 'ois_candies': 0, 'ois_dream': 0, 'ois_dristor2': 0, 'ois_monopoly': 0, 'ois_panama': random.randint(0,100), 'ois_patrol': 0, 'ois_sumtree': 0, 'ois_tournament2': 0, 'ois_vendingmachines': 0, 'Total': random.randint(0,100)}]

def load_data_user(username: str):
    json_data = {
        'action': 'get',
        'username': username,
    }
    user_api_url = 'https://training.olinfo.it/api/user'
    response = requests.post(user_api_url, json=json_data)
    if not response.json()['success']:
        return None
    first_name = response.json()['first_name']
    last_name = response.json()['last_name']
    scores = response.json()['scores']

    row = {"User":first_name + ' ' + last_name + ' (' + username + ')'}
    for problem in problems:
        row[problem] = 0

    sum = 0
    for problem in scores:
        if problem['name'] in problems:
            row[problem['name']] = problem['score']
            sum += problem['score']
    row['Total'] = sum
    return row

#0 ottimizzazione nel caricarla, richiedo anche i full score
def load_data():
    data = []
    for user in users:
        data_user = load_data_user(user)
        if data_user != None:
            data.append(data_user)
        else:
            print("UTENTE NON TROVATO", user)

    data.sort(key=lambda x: x['Total'], reverse=True)
    return data

@app.route('/')
def scoreboard():
    start_time = time.time()
    data = load_data()
    time_elapsed = round(time.time() - start_time, 2)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template(RANKING_HTML, data=data, problems=problems,current_time=current_time,time_elapsed=time_elapsed)

'''
@app.route('/dev')
def scoreboard_dev():
    start_time = time.time()
    data = data_dev 
    data.sort(key=lambda x: x['Total'], reverse=True)
    time_elapsed = round(time.time() - start_time, 2)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template(RANKING_HTML, data=data, problems=problems,current_time=current_time,time_elapsed=time_elapsed)
'''
if __name__ == '__main__':
    app.run(debug=True)
