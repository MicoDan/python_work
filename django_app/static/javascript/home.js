// Fade-in effect for sections
window.addEventListener('scroll', function() {
    let elements = document.querySelectorAll('.fade-in');
    let screenHeight = window.innerHeight;

    elements.forEach(function(element) {
        let elementPosition = element.getBoundingClientRect().top;

        if (elementPosition < screenHeight) {
            element.classList.add('fadeIn');
        }
    });
});

// Slide-in effect for sections
window.addEventListener('scroll', function() {
    let elements = document.querySelectorAll('.slide-in');
    let screenHeight = window.innerHeight;

    elements.forEach(function(element) {
        let elementPosition = element.getBoundingClientRect().top;

        if (elementPosition < screenHeight) {
            element.classList.add('slideIn');
        }
    });
});





