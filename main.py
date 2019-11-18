
import env

import requests
import os
import csv



# https://www.alphavantage.co



# MSFT = Microsoft
SYMBOLE = "MSFT"

request_uri = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + SYMBOLE + "&interval=5min&outputsize=full&datatype=csv&apikey=" + env.API_KEY


if os.path.exists(env.DATA_FOLDER + SYMBOLE + ".csv"):
    print("We have the data !")

else:
    # We download the data
    request = requests.get(request_uri)

    if request.status_code == 200:
        # Decode the content
        content = request.content.decode('utf-8')

        # Read in csv format
        csv_format = csv.reader(content.splitlines(), delimiter=',')

        # Write in my data
        with open(env.DATA_FOLDER + SYMBOLE + ".csv", 'w') as output:
            writer = csv.writer(output, delimiter=',')
            writer.writerows(csv_format)