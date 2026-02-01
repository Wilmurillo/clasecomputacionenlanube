import streamlit as st
import pandas as pd

# ---------- FUNCIÓN ----------
def agregar_producto(nombre, descripcion, precio, cantidad):
    subtotal = float(precio) * float(cantidad)

    nueva_fila = {
        "Producto": nombre,
        "Descripción": descripcion,
        "Precio": precio,
        "Cantidad": cantidad,
        "Subtotal": subtotal
    }

    st.session_state.table_data = pd.concat(
        [st.session_state.table_data, pd.DataFrame([nueva_fila])],
        ignore_index=True
    )

# ---------- SESSION STATE ----------
if "table_data" not in st.session_state:
    st.session_state.table_data = pd.DataFrame(
        columns=["Producto", "Descripción", "Precio", "Cantidad", "Subtotal"]
    )

# ---------- TÍTULO ----------
st.title("🛒 Supermercado El Económico - Wilmer Murillo")

# ---------- FORMULARIO ----------
with st.form("producto_form", clear_on_submit=True):
    nombre = st.text_input("Nombre del producto")
    descripcion = st.text_input("Descripción del producto")
    precio = st.number_input("Precio", min_value=0.0, format="%.2f")
    cantidad = st.number_input("Cantidad", min_value=1, step=1)

    agregar = st.form_submit_button("Agregar producto")

if agregar:
    if nombre.strip() == "":
        st.warning("Debe ingresar el nombre del producto")
    else:
        agregar_producto(nombre, descripcion, precio, cantidad)

# ---------- BOTÓN ELIMINAR ÚLTIMO ----------
if st.button("🗑️ Eliminar último producto"):
    if not st.session_state.table_data.empty:
        st.session_state.table_data = st.session_state.table_data.iloc[:-1]
        st.success("Último producto eliminado")
    else:
        st.warning("No hay productos para eliminar")

# ---------- TABLA ----------
st.subheader("📦 Productos agregados")
st.dataframe(st.session_state.table_data, use_container_width=True)

# ---------- TOTAL + ISV ----------
st.subheader("💳 Cálculo del Total")

subtotal_general = st.session_state.table_data["Subtotal"].sum()

tipo_isv = st.radio(
    "Seleccione el tipo de ISV",
    ["Sin ISV", "ISV 15%", "ISV 18% (Licores)"]
)

if tipo_isv == "ISV 15%":
    isv = subtotal_general * 0.15
elif tipo_isv == "ISV 18% (Licores)":
    isv = subtotal_general * 0.18
else:
    isv = 0

total = subtotal_general + isv

st.write(f"🧾 Subtotal: L. {subtotal_general:.2f}")
st.write(f"💸 ISV aplicado: L. {isv:.2f}")
st.write(f"💰 **Total a pagar: L. {total:.2f}**")
