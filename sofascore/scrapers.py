import requests



def main_live():

	headers = {'Host': 'www.sofascore.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
	'Accept': '*/*',
	'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
	'Accept-Encoding': 'gzip',
	'Content-type': 'application/json',
	'Referer': 'https://www.sofascore.com/pl/tenis/livescore',
	'X-Requested-With': 'XMLHttpRequest',
	'Connection':'keep-alive',
	'TE': 'Trailers'}

	r = requests.get('https://www.sofascore.com/tennis/livescore/json',headers=headers)
	r.status_code
	x = r.json()
	live = []

	for i in x['sportItem']['tournaments']:
	    for j in i['events']:
	        live.append(j)
	        
	print(len(live))


	print(live[0]['customId'],
	live[0]['slug'],
	live[0]['id'],
	live[0]['formatedStartDate'],
	live[0]['homeTeam']['name'],
	live[0]['awayTeam']['name'],
	live[0]['homeScore']['current'],
	live[0]['awayScore']['current'],

	live[0]['homeScore']['period1'],
	live[0]['awayScore']['period1'],
	      
	live[0]['homeScore']['period2'] if ('period2' in live[0]['homeScore']) else 0,
	live[0]['awayScore']['period2'] if ('period2' in live[0]['homeScore']) else 0,

	live[0]['homeScore']['period3'] if ('period3' in live[0]['homeScore']) else 0,
	live[0]['awayScore']['period3'] if ('period3' in live[0]['homeScore']) else 0,
	)

	live_events = []

	for i in live:
	    live_events.append(list([i['customId'],
	    i['slug'],
	    i['id'],
	    i['formatedStartDate'],
	    i['homeTeam']['name'],
	    i['awayTeam']['name'],
	    i['homeScore']['current'],
	    i['awayScore']['current'],
	    i['homeScore']['period1'],
	    i['awayScore']['period1'],    
	    i['homeScore']['period2'] if ('period2' in i['homeScore']) else 0,
	    i['awayScore']['period2'] if ('period2' in i['homeScore']) else 0,
	    i['homeScore']['period3'] if ('period3' in i['homeScore']) else 0,
	    i['awayScore']['period3'] if ('period3' in i['homeScore']) else 0,]
	    ))

	return live_events


def live_update(live_events):
    headers = {'Host': 'www.sofascore.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept': '*/*',
    'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip',
    'Content-type': 'application/json',
    'Referer': 'https://www.sofascore.com/pl/tenis/livescore',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection':'keep-alive',
    'TE': 'Trailers'}

    update_list = []
    for i in live_events:
	    re = requests.get('https://www.sofascore.com/event/{}/matches/json'.format(i),
	    	headers=headers)
	    event_update = re.json()
	    status = event_update['h2h']['events']['tournaments'][0]['events'][0]['status']['type']
	    if status == 'inprogress':
	        try:
	            period = event_update['h2h']['events']['tournaments'][0]['events'][0]['lastPeriod']
	            dict_home = event_update['h2h']['events']['tournaments'][0]['events'][0]['homeScore']
	            dict_away = event_update['h2h']['events']['tournaments'][0]['events'][0]['awayScore']
	            current_home = dict_home['current']
	            current_away = dict_away['current']
	            period1_home = dict_home['period1']
	            period1_away = dict_away['period1']
	            period2_home = dict_home['period2'] if ('period2' in dict_home) else 0
	            period2_away = dict_away['period2'] if ('period2' in dict_away) else 0
	            period3_home = dict_home['period3'] if ('period3' in dict_home) else 0
	            period3_away = dict_away['period3'] if ('period3' in dict_away) else 0
	        except:
	            pass

	        re_odds = requests.get('https://api.sofascore.com/api/v1/event/{}/odds/1/all'.format(i),
	                              headers=headers)
	        try:
	            odds = re_odds.json()
	            odds_home = eval(odds['markets'][0]['choices'][0]['fractionalValue'])+1
	            odds_away = eval(odds['markets'][0]['choices'][1]['fractionalValue'])+1
	        except:
	            pass
	        print(re.status_code,
             period,
             current_home,
             current_away,
             period1_home,
             period1_away,
             period2_home,
             period2_away,
             period3_home,
             period3_away,
             '\n',
             re_odds.status_code,
             odds_home,
             odds_away)

	        
	        update_list.append({'event_id':i,
	        	'status':status,
	        	'period':period,
	        	'current_home':current_home,
	        	'current_away':current_away,
	        	'period1_home':period1_home,
	        	'period1_away':period1_away,
	        	'period2_home':period2_home,
	        	'period2_away':period2_away,
	        	'period3_home':period3_home,
	        	'period3_away':period3_away,
	        	'odds_home':odds_home,
	        	'odds_away':odds_away})
	    else:
	        print('----------',status,'---------')
	        update_list.append({'event_id':i,'status':status})

    print(len(update_list))

    return update_list