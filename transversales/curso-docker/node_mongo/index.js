import express from "express";
import mongoose from "mongoose";
import "dotenv/config"; // <--- INYECTA LAS VARIABLES DEL .env (NUEVO)

const Animal = mongoose.model('Animal', new mongoose.Schema({
    tipo:   String,
    estado: String,
}));

const app = express();

// AHORA LEE DIRECTAMENTE DESDE .env
mongoose.connect(process.env.MONGO_URI);

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

// APROVECHAMOS PARA LEER EL PUERTO TAMBIÉN
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Listening on port ${PORT}...`));