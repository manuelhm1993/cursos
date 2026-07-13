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
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![UML](https://img.shields.io/badge/uml-%23FBB040.svg?style=for-the-badge&logo=&logoColor=white)

---

## Arquitectura del repositorio

Repo con raíz común `cursos/`. Cada curso se desarrolla en una **rama independiente**
y, al alcanzar un hito, se fusiona a `master` aportando su carpeta. El primer curso
registrado fue **hosting** — de ese merge inicial se ramificó el resto.

```
cursos/
├── curso-hosting/          → rama: curso-hosting  (semilla del repo)
├── curso-git/              → rama: curso-git
├── curso-vscode/           → rama: curso-vscode
├── curso-sql/              → rama: curso-sql (+ ramas de sección)
│   ├── pildoras-informaticas/
│   └── soy-dalto/
│       ├── resources/
│       │   └── databases/  → northwind.db (fuente única de datos)
│       ├── seccion-basica/
│       ├── seccion-intermedia/
│       └── seccion-avanzada/
│           └── python/     → SQL + Python + pandas + matplotlib
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
| **SQL** | [Curso de SQL](https://www.youtube.com/watch?v=DFg1V-rO6Pg) | [Soy Dalto](https://www.youtube.com/@soydalto) | ✅ Terminado |
| **SQL** | [Curso de MySQL](https://www.youtube.com/watch?v=iOiyJgnN71c&list=PLU8oAlHdN5Bmx-LChV4K3MbHrpZKefNwn) | [Píldoras Informáticas](https://www.youtube.com/@pildorasinformaticas) | 🔄 En proceso (triggers) |
| **UML** | _por definir_ | — | 🔄 En paralelo |
| **Python** | _múltiples subcursos — se detalla al progresar_ | — | ⏳ Pendiente |

**Leyenda:** ✅ Terminado · 🔄 En proceso · ⏳ Pendiente

> **SQL** se cursa con dos fuentes complementarias: la base ágil de **Soy Dalto** (terminado)
> y la profundización de **Píldoras Informáticas**, que se sigue hasta cerrar cada sección
> (pendiente solo el módulo de triggers).

---

## Convención de trabajo

- **Una rama por curso** (`curso-git`, `curso-vscode`, `curso-hosting`, `curso-sql`, `curso-python`…).
- Ramas de sección para cursos largos (SQL: `seccion-basica`, `seccion-intermedia`, `seccion-avanzada`, `consultas-accion`, `ddl`, `triggers`; Python: prefijo `cpy-`).
- Merge `--no-ff` a la rama del curso al cerrar un hito, y de ahí a `master` → la carpeta del curso queda incorporada.
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

### Entornos Python

Los ejercicios de Python (curso SQL avanzado y curso Python) usan librerías externas
(`pandas`, `matplotlib`). A partir del curso de Python se estandariza el uso de
**entornos virtuales** (`venv`) por proyecto — equivalente conceptual a `vendor/` (Composer)
o `node_modules/` (npm). El `.gitignore` ya excluye `venv/`.

```bash
py -m venv .venv
source .venv/Scripts/activate    # Git Bash en Windows
py -m pip install -r requirements.txt
```

---

## Notas

- Estructura resultado de varias iteraciones prueba-error hasta llegar a la arquitectura actual (rama + carpeta por curso).
- Repo en cuenta **personal** (`manuelhm1993`), no en la organización MHenriquezCA.
- Resolución de rutas en scripts Python: `Path(__file__).parent` para referenciar la BD relativa al script, no al directorio de ejecución.
- Python se detallará (subcursos, ramas, carpetas) cuando arranque formalmente, tras cerrar los triggers de SQL.

---

Desarrollado por [MHenriquez C.A.](https://mhenriquez.com) · Maracaibo, Venezuela