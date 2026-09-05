import { createApp } from 'vue';
import { createPinia } from 'pinia';
import ShowProducts from './components/Products/ShowProducts.vue';

const selector = '#ver_producto';
const product = document.querySelector(selector);

const pinia = createPinia();

const app = createApp(ShowProducts, {
    id: parseInt(product.getAttribute('data-id')),
});

app.use(pinia);
app.mount(product);