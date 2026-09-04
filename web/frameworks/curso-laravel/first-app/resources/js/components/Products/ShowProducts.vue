<template>
    <div class="container mt-5 mb-5">
        <div class="row">
            <div class="col-12 col-sm-6">
                <figure>
                    <img class="img-fluid" src="data:image/jpeg;base64,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" alt="Imagen de prueba">
                </figure>
            </div>
            <div class="col-12 col-sm-6">
                <div class="row">
                    <div class="col-12">
                        <h1>{{ nombre }}</h1>
                    </div>

                    <div class="col-12">
                        <p>DESCRIPCIÓN DEL PRODUCTO</p>
                    </div>

                    <div class="col-12">
                        <h6><strong>STOCK:</strong> {{ stock }}</h6>
                    </div>

                    <div class="col-12">
                        <h6><strong>PRECIO:</strong> ${{ precio }}</h6>
                    </div>

                    <div class="col-12 mt-3">
                        <AgregarAlCarrito :id="props.id" :stock="stock" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { onMounted, ref } from 'vue';
    import axios from 'axios'; // Importación modular estéril

    import AgregarAlCarrito from '../Carrito/AgregarAlCarrito.vue';

    // Props
    const props = defineProps({
        id: {
            type: Number,
            default: 0,
        },
    });

    // Data
    const nombre   = ref("");
    const precio   = ref(0);
    const stock    = ref(0);

    // Eventos
    onMounted(async () => {
        try {
            // Pausa la ejecución hasta que tu Controlador de Laravel responda
            const response = await axios.get(`/api/products/${props.id}`);
            
            const product = response.data;

            /* Usando fetch
            // 1. Ejecución de la petición nativa
            const response = await fetch(`/api/products/${props.id}`);

            // 2. Fetch no rechaza promesas en errores 404/500, debes interceptarlos manualmente
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            // 3. Deserialización obligatoria (El paso que Axios hace automático)
            const product = await response.json();
            */

            nombre.value = product.nombre;
            precio.value = product.precio;
            stock.value  = product.stock;

            // Inspección táctica en la consola
            // console.log('Payload del servidor:', product);
        } catch (error) {
            // Intercepta errores 404 o 500 de la API
            console.error('Fallo en la comunicación HTTP:', error);
        }
    });
</script>

<style scoped>
</style>