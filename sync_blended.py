import os
import requests

MOODLE_URL = os.environ["MOODLE_URL"].rstrip("/")
TOKEN = os.environ["MOODLE_TOKEN"]

COURSE_ID = 3267
COHORT_ID = 1

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

# Usuarios matriculados en el curso
course_users = moodle_call("core_enrol_get_enrolled_users", {
    "courseid": COURSE_ID
})

course_user_ids = {int(user["id"]) for user in course_users}

# Usuarios actuales en la cohorte
cohort_members = moodle_call("core_cohort_get_cohort_members", {
    "cohortids[0]": COHORT_ID
})

current_cohort_ids = set()

for cohort in cohort_members:
    if int(cohort["cohortid"]) == COHORT_ID:
        current_cohort_ids = {int(userid) for userid in cohort["userids"]}

to_add = sorted(course_user_ids - current_cohort_ids)
to_remove = sorted(current_cohort_ids - course_user_ids)

print(f"Usuarios en curso: {len(course_user_ids)}")
print(f"Usuarios en cohorte: {len(current_cohort_ids)}")
print(f"A añadir: {len(to_add)}")
print(f"A eliminar: {len(to_remove)}")


# Altas
if to_add:
    params = {}
    for i, userid in enumerate(to_add):
        params[f"members[{i}][cohortid]"] = COHORT_ID
        params[f"members[{i}][userid]"] = userid

    moodle_call("core_cohort_add_cohort_members", params)
    print("Usuarios añadidos correctamente.")

# Bajas
if to_remove:
    params = {}
    for i, userid in enumerate(to_remove):
        params[f"members[{i}][cohortid]"] = COHORT_ID
        params[f"members[{i}][userid]"] = userid

    moodle_call("core_cohort_delete_cohort_members", params)
    print("Usuarios eliminados correctamente.")

print("Sincronización finalizada.")
