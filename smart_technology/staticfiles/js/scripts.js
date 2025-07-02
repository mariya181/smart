document.addEventListener("DOMContentLoaded", function () {

    // === CARROUSEL BASQUE ===
    const images = document.querySelectorAll('.carousel img');
    let currentIndex = 0;

    if (images.length > 0) {
        setInterval(() => {
                images.forEach(img => img.classList.remove('visible'));
                currentIndex = (currentIndex + 1) % images.length;
                images[currentIndex].classList.add('visible');
            },
            300000); // Change image touts les 3 secondes
    }

    // === COMPUTERS ANIMAS ===
    const stats = document.querySelectorAll('.stat .number');

    if (stats.length > 0) {
        function animateCounter(el) {
            const target = parseInt(el.getAttribute('data-target'), 10);
            let count = 0;
            const increment = Math.ceil(target / 100);

            const updateCounter = () => {
                count += increment;
                if (count >= target) {
                    el.textContent = target;
                } else {
                    el.textContent = count;
                    requestAnimationFrame(updateCounter);
                }
            };

            updateCounter();
        }

        stats.forEach(stat => animateCounter(stat));
    }



});
document.addEventListener("DOMContentLoaded", function () {
    const burger = document.querySelector('.burger-menu');
    const navMenu = document.querySelector('.nav-menu');


});
function scrollCarousel(direction) {
  const track = document.getElementById("carouselTrack");
  const scrollAmount = 250; // Tu peux ajuster la vitesse ici
  track.scrollLeft += direction *scrollAmount;
}
function toggleMenu() {
    const navMenu = document.querySelector('.nav-menu');
    if (navMenu) {
        navMenu.classList.toggle('active');
    }
}




