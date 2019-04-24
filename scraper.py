from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

my_url = 'https://www.airport-jfk.com/departures.php'


uClient = uReq(my_url)  # Download the page

page_html = uClient.read()  # Store HTML as variable

uClient.close()  # close client connection

page_soup = soup(page_html, "html.parser")

table = page_soup.find("div", {"class": "flights_scroll_nou"})
rows = table.findAll("div", {"id": "flight_detail"})


destinations = []
for i in range(len(rows)):
    results = str((rows[i].findAll('div', {"id": "fdest"})))
    lower_bound = results.find('<b>', 1)
    upper_bound = results.find('</b>', 1)
    destinations.append(results[lower_bound+3:upper_bound])



airline = []
for i in range(len(rows)):
    results = str((rows[i].findAll('div', {"id": "fair"})))
    lower_bound = results.find('>', 20)
    upper_bound = results.find('</a>', 1)
    airline.append(results[lower_bound + 1:upper_bound])



flight = []
for i in range(len(rows)):
    results = str((rows[i]).findAll('div', {"id": "fnum"}))
    lower_bound = results.find('>', 20)
    upper_bound = results.find('</a>', 1)
    flight.append(results[lower_bound + 1:upper_bound])



departure = []
for i in range(len(rows)):
    results = str((rows[i]).findAll('div', {"id": "fhour"}))
    lower_bound = results.find('>', 20)
    upper_bound = results.find('</a>', 1)
    departure.append(results[lower_bound + 1:upper_bound])


terminal = []
for i in range(len(rows)):
    results = str((rows[i]).findAll('div', {"id": "fterm"}))
    lower_bound = results.find('>', 15)
    upper_bound = results.find('<', 3)
    terminal.append((results[lower_bound + 1: upper_bound]))

#print(terminal)


status = []
for i in range(len(rows)):
    G = str((rows[i]).findAll('div', {"id": "fstatus_G"}))
    lower_bound = G.find('>', 25)
    upper_bound = G.find('</a>', 1)
    G_final = G[lower_bound + 1: upper_bound]

    GR = str((rows[i]).findAll('div', {"id": "fstatus_GR"}))
    lower_bound = GR.find('>', 25)
    upper_bound = GR.find('</a>', 1)
    GR_final = GR[lower_bound + 1: upper_bound]

    R = str((rows[i]).findAll('div', {"id": "fstatus_R"}))
    lower_bound = R.find('>', 25)
    upper_bound = R.find('</a>', 1)
    R_final = R[lower_bound + 1: upper_bound]

    O = str((rows[i]).findAll('div', {"id": "fstatus_O"}))
    lower_bound = R.find('>', 25)
    upper_bound = R.find('</a>', 1)
    O_final = O[lower_bound + 1: upper_bound]

    Y = str((rows[i]).findAll('div', {"id": "fstatus_Y"}))
    lower_bound = Y.find('>', 25)
    upper_bound = Y.find('</a>', 1)
    Y_final = Y[lower_bound + 1: upper_bound]

    if G_final != '[':
        results = str((rows[i]).findAll('div', {"id": "fstatus_G"}))
    elif GR_final != '[':
        results = str((rows[i]).findAll('div', {"id": "fstatus_GR"}))
    elif R_final != '[':
        results = str((rows[i]).findAll('div', {"id": "fstatus_R"}))
    elif O_final != '[':
        results = str((rows[i]).findAll('div', {"id": "fstatus_O"}))
    elif Y_final != '[':
        results = str((rows[i]).findAll('div', {"id": "fstatus_Y"}))

    lower_bound = results.find('>', 25)
    upper_bound = results.find('</a>', 1)
    status.append(results[lower_bound + 1: upper_bound])


# Add the curent day to the flight data:
import datetime
currentDT = datetime.datetime.now()
a = [currentDT.strftime("%Y/%m/%d")] * len(rows)
import pandas as pd

#Create dataframe
jfk_depart = pd.DataFrame(
    {"Destination": destinations,
     'Airline': airline,
     'Flight_Number': flight,
     'Departure_Time': departure,
     'Terminal': terminal,
     'Status': status,
     'Day': a
    })


