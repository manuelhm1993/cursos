import express from "express";
import mongoose from "mongoose";
import "dotenv/config"; // <--- INYECTA LAS VARIABLES DEL .env (NUEVO)

// AHORA LEE DIRECTAMENTE DESDE .env
const USER     = process.env.DB_USER;
const PASSWORD = process.env.DB_PASSWORD;
const DB_PORT  = process.env.DB_PORT;
const DOMAIN   = process.env.DOMAIN;
const DB_NAME  = process.env.DB_NAME;
const PORT     = process.env.APP_PORT || 3000; 

const Animal = mongoose.model('Animal', new mongoose.Schema({
    tipo:   String,
    estado: String,
}));

const app = express();

// Construcción perfecta de la URI
const url = `mongodb://${USER}:${PASSWORD}@${DOMAIN}:${DB_PORT}/${DB_NAME}?authSource=admin`;

mongoose.connect(url)
.then(() => console.log('Conexión a MongoDB exitosa.'))
.catch(err => console.error('Error conectando a Mongo:', err));

app.get('/', async (_req, res) => {
    console.log('Listando...');
    const animales = await Animal.find();
    return res.send(animales);
});

app.get('/crear', async (_req, res) => {
    console.log('Creando...');
    const result = await Animal.create({tipo: 'Chanchito', estado: 'Feliz'});
    return res.send(`Éxito. Registro creado: ${result}`);
});

app.delete('/borrar', async (_req, res) => {
    console.log('Eliminando...');
    const result = await Animal.deleteMany({});
    return res.send(`Éxito. Registros eliminados ${result.deletedCount}`);
});

app.listen(PORT, () => console.log(`Listening on port ${PORT}...`));