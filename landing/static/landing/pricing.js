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

Array.from(possibleOptions).forEach(function(option) {
  option.addEventListener('click', selectOption);
});


//Clear selections

var clearSelections = function() {
  toEvaluate = document.getElementsByClassName("option");
  Array.from(toEvaluate).forEach(function(posibleSelection) {
    posibleSelection.classList.remove("selectedop");
  });
  calculateEstimate();
  document.getElementById("total").innerHTML = "$" + "0.00";
}

document.getElementById("reset").addEventListener('click', clearSelections);

//Calculate estimate monthly cost
var estimate = 0.00;
var selected = document.getElementsByClassName("selectedop");

var calculateEstimate = function() {
  estimate = 0.00
  Array.from(selected).forEach(function(selection) {
    estimate += parseInt(selection.getAttribute("value"));
  });
  var thousands = parseInt(estimate/1000);
  var units = estimate%1000;
  if (units == 0 && estimate != 0) {
    units = "000";
  }
  if (thousands == 0) {
    var total = units + ".00";
  } else {
    var total = thousands + "," + units + ".00";
  }
  var money = (thousands * 1000) + units;
  document.getElementById("total").innerHTML = "$" + total;
}
