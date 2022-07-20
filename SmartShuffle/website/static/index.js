function deletePlaylist(playlistID){
    fetch('/delete-playlist', {
        method: 'POST',
        body: JSON.stringify({playlistID: playlistID})
    }).then((_res) => {
        window.location.href ="/";
    });
}

function viewPlaylist(pid, pname){
    fetch(`/playlist/${pid}/${pname}`, {
        method: 'GET',
    }).then((_res) => {
        window.location.href = `/playlist/${pid}/${pname}`
    });
}