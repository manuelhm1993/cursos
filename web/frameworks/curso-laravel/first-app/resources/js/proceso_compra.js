import { createApp } from 'vue';
import { createPinia } from 'pinia'

import ProcesoCompra from './components/ProcesoCompra/ProcesoCompra.vue';

const selector = '#proceso_compra';
const pinia = createPinia();
const app = createApp(ProcesoCompra);

app.use(pinia);
app.mount(selector);