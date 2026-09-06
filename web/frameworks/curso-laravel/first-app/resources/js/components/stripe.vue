<template>
  <div class="carrito-container">
    <!-- 1. El lienzo vacío donde Stripe inyectará el formulario -->
    <div id="payment-element"></div>
    
    <button @click="procesarPago" :disabled="!stripeListo" class="btn-pagar">
      Pagar Ahora
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { loadStripe } from '@stripe/stripe-js';

const stripeListo = ref(false);
let stripe;
let elements;

onMounted(async () => {
    // 2. Inicializar Stripe con tu Llave PÚBLICA (pk_test_...)
    stripe = await loadStripe('pk_test_TU_LLAVE_PUBLICA_AQUI');

    // Aquí deberías hacer la petición fetch/axios a tu backend para obtener el secret
    // const response = await axios.post('http://localhost:8000/api/finalizar-compra', datosCarrito);
    // const clientSecret = response.data.client_secret;
    
    // Usaremos el secret temporal que obtuviste en tu dd() para esta prueba
    const clientSecret = 'pi_3UCZS7Fq2uo14GOi0cEt4QYK_secret_N7uJVc2B3P8TxQQQdmPvEmvNN';

    // 3. Crear la instancia de Elements enlazada a este cobro específico
    elements = stripe.elements({ clientSecret });

    // 4. Generar el componente visual de pago y montarlo en el div
    const paymentElement = elements.create('payment');
    paymentElement.mount('#payment-element');
    
    stripeListo.value = true;
});

const procesarPago = async () => {
    // 5. Stripe toma el control, lee el iFrame y procesa el cobro
    const { error } = await stripe.confirmPayment({
        elements,
        confirmParams: {
            // A dónde redirigir al usuario si el banco exige autenticación adicional
            return_url: 'http://localhost:3000/compra-exitosa', 
        },
    });

    if (error) {
        console.error("Error en el pago:", error.message);
    }
};
</script>