// fetches and lists the title for all movies
// by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  dataType: 'json',
  success: function (movieList) {
    $.each(movieList.results, function (index, movie) {
      $('ul#list_movies').append(`<li>${movie.title}</li>`);
    });
  },
  error: function () {
    console.error('Failed to retrieve movie list');
  }
});
