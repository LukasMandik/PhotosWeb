let hamburger = document.querySelector(".hamburger");
let menu = document.querySelector(".menu");

	hamburger.addEventListener("click", function(){
		menu.classList.toggle("active");
	})


// var navBar = document.querySelector(".navbar"); // vyberte navigačný panel
// var offset = 100; // nastavte hodnotu posunu, po ktorom sa zmení veľkosť
// var lastScrollPos = 0;
//
// window.addEventListener("scroll", function() { // pridajte event listener na posun stránky
//   var currentScrollPos = window.pageYOffset; // zistite aktuálnu pozíciu posunu stránky
//   if (currentScrollPos > lastScrollPos && currentScrollPos > offset) { // ak sme posunuli smerom nadol a sme dostatočne ďaleko od začiatku stránky
//     navBar.classList.add("small"); // pridajte triedu pre menší navigačný panel
//   } else { // ak sme posunuli smerom nahor alebo sme príliš blízko začiatku stránky
//     navBar.classList.remove("small"); // odstráňte triedu pre menší navigačný panel
//   }
//   lastScrollPos = currentScrollPos; // uložte aktuálnu pozíciu posunu ako poslednú
// });



var navBar = document.querySelector(".main_navbar"); // vyberte navigačný panel
var offset = 70; // nastavte hodnotu posunu, po ktorom sa zmení veľkosť
var scrollPos = 0; // uložte aktuálnu pozíciu scrollovania

window.addEventListener("scroll", scrollHandler);
window.addEventListener("load", scrollHandler);

function scrollHandler() {
  var currentScrollPos = window.pageYOffset;

  if (currentScrollPos > scrollPos && currentScrollPos > offset) { // ak sme posunuli pod určitý bod
    navBar.classList.add("small"); // pridajte triedu pre menší navigačný panel
    navBar.style.transition = "all 0.5s ease-in-out"; // pridajte transition
  } else if (currentScrollPos < (scrollPos - 7)) { // ak sme posunuli nad určitý bod
    navBar.classList.remove("small"); // odstráňte triedu pre menší navigačný panel
    navBar.style.transition = "all 0.5s ease-in-out"; // pridajte transition
  }

  scrollPos = currentScrollPos; // uložte novú pozíciu scrollovania
}
