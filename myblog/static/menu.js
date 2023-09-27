document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const menu = document.querySelector('.menu');

    mobileMenuToggle.addEventListener('click', function() {
        menu.classList.toggle('open');
    });
});

//function adjustFooterPosition() {
//        const contentHeight = document.querySelector('.container').offsetHeight;
//        const viewportHeight = window.innerHeight;
//        const footer = document.querySelector('footer');
//
//        if (contentHeight < viewportHeight) {
//            footer.style.position = 'fixed';
//            footer.style.bottom = '0';
//        } else {
//            footer.style.position = 'static';
//        }
//    }
//
//    window.addEventListener('resize', adjustFooterPosition);
//    window.addEventListener('load', adjustFooterPosition);