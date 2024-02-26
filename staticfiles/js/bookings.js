document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-edit-book");
  const bookingText = document.getElementById("id_message");
  const bookingForm = document.getElementById("bookingForm");
  const submitButton = document.getElementById("submitButtonBook");

  editButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      let bookingId = e.target.getAttribute("data-booking_id");
      let bookingContent = document.getElementById(`booking${bookingId}`);
      bookingText.value = bookingContent.innerText;
      submitButton.innerText = "Update";
      bookingForm.setAttribute("action", `booking_edit/${bookingId}`);
    });
  });
});
