import streamlit as st
import pandas as pd

# ---------- FUNCIÓN ----------
def calcular_subtotal(nombre, descripcion, precio, cantidad):
    subtotal = float(precio) * float(cantidad)

    nueva_fila = {
        "producto": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "cantidad": cantidad,
        "subtotal": subtotal
    }

    st.session_state.table_data = pd.concat(
        [st.session_state.table_data, pd.DataFrame([nueva_fila])],
        ignore_index=True
    )

# ---------- SESSION STATE ----------
if "table_data" not in st.session_state:
    st.session_state.table_data = pd.DataFrame(
        columns=["producto", "descripcion", "precio", "cantidad", "subtotal"]
    )

# ---------- TÍTULO ----------
st.title("Supermercado El Económico - Wilmer Murillo")

# ---------- FORMULARIO ----------
with st.form("producto_form", clear_on_submit=True):
    producto_nombre = st.text_input("Nombre del producto")
    producto_descripcion = st.text_input("Descripción del producto")
    producto_precio = st.number_input(
        "Precio",
        min_value=0.0,
        format="%.2f"
    )
    producto_cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        step=1
    )

    agregar = st.form_submit_button("Agregar producto")

if agregar:
    calcular_subtotal(
        producto_nombre,
        producto_descripcion,
        producto_precio,
        producto_cantidad
    )

# ---------- BOTÓN ELIMINAR ÚLTIMO ----------
if st.button("🗑️ Eliminar último producto"):
    if not st.session_state.table_data.empty:
        st.session_state.table_data = st.session_state.table_data.iloc[:-1]
        st.success("Producto eliminado")
    else:
        st.warning("No hay productos para eliminar")

# ---------- TABLA ----------
st.subheader("Productos agregados")
st.dataframe(st.session_state.table_data, use_container_width=True)

# ---------- TOTAL ----------
if st.button("Calcular Total a Pagar"):
    total = st.session_state.table_data["subtotal"].sum()
    st.subheader("Total a pagar")
    st.write(f"💰 L. {total:.2f}")
