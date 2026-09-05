<template>
    <div class="container my-3">
        <div class="row">
            <!-- Componentes de cada paso -->
            <Productos v-if="paso === 1" />
            <DatosCliente v-if="paso === 2" />
        </div>

        <div class="d-flex justify-content-between mt-3">
            <button type="button" class="btn btn-danger" @click="anteriorSiguiente" aria-btn="anterior" :disabled="paso === 1">Anterior</button>
            <button type="button" class="btn btn-primary" @click="anteriorSiguiente" aria-btn="siguiente">Siguiente</button>
        </div>
    </div>
</template>

<script setup>
    // Imports
    import { onMounted, ref } from 'vue';
    import { useCarritoStore } from '../../stores/cart';
    import Productos from './Productos.vue';
    import DatosCliente from './DatosCliente.vue';

    // Métodos
    const anteriorSiguiente = (e) => {
        const btn = e.target.getAttribute('aria-btn');

        if(btn == 'siguiente') {
            paso.value++;
        }
        else if(btn == 'anterior') {
            paso.value--;
        }
    };

    // Store
    const store = useCarritoStore();

    // Data
    const paso = ref(1);

    // Eventos
    onMounted(() => {
        store.getProductos();
    });
</script>

<style scoped></style>