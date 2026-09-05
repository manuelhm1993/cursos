<template>
    <div class="row">
        <div class="col-12 mt-3">
            <div class="card">
                <h5 class="card-header">Productos</h5>
                <div class="card-body">
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
                            <tr v-for="product in storeCarrito.products">
                                <td>{{ product.nombre }}</td>
                                <td>{{ product.cantidad }}</td>
                                <td>${{ product.precio }}</td>
                                <td>${{ product.precio * product.cantidad }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="col-12 mt-3">
            <div class="card">
                <h5 class="card-header">Datos del cliente</h5>
                <div class="card-body">
                    <ul class="list-group">
                        <li class="list-group-item"><strong>Nombre:</strong> {{ storeProcesoCompra.nombre }}</li>
                        <li class="list-group-item"><strong>Apellido:</strong> {{ storeProcesoCompra.apellido }}</li>
                        <li class="list-group-item"><strong>Email:</strong> {{ storeProcesoCompra.email }}</li>
                        <li class="list-group-item"><strong>Teléfono:</strong> {{ storeProcesoCompra.telefono }}</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="col-12 mt-3">
            <div class="card">
                <h5 class="card-header">Método de entrega</h5>
                <div class="card-body">
                    <ul class="list-group">
                        <li class="list-group-item"><strong>Tipo:</strong> {{ storeProcesoCompra.tipo_envio }}</li>
                    </ul>
                    <div v-if="storeProcesoCompra.tipo_envio === 'Delivery'">
                        <ul class="list-group">
                            <li class="list-group-item"><strong>Dirección:</strong> {{ storeProcesoCompra.direccion }}</li>
                            <li class="list-group-item"><strong>Código postal:</strong> {{ storeProcesoCompra.codigo_postal }}</li>
                            <li class="list-group-item"><strong>Municipio:</strong> {{ storeProcesoCompra.municipio }}</li>
                            <li class="list-group-item"><strong>Estado:</strong> {{ storeProcesoCompra.estado }}</li>
                            <li class="list-group-item"><strong>País:</strong> {{ storeProcesoCompra.pais }}</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    // Imports
    import { useCarritoStore } from '../../stores/cart';
    import { useProcesoCompraStore } from '../../stores/proceso_compra';

    // Stores
    const storeCarrito = useCarritoStore();
    const storeProcesoCompra = useProcesoCompraStore();
</script>

<style scoped></style>