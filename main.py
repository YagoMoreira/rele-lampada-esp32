from machine import Pin
import time

# --- Configuração do Pino de Controle do Relé ---
# O pino IN do relé está conectado ao GPIO 15.
# Configuramos o pino como uma saída.
pino_rele = Pin(15, Pin.OUT)

print("Iniciando controle da lâmpada via relé...")

# --- Loop Principal ---
while True:
    # A maioria dos módulos relé no Wokwi e no mundo real
    # são "ativos em nível baixo", o que significa que um sinal 0 (LOW) liga o relé.
    
    print("Ligando a lâmpada...")
    pino_rele.value(0) # Envia sinal LOW para ligar o relé
    time.sleep(3)      # Mantém a lâmpada acesa por 3 segundos

    print("Desligando a lâmpada...")
    pino_rele.value(1) # Envia sinal HIGH para desligar o relé
    time.sleep(3)      # Mantém a lâmpada apagada por 3 segundos
