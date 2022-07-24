# SmartShuffle


[NUMBER OF PLAYS FOR A SONG]
  The number of plays a song has within a playlist is recorded under the 'num_plays' field and is crucial to the implementation of the SmartShuffle algorithm.

  The 'num_plays' field should follow two ideal rules.
    - This field should belong to the relationship between the song and the playlist.
    - A 'play' for a song is valid and recorded only if the song is played continuously for at least 30 seconds.

  These rules exceed the current scope of the project and hence will be ignored in favor of a simpler implementation.

  Since we are not modeling songs in our database (only Users and Playlists) and mainly wish to visualize the shuffling algorithm, it is sufficient for this project's
  scope to have the field belong to a song inside a playlist. A 'play' will also be recorded as soon as a song is played, not according to the rule above.

