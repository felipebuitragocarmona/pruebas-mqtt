import paho.mqtt.client as mqtt
from gpiozero import LED

# Definir los callbacks para los eventos de conexión, suscripción y recepción de mensajes
def on_connect(client, userdata, flags, rc):
    print("Conectado al broker. Código de resultado: " + str(rc))
    client.subscribe("santiagoMR1187")  # Suscribirse a un topic al conectarse

def on_message(client, userdata, msg):
    print("Mensaje recibido: " + msg.topic + " " + str(msg.payload))
    if msg.payload.deconde("utf-8")=="ON":
        mi_led.on()
    elif msg.payload.deconde("utf-8")=="OFF":
        mi_led.off()

mi_led=LED(15)
# Crear una instancia del cliente MQTT
client = mqtt.Client()

# Configurar los callbacks
client.on_connect = on_connect
client.on_message = on_message

# Especificar la dirección del broker MQTT
broker_address = "test.mosquitto.org"  # Cambiar por la dirección de tu broker

# Conectarse al broker
client.connect(broker_address, 1883, 60)

# Iniciar el bucle de procesamiento de mensajes
client.loop_forever()

