# PPE DETECTION SERVICE 🚀

## ✨ Starting

Install venv:

```bash
python -m venv venv
```

Start in Windows:

```bash
venv\Scripts\activate
```

Install Requirements:

```bash
pip install -r requirements.txt
```

Run migration script to create necessary tables:

```bash
python app\database\migrations\create_log.py
```

## 🐢 Run

```bash
uvicorn app.main:app --reload
```

# Closing 🏁
