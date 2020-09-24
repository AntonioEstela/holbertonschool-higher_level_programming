// script that takes the element header and changes its color to red

$('DIV#toggle_header').on('click', () => {
  $('header').toggleClass('red green');
});
