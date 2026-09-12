import sys
import time

def escribir_lento(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def chatbot_gluper():
    print("=" * 60)
    print("🤖 ¡Hola! Bienvenido al asistente virtual de GLUPER BOX 🥗📦")
    print("=" * 60)
    escribir_lento("Tu solución fácil para comer sano, ahorrar tiempo y lograr tus metas.")
    
    nombre = input("\n👉 ¿Cómo te llamas?: ")
    escribir_lento(f"\n¡Mucho gusto, {nombre}! ✨ ¿En qué te puedo ayudar hoy?")

    while True:
        print("\n" + "-" * 50)
        print("1️⃣ Ver qué incluye la caja Gluper Box 📦")
        print("2️⃣ Consultar el menú y suplementos del LUNES 🥑")
        print("3️⃣ Ver información de precios y ahorro 💸")
        print("4️⃣ ¿Cómo hacer mi pedido de la semana? 🛒")
        print("5️⃣ Hablar con un asesor humano 👤")
        print("6️⃣ Salir 👋")
        print("-" * 50)
        
        opcion = input("Escribe el número de tu opción (1-6): ").strip()

        if opcion == "1":
            escribir_lento("\n📦 Nuestra Gluper Box incluye:")
            escribir_lento("• 3 Comidas completas al día (Desayuno, Almuerzo y Cena) 🥗")
            escribir_lento("• 1 Postre de media tarde saludable 🍓")
            escribir_lento("• Bebidas naturales de acompañamiento 🥤")
            escribir_lento("• Suplementos/Vitaminas de venta libre recomendados 💊")
            escribir_lento("• Guía nutricional paso a paso para la semana 📋")

        elif opcion == "2":
            escribir_lento("\n🥑 Menú Ejemplo — LUNES (Arranque de Energía):")
            escribir_lento("🍳 Desayuno: Omelette de claras con espinacas + Café verde")
            escribir_lento("🥗 Almuerzo: Pechuga a la plancha con quinoa y vegetales + Té verde")
            escribir_lento("🌙 Cena: Ensalada de atún con aguacate y ajonjolí + Infusión")
            escribir_lento("🍓 Postre: Mousse proteico de yogur griego con frutos rojos")
            escribir_lento("💊 Suplementos: Multivitamínico + Omega 3 (Venta libre)")

        elif opcion == "3":
            escribir_lento("\n💸 Información de Ahorro:")
            escribir_lento("Comer fuera o pedir delivery diario te cuesta más dinero y calorías.")
            escribir_lento("Con Gluper aseguras nutrición completa, ahorras más de 10 horas de cocina a la semana y cero desperdicios.")

        elif opcion == "4":
            escribir_lento("\n🛒 ¿Cómo pedir?")
            escribir_lento("Los pedidos para la semana cierran el VIERNES.")
            escribir_lento("Puedes coordinar tu envío directo a través de nuestro Instagram @gluper o WhatsApp.")

        elif opcion == "5":
            escribir_lento(f"\n👤 ¡Entendido {nombre}! Un especialista de Gluper te responderá en breve. Déjanos tu número de teléfono.")
            input("Escribe tu número aquí: ")
            escribir_lento("✅ ¡Gracias! Te contactaremos hoy mismo.")

        elif opcion == "6":
            escribir_lento(f"\n¡Gracias por consultar a Gluper Box, {nombre}! ¡Que tengas un excelente día saludable! 🥗✨")
            break

        else:
            escribir_lento("\n⚠️ Opción no válida. Por favor ingresa un número del 1 al 6.")

if __name__ == "__main__":
    chatbot_gluper()
