import paho.mqtt.client as mqtt

# Crear una instancia del cliente MQTT
client = mqtt.Client()

# Especificar la dirección del broker MQTT
broker_address = "test.mosquitto.org"  # Cambiar por la dirección de tu broker

# Conectarse al broker
client.connect(broker_address, 1883, 60)

# Publicar un mensaje en un topic específico
topic = "santiagoMR1187"  # Cambiar por el topic deseado
message = "Hola, mundo! desde Raspberry Ian y Felipe"  # Mensaje a publicar

# Publicar el mensaje
client.publish(topic, message)

# Desconectarse del broker MQTT
client.disconnect()
