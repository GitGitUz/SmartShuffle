from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Playlist
from .shuffle import *
from . import db, spotify
import json
from operator import itemgetter

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def playlists():
    if request.method == 'POST':
        playlist_name = request.form.get('playlist_name')
        playlist_description = request.form.get('playlist_description')

        if len(playlist_name) < 1:
            flash('Name is too short!', category='error')
        else:
            new_playlist = Playlist(name=playlist_name, description = playlist_description, songs=json.loads('{"tracks":[]}'), count=0, user_id=current_user.id)
            db.session.add(new_playlist)
            db.session.commit()
            flash('Playlist created!', category='success')

    return render_template("playlists.html", user=current_user)

@views.route('/playlist/<pid>', methods=['GET', 'POST'])
@login_required
def songs(pid):
    playlist = Playlist.query.get(int(pid))
    if request.method == 'GET':
        if playlist:
            if playlist.user_id == current_user.id:
                return render_template("playlist_songs.html", user=current_user, playlist=playlist, searchResults=None)
        
        return render_template("playlist_songs.html", user=current_user, playlist=None)
    else:
        song_name = request.form.get('song_name')
        searchResults = spotify.search(song_name,10,0,"track")
        searchResults = searchResults['tracks']
        tracks = searchResults['items']
        songs= []
        for track in tracks:
            temp = {
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "album": track['album']['name'],
                "id": track['id'],
                "url": track['external_urls']['spotify']
            }
            songs.append(temp)
        
        return render_template("playlist_songs.html", user=current_user, playlist=playlist, searchResults=songs)

@views.route('/shuffle/<pid>', methods=['GET'])
@login_required
def shuffle(pid):
    playlist = Playlist.query.get(int(pid))

    if playlist:
        shuffled_songs = spotifyShuffle(playlist.songs['tracks'])
        return render_template("shuffled.html", user=current_user, shuffled_songs=shuffled_songs)
    return jsonify({})

@views.route('/delete-playlist', methods=['POST'])
def delete_playlist():
    playlist = json.loads(request.data)
    playlistID = playlist['playlistID']
    playlist = Playlist.query.get(playlistID)

    if playlist:
        if playlist.user_id == current_user.id:
            db.session.delete(playlist)
            db.session.commit()
    
    return jsonify({})

@views.route('/add-song', methods=['POST'])
def add_song():
    data = json.loads(request.data)
    song = data['song']
    pid = data['pid']

    playlist = Playlist.query.get(pid)

    if playlist:
        if playlist.user_id == current_user.id:
            playlist.songs['tracks'].append(song)
            playlist.count+=1
            db.session.commit()
    
    return jsonify({})

@views.route('/remove-song', methods=['POST'])
def remove_song():
    data = json.loads(request.data)
    song = data['song']
    pid = data['pid']

    playlist = Playlist.query.get(pid)

    if playlist:
        if playlist.user_id == current_user.id:
            playlist.songs['tracks'].remove(song)
            playlist.count-=1
            db.session.commit()

    return jsonify({})

@views.route('/edit-desc', methods=['POST'])
def change_desc():
    data = json.loads(request.data)
    desc = data['desc']
    pid = data['pid']

    playlist = Playlist.query.get(pid)

    if playlist:
        if playlist.user_id == current_user.id:
            playlist.description = desc
            db.session.commit()

    return jsonify({})
