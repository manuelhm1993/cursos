<template>
    <h2>Productos</h2>
    
    <table class="table">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Cantidad</th>
                <th>Precio</th>
                <th>Subtotal</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="product in store.products">
                <td>{{ product.nombre }}</td>
                <td>${{ product.precio }}</td>
                <td>{{ product.cantidad }}</td>
                <td>${{ product.precio * product.cantidad }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script setup>
    import { useCarritoStore } from '../../stores/cart';

    // Store
    const store = useCarritoStore();
</script>

<style scoped></style>