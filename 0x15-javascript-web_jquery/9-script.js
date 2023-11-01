// fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello

$(document).ready(function (){
  $.ajax({
  type: 'GET',
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  dataType: 'json',
  success: function (greetings) {
    $('DIV#hello').text(greetings.hello);
  },
  error: function () {
    console.error('The translation of hello is not found');
  }
  });
});
