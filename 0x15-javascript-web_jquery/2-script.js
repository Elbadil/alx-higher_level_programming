// updates the text color of the <header> element to red when
// when the user clicks on the tag #red_header

$(document).ready(function () {
  $('DIV#red_header').click(function () {
    const header = $('header');
    if (header.length > 0) {
      header.css('color', '#FF0000');
    } else {
      console.error('Header element not found');
    }
  });
});
