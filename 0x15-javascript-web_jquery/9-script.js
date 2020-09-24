// script that takes the element header and changes its color to red

$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  $('DIV#hello').append(`${data.hello}`);
});
