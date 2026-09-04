<template>
    <div class="row align-items-center justify-content-between">
        <div class="col-12 col-sm-6">
            <input type="number" placeholder="Ingrese la cantidad" class="form-control" :max="props.product.stock" v-model="cantidad">
        </div>

        <div class="col-12 col-sm-6">
            <button class="btn btn-success" type="button" @click="agregarAlCarrito">Agregar al carrito</button>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';

    // Props
    const props = defineProps({
        product: {
            type: Object,
            default: () => ({}),
        }
    });

    // Data
    const cantidad = ref(0);

    // Métodos
    const agregarAlCarrito = () => {
        // Validar stock
        if(props.product.stock < cantidad.value) return;

        // Obtener el carrito si existe en local storage o crear un array vacío
        const products = JSON.parse(localStorage.getItem("products")) || [];

        const indexExisteProducto = products.findIndex((item) => parseInt(item.id) === parseInt(props.product.id));

        // Si no existe el producto se agrega al carrito
        if(indexExisteProducto === -1) {
            products.push({
                id: props.product.id,
                nombre: props.product.nombre,
                precio: props.product.precio,
                cantidad: cantidad.value,
            });
        }
        else {
            // Caso contrario se incrementa la cantidad
            products[indexExisteProducto].cantidad += cantidad.value;
        }

        cantidad.value = 0;

        // Actualizar o crear el carrito en localStorage
        localStorage.setItem("products", JSON.stringify(products));
    };
</script>

<style scoped>
</style>