function goToUrl(url) {
  window.location = url;
}

function closeDropdown(event) {
  event.target.closest("details").removeAttribute("open");
}

function submitForm(val) {
  console.log(val.value);
}
