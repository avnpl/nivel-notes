// Deprecated
// Doesn't work for some reason. Had to include in base.html as
// inline javascript
// Probably is not getting linked to base.html

function deleteNote(noteId){
    fetch("/delete-note",{
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
    console.log(noteId)
}