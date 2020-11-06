$(document).ready(function(){
  $(".owl-carousel").owlCarousel({
    responsiveClass:true,
    responsive:{
    0:{
        items: 1,
        nav: false
    },
    640:{
        items:3,
        nav: false
    }}
  });
});


const $overlay = document.getElementById('overlay');
const $buttonMenu = document.getElementById('button_mobile_menu');
const $menu = document.getElementById('mobile_aside');
const $menuLinks = document.querySelectorAll('#mobile_aside .menu .menu-link');

$buttonMenu.addEventListener('click', function(eve) {
  eve.preventDefault();
  $overlay.style.display = 'block';
  $menu.classList.toggle('mobile_aside--hide')
})

$overlay.addEventListener('click', function(eve) {
  eve.preventDefault();
  closeMenu();
})

$menuLinks.forEach(elem => elem.addEventListener('click', function(eve) {
  closeMenu();
}))

function closeMenu() {
  $overlay.style.display = 'none';
  $menu.classList.toggle('mobile_aside--hide')
}