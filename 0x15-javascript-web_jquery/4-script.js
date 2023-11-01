// toggles the class of the <header> element when the user
// clicks on the tag DIV#toggle_header

$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    const header = $('header');
    if (header.length > 0) {
      header.toggleClass('green red');
    } else {
      console.error('Header element not found');
    }
  });
});
