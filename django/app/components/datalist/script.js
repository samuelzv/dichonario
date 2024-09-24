function setIdDataListComponent(e, field_name) {
  var author_name = document.getElementById(e.id).value;
  var list = e.getAttribute('list');
  var options = document.querySelectorAll('#' + list + ' option');

  document.getElementById(field_name).value = '';
  for (var i = 0; i < options.length; i++) {
    var option = options[i];

    if (option.innerText === author_name) {
      document.getElementById(field_name).value = option.getAttribute('data-id');
      break;
    }
  }
}

