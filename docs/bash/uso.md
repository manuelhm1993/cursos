# Uso básico de bash

---

### Creación de una ssh-key
```bash
1. Crear la clave de clave ssh con un algoritmo específico y un comentario: 
ssh-keygen -t ed25519 -C "manuelhm1993@gmail.com"
2. Verificar la clave pública: # (la única que se comparte)
cat ~/.ssh/id_ed25519.pub
3. Copiar la .pub y configurarla dentro de el servicio de host y las claves autorizadas, luego entrar:
ssh -T git@github.com
```

### Crear multientornos divididos por directorios 
```bash
1. Crear los directorios por proyecto
mkdir -p ~/.ssh/github ~/.ssh/banahosting ~/.ssh/server ~/.ssh/pruebas
2. Mover las claves
mv ~/.ssh/id_ed25519* ~/.ssh/github/
3. Configurar permisos del config
touch ~/.ssh/config
chmod 600 ~/.ssh/config
4. Escribir el config
nano ~/.ssh/config
# --- GITHUB ---
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/github/id_ed25519

# --- BANAHOSTING (Plantilla para tu futuro VPS/Hosting) ---
Host banahosting
    HostName ip_o_dominio_del_servidor
    User tu_usuario_cpanel
    IdentityFile ~/.ssh/banahosting/llave_bana
    Port 22
```