// function deleteNote(noteId) {
//   fetch("/delete-note", {
//     method: "POST",
//     body: JSON.stringify({ noteId: noteId }),
//   }).then((_res) => {
//     window.location.href = "/";
//   });
// }

function toggleDescription(tileId) {
  var tile = document.getElementById(tileId);
  var description = tile.querySelector('.description');

  if (description.style.maxHeight) {
      description.style.maxHeight = null;
  } else {
      description.style.maxHeight = description.scrollHeight + "px";
  }
}