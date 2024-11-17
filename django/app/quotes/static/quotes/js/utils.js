function goToUrl(url) {
  window.location = url;
}

function closeDropdown(event) {
  event.target.closest("details").removeAttribute("open");
}

function addTransitionClass(target) {
  var previous = document.querySelector('.sample-transition');
  if (previous) {
    previous.classList.remove('sample-transition');
  }
  var element = document.querySelector(target);
  if (element) {
    element.classList.add('sample-transition');
  }
}

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


