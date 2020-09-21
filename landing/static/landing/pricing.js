//Sticky header
window.onscroll = function() {scrollTo()};

var header = document.getElementById("pricingcomponents");
var sticky = header.offsetTop;

function scrollTo() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

//Select option
var possibleOptions = document.getElementsByClassName("possible");

var selectOption = function(event) {
  classes = event.srcElement.classList;
  toEvaluate = document.getElementsByClassName(classes);
  Array.from(toEvaluate).forEach(function(element){
    element.parentElement.parentElement.classList.remove("selectedop");
  })
  event.srcElement.parentElement.parentElement.classList.add("selectedop");

  calculateEstimate();
}

//Deselect all 




Array.from(possibleOptions).forEach(function(option) {
  option.addEventListener('click', selectOption);
});

//Calculate estimate monthly cost
var estimate = 0.00;
var selected = document.getElementsByClassName("selectedop");

var calculateEstimate = function() {
  estimate = 0.00
  Array.from(selected).forEach(function(selection) {
    estimate += parseInt(selection.getAttribute("value"));
  });
  document.getElementById("total").innerHTML = "$" + estimate;
}
