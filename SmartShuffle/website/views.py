from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Playlist
from . import db
import json

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
            new_playlist = Playlist(name=playlist_name, description = playlist_description, user_id=current_user.id)
            db.session.add(new_playlist)
            db.session.commit()
            flash('Playlist created!', category='success')

    return render_template("playlists.html", user=current_user)

@views.route('/playlist/<pid>/<pname>', methods=['GET'])
@login_required
def songs(pid, pname):
    playlist = Playlist.query.get(int(pid))

    if playlist:
        if playlist.user_id == current_user.id:
            return render_template("playlist_songs.html", user=current_user, playlist = playlist)

    return render_template("playlist_songs.html", user=current_user, playlist = None)

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
