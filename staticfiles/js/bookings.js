document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-edit");
  const bookingText = document.getElementById("id_message");
  const bookingForm = document.getElementById("booking-form");
  const submitButton = document.getElementById("submit-buttonbook");

  const deleteModal = new bootstrap.Modal(
    document.getElementById("deleteModal")
  );
  const deleteButtons = document.querySelectorAll(".btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

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

  deleteButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      let bookingId = e.target.getAttribute("data-booking_id");
      deleteConfirm.href = `delete_booking/${bookingId}`;
      deleteModal.show();
    });
  });
});