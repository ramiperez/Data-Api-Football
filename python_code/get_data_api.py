from urllib.request import urlopen
import json

#Obtengo la key almacenada en un archivo plano
key = open("key.txt", "r").read().split('"')[1:2][0]

#Declaración de variables
prefix_url = 'https://apiv3.apifootball.com/?action=get_'
url_get_countries = prefix_url + 'countries&APIkey=' + key
url_get_leagues = prefix_url + 'leagues&country_id=6&APIkey=' + key
url_get_teams = prefix_url + 'teams&league_id=302&APIkey=' + key
url_get_standings = prefix_url + 'standings&league_id=302&APIkey=' + key

#Función para leer el contenido de las urls
def urls_(url):
    response = urlopen(url)
    response_json = json.loads(response.read())
    return response_json

#Función para obtener el país de cada equipo
def country_():
    country_json = urls_(url_get_countries)
    country=[]
    for data in country_json:
        country.append({
            "country_id": data['country_id'],
            "country_name":  data['country_name']
        })
    return country

#Función para obtener las competiciones que tiene cada país
def compe_():
    country_c = urls_(url_get_leagues)
    compe=[]
    for data in country_c:
        compe.append({
            "country_id": data['country_id'],
            "country_name": data['country_name'],
            "league_id": data['league_id'],
            "league_name": data['league_name'],
            "league_season": data['league_season']
        })
    return compe

#Función para obtener los equipos de cada país
def teams_():
    country_t = urls_(url_get_teams)
    team=[]
    for data in country_t:
        for player in data['players']: 
            for coach in data['coaches']:
                team.append({
                "team_id" : data['team_key'], 
                "team_name" : data['team_name'],
                "player_key": player['player_key'],
                "player_id": player['player_id'],
                "player_name": player['player_name'],
                "player_number": player['player_number'],
                "player_type": player['player_type'],
                "player_age": player['player_age'],
                "player_match_played": player['player_match_played'],
                "player_goals": player['player_goals'],
                "player_yellow_cards": player['player_yellow_cards'],
                "player_red_cards": player['player_red_cards'],
                "player_assists": player['player_assists'],
                "player_birthdate": player['player_birthdate'],
                "player_is_captain": player['player_is_captain'],
                "player_goals_conceded": player['player_goals_conceded'],
                "player_fouls_committed": player['player_fouls_committed'],
                "coach_name": coach['coach_name']
                })
    return team

#Función para estadísticas de cada equipo
def standing_():
    standing=[]
    country_s = urls_(url_get_standings)
    for data  in country_s:
        standing.append({
            "country_name": data['country_name'],
            "league_id": data['league_id'],
            "league_name": data['league_name'],
            "team_id": data['team_id'],
            "team_name": data['team_name'],
            "overall_promotion": data['overall_promotion'],
            "overall_league_position": data['overall_league_position'],
            "overall_league_W": data['overall_league_W'],
            "overall_league_D": data['overall_league_D'],
            "overall_league_L": data['overall_league_L'],
            "overall_league_GF": data['overall_league_GF'],
            "overall_league_GA": data['overall_league_GA'],
            "overall_league_PTS": data['overall_league_PTS'],
            "home_league_position": data['home_league_position']
        })
    return standing

# country_()
# compe_()
# teams_()
# standing_()