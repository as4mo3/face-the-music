# emotion_labels = ['angry', 'disgusted', 'scared', 'happy', 'sad', 'surprised', 'neutral']

angry_params = {
    'min_acousticness': 0,
    'min_danceability': 0.2,
    'min_energy': 0.4,
    'min_instrumentalness': 0,
    'min_liveness': 0,
    'min_loudness': -60,
    'min_popularity': 0,
#     'min_speechiness': 0,
    'min_tempo': 80,
    'min_valence': 0,
    
    'max_acousticness': 0.8,
    'max_danceability': 0.65,
    'max_energy': 1,
    'max_instrumentalness': 1,
    'max_liveness': 0.4,
    'max_loudness': 0,
    'max_popularity': 100,
    'max_speechiness': 1,
#     'max_tempo': 120,
    'max_valence': 0.6,
    
    'target_acousticness': 0.3,
    'target_danceability': 0.4,
    'target_energy': 0.65,
    'target_instrumentalness': 0.5,
    'target_liveness': 0.5,
#     'target_loudness': -60,
#     'target_popularity': 0.5,
    'target_speechiness': 0.2,
    'target_tempo': 140,
    'target_valence': 0.2    
}

disgusted_params = {
    'min_acousticness': 0,
    'min_danceability': 0.2,
    'min_energy': 0.4,
    'min_instrumentalness': 0,
    'min_liveness': 0,
    'min_loudness': -60,
    'min_popularity': 0,
    'min_speechiness': 0,
    'min_tempo': 0,
    'min_valence': 0,
    
    'max_acousticness': 1,
    'max_danceability': 0.6,
    'max_energy': 0.7,
    'max_instrumentalness': 1,
    'max_liveness': 0.4,
    'max_loudness': 0,
#     'max_popularity': 100,
    'max_speechiness': 1,
    'max_tempo': 120,
    'max_valence': 0.5,
    
#     'target_acousticness': 0.5,
    'target_danceability': 0.4,
    'target_energy': 0.55,
    'target_instrumentalness': 0.5,
    'target_liveness': 0.5,
    'target_loudness': -60,
#     'target_popularity': 0.5,
    'target_speechiness': 0.5,
#     'target_tempo': 0.5,
    'target_valence': 0.2
}

scared_params = {
    'min_acousticness': 0,
    'min_danceability': 0,
    'min_energy': 0,
    'min_instrumentalness': 0,
    'min_liveness': 0,
    'min_loudness': -60,
    'min_popularity': 0,
    'min_speechiness': 0,
    'min_tempo': 0,
    'min_valence': 0,
    
    'max_acousticness': 1,
    'max_danceability': 0.4,
    'max_energy': 0.5,
    'max_instrumentalness': 1,
    'max_liveness': 0.4,
#     'max_loudness': 0,
#     'max_popularity': 100,
    'max_speechiness': 0.5,
    'max_tempo': 120,
    'max_valence': 0.6,
    
    'target_acousticness': 0.5,
    'target_danceability': 0.2,
    'target_energy': 0.3,
    'target_instrumentalness': 0.5,
    'target_liveness': 0.5,
    'target_loudness': -60,
#     'target_popularity': 0.5,
    'target_speechiness': 0.5,
#     'target_tempo': 0.5,
    'target_valence': 0.35    
}

happy_params = {
    'min_acousticness': 0,
    'min_danceability': 0.5,
    'min_energy': 0.5,
    'min_instrumentalness': 0,
    'min_liveness': 0,
    'min_loudness': -60,
#     'min_popularity': 0,
    'min_speechiness': 0,
    'min_tempo': 60,
    'min_valence': 0.4,
    
    'max_acousticness': 1,
    'max_danceability': 1,
    'max_energy': 1,
    'max_instrumentalness': 1,
    'max_liveness': 0.4,
    'max_loudness': 0,
    'max_popularity': 100,
    'max_speechiness': 1,
    'max_tempo': 120,
    'max_valence': 1,
    
#     'target_acousticness': 0.5,
    'target_danceability': 0.8,
    'target_energy': 0.8,
#     'target_instrumentalness': 0.5,
    'target_liveness': 0.3,
#     'target_loudness': -60,
#     'target_popularity': 0.5,
#     'target_speechiness': 0.5,
#     'target_tempo': 0.5,
    'target_valence': 0.8    
}

