function smoothScroll(id){
    document.querySelector(id).scrollIntoView({
        behavior: 'smooth'
    });
}

function paddedSmoothScroll(id) {
    document.querySelector(id).scrollIntoView({
        behavior: 'smooth'
    });
}