import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gluper Box Bot", page_icon="🥗", layout="centered")

st.title("🥗 Asistente Virtual — Gluper Box 📦")
st.write("¡Hola! Bienvenido al chat oficial de **Gluper Box**. ¿En qué te puedo ayudar hoy?")

# Menús por día
menus = {
    "lunes": "🥑 **Lunes — Arranque de Energía Fit:**\n* **Desayuno:** Omelette de claras con espinaca + Café verde ☕\n* **Almuerzo:** Pechuga a la plancha con quinoa + Té verde 🥗\n* **Cena:** Ensalada de atún con aguacate 🥑\n* **Postre:** Mousse proteico de frutos rojos 🍓\n* **Suplemento:** Multivitamínico + Omega 3 💊",
    "martes": "🥗 **Martes — Digestión Ligera:**\n* **Desayuno:** Smoothie bowl de espirulina y banano 🍌\n* **Almuerzo:** Filete de salmón al horno con espárragos 🐟\n* **Cena:** Crema de calabacín y semillas de chía 🥣\n* **Postre:** Gelatina ligera sin azúcar 🍧\n* **Suplemento:** Probióticos + Magnesio 💊",
    "miercoles": "🍓 **Miércoles — Vitalidad y Antioxidantes:**\n* **Desayuno:** Pancakes de avena con chía y fresas 🥞\n* **Almuerzo:** Bowl de pollo, camote y garbanzos 🥙\n* **Cena:** Sopa de verduras desintoxicante 🍜\n* **Postre:** Yogur griego con arándanos 🫐\n* **Suplemento:** Vitamina C + Colágeno 💊",
    "jueves": "🌿 **Jueves — Equilibrio y Sabor:**\n* **Desayuno:** Toast de pan integral con aguacate y huevo 🍞\n* **Almuerzo:** Carne magra salteada con brócoli y arroz integral 🥩\n* **Cena:** Ensalada mediterránea con queso feta 🥗\n* **Postre:** Manzana horneada con canela 🍎\n* **Suplemento:** Complejo B + Zinc 💊",
    "viernes": "🔥 **Viernes — Cierre Semanal:**\n* **Desayuno:** Waffles de proteína con miel de agave 🧇\n* **Almuerzo:** Tacos saludables de lechuga con pavo molido 🌮\n* **Cena:** Wrap integral de pollo y vegetales 🌯\n* **Postre:** Choco-fit mugcake sin azúcar 🍫\n* **Suplemento:** Multivitamínico + Omega 3 💊",
    "sabado": "🍊 **Sábado — Detox y Renovación:**\n* **Desayuno:** Jugo verde desintoxicante + Huevos revueltos 🍳\n* **Almuerzo:** Ceviche vegetal de hongos y palmito 🥗\n* **Cena:** Pizza con base de coliflor y vegetales 🍕\n* **Postre:** Parfait de chía con mango 🥭\n* **Suplemento:** Espirulina + Antioxidantes 💊",
    "domingo": "✨ **Domingo — Recarga Saludable:**\n* **Desayuno:** Omelette de champiñones y queso bajo en grasa 🍳\n* **Almuerzo:** Pechuga de pavo al romero con puré de camote 🦃\n* **Cena:** Ensalada de espinacas, fresas y nueces 🥗\n* **Postre:** Pudding de chía y vainilla 🍮\n* **Suplemento:** Calcio + Vitamina D 💊"
}

# Inicializar historial
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy tu asistente de Gluper Box. Selecciona una opción abajo o escribe tu consulta. 📦"}
    ]

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.markdown("---")

# --- ÚNICOS 3 BOTONES PRINCIPALES ---
st.subheader("💡 Opciones Rápidas")
c1, c2, c3 = st.columns(3)

btn_precios = c1.button("💵 Precios")
btn_incluye = c2.button("📦 ¿Qué incluye?")
btn_pedido = c3.button("🛒 ¿Cómo pedir?")

# --- SELECTOR DE MENÚ POR DÍA O SEMANA COMPLETA ---
st.subheader("🥑 CONSULTAR MENÚ")
col_sel, col_btn_menu = st.columns([2, 1])
with col_sel:
    opcion_menu = st.selectbox(
        "Selecciona el día o la semana completa:",
        ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo", "Semana Completa"],
        label_visibility="collapsed"
    )
