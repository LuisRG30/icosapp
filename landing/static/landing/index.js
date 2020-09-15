//Enable Header Scroll
window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("header");

// Get the offset position of the navbar
var sticky = document.getElementById("three").offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    header.style.position = 'fixed';
    header.classList.add("appear");
    header.classList.remove("disappear");
  } else {
    header.classList.remove("appear");
    header.classList.add("disappear");
    header.addEventListener("animationend", () => {
        if (header.style.position == "fixed"){
            header.style.position = "absolute";
        } else{
            header.style.position = "fixed";
        }
    });
  }
}