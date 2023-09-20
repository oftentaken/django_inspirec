document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const menu = document.querySelector('.menu');

    mobileMenuToggle.addEventListener('click', function() {
        menu.classList.toggle('open');
    });
});
