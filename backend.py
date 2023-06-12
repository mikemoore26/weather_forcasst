import requests
API_KEY = "f5d17eb466784a402ff2ac57f3f5d3e0"

def get_data(location,days,option):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    res = requests.get(url)
    data = res.json()
    filter_data = data['list']
    nr_values = 8 * days
    filter_data = filter_data[:nr_values]


    return filter_data


if __name__ == "__main__":
    get_data("East New York",3,"Temperature")
