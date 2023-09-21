from flask import Flask, render_template
import requests, datetime,time
app = Flask(__name__)
RANKING_HTML = 'ranking.html'

# Define the list of problems
problems = ["easy1", "oii_pangramma", "ois_constellation", "ois_tractor", "ois_candies", "ois_dream", "ois_dristor2", "ois_monopoly", "ois_panama", "ois_patrol", "ois_sumtree", "ois_tournament2", "ois_vendingmachines"]
#users = ["Matteo Arcari", "Serena Federici", "Matteo Disconsi", "Lorenzo Bianchi", "Vincenzo Sanzone", "Edi De Candido"]
users = ["lorenzoferrari", "Mazza", "eliasol", "eric", "nicolas", "pety", "barchero", "Yeah", "hoom","0xA1E", "Alan_Bovo", "leo.perretta"]

'''
data = [
    {"User": "Matteo Arcari", "circuito": 100, "fortezza": 100, "tubature": 100, "spesa":50,"Total": 300},
    {"User": "Serena Federici", "circuito": 100, "fortezza": 60, "tubature": 30, "spesa":50,"Total": 190},
    {"User": "Matteo Disconsi", "circuito": 100, "fortezza": 60, "tubature": 0, "spesa":50,"Total": 160},
    {"User": "Lorenzo Bianchi", "circuito": 100, "fortezza": 30, "tubature": 30, "spesa":50,"Total": 160},
    {"User": "Vincenzo Sanzone", "circuito": 100, "fortezza": 0, "tubature": 30, "spesa":30,"Total": 130},
    {"User": "Edi De Candido", "circuito": 31, "fortezza": 0, "tubature": 0, "spesa":50,"Total": 31},
]
'''

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

if __name__ == '__main__':
    app.run(debug=True)
