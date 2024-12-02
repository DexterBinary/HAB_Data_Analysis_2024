import csv

inputFile = '../data/processed/rawGPSData.txt'
outputFile = '../data/modified/GPSData.csv'

with open(inputFile, 'r') as inFile:
    lines = inFile.readlines()

data = []
headers = ['TIME', 'BAR ALT', 'MBS', 'AIRT', 'DRAD', 'LAT', 'LON', 'GPS ALT']
data.append(headers)

for line in lines:
    parts = line.split()
    if len(parts) < 8:
        continue

    time = parts[0]
    barAlt = parts[1]
    mbs = parts[2]
    airt = parts[3]
    drad = parts[4]
    lat = parts[5]
    lon = parts[6]
    gpsAlt = parts[7]
    
    lat = lat.replace('-', '.').replace('..', '-')
    lon = lon.replace('-', '.').replace('..', '-')
    
    data.append([time, barAlt, mbs, airt, drad, lat, lon, gpsAlt])

with open(outputFile, 'w', newline='') as outFile:
    writer = csv.writer(outFile)
    writer.writerows(data)

print(f"Data has been converted to CSV format and saved to {outputFile}")
