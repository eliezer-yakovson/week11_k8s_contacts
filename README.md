# Contacts API (FastAPI + MongoDB)

פרויקט קטן של API לניהול אנשי קשר.
השרת כתוב ב‑FastAPI ושומר נתונים ב‑MongoDB דרך PyMongo.

ה‑API כולל כמה נתיבים פשוטים:

- `GET /contacts` מחזיר את כל אנשי הקשר.
- `POST /contacts` יוצר איש קשר חדש.
- `PUT /contacts/{id}` מעדכן איש קשר לפי id.
- `DELETE /contacts/{id}` מוחק איש קשר לפי id.
- `GET /health/db` בודק שהחיבור ל‑MongoDB חי.

ככה נראה Contact:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "phone_number": "050-1234567"
}
```

האפליקציה קוראת כמה משתני סביבה (ולכולם יש ברירות מחדל):

- `MONGO_HOST` (ברירת מחדל: `localhost`)
- `MONGO_PORT` (ברירת מחדל: `27017`)
- `MONGO_DB` (ברירת מחדל: `contactsdb`)

הרצה מקומית (Python).
קודם מרימים MongoDB. אפשר עם Docker:

```bash
docker run --rm -p 27017:27017 --name mongo-contacts mongo:7.0
```

אחר כך מתקינים תלויות:

```bash
pip install -r app/requirements.txt
```

ואז מריצים את השרת:

```bash
python app/main.py
```

השרת יעלה על `http://127.0.0.1:8000`.

דוגמאות `curl`.
יצירה:

```bash
curl -X POST http://127.0.0.1:8000/contacts -H "Content-Type: application/json" -d "{\"first_name\":\"John\",\"last_name\":\"Doe\",\"phone_number\":\"050-1234567\"}"
```

קריאה:

```bash
curl http://127.0.0.1:8000/contacts
```

בדיקת DB:

```bash
curl http://127.0.0.1:8000/health/db
```

הרצה על Kubernetes.
בתיקיית `k8s/` יש Pod + Service ל‑MongoDB ול‑API.
ה‑API נחשף כ‑NodePort על `30080`.

ככה מרימים:

```bash
kubectl apply -f k8s/mongodb-pod.yaml
kubectl apply -f k8s/mongodb-service.yaml
kubectl apply -f k8s/api-pod.yaml
kubectl apply -f k8s/api-service.yaml
```

ככה בודקים:

```bash
curl http://localhost:30080/health/db
curl http://localhost:30080/contacts
```

אם עובדים עם minikube, לפעמים צריך להשתמש ב‑`minikube service api-service --url` במקום `localhost`.
