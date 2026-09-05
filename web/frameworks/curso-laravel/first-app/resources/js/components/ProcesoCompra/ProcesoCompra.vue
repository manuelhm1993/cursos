<template>
    <div class="container my-3">
        <div class="row">
            <!-- Componentes de cada paso -->
            <!--  -->
            <!-- v-if destruye el componente al ser false, v-show le da d-none -->
            <Productos v-show="paso === 1" /> 
            <DatosCliente v-show="paso === 2" />
            <MetodoEntrega v-show="paso === 3" />
            <ResumenCompra v-show="paso === 4" />
        </div>

        <div class="d-flex justify-content-between mt-3">
            <button type="button" class="btn btn-danger" @click="anteriorSiguiente" aria-btn="anterior" :disabled="paso === 1">Anterior</button>
            <button type="button" class="btn btn-primary" @click="anteriorSiguiente" aria-btn="siguiente" v-if="paso < 4">Siguiente</button>
            <button type="button" class="btn btn-success" @click="finalizarCompra" aria-btn="finalizarCompra" v-if="paso === 4">Finalizar compra</button>
        </div>
    </div>
</template>

<script setup>
    // Imports
    import { onMounted, ref } from 'vue';
    import { useCarritoStore } from '../../stores/cart';
    import Productos from './Productos.vue';
    import DatosCliente from './DatosCliente.vue';
    import MetodoEntrega from './MetodoEntrega.vue';
    import ResumenCompra from './ResumenCompra.vue';
    import { useProcesoCompraStore } from '../../stores/proceso_compra/index.js';
    import axios from 'axios';

    // Store
    const storeCarrito = useCarritoStore();
    const storeProcesoDeCompra = useProcesoCompraStore();

    // Data
    const paso = ref(1);

    // Métodos
    const finalizarCompra = (e) => {

        axios.post('/api/carrito/finalizar-compra', {
			products: storeCarrito.products,

			nombre: storeProcesoDeCompra.nombre,
			apellido: storeProcesoDeCompra.apellido,
			email: storeProcesoDeCompra.email,
			telefono: storeProcesoDeCompra.telefono,

			tipo_envio: storeProcesoDeCompra.tipo_envio,
			direccion: storeProcesoDeCompra.direccion,
			codigo_postal: storeProcesoDeCompra.codigo_postal,
			estado: storeProcesoDeCompra.estado,
			municipio: storeProcesoDeCompra.municipio,
			pais: storeProcesoDeCompra.pais,
		})
		.then((response) => {
			console.log("se finalizó la compra");
		}).catch((err) => {
			console.error(err);
		});
    };

    const anteriorSiguiente = (e) => {
        const btn = e.target.getAttribute('aria-btn');

        if(btn == 'siguiente') {
            paso.value++;
        }
        else if(btn == 'anterior') {
            paso.value--;
        }
    };

    // Eventos
    onMounted(() => {
        storeCarrito.getProductos();
    });
</script>

<style scoped></style>