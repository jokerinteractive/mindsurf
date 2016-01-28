(function () {
  'use strict';
  
  var
    d = document,
    logo = d.querySelector('.logo'),
    nav = d.querySelector('.navigation');

  function show(e) {
    e.preventDefault();
    nav.classList.toggle('nav-active');
  }

  logo.addEventListener('click', show);
  logo.addEventListener('tap', show);

}());