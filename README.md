<img width="2448" height="435" alt="image" src="https://github.com/user-attachments/assets/da5a7578-f579-40fe-b05f-18a40603bee3" />Esta tarea programada fue creada ante la necesidad de crear una herramienta externa para Moodle capaz de sincronizar los participantes de un aula concreta con una cohorte en específico.
De esta forma, la tarea actualizará los miembros de esta cohorte (utilizada para restringir el acceso a ciertas aulas/secciones/actividades) en la plataforma Moodle en función de la actualización de participantes de este aula.
La actualización de alumnos matriculados en este aula estará gestionada por ALEXIA, es decir, la gestión de matrículas del módulo se maneja a través de Alexia, pero no se puede automatricular a su vez dentro de cohortes en este portal (sí en grupos, pero no cohortes).

Ante esta brecha, se creó esta tarea programada, la cual completa la automatización para asignar la cohorte a los alumnos que forman parte de este módulo y así diferenciar una modalidad de estudios y otra.

Dentro de cada aula, existirán contenidos exclusivos para los miembros de esta Cohorte, significado de constar con dicha modalidad.

La finalidad es mantener actualizada una cohorte de forma automática sin necesidad de gestionar manualmente sus miembros desde la interfaz de Moodle.

*TODA LA IMPLEMENTACIÓN SE REALIZÓ EN PLATAFORMA MOODLE SANDBOX CEACFPTEST: "https://ceacfptest.virtualtoptraining.com/"

Requisitos creados en Moodle:

Se creó un usuario técnico dedicado:

- Usuario: `SincronizadorCohortes GibHub`
- correo: sincronizadorcohortes@alu.ceacfp.es
- Rol personalizado: `BlendedSincro`


Creado rol específico: BLENDEDSINCRO:
Contextos permitidos: Sistema, Usuario, Curso, Módulo de actividad, Bloque

El rol dispone de los permisos necesarios para:

- moodle/course:viewparticipants
- moodle/cohort:view 
- moodle/cohort:assign
- moodle/course:useremail
- moodle/user:update
- moodle/user:viewdetails
- moodle/user:viewhiddendetails
- moodle/site:accessallgroups


*Se puede revisar a futuro viabilidad de crear rol o asignar uno ya existente.*

### Servicios Web

Se habilitó un servicio web personalizado:BlendedSincro

**Github Cohort Sync**

Funciones habilitadas:

- `core_enrol_get_enrolled_users`
- `core_cohort_add_cohort_members`
- `core_cohort_get_cohort_members`
- `core_cohort_delete_cohort_members`
  
El usuario técnico fue añadido como usuario autorizado del servicio.
<img width="2448" height="435" alt="image" src="https://github.com/user-attachments/assets/39d45e99-cee4-480e-a4ee-410541928d22" />

### Token

Se generó un token asociado al usuario técnico y al servicio web personalizado.
