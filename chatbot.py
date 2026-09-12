import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gluper Box Bot", page_icon="🥗", layout="centered")

st.title("🥗 Asistente Virtual — Gluper Box 📦")
st.write("¡Hola! Bienvenido al chat de **Gluper**. ¿En qué te podemos ayudar hoy?")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy tu asistente de Gluper Box. Selecciona una opción o escribe tu pregunta sobre el menú de la semana, precios o pedidos."}
    ]

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Menús por día
menus = {
    "lunes": "🥑 **Lunes — Arranque de Energía Fit:**\n- **Desayuno:** Omelette de claras con espinaca + Café verde ☕\n- **Almuerzo:** Pechuga a la plancha con quinoa + Té verde 🥗\n- **Cena:** Ensalada de atún con aguacate 🥑\n- **Postre:** Mousse proteico de frutos rojos 🍓\n- **Suplemento:** Multivitamínico + Omega 3 💊",
    "martes": "🥗 **Martes — Digestión Ligera:**\n- **Desayuno:** Smoothie bowl de espirulina y banano 🍌\n- **Almuerzo:** Filete de salmón al horno con espárragos 🐟\n- **Cena:** Crema de calabacín y semillas de chía 🥣\n- **Postre:** Gelatina ligera sin azúcar 🍧\n- **Suplemento:** Probióticos + Magnesio 💊",
    "miercoles": "🍓 **Miércoles — Vitalidad y Antioxidantes:**\n- **Desayuno:** Pancakes de avena con chía y fresas 🥞\n- **Almuerzo:** Bowl de pollo, camote y garbanzos 🥙\n- **Cena:** Sopa de verduras desintoxicante 🍜\n- **Postre:** Yogur griego con arándanos 🫐\n- **Suplemento:** Vitamina C + Colágeno 💊",
    "jueves": "🌿 **Jueves — Equilibrio y Sabor:**\n- **Desayuno:** Toast de pan integral con aguacate y huevo 🍞\n- **Almuerzo:** Carne magra salteada con brócoli y arroz integral 🥩\n- **Cena:** Ensalada mediterránea con queso feta 🥗\n- **Postre:** Manzana horneada con canela 🍎\n- **Suplemento:** Complejo B + Zinc 💊",
    "viernes": "🔥 **Viernes — Cierre Semanal:**\n- **Desayuno:** Waffles de proteína con miel de agave 🧇\n- **Almuerzo:** Tacos saludables de lechuga con pavo molido 🌮\n- **Cena:** Wrap integral de pollo y vegetales 🌯\n- **Postre:** Choco-fit mugcake sin azúcar 🍫\n- **Suplemento:** Multivitamínico + Omega 3 💊",
    "sabado": "🍊 **Sábado — Detox y Renovación:**\n- **Desayuno:** Jugo verde desintoxicante + Huevos revueltos 🍳\n- **Almuerzo:** Ceviche vegetal de hongos y palmito 🥗\n- **Cena:** Pizza con base de coliflor y vegetales 🍕\n- **Postre:** Parfait de chía con mango 🥭\n- **Suplemento:** Espirulina + Antioxidantes 💊",
    "domingo": "✨ **Domingo — Recarga Saludable:**\n- **Desayuno:** Omelette champiñones y queso bajo en grasa 🍳\n- **Almuerzo:** Pechuga de pavo al romero con puré de camote 🦃\n- **Cena:** Ensalada de espinacas, fresas y nueces 🥗\n- **Postre:** Pudding de chía y vainilla 🍮\n- **Suplemento:** Calcio + Vitamina D 💊"
}

# Opciones rápidas con botones
st.subheader("💡 Consultas rápidas:")
col1, col2 = st.columns(2)

opcion = None
if col1.button("📦 Ver qué incluye la caja"):
    opcion = "incluye"
if col2.button("💵 Ver Precios y Planes"):
    opcion = "precios"
if col1.button("🛒 ¿Cómo hacer mi pedido?"):
    opcion = "pedido"
