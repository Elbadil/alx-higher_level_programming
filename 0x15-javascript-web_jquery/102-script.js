// JavaScript script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
  // store the input object inside langInput
  const langInput = $('INPUT#language_code');
  $('INPUT#btn_translate').click(function () {
    const lang = langInput.val(); // Getting the value of the stored object
    $.ajax({
      type: 'GET',
      url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
      dataType: 'json',
      success: function (translation) {
        // decoding the value of hello
        const decodedText = $('<div/>').html(translation.hello).text();
        $('DIV#hello').text(decodedText);
      }
    });
  });
});
