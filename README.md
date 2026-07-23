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
├── curso-hosting/              → rama:    curso-hosting  (semilla del repo)
├── curso-git/                  → rama:    curso-git
├── curso-vscode/               → rama:    curso-vscode
├── curso-sql/                  → rama:    curso-sql 
├── curso-python/               → carpeta: agrupa-distribuciones
│   ├── fundamentos/            → rama:    curso-python
│   ├── poo-solid/              → rama:    curso-poo-solid-python
│   └── senior/                 → rama:    curso-python-senior  (en proceso)
└── curso-siguiente/
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
| **SQL** | [Curso de MySQL](https://www.youtube.com/watch?v=iOiyJgnN71c&list=PLU8oAlHdN5Bmx-LChV4K3MbHrpZKefNwn) | [Píldoras Informáticas](https://www.youtube.com/@pildorasinformaticas) | ✅ Terminado |
| **Python** | [Curso de Python](https://www.youtube.com/watch?v=nKPbfIU442g) | [Soy Dalto](https://www.youtube.com/@soydalto) | 🔄 En proceso |
| **Python** | [Curso de Python](https://www.youtube.com/watch?v=tDYr14IIu_4&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS) | [Píldoras Informáticas](https://www.youtube.com/@pildorasinformaticas) | 🔄 En proceso |
| **UML** | _por definir_ | — | ⏳ Pendiente |

**Leyenda:** ✅ Terminado · 🔄 En proceso · ⏳ Pendiente

> **SQL** se cursó con dos fuentes complementarias: la base ágil de **Soy Dalto**
> y la profundización de **Píldoras Informáticas** — ambas completadas.
>
> **Python** sigue el mismo esquema de dos fuentes (**Soy Dalto** + **Píldoras Informáticas**)
> para la base del lenguaje. La ruta prevista continúa con **POO** (Soy Dalto) y luego
> **Django** y **automatizaciones** (Píldoras Informáticas). Cada etapa se detalla en la
> tabla al arrancar formalmente.
>
> **UML** y **desarrollo web frontend** quedan encolados tras cerrar Python, Django y automatizaciones.

---

## Convención de trabajo

- **Una rama por curso** (`curso-git`, `curso-vscode`, `curso-hosting`, `curso-sql`, `curso-python`, `curso-poo-solid-python`…).
- Ramas de sección para cursos largos (SQL: `seccion-basica`, `seccion-intermedia`, `seccion-avanzada`…).
- Merge `--no-ff` a la rama del curso al cerrar un hito, y de ahí a `master` → la carpeta del curso queda incorporada.
- Tags versionados por cierre de curso (`v1.0.0` hosting, `v2.0.0` git, `v3.0.0` vscode, `v4.0.0` sql, `v5.0.0` python…).
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
**entornos virtuales** (`.venv`) por proyecto — equivalente conceptual a `vendor/` (Composer)
o `node_modules/` (npm). El `.gitignore` ya excluye `.venv/`.

```bash
py -m venv .venv                  # crear el entorno con Python 3.14 (launcher py)
source .venv/Scripts/activate     # activar — Git Bash en Windows
pip install -r requirements.txt   # ya dentro del venv, pip pelado es el correcto
```

> Fuera del `.venv` usar siempre `py` (nunca `python`/`pip` pelados, que resolverían
> al Python 3.13 de Laragon). Dentro del `.venv`, `python` y `pip` ya apuntan al entorno.

---

## Notas

- Estructura resultado de varias iteraciones prueba-error hasta llegar a la arquitectura actual (rama + carpeta por curso).
- Repo en cuenta **personal** (`manuelhm1993`), no en la organización MHenriquezCA.
- Resolución de rutas en scripts Python: `Path(__file__).parent` para referenciar la BD relativa al script, no al directorio de ejecución.
- Python se detallará (subcursos, ramas, carpetas) conforme avance cada etapa del plan.

---

Desarrollado por [MHenriquez C.A.](https://mhenriquez.com) · Maracaibo, Venezuela