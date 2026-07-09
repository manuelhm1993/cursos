# `<mh/>` cursos — Ruta de aprendizaje

Repositorio de seguimiento del plan de estudio del Ing. Manuel Henriquez / MHenriquez C.A.
Cada curso vive en su propia rama y aporta su carpeta al hacer merge a `master`,
permitiendo avanzar de forma independiente sin desordenar el árbol.

🏢 [MHenriquez C.A.](https://github.com/MHenriquezCA) · 👤 [manuelhm1993](https://github.com/manuelhm1993)

---

### Stack de aprendizaje 💻

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![VSCode](https://img.shields.io/badge/vscode-%23007ACC.svg?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![cPanel](https://img.shields.io/badge/cpanel-%23FF6C2C.svg?style=for-the-badge&logo=cpanel&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%234479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![UML](https://img.shields.io/badge/uml-%23FBB040.svg?style=for-the-badge&logo=&logoColor=white)

---

## Arquitectura del repositorio

Repo con raíz común `cursos/`. Cada curso se desarrolla en una **rama independiente**
y, al alcanzar un hito, se fusiona a `master` aportando su carpeta. El primer curso
registrado fue **hosting** — de ese merge inicial se ramificó el resto.

```
cursos/
├── curso-git/              → rama: curso-git
├── curso-vscode/           → rama: curso-vscode
├── curso-hosting/          → rama: curso-hosting  (semilla del repo)
├── curso-sql/              → rama: seccion-basica / cpy-seccion-intermedia
│   ├── pildoras-informaticas/
│   │   ├── clausulas-operadores/
│   │   ├── ejercicios/
│   │   └── resources/
│   └── soy-dalto/
│       ├── resources/
│       └── seccion-basica/
└── curso-python/           → rama: curso-python  (en preparación)
```

> El detalle operativo del progreso vive en Trello (espacio *Aprendizaje*).
> Este README refleja el estado macro; se actualiza conforme avanza cada curso.

---

## Cursos y progreso

| Curso | Fuente | Canal | Estado |
|-------|--------|-------|--------|
| **Git** | [Curso de Git](https://www.youtube.com/watch?v=9ZJ-K-zk_Go) | [Soy Dalto](https://www.youtube.com/@soydalto) | ✅ Terminado |
| **VSCode** | [Curso de VSCode](https://www.youtube.com/watch?v=TbzrOz8HbFM) | [Soy Dalto](https://www.youtube.com/@soydalto) | ✅ Terminado |
| **Hosting** | [Curso de Hosting desde Cero](https://www.youtube.com/watch?v=hikoV1Q9EzY) | [Soy Dalto](https://www.youtube.com/@soydalto) | ✅ Terminado |
| **SQL** | [Curso de SQL](https://www.youtube.com/watch?v=DFg1V-rO6Pg) | [Soy Dalto](https://www.youtube.com/@soydalto) | 🔄 En proceso |
| **SQL** | [Curso de MySQL](https://www.youtube.com/watch?v=iOiyJgnN71c&list=PLU8oAlHdN5Bmx-LChV4K3MbHrpZKefNwn) | [Píldoras Informáticas](https://www.youtube.com/@pildorasinformaticas) | 🔄 En proceso |
| **UML** | _por definir_ | — | 🔄 En paralelo |
| **Python** | _múltiples subcursos — se detalla al progresar_ | — | ⏳ Pendiente |

**Leyenda:** ✅ Terminado · 🔄 En proceso · ⏳ Pendiente

> **SQL** se cursa con dos fuentes complementarias: la base ágil de **Soy Dalto**
> y la profundización de **Píldoras Informáticas**, que se sigue hasta cerrar cada sección.

---

## Convención de trabajo

- **Una rama por curso** (`curso-git`, `curso-vscode`, `curso-hosting`, `curso-python`…).
- Ramas de sección para cursos largos (ej. SQL: `seccion-basica`, `cpy-seccion-intermedia`).
- Merge a `master` al cerrar un hito → la carpeta del curso queda incorporada.
- Tags versionados por cierre de curso (`v1.0.0` hosting, `v2.0.0` git, `v3.0.0` vscode…).
- Commits semánticos en español.

---

## Setup local

```bash
git clone https://github.com/manuelhm1993/cursos.git
cd cursos
git branch -a          # ver todas las ramas de cursos
git checkout <rama>    # entrar a un curso específico
```

Sin build step — material de estudio, scripts y esquemas planos.

---

## Notas

- Estructura resultado de varias iteraciones prueba-error hasta llegar a la arquitectura actual (rama + carpeta por curso).
- Repo en cuenta **personal** (`manuelhm1993`), no en la organización MHenriquezCA.
- Python se detallará (subcursos, ramas, carpetas) cuando arranque, al cerrar SQL.

---

Desarrollado por [MHenriquez C.A.](https://mhenriquez.com) · Maracaibo, Venezuela
