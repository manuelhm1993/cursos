document.addEventListener('DOMContentLoaded', () => {
    const contenido = document.querySelector(".contenido");

    // 1. LA LOOKUP TABLE (El cerebro de las operaciones)
    // Mapeamos el atributo 'name' del input a una función anónima.
    const styleActions = {
        "width": (val) => contenido.style.width = `${val}px`,
        "height": (val) => contenido.style.height = `${val}px`,
        "padding": (val) => contenido.style.padding = `${val}px`,
        "margin": (val) => contenido.style.margin = `${val}px`,
        "border-width": (val) => contenido.style.borderWidth = `${val}px`,
        "border-radius": (val) => contenido.style.borderRadius = `${val}px`,
        "box-sizing": (val) => contenido.style.boxSizing = val // Nota: no lleva 'px'
    };

    // 2. DELEGACIÓN DE EVENTOS
    document.addEventListener("input", (e) => {
        const inputName = e.target.name;
        const inputValue = e.target.value;

        // Buscamos la función correspondiente en la tabla
        const action = styleActions[inputName];

        // Si la función existe (el input está mapeado), la ejecutamos de inmediato
        if (action) {
            action(inputValue);
        }
    });
});