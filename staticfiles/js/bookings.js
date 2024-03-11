// JS script with event listeners for editing and deleting a makeover booking
// Note: A defensive design was built in to the delete funtion with a modal

// constants for edit event listener
const editButtons = document.querySelectorAll(".btn-edit");
const bookingText = document.getElementById("id_message");
const bookingForm = document.getElementById("booking-form");
const submitButton = document.getElementById("submit-buttonbook");

// constants for delete event listener
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.querySelectorAll(".btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// here is editing functionality which fills the message box with details to be edited
// this shows the user they are editing the intended booking
editButtons.forEach((button) => {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("data-booking_id");
    let bookingContent = document.getElementById(`booking${bookingId}`);
    let message = bookingContent.querySelector(".booking-message").innerText;
    bookingText.value = message;
    submitButton.innerText = "Update";
    bookingForm.setAttribute("action", `booking_edit/${bookingId}`);
  });
});

// here is the code which enables the deletion functionality
// this prompts the user to confirm they really want to delete a booking
deleteButtons.forEach((button) => {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("data-booking_id");
    deleteConfirm.href = `delete_booking/${bookingId}`;
    deleteModal.show();
  });
});
