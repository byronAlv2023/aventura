def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

def main():
    compra_1 = 600
    compra_2 = 1200
    porcentaje_descuento = 15

    # Llamadas a la función calcular_descuento
    descuento_1 = calcular_descuento(compra_1)
    descuento_2 = calcular_descuento(compra_2, porcentaje_descuento)

    # Calcular el monto final a pagar después del descuento
    compra_final_1 = compra_1 - descuento_1
    compra_final_2 = compra_2 - descuento_2

    # Mostrar resultados
    print("Resultados de la primera llamada:")
    print("Total de la compra:", compra_1)
    print("Porcentaje de descuento aplicado:", 10, "%")
    print("Total del descuento:", descuento_1)
    print("Total final a pagar después del descuento:", compra_final_1)

    print("Resultados de la segunda llamada:")
    print("Total de la compra:", compra_2)
    print("Porcentaje de descuento aplicado:", 15, "%")
    print("Total del descuento:", descuento_2)
    print("Total final a pagar después del descuento:", compra_final_2)


if __name__ == "__main__":
    main()