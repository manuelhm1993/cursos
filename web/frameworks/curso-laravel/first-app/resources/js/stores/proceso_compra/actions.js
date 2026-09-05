export default {
    // Componente 2
    setNombre(value) {
        this.nombre = value;
    },
    setApellido(value) {
        this.apellido = value;
    },
    setEmail(value) {
        this.email = value;
    },
    setTelefono(value) {
        this.telefono = value;
    },
    // Componente 3
    setMetodoEnvio(e) {
        if(e.target.checked) {
            this.tipo_envio = e.target.value;
        }
    },
    setDireccion(value) {
        this.direccion = value;
    },
    setCodigoPostal(value) {
        this.codigo_postal = value;
    },
    setPais(value) {
        this.pais = value;
    },
    setEstado(value) {
        this.estado = value;
    },
    setMunicipio(value) {
        this.municipio = value;
    },
};