let hamburger = document.querySelector(".hamburger");
let menu = document.querySelector(".menu");

	hamburger.addEventListener("click", function(){
		menu.classList.toggle("active");
	})


var navBar = document.querySelector(".navbar"); // vyberte navigačný panel
var offset = 100; // nastavte hodnotu posunu, po ktorom sa zmení veľkosť
var lastScrollPos = 0;

window.addEventListener("scroll", function() { // pridajte event listener na posun stránky
  var currentScrollPos = window.pageYOffset; // zistite aktuálnu pozíciu posunu stránky
  if (currentScrollPos > lastScrollPos && currentScrollPos > offset) { // ak sme posunuli smerom nadol a sme dostatočne ďaleko od začiatku stránky
    navBar.classList.add("small"); // pridajte triedu pre menší navigačný panel
  } else { // ak sme posunuli smerom nahor alebo sme príliš blízko začiatku stránky
    navBar.classList.remove("small"); // odstráňte triedu pre menší navigačný panel
  }
  lastScrollPos = currentScrollPos; // uložte aktuálnu pozíciu posunu ako poslednú
});