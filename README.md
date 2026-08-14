# `<mh/>` cursos — Ruta de aprendizaje

Repositorio de seguimiento del plan de estudio del Ing. Manuel Henriquez / MHenriquez C.A.
Cada curso vive en su propia rama y aporta su carpeta al hacer merge a `master`,
permitiendo avanzar de forma independiente sin desordenar el árbol.

🏢 [MHenriquez C.A.](https://github.com/MHenriquezCA) · 🧑🏽‍💻 [manuelhm1993](https://github.com/manuelhm1993)

---

### Stack de aprendizaje 💻

#### Terminados
![Git](https://img.shields.io/badge/git-%23F03C2E.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23181717.svg?style=for-the-badge&logo=github&logoColor=white) ![VSCode](https://img.shields.io/badge/vscode-%23007ACC.svg?style=for-the-badge&logo=visualstudiocode&logoColor=white) ![cPanel](https://img.shields.io/badge/cpanel-%23FF6C2C.svg?style=for-the-badge&logo=cpanel&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%23003B57.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%234479A1.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![VirtualBox](https://img.shields.io/badge/virtualbox-%23FCC624.svg?style=for-the-badge&logo=virtualbox&logoColor=white) ![Linux](https://img.shields.io/badge/linux-%232F61B4.svg?style=for-the-badge&logo=linux&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%232496ED.svg?style=for-the-badge&logo=docker&logoColor=white) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white) ![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white)
#### En proceso
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/css-%23663399.svg?style=for-the-badge&logo=css&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![JSON](https://img.shields.io/badge/json-%23000000.svg?style=for-the-badge&logo=json&logoColor=white) 
#### Pendientes Q1 - Hacer ahora
![Vite](https://img.shields.io/badge/vite-%239135FF.svg?style=for-the-badge&logo=vite&logoColor=white) ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2306B6D4.svg?style=for-the-badge&logo=tailwindcss&logoColor=white) ![React](https://img.shields.io/badge/react-%2361DAFB.svg?style=for-the-badge&logo=react&logoColor=white) ![Laravel](https://img.shields.io/badge/laravel-%23FF2D20.svg?style=for-the-badge&logo=laravel&logoColor=white) ![Livewire](https://img.shields.io/badge/livewire-%234E56A6.svg?style=for-the-badge&logo=livewire&logoColor=white) ![Flux](https://img.shields.io/badge/flux-%235468FF.svg?style=for-the-badge&logo=flux&logoColor=white) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![FastAPI](https://img.shields.io/badge/fastapi-%23009688.svg?style=for-the-badge&logo=fastapi&logoColor=white) 
#### Pendientes Q2 - Agendar
![Bash](https://img.shields.io/badge/bash-%234EAA25.svg?style=for-the-badge&logo=gnubash&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232088FF.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Ubuntu](https://img.shields.io/badge/ubuntu-%23E95420.svg?style=for-the-badge&logo=ubuntu&logoColor=white) ![Claude](https://img.shields.io/badge/claude-%23D97757.svg?style=for-the-badge&logo=claude&logoColor=white) ![OpenCode](https://img.shields.io/badge/opencode-%23000000.svg?style=for-the-badge&logo=opencode&logoColor=white) ![n8n](https://img.shields.io/badge/n8n-%23EA4B71.svg?style=for-the-badge&logo=n8n&logoColor=white)
#### Pendientes Q3 - Delegar
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) ![Java](https://img.shields.io/badge/java-%23F89820.svg?style=for-the-badge&logo=java&logoColor=white) ![NodeJS](https://img.shields.io/badge/node.js-%235FA04E.svg?style=for-the-badge&logo=node.js&logoColor=white) 
#### Pendientes Q4 - Borrar
![Debian](https://img.shields.io/badge/debian-%23A81D33.svg?style=for-the-badge&logo=debian&logoColor=white) ![UML](https://img.shields.io/badge/uml-%23FABD14.svg?style=for-the-badge&logo=uml&logoColor=white) 

---

## Arquitectura del repositorio

Repositorio con raíz común `cursos/`. Cada curso se desarrolla en una **rama independiente**
y al alcanzar un hito, se fusiona a `master` aportando su carpeta. El primer curso
registrado fue **hosting** — de ese merge inicial se ramificó el resto.

```
cursos/
├── automatizaciones/           → directorio:     agrupa-distribuciones
│   └── curso-n8n/                  → rama:                                (stand-by)
├── docs/                       → directorio:     agrupa-distribuciones
│   ├── bash/                   → directorio:       uso-conceptos          (simple-docs)
│   ├── docker/                 → directorio:       uso-conceptos          (simple-docs)
│   └── vs/                     → directorio:       vs-tecnologías         (simple-docs)
├── frameworks/                 → directorio:     agrupa-distribuciones
├── ia/                         → directorio:     agrupa-distribuciones
├── lenguajes_pg/               → directorio:     agrupa-distribuciones
│   ├── curso-cpp/                  → rama:                                (stand-by)
│   ├── curso-java/                 → rama:                                (stand-by)
│   └── curso-python/           → directorio:     agrupa-distribuciones
│       ├── fundamentos/            → rama:         curso-python           (merged - v5.0.0) 
│       ├── poo-solid/              → rama:         curso-poo-solid-python (merged - v5.1.0)
│       └── senior/                 → rama:         curso-python-senior    (merged - v5.2.0)
├── transversales/              → directorio:     agrupa-distribuciones
│   ├── curso-docker/               → rama:         curso-docker           (merged - v7.0.0)
│   ├── curso-git/                  → rama:         curso-git              (merged - v2.0.0)
│   ├── curso-hosting/              → rama:         curso-hosting          (merged - v1.0.0)
│   ├── curso-markdown/             → rama:         curso-markdown         (merged - v6.0.0)
│   ├── curso-sql/                  → rama:         curso-sql              (merged - v4.0.0)
│   │   ├── pildoras-informaticas/  → directorio: agrupa-distribuciones
│   │   └── soy-dalto/              → directorio: agrupa-distribuciones
│   └── curso-vscode/               → rama:       curso-vscode             (merged - v3.0.0)
└── web/                        → directorio:     agrupa-distribuciones
    ├── back-end/               → directorio:     agrupa-distribuciones
    │   └── curso-php/              → rama:         curso-php              (merged - ) 
    └── front-end/              → directorio:     agrupa-distribuciones
        ├── curso-html/             → rama:         curso-html             (in-progress) 
        ├── curso-css/              → rama:         curso-css              (in-progress) 
        └── curso-js/               → rama:         curso-js               (in-progress) 

```

> El detalle operativo del progreso vive en Trello [Espacio Aprendizaje](https://trello.com/w/aprendizajemh/home).
> Este README refleja el estado macro; se actualiza conforme avanza cada curso.

---

## Cursos y progreso

| Curso | Fuente | Canal | Estado |
|:---|:---|:---|:---:|
| **Git** | [Curso de Git](https://www.youtube.com/watch?v=9ZJ-K-zk_Go) | [Soy Dalto](https://www.youtube.com/@soydalto) | ✅ Terminado |
| **VSCode** | [Curso de VSCode](https://www.youtube.com/watch?v=TbzrOz8HbFM) | [Soy Dalto](https://www.youtube.com/@soydalto) | ✅ Terminado |
| **Hosting** | [Curso de Hosting desde Cero](https://www.youtube.com/watch?v=hikoV1Q9EzY) | [Soy Dalto](https://www.youtube.com/@soydalto) | ✅ Terminado |
| **SQL** | [Curso de SQL (SQLite)](https://www.youtube.com/watch?v=DFg1V-rO6Pg) | [Soy Dalto](https://www.youtube.com/@soydalto) | ✅ Terminado |
| **SQL** | [Curso de SQL (MySQL)](https://www.youtube.com/watch?v=iOiyJgnN71c&list=PLU8oAlHdN5Bmx-LChV4K3MbHrpZKefNwn) | [Píldoras Informáticas](https://www.youtube.com/@pildorasinformaticas) | ✅ Terminado |
| **Python** | [Curso de Python](https://www.youtube.com/watch?v=nKPbfIU442g) | [Soy Dalto](https://www.youtube.com/@soydalto) | ✅ Terminado |
| **Python** | [Curso de Python](https://www.youtube.com/watch?v=tDYr14IIu_4&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS) | [Píldoras Informáticas](https://www.youtube.com/@pildorasinformaticas) | ✅ Terminado |
| **Máquinas virtuales** |[Curso de VM](https://www.youtube.com/watch?v=uiFZUfmFAus) | [HolaMundo](https://www.youtube.com/@HolaMundoDev) | ✅ Terminado |
| **Linux** |[Curso de Linux](https://www.youtube.com/watch?v=L906Kti3gzE) | [HolaMundo](https://www.youtube.com/@HolaMundoDev) | ✅ Terminado |
| **Docker** |[Curso de Docker](https://www.youtube.com/watch?v=4Dko5W96WHg) | [HolaMundo](https://www.youtube.com/@HolaMundoDev) | ✅ Terminado |
| **Docker** |[Curso de Docker](https://www.youtube.com/@roelcode/search?query=docker) | [Roelcode](https://www.youtube.com/@roelcode) | ✅ Terminado |
| **PHP** |[Curso de PHP](https://www.youtube.com/watch?v=_rEj-RE8cLs&list=PLZ2ovOgdI-kUSqWuyoGJMZL6xldXw6hIg) | [CodersFree](https://www.youtube.com/@CodersFree) | ✅ Terminado |
| **HTML** |[Curso de HTML](https://www.youtube.com/watch?v=ELSm-G201Ls&list=PLE8uP447fYpiWxfqCnoHZx03zCsUAzDUW) | [Soy Dalto](https://www.youtube.com/@soydalto) | 🔄 En proceso |
| **CSS** |[Curso de CSS](https://www.youtube.com/watch?v=ELSm-G201Ls&list=PLE8uP447fYpiWxfqCnoHZx03zCsUAzDUW) | [Soy Dalto](https://www.youtube.com/@soydalto) | 🔄 En proceso |
| **JavaScript** |[Curso de JavaScript](https://www.youtube.com/watch?v=z95mZVUcJ-E&list=PLE8uP447fYpiWxfqCnoHZx03zCsUAzDUW&index=5) | [Soy Dalto](https://www.youtube.com/@soydalto) | ⏳ Pendiente  |

**Leyenda:** ✅ Terminado · ⏸️ En pausa · 🔄 En proceso · ⏳ Pendiente 

> **Git, VSCode && Hosting:** fueron las bases transversales para el control de versiones, desarrollo y deploy que marcaron el inicio del camino a *junior-dev*.
> **SQL:** se cursó con dos fuentes complementarias la base ágil de *Soy Dalto* y la profundización de *Píldoras Informáticas*.
> **Python:** sigue el mismo esquema de dos fuentes Soy Dalto + Píldoras Informáticas. Para la base del lenguaje. 
> **Python:** *POO-SOLID* Soy Dalto *POO* Píldoras Informáticas. Para arquitectura y patrones de diseño.
> **Python:** *TKinter, DB, Documentación, Testing && Ejecutables* Píldoras Informáticas. Para el desarrollo de sistemas completos. Este punto marca la transición de *junior-dev* a *semi-senior-dev*.
> **VM, WSL2 - Ubuntu && Docker** *HolaMundo*, se aprendió el uso de VM solo por arquitectura, pero respecto a docker quedó en el pasado. Con el WSL2 y Docker para el manejo de contenedores y entornos aislados, fueron la transición de *semi-senior-dev* a *senior-dev*.
> **Laravel - Sail - Bash && Github Actions** *Rodrigo Río* + *MoureDev*, complementa las bases entre el front-end y back-end para la transición de *senior-dev* a *senior-dev-fullstack*.

---

## Convención de trabajo

- **Una rama general por curso** (`curso-git`, `curso-vscode`, `curso-hosting`, `curso-sql`, `curso-python`, `curso-docker`, `curso-markdown`…).
- Ramas de sección para cursos largos (SQL: `seccion-basica`, `seccion-intermedia`, `seccion-avanzada`…).
- Merge `--no-ff` a la rama del curso al cerrar un hito, y de ahí a `master` → la carpeta del curso queda incorporada.
- Tags versionados por cierre de curso (`v1.0.0` hosting, `v2.0.0` git, `v3.0.0` vscode, `v4.0.0` sql, `v5.0.0` python, `v5.1.0` python-poo-solid, `v5.2.0` python-tkinter-db-tdd, `v6.0.0` docker, …).
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

### Entornos

Los ejercicios de Python (curso SQL avanzado y curso Python) usan librerías externas
(`pandas`, `matplotlib`). A partir del curso de Python se estandariza el uso de
**entornos virtuales** (`.venv`) por proyecto — equivalente conceptual a `vendor/` (Composer)
o `node_modules/` (npm). El `.gitignore` ya excluye `.venv/`.

```bash
py -m venv .venv                  # crear el entorno con Python 3.14 (launcher py)
source .venv/Scripts/activate     # activar — Git Bash en Windows
pip install -r requirements.txt   # ya dentro del venv, pip pelado es el correcto
```

> Fuera del `.venv` usar siempre `py` (nunca `python`/`pip`, que resolverían al Python 3.13 de Laragon). Dentro del `.venv`, `python` y `pip` ya apuntan al entorno. Actualmente esto está solucionado con WSL2 y Docker.

---

## Notas

- Estructura resultado de varias iteraciones prueba-error hasta llegar a la arquitectura actual (rama + carpeta por curso).
- Repo en cuenta **personal** (`manuelhm1993`), no en la organización MHenriquezCA.
- Resolución de rutas en scripts Python: `Path(__file__).resolve().parent.parent / "data/usuarios.db"` para referenciar la BD relativa al script, no al directorio de ejecución.
- Python se detallará (subcursos, ramas, carpetas) conforme avance cada etapa del plan.

---

Desarrollado por [MHenriquez C.A.](https://mhenriquez.com) · Maracaibo, Venezuela