sad_params = {
    'min_acousticness': 0,
    'min_danceability': 0,
    'min_energy': 0,
    'min_instrumentalness': 0,
    'min_liveness': 0,
    'min_loudness': -60,
    'min_popularity': 0,
#     'min_speechiness': 0,
    'min_tempo': 0,
    'min_valence': 0,
    
    'max_acousticness': 1,
    'max_danceability': 0.4,
    'max_energy': 0.5,
    'max_instrumentalness': 1,
    'max_liveness': 0.4,
    'max_loudness': 0,
#     'max_popularity': 100,
    'max_speechiness': 1,
    'max_tempo': 120,
    'max_valence': 0.4,
    
    'target_acousticness': 0.6,
    'target_danceability': 0.2,
    'target_energy': 0.2,
    'target_instrumentalness': 0.8,
    'target_liveness': 0.3,
#     'target_loudness': -60,
#     'target_popularity': 0.5,
    'target_speechiness': 0.5,
    'target_tempo': 80,
    'target_valence': 0.2  
}

surprised_params = {
    'min_acousticness': 0.3,
    'min_danceability': 0.4,
    'min_energy': 0.3,
#     'min_instrumentalness': 0,
    'min_liveness': 0,
    'min_loudness': -60,
    'min_popularity': 0,
    'min_speechiness': 0,
    'min_tempo': 0,
    'min_valence': 0.2,
    
    'max_acousticness': 1,
    'max_danceability': 0.6,
    'max_energy': 0.8,
    'max_instrumentalness': 1,
    'max_liveness': 0.4,
    'max_loudness': 0,
    'max_popularity': 100,
    'max_speechiness': 1,
#     'max_tempo': 120,
    'max_valence': 1,
    
    'target_acousticness': 0.5,
    'target_danceability': 0.5,
    'target_energy': 0.5,
    'target_instrumentalness': 0.5,
    'target_liveness': 0.5,
    'target_loudness': -60,
#     'target_popularity': 0.5,
    'target_speechiness': 0.5,
    'target_tempo': 108,
    'target_valence': 0.5    
}

neutral_params = {
    'min_acousticness': 0,
    'min_danceability': 0,
    'min_energy': 0.3,
    'min_instrumentalness': 0,
    'min_liveness': 0,
    'min_loudness': -60,
    'min_popularity': 0,
    'min_speechiness': 0,
    'min_tempo': 0,
    'min_valence': 0.3,
    
    'max_acousticness': 0.8,
    'max_danceability': 0.5,
    'max_energy': 0.7,
    'max_instrumentalness': 1,
    'max_liveness': 0.2,
    'max_loudness': 0,
    'max_popularity': 100,
    'max_speechiness': 0.6,
    'max_tempo': 140,
    'max_valence': 0.7,
    
    'target_acousticness': 0.5,
    'target_danceability': 0.4,
    'target_energy': 0.5,
    'target_instrumentalness': 0.5,
    'target_liveness': 0.5,
    'target_loudness': -60,
#     'target_popularity': 0.5,
    'target_speechiness': 0.5,
#     'target_tempo': 0.5,
    'target_valence': 0.45    
}

# emotion_labels = ['angry', 'disgusted', 'scared', 'happy', 'sad', 'surprised', 'neutral']

emotion_params = {'Angry': angry_params, 'Disgusted': disgusted_params, 'Scared': scared_params, 'Happy': happy_params, \
                  'Sad': sad_params, 'Surprised': surprised_params, 'Neutral': neutral_params}