import os
import requests

MOODLE_URL = os.environ["MOODLE_URL"].rstrip("/")
TOKEN = os.environ["MOODLE_TOKEN"]

COURSE_ID = 3267

response = requests.post(
    f"{MOODLE_URL}/webservice/rest/server.php",
    data={
        "wstoken": TOKEN,
        "wsfunction": "core_enrol_get_enrolled_users",
        "moodlewsrestformat": "json",
        "courseid": COURSE_ID
    },
    timeout=30
)

response.raise_for_status()
users = response.json()

print(f"Usuarios encontrados: {len(users)}")

for user in users[:10]:
    print(user["id"], user["fullname"])
