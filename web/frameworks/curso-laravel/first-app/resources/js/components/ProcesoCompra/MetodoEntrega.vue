<template>
    <div>
        <form>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="tipo_envio" id="tipo_envio1" value="Delivery" @change="store.setMetodoEnvio($event)" checked>
                <label class="form-check-label" for="tipo_envio1">Delivery</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="tipo_envio" id="tipo_envio2" value="Pick up" @change="store.setMetodoEnvio($event)">
                <label class="form-check-label" for="tipo_envio2">Pick up</label>
            </div>
            <div class="mt-3" v-if="store.tipo_envio === 'Delivery'">
                <div class="mb-3">
                    <label for="direccion" class="form-label">Dirección</label>
                    <input type="text" class="form-control" id="direccion" name="direccion" placeholder="Calle 123" @change="store.setDireccion($event.target.value)">
                </div>
                <div class="mb-3">
                    <label for="codigo_postal" class="form-label">Código postal</label>
                    <input type="text" class="form-control" id="codigo_postal" name="codigo_postal" placeholder="4005" @change="store.setCodigoPostal($event.target.value)">
                </div>
                <div class="mb-3">
                    <label for="municipio" class="form-label">Municipio</label>
                    <input type="municipio" class="form-control" id="municipio" name="municipio" placeholder="Maracaibo" @change="store.setMunicipio($event.target.value)">
                </div>
                <div class="mb-3">
                    <label for="estado" class="form-label">Estado</label>
                    <input type="estado" class="form-control" id="estado" name="estado" placeholder="Zulia" @change="store.setEstado($event.target.value)">
                </div>
                <div class="mb-3">
                    <label for="pais" class="form-label">País</label>
                    <input type="text" class="form-control" id="pais" name="pais" placeholder="Venezuela" @change="store.setPais($event.target.value)">
                </div>
            </div>
        </form>
    </div>
</template>

<script setup>
    // Imports
    import { useProcesoCompraStore } from '../../stores/proceso_compra';

    // Store
    const store = useProcesoCompraStore();
</script>

<style scoped></style>