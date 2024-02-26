const editButtons = document.getElementsByClassName("btn-edit-book");
const bookingText = document.getElementById("id_message");
const bookingForm = document.getElementById("bookingForm");
const submitButton = document.getElementById("submitButtonBook");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("booking_id");
    let bookingContent = document.getElementsByTagName("h5").innerText;
    bookingText.value = bookingContent;
    submitButton.innerText = "Update";
    bookingForm.setAttribute("action", `booking_edit/${bookingId}`);
  });
}
