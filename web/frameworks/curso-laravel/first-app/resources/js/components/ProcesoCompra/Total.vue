<template>
    <div class="card">
        <h5 class="card-header">Total</h5>
        <div class="card-body">
            <h6>${{ total }}</h6>
        </div>
    </div>
</template>

<script setup>
    // Imports
    import { ref, watch } from 'vue';
    import { useCarritoStore } from '../../stores/cart';
    import { storeToRefs } from 'pinia';
    import axios from 'axios';

    // Store
    const store = useCarritoStore();

    // Data
    const total = ref(0);
    const { products } = storeToRefs(store);

    // Métodos
    watch(products, () => {
        axios.post('/api/carrito/calcular-total', {
            products: store.products,
        }).then((result) => {
            total.value = result.data.total;
        }).catch((err) => {
            console.error(err);
        });
    }, {
        deep: true, // Ver los objetos dentro del array
    }); 
</script>

<style scoped></style>