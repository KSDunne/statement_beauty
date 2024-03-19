// credit: blog post comments code taken from I think therefore I blog.
// credit: https://github.com/Code-Institute-Solutions/blog/blob/main/12_views_part_3/05_edit_delete/static/js/comments.js

// constants for comment edit functionality
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const editModal = new bootstrap.Modal(document.getElementById("editModal"));

// edit comment functionality here. it shows the targeted comment in the form box
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    let commentContent = document.getElementById(
      `comment${commentId}`
    ).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

// Add event listener to each edit button
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    // Trigger the modal to show
    editModal.show();
  });
}