if col2.button("📅 Ver Menú Completo (Semanal)"):
    opcion = "menu_completo"

# Entrada del usuario por texto
prompt_usuario = st.chat_input("Escribe tu duda o el día de la semana (ej. 'menú del viernes')...")

# Lógica del bot
respuesta_bot = ""

if opcion == "incluye":
    respuesta_bot = "📦 **La Gluper Box incluye:**\n- 3 Comidas completas al día (Desayuno, Almuerzo, Cena)\n- 1 Postre saludable de media tarde\n- Bebidas naturales diarias\n- Suplementos y vitaminas de venta libre\n- Guía nutricional personalizada 📋"
elif opcion == "precios":
    respuesta_bot = "💵 **Precios y Planes de Gluper Box:**\n- 📦 **Plan Semanal (7 Días):** Q450.00 / $58.00 USD (Incluye 21 comidas, 7 postres, bebidas y suplementos)\n- 📦 **Plan Quincenal (14 Días):** Q850.00 / $110.00 USD (Ahorras 5%)\n- 📦 **Plan Mensual (30 Días):** Q1,600.00 / $205.00 USD (Ahorras 12% + Envío gratis) 🚚\n\n*Aceptamos tarjetas de crédito, débito y transferencia bancaria.* 💳"
elif opcion == "pedido":
    respuesta_bot = "🛒 **¿Cómo pedir?** Cerramos pedidos todos los **VIERNES** a las 6:00 PM para garantizar ingredientes 100% frescos la semana siguiente. Escríbenos a nuestro Instagram **@gluper** o por WhatsApp para tomar tus datos de entrega. 📲"
elif opcion == "menu_completo":
    respuesta_bot = "📅 **Menú de la Semana Gluper Box:**\n Puedes preguntarme por cualquier día en específico (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado o Domingo).\n\n" + "\n\n".join(menus.values())
elif prompt_usuario:
    user_input = prompt_usuario.lower()
    
    # Buscar días específicos
    if "lunes" in user_input:
        respuesta_bot = menus["lunes"]
    elif "martes" in user_input:
        respuesta_bot = menus["martes"]
    elif "miercoles" in user_input or "miércoles" in user_input:
        respuesta_bot = menus["miercoles"]
    elif "jueves" in user_input:
        respuesta_bot = menus["jueves"]
    elif "viernes" in user_input:
        respuesta_bot = menus["viernes"]
    elif "sabado" in user_input or "sábado" in user_input:
        respuesta_bot = menus["sabado"]
    elif "domingo" in user_input:
        respuesta_bot = menus["domingo"]
    elif "precio" in user_input or "costo" in user_input or "cuanto" in user_input or "cuánto" in user_input or "plan" in user_input:
        respuesta_bot = "💵 **Precios de Gluper Box:**\n- **Plan Semanal (7 días):** Q450.00\n- **Plan Quincenal (14 días):** Q850.00\n- **Plan Mensual (30 días):** Q1,600.00 (Envío gratis) 🚚"
    elif "menu" in user_input or "menú" in user_input or "comida" in user_input:
        respuesta_bot = "Nuestros menús cambian a diario. Escribe el día que deseas consultar (ej. *'menú del martes'*) o haz clic en el botón de **Ver Menú Completo** arriba. 🥑"
    else:
        respuesta_bot = "¡Gracias por escribirnos! Un asesor humano de Gluper responderá a tu consulta muy pronto. Si prefieres atención inmediata, escríbenos a nuestro Instagram **@gluper**. 📩"

# Mostrar respuesta en pantalla
if respuesta_bot:
    if prompt_usuario:
        st.session_state.messages.append({"role": "user", "content": prompt_usuario})
        with st.chat_message("user"):
            st.markdown(prompt_usuario)
            
    st.session_state.messages.append({"role": "assistant", "content": respuesta_bot})
    with st.chat_message("assistant"):
        st.markdown(respuesta_bot)
