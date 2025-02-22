$(document).ready(function() {
  // When "Open Payment Proof" button is clicked in the "Review Payment" modal
  $('#reviewPayment .btn-primary').on('click', function () {
    $('#reviewPayment').modal('hide');  // Close the "Review Payment" modal
    setTimeout(function() {
      $('#paymentPreview').modal('show');  // Open the "Proof of Payment"
    }, 200);
  });

  // When the "Close" button in the "Proof of Payment" modal is clicked
  $('.proof-payment').on('click', function () {
    $('#paymentPreview').modal('hide');  // Close the "Proof of Payment" modal
    setTimeout(function() {
      $('#reviewPayment').modal('show');  // Reopen the "Review Payment" modal after a small delay
    }, 200);
  });

  // Optional: If you want to handle "Close" in the "Review Payment" modal (if needed)
  // $('.payment-info').on('click', function () {
  //   $('#reviewPayment').modal('hide');  // Close the "Review Payment" modal
  // });
});
