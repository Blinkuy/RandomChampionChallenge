# lol_random_champ

<div align="center">

**Random Champion Picker for League of Legends**  

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)  [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)  [![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)  
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)  [![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)  
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

</div>

---

## 📋 Project Overview

**lol_random_champ** — simple web application / tool for randomizing a champion pick in League of Legends.  
This tool helps users get a random champion (or build, depending on your implementation) from the pool of available champions — useful for players wanting a “random challenge” or to diversify picks.

---

## 🛠 Technologies

- **Python + FastAPI** — backend framework, routing and server logic  
- **SQLite** — lightweight database for storing data
- **JavaScript, HTML, CSS** — frontend interface (vanilla or minimal)  


---

## 🚀 Installation and Running

### Requirements

- Python 3.11.9
- `pip`  


### 1. Clone the repository

```bash
git clone https://github.com/Blinkuy/lol_random_champ.git
cd lol_random_champ
```

### 2. Install requirements

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run app

```bash
uvicorn src.main:app
```

Now you can acsess application using **[http://localhost:8000](http://localhost:8000)**
