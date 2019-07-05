from django.shortcuts import render
from .scrapers import main_live, live_update
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from .models import LiveTable
from .ssmgTransformers import * 
import runpy


def home_view(request):
	x = main_live()

	for i in x:
		new = LiveTable(customId=i[0],slug=i[1],
				event_id=i[2],formatedStartDate=i[3],
				homeTeam_name=i[4],awayTeam_name=i[5],
				current_home=i[6],current_away=i[7],
				period1_home=i[8],period1_away=i[9],
				period2_home=i[10],period2_away=i[11],
				period3_home=i[12],period3_away=i[13])
		try:
			new.save()
		except:
			pass
	qs = LiveTable.objects.all()
	context = {"eventList": qs }
	return render(request, 'sofascore/main.html', context)


def update_package(request):
	id_column = LiveTable.objects.values('event_id')
	id_list = [i['event_id'] for i in id_column]
	update_list = live_update(id_list)
	qs = LiveTable.objects.all()
	package = {}
	columns_to_update = ['current_home','current_away',
	        	'period1_home','period1_away','period2_home','period2_away',
	        	'period3_home','period3_away','odds_home','odds_away']

	for i in update_list:

		if i['status'] != 'inprogress':
			qs.get(event_id=i['event_id']).delete()
			package[i['event_id']] = 'remove'
			continue

		current_state = qs.filter(event_id=i['event_id']).values(*columns_to_update)
		check = {k:v for k,v in i.items() if k in columns_to_update}
		if current_state != check:
			match = qs.filter(event_id=i['event_id'])
			match.update(**check)
			package[i['event_id']] = check

	return JsonResponse(package)


	
def preds_package(request):
	qs = LiveTable.objects.all()
	x = runpy.run_path(settings.BASE_DIR+'\\sofascore\\predictors.py',run_name='__main__')
	package = {}
	print(x.keys())
	for i in qs:
		if (i.odds_away and i.odds_home and (i.period2_away != 0 or i.period2_home != 0) and not i.tennis_ssmg):
			arr=np.array([i.period1_home,i.period1_away,i.odds_home,i.odds_away])
			print(x['tennis_ssmg'].predict_proba(([arr],[1,2,3]))[0][1])
			i.tennis_ssmg = x['tennis_ssmg'].predict_proba(([arr],[1,2,3]))[0][1]
			i.save()
			package[i.event_id] = i.tennis_ssmg
	return JsonResponse(package)










