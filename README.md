# SmartShuffle
SmartShuffle seeks to supplement the existing Spotify shuffling algorithm in order to correct for users reporting that playlists with a large amount of songs play only a subset/percentage of those songs. This project first implements Spotify's existing shuffling algorithm as closely as possible according to their description which can be found here: https://engineering.atspotify.com/2014/02/how-to-shuffle-songs/. 

Core Algorithm:
  - On top of implementing Spotify's shuffling algorithm, SmartShuffle tracks how often a song is played within a playlist in order to decide which songs are pushed 
  closer to the top of the queue.(1) This ensures songs that aren't getting played as much have a higher chance of being played in the future. This balancing seeks to 
  improve on the feeling of randomness when a playlist is shuffled (described in detail in the above article). SmartShuffle therefore maintains a somewhat uniform 
  distribution of the queued songs when viewed based on the the number of times they've been played in the playlist.

Project Specifications:
  - This project is a Flask application mainly written in Python and HTML with some JavaScript to handle HTTP requests.
  - This project uses SQLite in conjunction with SQLAlchemy for database/database mapping operations.
  - This project uses Bootstrap for streamlined, responsive front-end styling.
  - This project utilizes the Spotipy Python library to simplify requests to the Spotify Web API for the song search engine.

Website Features:
  - Create User account, Login, Logout, Forgot Password (reset link sent to email).
  - Create Playlists, Search for songs, Add songs to playlist, Shuffle songs within a playlist.

(1)The number of plays a song has within a playlist is recorded under the 'plays' field and is crucial to the implementation of the SmartShuffle algorithm.

The 'plays' field should follow two ideal rules.
  - This field should belong to the relationship between the song and the playlist.
  - A "play" for a song is valid and recorded only if the song is played continuously for at least 30 seconds.

  These rules exceed the current scope of the project and hence will be ignored in favor of a simpler implementation.

  Since we are not modeling songs in our database (only Users and Playlists) and mainly wish to visualize the shuffling algorithm, it is sufficient for this project's
  scope to have the field belong to individual songs inside a playlist. A "play" will also be recorded as soon as a song is played, not according to the rule above. The 'plays' value for a song exists only for the lifetime of the song in the playlist. Once a song is removed, that value is essentially reset to 0.
