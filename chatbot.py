import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gluper Box Bot", page_icon="🥗", layout="centered")

st.title("🥗 Asistente Virtual — Gluper Box 📦")
st.write("¡Hola! Bienvenido al sistema inteligente de **Gluper Box**. ¿En qué te puedo ayudar hoy?")

# Diccionario de menús por día
menus = {
    "lunes": "🥑 **Lunes — Arranque de Energía Fit:**\n* **Desayuno:** Omelette de claras con espinaca + Café verde ☕\n* **Almuerzo:** Pechuga a la plancha con quinoa + Té verde 🥗\n* **Cena:** Ensalada de atún con aguacate 🥑\n* **Postre:** Mousse proteico de frutos rojos 🍓\n* **Suplemento:** Multivitamínico + Omega 3 💊",
    "martes": "🥗 **Martes — Digestión Ligera:**\n* **Desayuno:** Smoothie bowl de espirulina y banano 🍌\n* **Almuerzo:** Filete de salmón al horno con espárragos 🐟\n* **Cena:** Crema de calabacín y semillas de chía 🥣\n* **Postre:** Gelatina ligera sin azúcar 🍧\n* **Suplemento:** Probióticos + Magnesio 💊",
    "miercoles": "🍓 **Miércoles — Vitalidad y Antioxidantes:**\n* **Desayuno:** Pancakes de avena con chía y fresas 🥞\n* **Almuerzo:** Bowl de pollo, camote y garbanzos 🥙\n* **Cena:** Sopa de verduras desintoxicante 🍜\n* **Postre:** Yogur griego con arándanos 🫐\n* **Suplemento:** Vitamina C + Colágeno 💊",
    "jueves": "🌿 **Jueves — Equilibrio y Sabor:**\n* **Desayuno:** Toast de pan integral con aguacate y huevo 🍞\n* **Almuerzo:** Carne magra salteada con brócoli y arroz integral 🥩\n* **Cena:** Ensalada mediterránea con queso feta 🥗\n* **Postre:** Manzana horneada con canela 🍎\n* **Suplemento:** Complejo B + Zinc 💊",
    "viernes": "🔥 **Viernes — Cierre Semanal:**\n* **Desayuno:** Waffles de proteína con miel de agave 🧇\n* **Almuerzo:** Tacos saludables de lechuga con pavo molido 🌮\n* **Cena:** Wrap integral de pollo y vegetales 🌯\n* **Postre:** Choco-fit mugcake sin azúcar 🍫\n* **Suplemento:** Multivitamínico + Omega 3 💊",
    "sabado": "🍊 **Sábado — Detox y Renovación:**\n* **Desayuno:** Jugo verde desintoxicante + Huevos revueltos 🍳\n* **Almuerzo:** Ceviche vegetal de hongos y palmito 🥗\n* **Cena:** Pizza con base de coliflor y vegetales 🍕\n* **Postre:** Parfait de chía con mango 🥭\n* **Suplemento:** Espirulina + Antioxidantes 💊",
    "domingo": "✨ **Domingo — Recarga Saludable:**\n* **Desayuno:** Omelette de champiñones y queso bajo en grasa 🍳\n* **Almuerzo:** Pechuga de pavo al romero con puré de camote 🦃\n* **Cena:** Ensalada de espinacas, fresas y nueces 🥗\n* **Postre:** Pudding de chía y vainilla 🍮\n* **Suplemento:** Calcio + Vitamina D 💊"
}

# Inicializar historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy tu asistente inteligente de Gluper Box. 📦 Puedes consultarme por nuestros menús diarios, precios de las cajas o cómo realizar tu pedido."}
    ]

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- SECCIÓN INTERACTIVA DE MENÚS POR DÍA ---
st.markdown("---")
st.subheader("📅 Consulta un día específico")

col_dia, col_btn = st.columns([2, 1])
with col_dia:
    dia_seleccionado = st.selectbox(
        "Selecciona el día que quieres revisar:",
        ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo", "Ver Semana Completa"],
        label_visibility="collapsed"
    )

opcion_dia_click = False
with col_btn:
    if st.button("🔎 Ver Menú"):
        opcion_dia_click = True

# --- BOTONES DE CONSULTAS RÁPIDAS ---
st.subheader("💡 Consultas rápidas")
c1, c2, c3 = st.columns(3)

btn_incluye = c1.button("📦 ¿Qué incluye?")
btn_precios = c2.button("💵 Precios y Planes")
btn_pedido = c3.button("🛒 ¿Cómo pedir?")

