import { createApp } from 'vue';
import ShowProducts from './components/Products/ShowProducts.vue';

const selector = '#ver_producto';
const product = document.querySelector(selector);

createApp(ShowProducts, {
    id: parseInt(product.getAttribute('data-id')),
}).mount(product);