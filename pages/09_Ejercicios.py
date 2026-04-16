import streamlit as st
import random

st.set_page_config(page_title="Ejercicios Streamlit", page_icon="🧪")

st.markdown("# Ejercicios Prácticos de Streamlit")
st.markdown("---")


# Ejercicio 1: Saludo Simple

st.header("Ejercicio 1: Saludo Simple")

nombre = st.text_input("¿Cuál es tu nombre?", placeholder="Escribe tu nombre aquí...")

if nombre.strip():
    st.success(f"¡Hola, {nombre}!")

st.markdown("---")


# Ejercicio 2: Calculadora de Producto

st.header("Ejercicio 2: Calculadora de Producto")

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Primer número", value=0.0, key="num1")
with col2:
    num2 = st.number_input("Segundo número", value=0.0, key="num2")

producto = num1 * num2
st.info(f"Multiplicación: {num1} x {num2} = {producto}")

if num1 > 100 or num2 > 100:
    st.warning("⚠️ Números grandes")

st.markdown("---")


# Ejercicio 3: Convertidor de Temperatura

st.header("Ejercicio 3: Convertidor de Temperatura")

direccion = st.radio(
    "Dirección de conversión:",
    ["Celsius a Fahrenheit", "Fahrenheit a Celsius"],
    horizontal=True,
)

temp_input = st.number_input("Ingresa la temperatura:", value=0.0, key="temp")

if direccion == "Celsius a Fahrenheit":
    resultado_temp = (temp_input * 9 / 5) + 32
    st.success(f"🌡️ {temp_input} °C = {resultado_temp:.2f} °F")
else:
    resultado_temp = (temp_input - 32) * 5 / 9
    st.success(f"🌡️ {temp_input} °F = {resultado_temp:.2f} °C")

st.markdown("---")


# Ejercicio 4: Galería de Mascotas

st.header("Ejercicio 4: Galería de Mascotas")

tab_gatos, tab_perros, tab_aves = st.tabs(["🐱 Gatos", "🐶 Perros", "🐦 Aves"])

with tab_gatos:
    st.image(
        "https://w0.peakpx.com/wallpaper/515/748/HD-wallpaper-black-persian-cat-cute-animals-cats-persian-cats-pets-black-cat.jpg",
        caption="Un gatito adorable",
        use_container_width=True,
    )
    if st.button("❤️ Me gusta", key="like_gato"):
        st.toast("¡Te gusta esta mascota! 🐱")

with tab_perros:
    st.image(
        "https://img.freepik.com/fotos-premium/perro-border-collie-ojos-azules-sienta-bosque_357532-10173.jpg?semt=ais_hybrid&w=740&q=80",
        caption="Un perrito encantador",
        use_container_width=True,
    )
    if st.button("❤️ Me gusta", key="like_perro"):
        st.toast("¡Te gusta esta mascota! 🐶")

with tab_aves:
    st.image(
        "https://images.pexels.com/photos/12565161/pexels-photo-12565161.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        caption="Un ave colorida",
        use_container_width=True,
    )
    if st.button("❤️ Me gusta", key="like_ave"):
        st.toast("¡Te gusta esta mascota! 🐦")

st.markdown("---")


# Ejercicio 5: Caja de Comentarios

st.header("Ejercicio 5: Caja de Comentarios")

with st.form("formulario_comentarios"):
    asunto = st.text_input("Asunto:")
    mensaje = st.text_area("Mensaje:")
    enviado = st.form_submit_button("📨 Enviar")

if enviado:
    if mensaje.strip():
        st.write("📬 Datos recibidos:")
        st.json({"asunto": asunto, "mensaje": mensaje})
    else:
        st.error("El mensaje no puede estar vacío.")

st.markdown("---")


# Ejercicio 6: Login Simulado

st.header("Ejercicio 6: Login Simulado")

if "logueado" not in st.session_state:
    st.session_state.logueado = False

if not st.session_state.logueado:
    usuario = st.text_input("Usuario:", key="usuario_login")
    contrasena = st.text_input("Contraseña:", type="password", key="contrasena_login")

    if st.button("🔐 Ingresar"):
        if usuario == "admin" and contrasena == "1234":
            st.session_state.logueado = True
            st.success("✅ ¡Bienvenido, admin! Has iniciado sesión correctamente.")
            st.rerun()
        else:
            st.error("❌ Usuario o contraseña incorrectos.")
else:
    st.success("✅ Sesión activa como **admin**.")
    if st.button("🚪 Cerrar Sesión"):
        st.session_state.logueado = False
        st.rerun()

st.markdown("---")


# Ejercicio 7: Lista de Compras

st.header("Ejercicio 7: Lista de Compras")

if "lista_compras" not in st.session_state:
    st.session_state.lista_compras = []

producto = st.text_input("Producto a agregar:", key="producto_compra")

col_agregar, col_limpiar = st.columns([1, 1])

with col_agregar:
    if st.button("➕ Agregar"):
        if producto.strip():
            st.session_state.lista_compras.append(producto.strip())
            st.success(f'"{producto}" agregado a la lista.')
        else:
            st.warning("Escribe un producto antes de agregar.")

with col_limpiar:
    if st.button("🗑️ Limpiar Lista"):
        st.session_state.lista_compras = []
        st.info("Lista limpiada.")

if st.session_state.lista_compras:
    st.subheader("🛒 Tu lista de compras:")
    for i, item in enumerate(st.session_state.lista_compras, 1):
        st.write(f"{i}. {item}")
else:
    st.caption("La lista está vacía.")

st.markdown("---")


# Ejercicio 8: Gráfico Interactivo

st.header("Ejercicio 8: Gráfico Interactivo")

n = st.slider("Número de puntos (N):", min_value=10, max_value=100, value=50)

datos_aleatorios = [random.uniform(0, 100) for _ in range(n)]

st.line_chart(datos_aleatorios)

if st.button("🔄 Regenerar datos"):
    st.rerun()