# Input del usuario
prompt_usuario = st.chat_input("Escribe tu duda (ej. 'menú', 'precios', 'lunes')...")

# --- LÓGICA DE RESPUESTA INTELIGENTE ---
respuesta_bot = ""

# 1. Si usó el selector por día
if opcion_dia_click:
    dia_key = dia_seleccionado.lower().replace("é", "e").replace("á", "a")
    if dia_key == "ver semana completa":
        respuesta_bot = "📅 **Menú Completo de la Semana Gluper Box:**\n\n" + "\n\n---\n\n".join(menus.values())
    else:
        respuesta_bot = menus[dia_key]

# 2. Si usó los botones rápidos
elif btn_incluye:
    respuesta_bot = "📦 **La Gluper Box incluye:**\n* 3 Comidas completas al día (Desayuno, Almuerzo, Cena)\n* 1 Postre saludable de media tarde\n* Bebidas naturales diarias\n* Suplementos y vitaminas de venta libre\n* Guía nutricional personalizada 📋"

elif btn_precios:
    respuesta_bot = "💵 **Precios y Planes de Gluper Box:**\n* 📦 **Plan Semanal (7 Días):** Q450.00 / $58.00 USD (21 comidas + 7 postres + bebidas y suplementos)\n* 📦 **Plan Quincenal (14 Días):** Q850.00 / $110.00 USD (Ahorras 5%)\n* 📦 **Plan Mensual (30 Días):** Q1,600.00 / $205.00 USD (Ahorras 12% + Envío gratis) 🚚\n\n*Aceptamos tarjetas de crédito, débito y transferencia bancaria.* 💳"

elif btn_pedido:
    respuesta_bot = "🛒 **¿Cómo pedir?** Cerramos pedidos todos los **VIERNES** a las 6:00 PM para garantizar ingredientes 100% frescos la semana siguiente. Escríbenos a nuestro Instagram **@gluper** o por WhatsApp para tomar tus datos de entrega. 📲"

# 3. Si escribió por texto
elif prompt_usuario:
    input_clean = prompt_usuario.lower().strip()
    
    # Si solo escribe "menu" o "menú" sin especificar el día
    if input_clean in ["menu", "menú", "comida", "comidas"]:
        respuesta_bot = "🥑 ¡Con gusto! ¿De qué día te gustaría ver el menú? Escribe el día (*Lunes, Martes, Miércoles, Jueves, Viernes, Sábado o Domingo*), selecciona un día en el menú desplegable arriba 👆 o dime si prefieres ver el **'menú completo'**."
    
    # Días específicos por texto
    elif "lunes" in input_clean:
        respuesta_bot = menus["lunes"]
    elif "martes" in input_clean:
        respuesta_bot = menus["martes"]
    elif "miercoles" in input_clean or "miércoles" in input_clean:
        respuesta_bot = menus["miercoles"]
    elif "jueves" in input_clean:
        respuesta_bot = menus["jueves"]
    elif "viernes" in input_clean:
        respuesta_bot = menus["viernes"]
    elif "sabado" in input_clean or "sábado" in input_clean:
        respuesta_bot = menus["sabado"]
    elif "domingo" in input_clean:
        respuesta_bot = menus["domingo"]
    elif "completo" in input_clean or "semana" in input_clean:
        respuesta_bot = "📅 **Menú Completo de la Semana Gluper Box:**\n\n" + "\n\n---\n\n".join(menus.values())
        
    # Precios por texto
    elif any(p in input_clean for p in ["precio", "costo", "cuanto", "cuánto", "plan", "valor"]):
        respuesta_bot = "💵 **Precios de Gluper Box:**\n* **Plan Semanal (7 días):** Q450.00\n* **Plan Quincenal (14 días):** Q850.00\n* **Plan Mensual (30 días):** Q1,600.00 (Envío gratis) 🚚"
    
    else:
        respuesta_bot = "¡Gracias por escribirnos! 📩 Un asesor humano de Gluper responderá a tu consulta detallada muy pronto. Si prefieres atención inmediata, escríbenos por Instagram a **@gluper**."

# Mostrar respuesta en el chat
if respuesta_bot:
    if prompt_usuario:
        st.session_state.messages.append({"role": "user", "content": prompt_usuario})
        with st.chat_message("user"):
            st.markdown(prompt_usuario)
            
    st.session_state.messages.append({"role": "assistant", "content": respuesta_bot})
    with st.chat_message("assistant"):
        st.markdown(respuesta_bot)
