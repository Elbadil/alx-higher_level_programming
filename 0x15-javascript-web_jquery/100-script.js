// updates the text color of the <header> element to red (#FF0000)
// script must be imported from the <head> tag, not at the end of the HTML

document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');
  header.style = 'color: #FF0000';
});
