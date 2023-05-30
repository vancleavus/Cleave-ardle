import json
import time
import random
track_artist_pairs = []
with open('/usr/local/Cleaveardle/trackuris.json', 'r') as openJSONFile:
    track_artist_pairs = json.load(openJSONFile)
n = random.randrange(int(len(track_artist_pairs)/7))
with open("/usr/local/Cleaveardle/trackname.txt", 'w') as openTextFile:
    openTextFile.write(track_artist_pairs[(n*7)])
with open("/usr/local/Cleaveardle/trackuri.txt", 'w') as openTextFile:
    openTextFile.write(track_artist_pairs[(n*7) + 1])
with open("/usr/local/Cleaveardle/artistname.txt", 'w') as openTextFile:
    openTextFile.write(track_artist_pairs[(n*7) + 2])
with open("/usr/local/Cleaveardle/artisturi.txt", 'w') as openTextFile:
    openTextFile.write(track_artist_pairs[(n*7) + 3])
with open("/usr/local/Cleaveardle/albumname.txt", 'w') as openTextFile:
    openTextFile.write(track_artist_pairs[(n*7) + 4])
with open("/usr/local/Cleaveardle/albumimg.txt", 'w') as openTextFile:
    openTextFile.write(track_artist_pairs[(n*7) + 5])
with open("/usr/local/Cleaveardle/previewurl.txt", 'w') as openTextFile:
    openTextFile.write(track_artist_pairs[(n*7) + 6])
# print(n)
# print(int(len(track_artist_pairs)))
# print(int(len(track_artist_pairs)/7))