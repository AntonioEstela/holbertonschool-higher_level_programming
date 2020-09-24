// script that takes the element header and changes its color to red

$.get('https://swapi-api.hbtn.io/api/films/?format=json', data => {
  const films = data.results;

  for (const key in films) {
    $('UL#list_movies').append(`<li>${films[key].title}</li>`);
  }
});
