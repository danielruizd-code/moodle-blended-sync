Este proyecto sincroniza todos los usuarios matriculados en un curso de Moodle con una cohorte específic en CEACFPTEST

La finalidad es mantener actualizada una cohorte de forma automática sin necesidad de gestionar manualmente sus miembros desde la interfaz de Moodle.

Se creó un usuario técnico dedicado:

- Usuario: `SincronizadorCohortes GibHub`
- Rol personalizado: `BlendedSincro`

El rol dispone de los permisos necesarios para:

- Ver participantes de cursos.
- Ver cohortes.
- Añadir miembros a cohortes.
- Eliminar miembros de cohortes (para futuras ampliaciones).

### Servicios Web

Se habilitó un servicio web personalizado:BlendedSincro

**Github Cohort Sync**

Funciones habilitadas:

- `core_enrol_get_enrolled_users`
- `core_cohort_add_cohort_members`
- `core_cohort_delete_cohort_members`

El usuario técnico fue añadido como usuario autorizado del servicio.

### Token

Se generó un token asociado al usuario técnico y al servicio web personalizado.
