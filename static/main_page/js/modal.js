const buttonElem = document.querySelector('.modal_button');
const modalElem = document.querySelector('.modal');


const openModal = () => {
    modalElem.style.visibility = 'visible';
    modalElem.style.opacity = 1;
};

buttonElem.addEventListener('click', openModal);    