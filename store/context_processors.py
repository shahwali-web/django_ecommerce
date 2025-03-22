import datetime

def current_year(request):
    current_year_value = datetime.datetime.now().year
    return {"current_year_value_html": current_year_value}



