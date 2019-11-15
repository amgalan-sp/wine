import datetime

def get_winery_age():
	now = int(datetime.datetime.now().year)
	winery_found_year = 1919
	winery_age = now - winery_found_year
	return winery_age
	
if __name__ == '__main__':
    print(get_winery_age())
