/* navbar start */



document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll('.js-redirect-and-scroll').forEach(function(e) {
        e.addEventListener('click', () => {
            localStorage.setItem('navbarScrollTarget', e.dataset.scrollTarget);
            window.location.href = '/';
        });
    });
    
    const navbarScrollTargetId = localStorage.getItem('navbarScrollTarget')

    if (navbarScrollTargetId) {
        document.getElementById(navbarScrollTargetId).scrollIntoView();
        localStorage.removeItem('navbarScrollTarget');
    }

    document.querySelectorAll('.js-scroll').forEach(function(e) {
        e.addEventListener('click', function () {
            document.getElementById(e.dataset.scrollTarget).scrollIntoView();
        });
    });
    
});



/* navbar end */