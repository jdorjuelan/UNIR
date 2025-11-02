#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calculadora_promedios.py

Jonathan Dave Orjuela Navarrete
"""

from typing import List, Tuple

UMBRAL_DEFECTO = 5.0


def _leer_calificacion() -> float:
    # Lee una calificación válida (0 a 10). Acepta coma o punto decimal.
    while True:
        entrada = input("Ingrese la calificación (0 a 10): ").strip()
        # Permitir coma decimal y se reemplaza por punto
        entrada = entrada.replace(",", ".")
        try:
            valor = float(entrada)
            if 0.0 <= valor <= 10.0:
                return valor
            print("La calificación debe estar entre 0 y 10. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número (ej. 7.5).")


def _leer_materia() -> str:
    #Lee un nombre de materia no vacío.
    while True:
        nombre = input("Ingrese el nombre de la materia: ").strip()
        if nombre:
            return nombre
        print("El nombre de la materia no puede estar vacío.")


def _leer_continuar() -> bool:
    #Pregunta si se desea continuar (S/N). Devuelve True si continuar.
    while True:
        r = input("¿Desea ingresar otra materia? (S/N): ").strip().lower()
        if r in ("s", "si", "sí"):
            return True
        if r in ("n", "no"):
            return False
        print("Respuesta no válida. Escriba S para sí o N para no.")


def ingresar_calificaciones() -> Tuple[List[str], List[float]]:
    #Ingreso de Materias y Calificaciones
    materias: List[str] = []
    calificaciones: List[float] = []

    print("\n=== Ingreso de materias y calificaciones ===")
    while True:
        materia = _leer_materia()
        calificacion = _leer_calificacion()
        materias.append(materia)
        calificaciones.append(calificacion)
        if not _leer_continuar():
            break

    return materias, calificaciones


def calcular_promedio(calificaciones: List[float]) -> float:
    #Devuelve el promedio de la lista de calificaciones. Retorna 0.0 si está vacía.
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones: List[float], umbral: float = UMBRAL_DEFECTO) -> Tuple[List[int], List[int]]:
    #Devuelve dos listas de índices: (aprobadas, reprobadas), según el umbral. Aprobada: calificación >= umbral
    idx_aprobadas: List[int] = []
    idx_reprobadas: List[int] = []
    for i, nota in enumerate(calificaciones):
        if nota >= umbral:
            idx_aprobadas.append(i)
        else:
            idx_reprobadas.append(i)
    return idx_aprobadas, idx_reprobadas


def encontrar_extremos(calificaciones: List[float]) -> Tuple[int, int]:
    #Encontrar los extremos de las calificaciones.
    if not calificaciones:
        return -1, -1
    idx_max = max(range(len(calificaciones)), key=lambda i: calificaciones[i])
    idx_min = min(range(len(calificaciones)), key=lambda i: calificaciones[i])
    return idx_max, idx_min


def _imprimir_resumen(materias: List[str],
                      calificaciones: List[float],
                      promedio: float,
                      idx_aprobadas: List[int],
                      idx_reprobadas: List[int],
                      idx_max: int,
                      idx_min: int,
                      umbral: float) -> None:
    #Imprime el resumen final en formato legible.
    print("\n================= RESUMEN FINAL =================")
    if not materias:
        print("No se ingresaron materias. No hay datos para mostrar.")
        print("=================================================\n")
        return

    # Listado de materias
    print("\nMaterias y calificaciones:")
    print("-" * 45)
    for i, (m, c) in enumerate(zip(materias, calificaciones), start=1):
        print(f"{i:2d}. {m:<25} -> {c:>5.2f}")
    print("-" * 45)

    # Promedio
    print(f"\nPromedio general: {promedio:.2f}")

    # Aprobadas / Reprobadas
    print(f"\nUmbral de aprobación: {umbral:.2f}")
    if idx_aprobadas:
        aprobadas = ", ".join(materias[i] for i in idx_aprobadas)
        print(f"Materias aprobadas ({len(idx_aprobadas)}): {aprobadas}")
    else:
        print("Materias aprobadas (0): ninguna")

    if idx_reprobadas:
        reprobadas = ", ".join(materias[i] for i in idx_reprobadas)
        print(f"Materias reprobadas ({len(idx_reprobadas)}): {reprobadas}")
    else:
        print("Materias reprobadas (0): ninguna")

    # Extremos
    if idx_max != -1 and idx_min != -1:
        print("\nExtremos:")
        print(f"Mejor calificación: {materias[idx_max]} -> {calificaciones[idx_max]:.2f}")
        print(f"Peor calificación : {materias[idx_min]} -> {calificaciones[idx_min]:.2f}")

    print("=================================================\n")


def main() -> None:
    print("Calculadora de Promedios")
    materias, calificaciones = ingresar_calificaciones()

    if not materias:
        # Manejo de caso especial: sin datos
        _imprimir_resumen(materias, calificaciones, 0.0, [], [], -1, -1, UMBRAL_DEFECTO)
        return

    promedio = calcular_promedio(calificaciones)
    idx_aprobadas, idx_reprobadas = determinar_estado(calificaciones, UMBRAL_DEFECTO)
    idx_max, idx_min = encontrar_extremos(calificaciones)

    _imprimir_resumen(materias, calificaciones, promedio, idx_aprobadas, idx_reprobadas, idx_max, idx_min, UMBRAL_DEFECTO)


if __name__ == "__main__":
    main()
