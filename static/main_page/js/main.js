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
    


    /* navbar end */



    /* contactModal start */



    document.getElementById('js-contactModal-exit-button').addEventListener('click', function () {
        contactModal = document.getElementById('contactModal');
        modalInstance = bootstrap.Modal.getOrCreateInstance(contactModal);
        modalInstance.hide();
    });

    document.getElementById('js-show-agreementModal-in-contactModal').addEventListener('click', function(){
        agreementModal = new bootstrap.Modal(document.getElementById('agreementModal'));
        agreementModal.show();
    });




    /* contactModal end */



    contactsCheckbox = document.getElementById('js-contacts-checkbox')
    contactModalCheckbox = document.getElementById('js-contactModal-checkbox')

    document.getElementById('js-agreementModal-accept-button').addEventListener('click', function () {
        contactsCheckbox.checked = true;
        contactModalCheckbox.checked = true;
    });

    document.getElementById('js-agreementModal-decline-button').addEventListener('click', function () {
        contactsCheckbox.checked = false;
        contactModalCheckbox.checked = false;
    });



    /* agreement modal start */



    agreementModalFooterScrolledDown = document.getElementById('js-footer-scrolled-down')
    agreementModalFooterNotScrolledDown = document.getElementById('js-footer-not-scrolled-down')
    agreementModalEnd = document.getElementById('js-agreementModal-end')

    observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Element is on screen
                agreementModalFooterScrolledDown.style.display = 'block';
                agreementModalFooterNotScrolledDown.style.display = 'none';
            } else {
                // Element is off screen
                agreementModalFooterScrolledDown.style.display = 'none';
                agreementModalFooterNotScrolledDown.style.display = 'block';
            }
        });
    }, {
        threshold: 0.5
    });

    observer.observe(agreementModalEnd);

    document.getElementById('js-agreementModal-exit-btn').addEventListener('click', function () {
        const agreementModal = document.getElementById('agreementModal');
        const modalInstance = bootstrap.Modal.getOrCreateInstance(agreementModal);
        modalInstance.hide();
    });

    document.getElementById('js-agreementModal-link').addEventListener('click', function (e) {
        e.preventDefault();
        agreementModalEnd.scrollIntoView({behavior: 'smooth'});
    });



    /* agreement modal end */



    // alert after data submission

    function hideDiv() { 
        const targetDiv = document.getElementById('success-alert');
        setTimeout(() => { 
            targetDiv.style.display = 'none'; 
        }, 7500); 
    } 
    hideDiv()

    // phone-form validation


    const phoneForms = document.getElementsByClassName('phone-form');

    for (let i = 0; i < phoneForms.length; i++) {
        phoneForms[i].addEventListener('click', handlePhoneInput);
        phoneForms[i].addEventListener('input', handlePhoneInput);
        phoneForms[i].addEventListener('keydown', handlePhoneInput);
    }

    function handlePhoneInput(e) {
        const phoneInput = e.target;
        const cursorPosition = phoneInput.selectionStart;
        const rawValue = phoneInput.value;

        const formattedValue = formatPhoneNumber(rawValue);
        phoneInput.value = formattedValue;

        if (e.key === 'Backspace' || e.key === 'Delete') {
            setTimeout(() => {
                phoneInput.setSelectionRange(cursorPosition - 1, cursorPosition - 1);
            }, 0);
        }
        
        const userDigits = rawValue.replace(/\D/g, '').slice(0, 11);
        phoneInput.setCustomValidity(userDigits.length < 11 ? 'Должно быть 11 цифр' : '');
    }

    function formatPhoneNumber(rawValue) {
        let userInput = rawValue.replace(/\D/g, '');
        if (userInput.length > 11) userInput = userInput.slice(0, 11);

        let formattedPhoneNumber = '';
        if (userInput.length > 0) formattedPhoneNumber = '+7';
        if (userInput.length > 1) formattedPhoneNumber += ' ' + userInput.substring(1, 4);
        if (userInput.length > 4) formattedPhoneNumber += ' ' + userInput.substring(4, 7);
        if (userInput.length > 7) formattedPhoneNumber += '-' + userInput.substring(7, 9);
        if (userInput.length > 9) formattedPhoneNumber += '-' + userInput.substring(9, 11);

        return formattedPhoneNumber;
    }

});
