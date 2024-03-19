// The js code in this file is for the edit button on blog comments

/* 
* credit: blog post comments code taken from I think therefore I blog.
* credit: https://github.com/Code-Institute-Solutions/blog/blob/main/12_views_part_3/05_edit_delete/static/js/comments.js#L21
* credit: https://github.com/Code-Institute-Solutions/blog/blob/main/12_views_part_3/05_edit_delete/static/js/comments.js#L45
*/

// constants for comment edit functionality
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const editModal = new bootstrap.Modal(document.getElementById("editModal"));
const resetButton = document.getElementById("reset-button-comments");

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

// add event listener to each edit button to show a modal
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    // trigger the modal to show
    editModal.show();
  });
}

/*
* The reset function does the following:
* clear the comment text area
* reset the submit button text
* reset the action attribute of the form to its original state
* close the edit modal if it's open
*/

// reset function
function reset() {
  commentText.value = '';
  submitButton.innerText = "Submit";
  commentForm.setAttribute("action", "");
  editModal.hide();
}

// add event listener to reset button reset comment form
resetButton.addEventListener("click", (e) => {
  // call reset function
  reset();
});