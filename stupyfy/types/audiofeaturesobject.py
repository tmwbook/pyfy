class AudioFeaturesObject:
    def __init__(self, acousticness, analysis_url, danceability, duration_ms, energy,spotify_id, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time_signature, track_href, api_type, uri, valence):
        self.acousticness = acousticness
        self.analysis_url = analysis_url
        self.danceability = danceability
        self.duration_ms = duration_ms
        self.energy = energy
        self.id = spotify_id
        self.instrumentalness = instrumentalness
        self.key = key
        self.liveness = liveness
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.tempo = tempo
        self.time_signature = time_signature
        self.track_href = track_href
        self.type = api_type
        self.uri = uri
        self.valence = valence
