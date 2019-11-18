import datetime

def get_winery_age():
    now_year = int(datetime.datetime.now().year)
    winery_foundation_year = 1919
    winery_age = now_year - winery_foundation_year
    return winery_age
    
if __name__ == '__main__':
    print(get_winery_age())
