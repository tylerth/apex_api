import requests, json

# driver method to actually make request and get data
def player_request(api_key, user=None, platform=None):

    if user == None:
        user = input("Enter the username: ")
    if platform == None:
        platform = input("Enter the platform (PC, X1, PS): ")

    player_data_url = "https://api.mozambiquehe.re/bridge?version=5&platform={}&player={}&auth={}".format(platform, user, api_key)

    try:
        player_data = requests.get(player_data_url).json()
    except:
        # print(requests.get(player_data_url).text)
        player_data = requests.get(player_data_url).text
        print(requests.get(player_data_url))
        print(player_data)

    return player_data


# returns player name, level, and rank data
def get_player_data(player_data):
    username = player_data['global']['name']
    platform = player_data['global']['platform']
    level = player_data['global']['level']
    br_ranked = get_br_rank_data(player_data)
    arenas_ranked = get_arenas_rank_data(player_data)

    body = {}
    body['username'] = username
    body['platform'] = platform
    body['level'] = level
    body['br_ranked'] = br_ranked
    body['arenas_ranked'] = arenas_ranked

    player_str = "{}\nLevel {}\n{}".format(username, level, br_ranked)
    # return player_str
    return body



def get_br_rank_data(player_data):
    rank_name = player_data['global']['rank']['rankName']
    rank_div = player_data['global']['rank']['rankDiv']
    rank_score = player_data['global']['rank']['rankScore']

    body = {}
    body['rank_name'] = rank_name
    body['division'] = rank_div
    body['rp'] = rank_score


    return body


def get_arenas_rank_data(player_data):
    rank_name = player_data['global']['arena']['rankName']
    rank_div = player_data['global']['arena']['rankDiv']
    rank_score = player_data['global']['arena']['rankScore']

    body = {}
    body['rank_name'] = rank_name
    body['division'] = rank_div
    body['rp'] = rank_score


    return body


def get_legend_data(legend, player_data):
    # legend_data = player_data['legends']['all'][legend]['data']
    # tracker_1_name, tracker_1_value = legend_data[0]['name'], legend_data[0]['value']
    # tracker_2_name, tracker_2_value = legend_data[1]['name'], legend_data[1]['value']
    # tracker_3_name, tracker_3_value = legend_data[2]['name'], legend_data[2]['value']

    # body = {}

    # body['legend'] = legend
    # body[tracker_1_name] = tracker_1_value
    # body[tracker_2_name] = tracker_2_value
    # body[tracker_3_name] = tracker_3_value

    # return body
    body = {}

    # body['legend'] = legend
    
    try:
        legend_data = player_data['legends']['all'][legend]['data']
        tracker_1_name, tracker_1_value = legend_data[0]['name'], legend_data[0]['value']
        tracker_2_name, tracker_2_value = legend_data[1]['name'], legend_data[1]['value']
        tracker_3_name, tracker_3_value = legend_data[2]['name'], legend_data[2]['value']

        body[tracker_1_name] = tracker_1_value
        body[tracker_2_name] = tracker_2_value
        body[tracker_3_name] = tracker_3_value

    except:
        body['data'] = 'Missing data for {}'.format(legend)
    
    return body




def get_all_legends_data(player_data):
    legends = ['Bloodhound', 'Gibraltar', 'Lifeline', 'Pathfinder', 'Wraith', 'Bangalore', 'Caustic', 'Mirage', 'Octane', 'Crypto', 'Wattson', 'Revenant', 'Loba', 'Rampart', 'Horizon', 'Fuse', 'Valkyrie', 'Seer']

    legend_stats = {}

    for legend in legends:
        try:
            # legend_stats.append(get_legend_data(legend, player_data))
            legend_stats[legend] = get_legend_data(legend, player_data)
        except:
            s = legend + " data not found"
            # legend_stats.append(s)
            legend_stats[legend] = s

    return legend_stats


# returns json body of request for map rotation
def map_request(api_key):
    map_rotation_url = "https://api.mozambiquehe.re/maprotation?version=2&auth={}".format(api_key)

    try:
        map_data = requests.get(map_rotation_url).json()
    except:
        print(requests.get(map_rotation_url))
        print(requests.get(map_rotation_url).text)

    return map_data

def get_br_map_rotation(map_data):
    curr_map = map_data['battle_royale']['current']['map']
    rem_mins = map_data['battle_royale']['current']['remainingMins']

    next_map = map_data['battle_royale']['next']['map']
    next_map_dur = map_data['battle_royale']['next']['DurationInMinutes']

    body = {}
    body['current_map'] = curr_map
    body['remaining_mins'] = rem_mins
    body['next_map'] = next_map
    body['duration'] = next_map_dur    

    return body

def get_arenas_map_rotation(map_data):
    curr_map = map_data['arenas']['current']['map']
    rem_mins = map_data['arenas']['current']['remainingMins']

    next_map = map_data['arenas']['next']['map']
    next_map_dur = map_data['arenas']['next']['DurationInMinutes']

    body = {}
    body['current_map'] = curr_map
    body['remaining_mins'] = rem_mins
    body['next_map'] = next_map
    body['duration'] = next_map_dur    

    return body


def get_br_ranked_map_rotation(map_data):
    curr_map = map_data['ranked']['current']['map']
    next_map = map_data['ranked']['next']['map']

    body = {}
    body['current_map'] = curr_map
    body['next_map'] = next_map
    body['info'] = "Ranked Battle Royale map rotation."   

    return body


def get_arenas_ranked_map_rotation(map_data):
    curr_map = map_data['arenasRanked']['current']['map']
    rem_mins = map_data['arenasRanked']['current']['remainingMins']

    next_map = map_data['arenasRanked']['next']['map']
    next_map_dur = map_data['arenasRanked']['next']['DurationInMinutes']

    body = {}
    body['current_map'] = curr_map
    body['remaining_mins'] = rem_mins
    body['next_map'] = next_map
    body['duration'] = next_map_dur
    body['info'] = "Ranked Arenas map rotation."
    return body


def get_all_map_rotation_data(map_data):

    maps = {}
    maps['br_unranked'] = get_br_map_rotation(map_data)
    maps['arenas_unranked'] = get_arenas_map_rotation(map_data)
    maps['arenas_ranked'] = get_arenas_ranked_map_rotation(map_data)
    maps['br_ranked'] = get_br_ranked_map_rotation(map_data)

    return maps



# user = "iCATxMythos"
# platform = "X1"
# api_key = "Wd6slHMRDXFFpSF7UQro"


# main call for player data
# player_data = player_request(user=user, platform=platform, api_key=api_key)
# pprint.pprint(get_player_data(player_data))
# print("\n")
# print(get_legend_data("Valkyrie", player_data))

# print(get_all_legends_data(data))

# main call for map data
# map_data = map_request(api_key)

# print(get_br_map_rotation(map_data))
# print(get_all_map_rotation_data(map_data))