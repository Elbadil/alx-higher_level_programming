// adds the class red to the <header> element when the user
// clicks on the tag DIV#red_header

$(document).ready(function () {
  $('DIV#red_header').click(function () {
    const header = $('header');
    if (header.length > 0) {
      header.addClass('red');
    } else {
      console.error('Header element not found');
    }
  });
});
