var editButtons = document.getElementsByClassName("btn-edit-book");
var bookingText = document.getElementsByTagName("h5");
var bookingForm = document.getElementById("bookingForm");
var submitButton = document.getElementById("submitButtonBook");

// empty the comment text after post

bookingText.value = "";

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("booking_id");
     let bookingContent = document.getElementsByTagName("h5").inner;
    bookingText.value = bookingContent;
    submitButton.innerText = "Update";
    bookingForm.setAttribute("action", `edit_booking/${bookingId}`);
  });
}
