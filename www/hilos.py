import psycopg2
import threading
import time

MAX_HILOS = 30

exito_total = 0
fallo_total = 0
lock = threading.Lock()

#Función para reservar un asiento
def reservar_asiento(id_hilo):
    global exito_total, fallo_total

    try:
        #Conectar a la base de datos
        conn = psycopg2.connect(
            dbname="proyecto_2",
            user="usuario-db",
            password="contraseña-db",
            host="localhost",
            port="5434" #Verificar el puerto
        )

        cursor = conn.cursor()

        cursor.execute("BEGIN")

        cursor.execute("""
            UPDATE asientos 
            SET estado = 'reservado' 
            WHERE id_asiento = (
                SELECT id_asiento 
                FROM asientos 
                WHERE estado = 'disponible' 
                LIMIT 1 FOR UPDATE SKIP LOCKED
            ) RETURNING id_asiento
        """)
        
        result = cursor.fetchone()
        if result:
            id_asiento = result[0]
            print(f"Hilo {id_hilo} logró reservar el asiento {id_asiento} con éxito.")
            with lock:
                exito_total += 1
        else:
            print(f"Hilo {id_hilo} no logró reservar ningún asiento.")
            with lock:
                fallo_total += 1

        cursor.execute("COMMIT")

        #Cerrar la conexion
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Hilo {id_hilo} no pudo conectar a la DB: {e}")

#Funcion principal para crear y ejecutar los hilos
def main(num_hilos):
    global exito_total, fallo_total

    if num_hilos < 1 or num_hilos > MAX_HILOS:
        print(f"El número de hilos debe estar entre 1 y {MAX_HILOS}")
        return

    hilos = []

    start_time = time.time()

    for i in range(num_hilos):
        hilo = threading.Thread(target=reservar_asiento, args=(i + 1,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    #Calcular el tiempo promedio por hilo
    end_time = time.time()
    tiempo_promedio = (end_time - start_time) / num_hilos

    #Resumen
    print("\n--- RESUMEN ---")
    print(f"Usuarios exitosos: {exito_total}")
    print(f"Usuarios fallidos: {fallo_total}")
    print(f"Tiempo promedio por hilo: {tiempo_promedio:.4f} segundos")

if __name__ == "__main__":
    try:
        num_hilos = int(input("Ingrese el número de hilos: "))
        main(num_hilos)
    except ValueError:
        print("Por favor, ingrese un número válido.")
