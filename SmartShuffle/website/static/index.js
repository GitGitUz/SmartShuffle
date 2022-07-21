function deletePlaylist(playlistID){
    fetch('/delete-playlist', {
        method: 'POST',
        body: JSON.stringify({playlistID: playlistID})
    }).then((_res) => {
        window.location.href ="/";
    });
}

function viewPlaylist(pid){
    fetch(`/playlist/${pid}`, {
        method: 'GET',
    }).then((_res) => {
        window.location.href = `/playlist/${pid}`
    });
}

function addSong(song, pid){
    fetch(`/add-song`, {
        method: 'POST',
        body: JSON.stringify({song: song, pid: pid})
    }).then((_res) => {
        window.location.href = `/playlist/${pid}`
    });
}

function removeSong(song, pid){
    fetch(`/remove-song`, {
        method: 'POST',
        body: JSON.stringify({song: song, pid: pid})
    }).then((_res) => {
        window.location.href = `/playlist/${pid}`
    });
}