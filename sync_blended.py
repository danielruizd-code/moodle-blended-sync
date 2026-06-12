import os
import requests

MOODLE_URL = os.environ["MOODLE_URL"].rstrip("/")
TOKEN = os.environ["MOODLE_TOKEN"]

COURSE_ID = 3267
COHORT_ID = 7887

def moodle_call(function, params):
    response = requests.post(
        f"{MOODLE_URL}/webservice/rest/server.php",
        data={
            "wstoken": TOKEN,
            "wsfunction": function,
            "moodlewsrestformat": "json",
            **params
        },
        timeout=60
    )
    response.raise_for_status()
    data = response.json()

    if isinstance(data, dict) and "exception" in data:
        raise Exception(data)

    return data

course_users = moodle_call("core_enrol_get_enrolled_users", {
    "courseid": COURSE_ID
})

print(f"Usuarios encontrados en el curso: {len(course_users)}")

params = {}
for i, user in enumerate(course_users):
    params[f"members[{i}][cohorttype][type]"] = "id"
    params[f"members[{i}][cohorttype][value]"] = COHORT_ID
    params[f"members[{i}][usertype][type]"] = "id"
    params[f"members[{i}][usertype][value]"] = user["id"]

if params:
    moodle_call("core_cohort_add_cohort_members", params)
    print(f"Usuarios añadidos/sincronizados en la cohorte {COHORT_ID}: {len(course_users)}")
else:
    print("No hay usuarios para añadir.")

print("Proceso finalizado.")
