<template>
    <div>
        <form>
            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre</label>
                <input type="text" class="form-control" id="nombre" name="nombre" placeholder="John" @change="store.setNombre($event.target.value)">
            </div>
            <div class="mb-3">
                <label for="apellido" class="form-label">Apellido</label>
                <input type="text" class="form-control" id="apellido" name="apellido" placeholder="Doe" @change="store.setApellido($event.target.value)">
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" name="email" placeholder="youremail@example.com" @change="store.setEmail($event.target.value)">
            </div>
            <div class="mb-3">
                <label for="telefono" class="form-label">Teléfono</label>
                <input type="text" class="form-control" id="telefono" name="telefono" placeholder="0420-0000000" @change="store.setTelefono($event.target.value)">
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