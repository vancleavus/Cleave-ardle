# Cleaveardle

Spotify took down my favorite daily song-guessing game, [Heardle](https://www.spotify.com/heardle/). I decided to re-make it as best as I could. I promise this was my best.

The idea of Heardle was that you'd get the first second of the song, then you'd try to guess the song. If you weren't successful, you'd get the first 2 seconds, then you could guess again. Then 4 seconds, then 7, then 11, then finally 16. If you had the correct artist, you would get a yellow X instead of a red one to know you're on the right path. You could also just not guess and instead skip to get more of the song.

Believe it or not, don't love doing READMEs for things that probably won't get looked at. 'Pologies. If you're actually interested in more details, email me at [kevinjvancleave@gmail.com](mailto:kevinjvancleave@gmail.com).

I also don't really know what pull requests/issues are or how they work so uh more 'pologies.

## Visit the site
[http://kevinjvancleave.com:8088/Cleave-ardle.html](http://kevinjvancleave.com:8088/Cleave-ardle.html)

## Some Details
-index.html is where it's mostly all at.

-The python scripts, .txt files, and .json files are all used to pick the to-be-guessed song. 

-The playlistitemsN.json files are copied [web api response data from getting the playlist tracks](https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks) from [a playlist of the most-played songs on Spotify](https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza). GetSpotifyPlaylistTracks.py was then run once to create trackuris.json (which is just a very slimmed down version of the same data).

-I have a crontab entry setup to run the SwitchOutCleaveardle_nightly.py nightly. That script pulls a random song from trackuris.json and creates the *.txt files.

-The php script is a helper to the javascript in index.html to load the song/artist/etc. data.

-I have a node server running which does the actual API calls when performing searches.

## Some things I could fix
I wrote this whole thing in like 8 hours and I don't code for a living. I'm just glad it works.

-The search functionality/guess inputs are clunky. But do they work? Sure.

-The search could really be searching over only possible answers like (I think?) it did in regular Heardle. I could instead have it search through the tracks that are in the source playlist. But that means I would either need to do an API call to get all the playlist items (which I would need to do a few each time because you can only get 100 tracks each API call and there's 700+ songs), or not do an API call and just have it search through trackuris.json or something (and this mostly started as a practice for APIs so I didn't want to abandon that).

-I tried to get a button in to copy the result emoji squares that you could text your friends, but putting stuff on the clipboard was somehow really difficult. I think it might be easier if I setup HTTPS for the domain name/my Raspberry Pi hosting the site...? Unknown. For now, just highlight it yourself the old-fashioned way.

-I guess I could also have used the [Heardle Rewind playlist](https://open.spotify.com/playlist/37i9dQZF1DX45XuBi1dgIM) which is a playlist of all the Heardle songs-of-the-day when it was still up. It is fewer songs, and some of them aren't as well known (which I know is the point), but I like when I know the song and can win. Sue me.

