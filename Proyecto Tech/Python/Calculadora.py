import time

class CalculadoraHuellaCarbono:
    def __init__(self):
        self.puntaje_total = 0
        self.pregunta_actual = 1
        self.total_preguntas = 24
        self.puntajes_categorias = [0, 0, 0, 0]
        self.categorias = [
            {'nombre': '🛻 Transporte', 'peso': 1.5, 'emoji': '🛻'},
            {'nombre': '⚡ Energía', 'peso': 1.8, 'emoji': '⚡'},
            {'nombre': '🍽️ Alimentación', 'peso': 1.2, 'emoji': '🍽️'},
            {'nombre': '🛒 Consumo', 'peso': 1.0, 'emoji': '🛒'}
        ]
        self.equivalencia_arbol = 21


    def mostrar_progreso(self):
        progreso = (self.pregunta_actual / self.total_preguntas) * 100
        barra = f"[{'■' * int(progreso//5)}{'□' * (20 - int(progreso//5))}]"
        print(f"\nProgreso: {barra} {int(progreso)}%\n")
        time.sleep(0.3)

    def mostrar_pregunta(self, categoria_idx, pregunta, opciones):
        print(f"\n{self.categorias[categoria_idx]['emoji']} {self.categorias[categoria_idx]['nombre']}")
        self.mostrar_progreso()
        print(f"Pregunta {self.pregunta_actual}/24: {pregunta}")
        for idx, opcion in enumerate(opciones, 1):
            print(f"{idx}. {opcion['texto']}")
        
        while True:
            try:
                seleccion = int(input("\nSelecciona una opción (1-{}): ".format(len(opciones))))
                if 1 <= seleccion <= len(opciones):
                    puntaje = opciones[seleccion-1]['valor'] * self.categorias[categoria_idx]['peso']
                    self.puntaje_total += puntaje
                    self.puntajes_categorias[categoria_idx] += puntaje
                    self.pregunta_actual += 1
                    time.sleep(0.2)
                    return
                else:
                    print("⚠️ Opción inválida. Intenta nuevamente.")
            except ValueError:
                print("⚠️ Entrada inválida. Ingresa un número.")

    # █████████████████████████████ PREGUNTAS █████████████████████████████
    def hacer_preguntas_transporte(self):
        # Preguntas 1-6
        self.mostrar_pregunta(0, "¿Cuántos kilómetros recorres semanalmente en vehículo particular?", [
            {'texto': 'Menos de 50 km', 'valor': 50},
            {'texto': '50-250 km', 'valor': 150},
            {'texto': 'Más de 250 km', 'valor': 400}
        ])
        
        self.mostrar_pregunta(0, "¿Tu vehículo es a gasolina, diésel, híbrido o eléctrico?", [
            {'texto': 'Gasolina', 'valor': 100},
            {'texto': 'Diésel', 'valor': 80},
            {'texto': 'Híbrido', 'valor': 30},
            {'texto': 'Eléctrico', 'valor': 10}
        ])

        self.mostrar_pregunta(0, "¿Compartes tu vehículo con otras personas?", [
            {'texto': 'Siempre', 'valor': 20},
            {'texto': 'Ocasionalmente', 'valor': 40},
            {'texto': 'Nunca', 'valor': 0}
        ])

        self.mostrar_pregunta(0, "¿Utilizas transporte público regularmente?", [
            {'texto': 'Más de 5 veces/semana', 'valor': 20},
            {'texto': '2-4 veces/semana', 'valor': 40},
            {'texto': 'Menos de 2 veces', 'valor': 60},
            {'texto': 'Nunca', 'valor': 0}
        ])

        self.mostrar_pregunta(0, "¿Usas medios de transporte no motorizados?", [
            {'texto': 'Diariamente', 'valor': 10},
            {'texto': '3-4 veces/semana', 'valor': 30},
            {'texto': 'Ocasionalmente', 'valor': 50},
            {'texto': 'Nunca', 'valor': 0}
        ])

        self.mostrar_pregunta(0, "¿Viajas en avión al año?", [
            {'texto': 'Más de 4 vuelos', 'valor': 150},
            {'texto': '2-3 vuelos', 'valor': 80},
            {'texto': '1 vuelo', 'valor': 30},
            {'texto': 'No vuelo', 'valor': 0}
        ])

    def hacer_preguntas_energia(self):
    # Pregunta 7 
        self.mostrar_pregunta(1, "¿Cuál es el promedio mensual de tu factura de energía eléctrica?", [
            {'texto': 'Menos de $50', 'valor': 50},
            {'texto': '$50-$150', 'valor': 100},
            {'texto': 'Más de $150', 'valor': 200}
        ])

    # Pregunta 8
        self.mostrar_pregunta(1, "¿Tu hogar tiene paneles solares u otra fuente renovable?", [
            {'texto': 'Sí, totalmente renovable', 'valor': 10},
            {'texto': 'Parcialmente renovable', 'valor': 100},
            {'texto': 'No, solo energía convencional', 'valor': 200}
        ])

    # Pregunta 9
        self.mostrar_pregunta(1, "¿Qué usas para cocinar o calentar agua?", [
            {'texto': 'Gas natural', 'valor': 50},
            {'texto': 'Leña/carbón', 'valor': 70},
            {'texto': 'Electricidad', 'valor': 30},
            {'texto': 'Otro combustible', 'valor': 40}
        ])

    # Pregunta 10
        self.mostrar_pregunta(1, "¿Usas electrodomésticos de bajo consumo?", [
            {'texto': 'Sí, todos', 'valor': 20},
            {'texto': 'Algunos', 'valor': 40},
            {'texto': 'No', 'valor': 60}
        ])

    # Pregunta 11
        self.mostrar_pregunta(1, "¿Apagas los aparatos electrónicos completamente?", [
            {'texto': 'Siempre apagados', 'valor': 10},
            {'texto': 'Algunos en standby', 'valor': 30},
            {'texto': 'Suelo dejarlos en standby', 'valor': 60}
        ])

    # Pregunta 12
        self.mostrar_pregunta(1, "¿Aprovechas la luz natural?", [
            {'texto': 'Siempre la aprovecho', 'valor': 10},
            {'texto': 'A veces uso artificial', 'valor': 30},
            {'texto': 'Frecuentemente enciendo luces', 'valor': 60}
        ])

    def hacer_preguntas_alimentacion(self):
     # Pregunta 13
        self.mostrar_pregunta(2, "¿Frecuencia de consumo de carne roja semanal?", [
            {'texto': 'Diariamente', 'valor': 100},
            {'texto': '3-4 veces', 'valor': 60},
            {'texto': '1-2 veces', 'valor': 30},
            {'texto': 'Nunca', 'valor': 0}
        ])

    # Pregunta 14
        self.mostrar_pregunta(2, "¿Consumo de productos lácteos?", [
            {'texto': 'Diariamente', 'valor': 40},
            {'texto': '3-4 veces/semana', 'valor': 25},
            {'texto': 'Ocasionalmente', 'valor': 15},
            {'texto': 'Nunca (vegano)', 'valor': 0}
        ])
        
    # Pregunta 15

        self.mostrar_pregunta(2, "¿Incluyes frutas/verduras en tu dieta?", [
            {'texto': '7+ porciones diarias', 'valor': 50},   
            {'texto': '4-6 porciones', 'valor': 35},         
            {'texto': '1-3 porciones', 'valor': 20},         
            {'texto': 'Casi nunca', 'valor': 10}           
        ])
        
    # Pregunta 16

        self.mostrar_pregunta(2, "¿Productos locales y de temporada?", [
            {'texto': 'Siempre', 'valor': 15},
            {'texto': 'Más del 50%', 'valor': 25},
            {'texto': 'Menos del 30%', 'valor': 40},
            {'texto': 'Nunca', 'valor': 60}
        ])

    # Pregunta 17
        self.mostrar_pregunta(2, "¿Productos orgánicos o sostenibles?", [
            {'texto': 'Más del 70%', 'valor': 20},
            {'texto': 'Alrededor del 50%', 'valor': 35},
            {'texto': 'Menos del 30%', 'valor': 50},
            {'texto': 'Nunca', 'valor': 70}
        ])
        
    def hacer_preguntas_consumo(self):
    # Pregunta 18

        self.mostrar_pregunta(2, "¿Desperdicias comida frecuentemente?", [
            {'texto': 'Más de 3 veces/semana', 'valor': 60},
            {'texto': '1-2 veces/semana', 'valor': 40},
            {'texto': 'Casi nunca', 'valor': 20},
            {'texto': 'Planifico para no desperdiciar', 'valor': 10}
        ])

    # Pregunta 19
        self.mostrar_pregunta(3, "¿Reparas o donas objetos antes de desecharlos?", [
        {'texto': 'Siempre', 'valor': 10},
        {'texto': 'A veces', 'valor': 30},
        {'texto': 'Casi nunca', 'valor': 60}
    ])

    # Pregunta 20
        self.mostrar_pregunta(3, "¿Con qué frecuencia compras ropa nueva al mes?", [
            {'texto': 'Menos de 2 prendas', 'valor': 10},
            {'texto': '3-5 prendas', 'valor': 25},
            {'texto': '6-10 prendas', 'valor': 45},
            {'texto': 'Más de 10 prendas', 'valor': 70}
        ])

    # Pregunta 21
        self.mostrar_pregunta(3, "¿Adquieres productos de segunda mano o reutilizados?", [
            {'texto': 'Más del 50% de mis compras', 'valor': 20},
            {'texto': '25-50% de mis compras', 'valor': 35},
            {'texto': 'Menos del 25%', 'valor': 50},
            {'texto': 'Nunca', 'valor': 70}
        ])

    # Pregunta 22
        self.mostrar_pregunta(3, "¿Usas bolsas reutilizables o envases retornables?", [
            {'texto': 'Siempre', 'valor': 10},
            {'texto': 'Casi siempre', 'valor': 25},
            {'texto': 'Ocasionalmente', 'valor': 45},
            {'texto': 'Nunca', 'valor': 65}
        ])

    # Pregunta 23 (Nota: Similar a la 19 pero con opciones diferentes)
        self.mostrar_pregunta(3, "¿Reparas objetos antes de desecharlos?", [
            {'texto': 'Siempre lo intento', 'valor': 15},
            {'texto': 'Con algunos objetos', 'valor': 30},
            {'texto': 'Rara vez', 'valor': 50},
            {'texto': 'Nunca', 'valor': 70}
        ])

    # Pregunta 24
        self.mostrar_pregunta(3, "¿Tienes hábitos de consumo consciente?", [
            {'texto': 'Siempre planeo mis compras', 'valor': 10},
            {'texto': 'Mayoría consciente', 'valor': 25},
            {'texto': 'Compro por impulso a veces', 'valor': 45},
            {'texto': 'No controlo mis compras', 'valor': 70}
        ])

        

        # ... (Todas las preguntas implementadas siguiendo este patrón)
        # Implementa las 24 preguntas de igual forma

    # ████████████████████████████ RESULTADOS ████████████████████████████
    
    def generar_recomendaciones(self):
        recomendaciones = []
        if self.puntajes_categorias[0] > 5000:
            recomendaciones.append("🚗 Comparte vehículo o usa transporte público")
        if self.puntajes_categorias[1] > 4000:
            recomendaciones.append("💡 Reemplaza bombillas por LED")
        if self.puntajes_categorias[2] > 3000:
            recomendaciones.append("🍽️ Reduce consumo de carne roja")
        if self.puntajes_categorias[3] > 2000:
            recomendaciones.append("🛒 Compra productos de segunda mano")
        return recomendaciones if recomendaciones else ["🌟 ¡Eres un ejemplo de sostenibilidad!"]

    def calcular_equivalencias(self, huella_anual):
        return {
            'arboles': huella_anual / self.equivalencia_arbol,
            'vuelos': huella_anual / 250,
            'autos': huella_anual / 4600
        }

    def mostrar_resultados(self):
        huella_anual = self.puntaje_total * 12
        equivalencias = self.calcular_equivalencias(huella_anual)
        
        print("\n" + "="*55)
        print(f"🌍 Huella aproximada anual: {huella_anual:,.0f} kg CO₂")
        print(f"🌳 Árboles necesarios: {equivalencias['arboles']:.0f}")
        print(f"✈️ Vuelos equivalentes: {equivalencias['vuelos']:.1f}")
        print(f"🚗 Autos equivalentes: {equivalencias['autos']:.1f}")
        
        print("\n📌 Recomendaciones:")
        for idx, rec in enumerate(self.generar_recomendaciones(), 1):
            print(f"{idx}. {rec}")
            time.sleep(0.5)

    def calcular(self):
        print("\n=== 🌱 CALCULADORA DE HUELLA DE CARBONO ===\n")
        self.hacer_preguntas_transporte()
        self.hacer_preguntas_energia()
        self.hacer_preguntas_alimentacion()
        self.hacer_preguntas_consumo()
        self.mostrar_resultados()

if __name__ == "__main__":
    calculadora = CalculadoraHuellaCarbono()
    calculadora.calcular()