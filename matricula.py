import streamlit as st
import pandas as pd
from datetime import date

# ---------- FUNCIÓN ----------
def matricular_asignatura(
    alumno, edad, correo, campus, docente,
    asignatura, horario, modalidad, costo
):
    costo_mensual = costo / 3

    nueva_fila = {
        "Alumno": alumno,
        "Edad": edad,
        "Correo": correo,
        "Campus": campus,
        "Docente": docente,
        "Asignatura": asignatura,
        "Horario": horario,
        "Modalidad": modalidad,
        "Costo Total (L.)": costo,
        "Pago Mensual (L.)": round(costo_mensual, 2),
        "Fecha Matrícula": date.today()
    }

    st.session_state.table_data = pd.concat(
        [st.session_state.table_data, pd.DataFrame([nueva_fila])],
        ignore_index=True
    )

# ---------- SESSION STATE ----------
if "table_data" not in st.session_state:
    st.session_state.table_data = pd.DataFrame(
        columns=[
            "Alumno", "Edad", "Correo", "Campus", "Docente",
            "Asignatura", "Horario", "Modalidad",
            "Costo Total (L.)", "Pago Mensual (L.)", "Fecha Matrícula"
        ]
    )

# ---------- TÍTULO ----------
st.title("🎓 Sistema de Matrícula de Asignaturas")

# ---------- FORMULARIO ----------
with st.form("matricula_form", clear_on_submit=True):
    st.subheader("Datos del Alumno")
    alumno = st.text_input("Nombre completo del alumno")
    edad = st.number_input("Edad", min_value=15, max_value=80, step=1)
    correo = st.text_input("Correo institucional")

    st.subheader("Datos Académicos")
    campus = st.selectbox(
        "Campus",
        ["Tegucigalpa", "San Pedro Sula", "La Ceiba", "Virtual"]
    )

    docente = st.text_input("Nombre del docente")
    asignatura = st.text_input("Nombre de la asignatura")
    horario = st.selectbox(
        "Horario",
        ["Matutino", "Vespertino", "Nocturno"]
    )

    modalidad = st.radio(
        "Modalidad",
        ["Presencial", "Virtual", "Presencial por Zoom"]
    )

    costo = st.number_input(
        "Costo total de la asignatura (L.)",
        min_value=0.0,
        format="%.2f"
    )

    matricular = st.form_submit_button("📘 Matricular asignatura")

# ---------- ACCIÓN ----------
if matricular:
    if alumno.strip() == "" or asignatura.strip() == "":
        st.warning("Debe completar al menos el nombre del alumno y la asignatura")
    else:
        matricular_asignatura(
            alumno, edad, correo, campus, docente,
            asignatura, horario, modalidad, costo
        )
        st.success("Asignatura matriculada correctamente")

# ---------- BOTÓN ELIMINAR ÚLTIMA MATRÍCULA ----------
if st.button("🗑️ Eliminar última matrícula"):
    if not st.session_state.table_data.empty:
        st.session_state.table_data = st.session_state.table_data.iloc[:-1]
        st.success("Última matrícula eliminada")
    else:
        st.warning("No hay matrículas registradas")

# ---------- TABLA ----------
st.subheader("📋 Matrículas Registradas")
st.dataframe(st.session_state.table_data, use_container_width=True)

# ---------- RESUMEN DE PAGO ----------
st.subheader("💰 Resumen de Pago")

total_general = st.session_state.table_data["Costo Total (L.)"].sum()
pago_mensual_total = st.session_state.table_data["Pago Mensual (L.)"].sum()

st.write(f"📌 Total a pagar por el período: **L. {total_general:.2f}**")
st.write(f"📆 Pago mensual durante 3 meses: **L. {pago_mensual_total:.2f}**")
