function submitForm() {
  document.getElementById("search").value = document.getElementById("search_modal_field").value;
  var form = document.getElementById("quote_list_form");
  if (form) {
    form.submit();
  }
}

function clearAndSubmitForm() {
  document.getElementById("search").value = "";
  var form = document.getElementById("quote_list_form");
  if (form) {
    form.submit();
  }
}


