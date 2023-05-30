import json
import argparse
import time
trackData = []
playlistData1 = []
numNoPreview = 0
with open('playlistitems1.json', 'r') as openJSONFile:
    playlistData1 = json.load(openJSONFile)
time.sleep(5)
for i in playlistData1['items']:
    if i['track']['preview_url'] is None:
        numNoPreview += 1
    else:
        trackData.append(i['track']['name'])
        trackData.append(i['track']['uri'])
        artistNames=""
        artistURIs=""
        numArtists=0
        for artist in i['track']['artists']:
            if(numArtists != 0):
                artistNames += ","
                artistURIs += ","
            artistNames += artist['name']
            artistURIs += artist['uri']
            numArtists+=1
        trackData.append(artistNames)
        trackData.append(artistURIs)
        trackData.append(i['track']['album']['name'])
        trackData.append(i['track']['album']['images'][0]['url'])
        trackData.append(i['track']['preview_url'])
playlistData2 = []
with open('playlistitems2.json', 'r') as openJSONFile:
    playlistData2 = json.load(openJSONFile)
time.sleep(5)
for i in playlistData2['items']:
    if i['track']['preview_url'] is None:
        numNoPreview += 1
    else:
        trackData.append(i['track']['name'])
        trackData.append(i['track']['uri'])
        artistNames=""
        artistURIs=""
        numArtists=0
        for artist in i['track']['artists']:
            if(numArtists != 0):
                artistNames += ","
                artistURIs += ","
            artistNames += artist['name']
            artistURIs += artist['uri']
            numArtists+=1
        trackData.append(artistNames)
        trackData.append(artistURIs)
        trackData.append(i['track']['album']['name'])
        trackData.append(i['track']['album']['images'][0]['url'])
        trackData.append(i['track']['preview_url'])
playlistData3 = []
with open('playlistitems3.json', 'r') as openJSONFile:
    playlistData3 = json.load(openJSONFile)
time.sleep(5)
for i in playlistData3['items']:
    if i['track']['preview_url'] is None:
        numNoPreview += 1
    else:
        trackData.append(i['track']['name'])
        trackData.append(i['track']['uri'])
        artistNames=""
        artistURIs=""
        numArtists=0
        for artist in i['track']['artists']:
            if(numArtists != 0):
                artistNames += ","
                artistURIs += ","
            artistNames += artist['name']
            artistURIs += artist['uri']
            numArtists+=1
        trackData.append(artistNames)
        trackData.append(artistURIs)
        trackData.append(i['track']['album']['name'])
        trackData.append(i['track']['album']['images'][0]['url'])
        trackData.append(i['track']['preview_url'])
playlistData4 = []
with open('playlistitems4.json', 'r') as openJSONFile:
    playlistData4 = json.load(openJSONFile)
time.sleep(5)
for i in playlistData4['items']:
    if i['track']['preview_url'] is None:
        numNoPreview += 1
    else:
        trackData.append(i['track']['name'])
        trackData.append(i['track']['uri'])
        artistNames=""
        artistURIs=""
        numArtists=0
        for artist in i['track']['artists']:
            if(numArtists != 0):
                artistNames += ","
                artistURIs += ","
            artistNames += artist['name']
            artistURIs += artist['uri']
            numArtists+=1
        trackData.append(artistNames)
        trackData.append(artistURIs)
        trackData.append(i['track']['album']['name'])
        trackData.append(i['track']['album']['images'][0]['url'])
        trackData.append(i['track']['preview_url'])
playlistData5 = []
with open('playlistitems5.json', 'r') as openJSONFile:
    playlistData5 = json.load(openJSONFile)
time.sleep(5)
for i in playlistData5['items']:
    if i['track']['preview_url'] is None:
        numNoPreview += 1
    else:
        trackData.append(i['track']['name'])
        trackData.append(i['track']['uri'])
        artistNames=""
        artistURIs=""
        numArtists=0
        for artist in i['track']['artists']:
            if(numArtists != 0):
                artistNames += ","
                artistURIs += ","
            artistNames += artist['name']
            artistURIs += artist['uri']
            numArtists+=1
        trackData.append(artistNames)
        trackData.append(artistURIs)
        trackData.append(i['track']['album']['name'])
        trackData.append(i['track']['album']['images'][0]['url'])
        trackData.append(i['track']['preview_url'])
playlistData6 = []
with open('playlistitems6.json', 'r') as openJSONFile:
    playlistData6 = json.load(openJSONFile)
time.sleep(5)
for i in playlistData6['items']:
    if i['track']['preview_url'] is None:
        numNoPreview += 1
    else:
        trackData.append(i['track']['name'])
        trackData.append(i['track']['uri'])
        artistNames=""
        artistURIs=""
        numArtists=0
        for artist in i['track']['artists']:
            if(numArtists != 0):
                artistNames += ","
                artistURIs += ","
            artistNames += artist['name']
            artistURIs += artist['uri']
            numArtists+=1
        trackData.append(artistNames)
        trackData.append(artistURIs)
        trackData.append(i['track']['album']['name'])
        trackData.append(i['track']['album']['images'][0]['url'])
        trackData.append(i['track']['preview_url'])
playlistData7 = []
with open('playlistitems7.json', 'r') as openJSONFile:
    playlistData7 = json.load(openJSONFile)
time.sleep(5)
for i in playlistData7['items']:
    if i['track']['preview_url'] is None:
        numNoPreview += 1
    else:
        trackData.append(i['track']['name'])
        trackData.append(i['track']['uri'])
        artistNames=""
        artistURIs=""
        numArtists=0
        for artist in i['track']['artists']:
            if(numArtists != 0):
                artistNames += ","
                artistURIs += ","
            artistNames += artist['name']
            artistURIs += artist['uri']
            numArtists+=1
        trackData.append(artistNames)
        trackData.append(artistURIs)
        trackData.append(i['track']['album']['name'])
        trackData.append(i['track']['album']['images'][0]['url'])
        trackData.append(i['track']['preview_url'])
playlistData8 = []
with open('playlistitems8.json', 'r') as openJSONFile:
    playlistData8 = json.load(openJSONFile)
time.sleep(5)
for i in playlistData8['items']:
    if i['track']['preview_url'] is None:
        numNoPreview += 1
    else:
        trackData.append(i['track']['name'])
        trackData.append(i['track']['uri'])
        artistNames=""
        artistURIs=""
        numArtists=0
        for artist in i['track']['artists']:
            if(numArtists != 0):
                artistNames += ","
                artistURIs += ","
            artistNames += artist['name']
            artistURIs += artist['uri']
            numArtists+=1
        trackData.append(artistNames)
        trackData.append(artistURIs)
        trackData.append(i['track']['album']['name'])
        trackData.append(i['track']['album']['images'][0]['url'])
        trackData.append(i['track']['preview_url'])
with open('trackuris.json', 'w') as openJSONFile:
    json.dump(trackData, openJSONFile)
print(numNoPreview)
print(len(trackData))