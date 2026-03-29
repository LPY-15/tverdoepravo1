flatpickr(".flatpickr_calendar", {
    plugins: [customYearDropdownPlugin],
    dateFormat: "Y-m-d",
    position: 'above',
    disableMobile: true,
    locale: "ru",
    altInput: true,
    allowInput: true,
    altFormat: "d.m.Y",
});


function customYearDropdownPlugin (fp) {
    return {
    onReady() {

        const monthsContainer = fp.calendarContainer.querySelector('.flatpickr-months');

        const yearElements = monthsContainer.querySelectorAll('.cur-year, .arrowUp, .arrowDown');
        yearElements.forEach(el => el.style.display = 'none');

        const yearSelect = document.createElement('select');
        yearSelect.classList.add('flatpickr-custom-year-dropdown');

        for (let year = 1990; year <= 2030; year++) {
            const option = document.createElement('option');
            option.value = year;
            option.textContent = year;
            yearSelect.appendChild(option);
        }

        yearSelect.value = fp.currentYear;

        monthsContainer.appendChild(yearSelect);

        yearSelect.addEventListener('change', (e) => {
            fp.changeYear(parseInt(e.target.value, 10));
            fp.redraw();
        });

        fp.config.onYearChange.push(() => {
            yearSelect.value = fp.currentYear;
        });
    }
    };
};



const firstPage = document.getElementById('js-refusal-modal-1-page')
const secondPage = document.getElementById('js-refusal-modal-2-page')
const thirdPage = document.getElementById('js-refusal-modal-3-page')
const refusalModalCheckbox = document.getElementById('js-refusalModal-checkbox')

document.addEventListener("DOMContentLoaded", function () {

    document.getElementById('js-agreementModal-accept-button').addEventListener('click', () => refusalModalCheckbox.checked = true);
    document.getElementById('js-agreementModal-decline-button').addEventListener('click', () => refusalModalCheckbox.checked = false);

    document.getElementById('js-refusalModal-exit-button').addEventListener('click', function () {
        const refusalModal = document.getElementById('refusalModal');
        const modalInstance = bootstrap.Modal.getOrCreateInstance(refusalModal);
        modalInstance.hide();
        console.log(modalInstance);
    });

    document.getElementById('js-show-agreementModal-in-refusalModal').addEventListener('click', function(){
        const agreementModal = new bootstrap.Modal(document.getElementById('agreementModal'));
        agreementModal.show();
    });


    document.getElementById('js-refusal-modal-2-page-back-button').addEventListener('click', function(e) {
        e.preventDefault();
        firstPage.style.display = 'block'
        secondPage.style.display = 'none'
    });

    document.getElementById('js-refusal-modal-3-page-back-button').addEventListener('click', function(e) {
        e.preventDefault();
        secondPage.style.display = 'block'
        thirdPage.style.display = 'none'
    });


    const passportSeriesAndNumber = document.getElementsByClassName('passport_series_and_number');

    for (let i = 0; i < passportSeriesAndNumber.length; i++) {
        passportSeriesAndNumber[i].addEventListener('input', function (e) {
            let userInput = e.target.value.replace(/\D/g, '');
            if (userInput.length > 11) userInput = userInput.slice(0, 11); 

            let formattedString = '';
            
            if (userInput.length > 0) {
                formattedString = '' + userInput.substring(0, 4);
            }
            if (userInput.length > 4) {
                formattedString += ' ' + userInput.substring(4, 10);
            }

            e.target.value = formattedString;

            if (userInput.length < 10) {
                e.target.setCustomValidity('Должно быть 10 цифр');
            } else {
                e.target.setCustomValidity('');
            }
        });   
    }
});

$(document).ready(function() {

    const refusalModalSubmitUrl = $('#refusalModal').data('ajax-page-submit');

    $('#js-refusal-modal-1-page').on('submit', function (e) {

        e.preventDefault();
        
        const refusalFormName = $('#refusal_form_name').val()
        const refusalFormEmail = $('#refusal_form_email').val()
        const refusalFormPhone = $('#refusal_form_phone').val()

        $.ajax({
            type: 'POST',
            url: refusalModalSubmitUrl,
            data: {
                form_step: 'step1',
                refusal_form_name: refusalFormName,
                refusal_form_email: refusalFormEmail,
                refusal_form_phone: refusalFormPhone,
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            },
            success: function(response, data) {
                console.log('1 step completed')
                $('#js-refusal-modal-1-page').hide();
                $('#js-refusal-modal-2-page').show();
            },
        });
    });

    $('#js-refusal-modal-2-page').on('submit', function (e) {
        
        e.preventDefault();

        const passportSeriesAndNumber = $('#passport_series_and_number').val()
        const passportIssueOrg = $('#passport_issue_org').val()
        const passportIssueDate = $('#passport_issue_date').val()
        const declarantAddress = $('#declarant_address').val()

        $.ajax({
            type: 'POST',
            url: refusalModalSubmitUrl,
            data: {
                form_step: 'step2',
                passport_series_and_number: passportSeriesAndNumber,
                passport_issue_org: passportIssueOrg,
                passport_issue_date: passportIssueDate,
                declarant_address: declarantAddress,
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            },
            success: function(response, data) {
                console.log('2 step completed')
                $('#js-refusal-modal-2-page').hide();
                $('#js-refusal-modal-3-page').show();
            },
        });
    });
    $('#additional_creditor_page_open_button').on('click', function (e) {
        e.preventDefault();

        const creditoNameOrTaxIdentificationNumber = $('#creditor_name_or_tax_identification_number').val()
        const creditAgreementNumber = $('#credit_agreement_number').val()
        const creditorAddress = $('#creditor_address').val()
        const creditAgreementDate = $('#credit_agreement_date').val()

        $.ajax({
            type: 'POST',
            url: refusalModalSubmitUrl,
            data: {
                form_step: 'step3',
                creditor_name_or_tax_identification_number: creditoNameOrTaxIdentificationNumber,
                credit_agreement_number: creditAgreementNumber,
                creditor_address: creditorAddress,
                credit_agreement_date: creditAgreementDate,
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            },
            xhrFields: {
                withCredentials: true
            },
            crossDomain: false,
            success: function(response, data) {
                console.log('3 step completed')
                thirdPage.reset();
            },
        });
    });
});