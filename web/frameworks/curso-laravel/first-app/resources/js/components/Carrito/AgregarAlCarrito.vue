<template>
    <div class="row align-items-center justify-content-between">
        <div class="col-12 col-sm-6">
            <input type="number" placeholder="Ingrese la cantidad" class="form-control" min="0" :max="props.product.stock" v-model="cantidad">
        </div>

        <div class="col-12 col-sm-6">
            <button class="btn btn-success" type="button" @click="agregarAlCarrito">Agregar al carrito</button>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import { useCarritoStore } from '../../stores/cart';

    // Props
    const props = defineProps({
        product: {
            type: Object,
            default: () => ({}),
        }
    });

    // Store
    const store = useCarritoStore();

    // Data
    const cantidad = ref(0);

    // Métodos
    const agregarAlCarrito = () => {
        // Validar stock
        if(props.product.stock < cantidad.value) return;

        store.agregarAlCarrito(props.product, cantidad);
    };
</script>

<style scoped>
</style>