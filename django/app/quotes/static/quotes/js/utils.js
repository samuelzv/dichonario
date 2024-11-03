function goToUrl(url) {
  window.location = url;
}

function closeDropdown(event) {
  event.target.closest("details").removeAttribute("open");
}

function submitForm(val) {
  console.log(val.value);
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
