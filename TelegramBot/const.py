TOKEN = '6243198540:AAE9Xa9cUQijm6VdJxd7_oRoNSGhdw3cVaI'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 432328645

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data


WEATHER_TOKEN = '2db5106bade3097a81675107cf334e81'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
