import time
import turtle  # the turtle graphics library.
from datetime import datetime

import requests
import tzlocal


def movingISS(naptime=1):
    # set up turtle
    scr = turtle.Screen()
    scr.setup(720, 360)
    scr.setworldcoordinates(-180, -90, 180, 90)
    scr.bgpic('map2.gif')
    scr.register_shape('iss2.gif')
    iss = turtle.Turtle()
    iss.shape('iss2.gif')
    iss.setheading(90)
    iss.penup()
    coords = []
    for x in xrange(10):
        response = requests.get("http://api.open-notify.org/iss-now.json")
        pos = response.json().get('iss_position')
        lat = float(pos['latitude'])
        lon = float(pos['longitude'])
        print('Going to {0}, {1}'.format(lat, lon))
        iss.goto(lon, lat)
        time.sleep(naptime)
    turtle.mainloop()


def mapMyRun(coords=[42.375002, -71.109720]):
    scr = turtle.Screen()
    scr.setup(720, 360)
    scr.setworldcoordinates(-180, -90, 180, 90)
    scr.bgpic('map2.gif')
    scr.register_shape('iss2.gif')
    iss = turtle.Turtle()
    iss.shape('iss2.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(coords[1], coords[0])
    turtle.mainloop()


def overHome(coords=[42.375002, -71.109720]):
    url = "http://api.open-notify.org/iss-pass.json?lat={0}&lon={1}&alt=200&n=5".format(coords[0], coords[1])
    response = requests.get(url)
    r = response.json()
    mapMyRun(coords)
    location = r.get('request')

    for x in r.get('response'):
        time = x['risetime']

        unix_timestamp = float(time)
        local_timezone = tzlocal.get_localzone()  # get pytz timezone
        local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)

        print(local_time.strftime("%Y-%m-%d %H:%M:%S"))


def whosUpThere():
    r = requests.get("http://api.open-notify.org/astros.json")

    number = r.json().get('number')
    astronauts = r.json().get('people')
    astronauts = [str(p['name']) for p in astronauts]
    print("Currently, there are {0} astronauts on "
          "the International Space Station!\n{1}".format(number,
                                                         astronauts))


# movingISS(1)
# whosUpThere()
overHome()
