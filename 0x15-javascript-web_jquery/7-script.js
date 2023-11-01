// fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (character) {
      $('DIV#character').text(character.name);
    },
    error: function () {
      console.error('Character not found');
    }
  });
});
