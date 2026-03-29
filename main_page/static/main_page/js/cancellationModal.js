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



const cancellationModalСheckbox = document.getElementById('js-cancellationModal-checkbox')
document.getElementById('js-agreementModal-accept-button').addEventListener('click', () => cancellationModalСheckbox.checked = true);
document.getElementById('js-agreementModal-decline-button').addEventListener('click', () => cancellationModalСheckbox.checked = false);



document.getElementById('court_type').addEventListener('change', function (e) {
    e.target.classList.add('css-white-court-type');
});
    


document.getElementById('js-cancellationModal-exit-button').addEventListener('click', function () {
    const cancellationModal = document.getElementById('cancellationModal');
    const modalInstance = bootstrap.Modal.getOrCreateInstance(cancellationModal);
    modalInstance.hide();
});

document.getElementById('js-show-agreementModal-in-cancellationModal').addEventListener('click', function(){
    const agreementModal = new bootstrap.Modal(document.getElementById('agreementModal'));
    agreementModal.show();
});

const firstPage = document.getElementById('js-cancellation-modal-1-page')
const secondPage = document.getElementById('js-cancellation-modal-2-page')
const thirdPage = document.getElementById('js-cancellation-modal-3-page')

document.getElementById('js-cancellation-modal-2-page-back-button').addEventListener('click', function(e) {
    e.preventDefault();
    firstPage.style.display = 'block'
    secondPage.style.display = 'none'
});

document.getElementById('js-cancellation-modal-3-page-back-button').addEventListener('click', function(e) {
    e.preventDefault();
    secondPage.style.display = 'block'
    thirdPage.style.display = 'none'
});

$(document).ready(function() {

    const cancellationModalSubmitUrl = $('#cancellationModal').data('ajax-page-submit');

    $('#js-cancellation-modal-1-page').on('submit', function (e) {

        e.preventDefault();
        
        const debtorName = $('#debtor_name').val()
        const debtorAddress = $('#debtor_address').val()
        const debtorEmail = $('#debtor_email').val()
        const debtorPhone = $('#debtor_phone').val()


        $.ajax({
            type: 'POST',
            url: cancellationModalSubmitUrl,
            data: {
                form_step: 'step1',
                debtor_name: debtorName,
                debtor_address: debtorAddress,
                debtor_email: debtorEmail,
                debtor_phone: debtorPhone,
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            },
            success: function(response, data) {
                $('#js-cancellation-modal-1-page').hide();
                $('#js-cancellation-modal-2-page').show();
            },
        });
    });
    $('#js-cancellation-modal-2-page').on('submit', function (e) {
        
        e.preventDefault();

        const courtType = $('#court_type').val()
        const courtName = $('#court_name').val()
        const courtAddress = $('#court_address').val()
        const courtOrderNumber = $('#court_order_number').val()
        const orderIssuingDate = $('#order_issuing_date').val()
        const orderReceivingDate = $('#order_receiving_date').val()


        $.ajax({
            type: 'POST',
            url: cancellationModalSubmitUrl,
            data:{
                form_step: 'step2',
                court_type: courtType,
                court_name: courtName,
                court_address: courtAddress,
                court_order_number: courtOrderNumber,
                order_issuing_date: orderIssuingDate,
                order_receiving_date: orderReceivingDate,
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            },
            success: function(response, data) {
                $('#js-cancellation-modal-2-page').hide();
                $('#js-cancellation-modal-3-page').show();
            },
        }); 
    });
    
});