ver_menu_click = col_btn_menu.button("🔎 Ver Menú")

# Entrada de texto del usuario
prompt_usuario = st.chat_input("Escribe tu duda aquí...")

# Lógica del chatbot
respuesta_bot = ""

# Acciones por Botones
if btn_precios:
    respuesta_bot = "💵 **Precios y Planes de Gluper Box:**\n* 📦 **Plan Semanal (7 Días):** Q450.00 / $58.00 USD (21 comidas + 7 postres + bebidas y suplementos)\n* 📦 **Plan Quincenal (14 Días):** Q850.00 / $110.00 USD (Ahorras 5%)\n* 📦 **Plan Mensual (30 Días):** Q1,600.00 / $205.00 USD (Ahorras 12% + Envío gratis) 🚚\n\n*Aceptamos tarjetas de crédito, débito y transferencia bancaria.* 💳"

elif btn_incluye:
    respuesta_bot = "📦 **La Gluper Box incluye:**\n* 3 Comidas completas al día (Desayuno, Almuerzo, Cena)\n* 1 Postre saludable de media tarde\n* Bebidas naturales diarias\n* Suplementos y vitaminas de venta libre\n* Guía nutricional personalizada 📋"

elif btn_pedido:
    respuesta_bot = "🛒 **¿Cómo pedir?** Cerramos pedidos todos los **VIERNES** a las 6:00 PM para garantizar ingredientes 100% frescos la semana siguiente. Escríbenos a nuestro Instagram **@gluper** o por WhatsApp para tomar tus datos de entrega. 📲"

elif ver_menu_click:
    dia_key = opcion_menu.lower().replace("é", "e").replace("á", "a")
    if dia_key == "semana completa":
        respuesta_bot = "📅 **Menú Completo de la Semana Gluper Box:**\n\n" + "\n\n---\n\n".join(menus.values())
    else:
        respuesta_bot = menus[dia_key]

# Acciones por Texto del Usuario
elif prompt_usuario:
    text = prompt_usuario.lower().strip()
    
    # 🤫 FUNCIÓN OCULTA / EASTER EGG (Respuesta ruda a clientes indecisos o tacaños)
    frases_ocultas = [
        "no quiero", "si no quiero", "esta caro", "está caro", "mas barato", 
        "más barato", "otro lado", "muy caro", "no me gusta", "mejor no"
    ]
    
    if any(frase in text for frase in frases_ocultas):
        respuesta_bot = "🚨 **Tonces largate de aqui que estas ocupando espacio para los demas clientes.** 😤"
    
    # Menú genérico
    elif text in ["menu", "menú", "comida", "comidas"]:
        respuesta_bot = "🥑 Puedes seleccionar un día específico o la **'Semana Completa'** en el menú desplegable arriba 👆 o escribirme directamente el día que buscas (ej. *'menú del martes'*)."
    
    # Días por texto
    elif "lunes" in text:
        respuesta_bot = menus["lunes"]
    elif "martes" in text:
        respuesta_bot = menus["martes"]
    elif "miercoles" in text or "miércoles" in text:
        respuesta_bot = menus["miercoles"]
    elif "jueves" in text:
        respuesta_bot = menus["jueves"]
    elif "viernes" in text:
        respuesta_bot = menus["viernes"]
    elif "sabado" in text or "sábado" in text:
        respuesta_bot = menus["sabado"]
    elif "domingo" in text:
        respuesta_bot = menus["domingo"]
    elif "semana" in text or "completo" in text:
        respuesta_bot = "📅 **Menú Completo de la Semana Gluper Box:**\n\n" + "\n\n---\n\n".join(menus.values())
        
    else:
        respuesta_bot = "¡Gracias por escribirnos! 📩 Un asesor humano de Gluper responderá a tu consulta muy pronto. Si prefieres atención inmediata, escríbenos por Instagram a **@gluper**."

# Publicar respuesta en pantalla
if respuesta_bot:
    if prompt_usuario:
        st.session_state.messages.append({"role": "user", "content": prompt_usuario})
        with st.chat_message("user"):
            st.markdown(prompt_usuario)
            
    st.session_state.messages.append({"role": "assistant", "content": respuesta_bot})
    with st.chat_message("assistant"):
        st.markdown(respuesta_bot)
