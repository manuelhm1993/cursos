document.addEventListener('DOMContentLoaded', () => {
    const modal = document.querySelector('.modal');

    document.addEventListener('click', (e) => {
        const elemento = e.target;

        if(elemento.classList.contains('modal__close-button')) {
            modal.style.display = 'none';
        }
    });
});