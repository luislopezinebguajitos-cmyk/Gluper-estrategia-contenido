import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gluper Box Bot", page_icon="🥗", layout="centered")

st.title("🥗 Asistente Virtual — Gluper Box 📦")
st.write("¡Hola! Bienvenido al chat de **Gluper**. ¿En qué te podemos ayudar hoy?")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy tu asistente de Gluper Box. Selecciona una opción o escribe tu pregunta sobre los menús, suplementos o pedidos."}
    ]

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Opciones rápidas con botones
st.subheader("💡 Consultas rápidas:")
col1, col2 = st.columns(2)

opcion = None
if col1.button("📦 Ver qué incluye la caja"):
    opcion = "incluye"
if col2.button("🥑 Menú y Suplementos Lunes"):
    opcion = "lunes"
if col1.button("💸 Precios y Ahorro"):
    opcion = "precios"
if col2.button("🛒 ¿Cómo hacer mi pedido?"):
    opcion = "pedido"

# Entrada del usuario por texto
prompt_usuario = st.chat_input("Escribe tu duda aquí...")

# Lógica del bot
respuesta_bot = ""

if opcion == "incluye":
    respuesta_bot = "📦 **La Gluper Box incluye:**\n- 3 Comidas completas al día (Desayuno, Almuerzo, Cena)\n- 1 Postre saludable de media tarde\n- Bebidas naturales\n- Suplementos y vitaminas de venta libre\n- Guía nutricional personalizada 📋"
elif opcion == "lunes":
    respuesta_bot = "🥑 **Menú del Lunes:**\n- **Desayuno:** Omelette de claras + Café verde ☕\n- **Almuerzo:** Pechuga a la plancha con quinoa + Té verde 🥗\n- **Cena:** Ensalada de atún con aguacate 🥑\n- **Postre:** Mousse proteico de frutos rojos 🍓\n- **Suplementos:** Multivitamínico + Omega 3 💊"
elif opcion == "precios":
    respuesta_bot = "💸 **Beneficio y Ahorro:** Comer fuera a diario cuesta más dinero y calorías. Con Gluper ahorras más de 10 horas a la semana de cocina y aseguras tus metas saludables. ¡Pregunta por nuestras cajas semanales! 💵"
elif opcion == "pedido":
    respuesta_bot = "🛒 **¿Cómo pedir?** Cerramos pedidos todos los VIERNES para garantizar ingredientes frescos. Escríbenos a nuestro Instagram @gluper para tomar tus datos de entrega 📲"
elif prompt_usuario:
    user_input = prompt_usuario.lower()
    if "menu" in user_input or "comida" in user_input:
        respuesta_bot = "Nuestros menús varían cada día e incluyen proteína, carbohidratos complejos, vegetales frescos, bebidas y suplementos. ¿Te gustaría ver el menú del Lunes?"
    elif "precio" in user_input or "costo" in user_input or "cuanto" in user_input:
        respuesta_bot = "Nuestras cajas semanales incluyen toda la alimentación de lunes a domingo. Escríbenos por Instagram para consultar las promociones de esta semana. 💳"
    else:
        respuesta_bot = "¡Gracias por escribirnos! Un asesor humano de Gluper revisará tu mensaje muy pronto. Si prefieres, escríbenos a WhatsApp o Instagram @gluper. 📩"

# Mostrar respuesta en pantalla
if respuesta_bot:
    if prompt_usuario:
        st.session_state.messages.append({"role": "user", "content": prompt_usuario})
        with st.chat_message("user"):
            st.markdown(prompt_usuario)
            
    st.session_state.messages.append({"role": "assistant", "content": respuesta_bot})
    with st.chat_message("assistant"):
        st.markdown(respuesta_bot)
