export default {
    getProductos() {
        this.products = JSON.parse(localStorage.getItem('products')) || [];
    },
    agregarAlCarrito(product, cantidad) {
        const indexExisteProducto = this.products.findIndex((item) => parseInt(item.id) === parseInt(product.id));

        // Si no existe el producto se agrega al carrito
        if(indexExisteProducto === -1) {
            this.products.push({
                id: product.id,
                nombre: product.nombre,
                precio: product.precio,
                cantidad: cantidad.value,
            });
        }
        else {
            // Caso contrario se incrementa la cantidad
            this.products[indexExisteProducto].cantidad += cantidad.value;
        }

        cantidad.value = 0;

        // Actualizar o crear el carrito en localStorage
        localStorage.setItem("products", JSON.stringify(this.products));
    },
    setCantidad(productId, cantidad) {
        // Buscar el index del producto
        const indexExisteProducto = this.products.findIndex((item) => parseInt(item.id) === parseInt(productId));

        // Si el producto existe, se edita la cantidad
        if(indexExisteProducto === -1) {
            return;
        }

        if(cantidad > 0) {
            this.products[indexExisteProducto].cantidad = cantidad;
        }
        else {
            this.products.splice(indexExisteProducto, 1);
        }

        // Actualizar o crear el carrito en localStorage
        localStorage.setItem("products", JSON.stringify(this.products));
    },
};