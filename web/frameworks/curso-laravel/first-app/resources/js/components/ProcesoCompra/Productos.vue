<template>
    <div class="row">
        <div class="col-12 col-sm-9">
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
                        <td>
                            <input type="number" class="form-control" :value="product.cantidad" @change="store.setCantidad(product.id, $event.target.value)">
                        </td>
                        <td>${{ product.precio }}</td>
                        <td>${{ product.precio * product.cantidad }}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="col-12 col-sm-3">
            <Total />
        </div>
    </div>
</template>

<script setup>
    import { useCarritoStore } from '../../stores/cart';
    import Total from './Total.vue';

    // Store
    const store = useCarritoStore();
</script>

<style scoped></style>