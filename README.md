# Controle de Relé com ESP32 (Wokwi)

Simulação em MicroPython que liga e desliga uma lâmpada através de um módulo relé, alternando o estado a cada 3 segundos.

## 🔌 Componentes
- ESP32 DevKit C V4
- Módulo relé (ativo em nível baixo)
- LED (representando a lâmpada) + resistor

## 🧷 Conexões

| ESP32 | Componente |
|---|---|
| GPIO 15 | IN (relé) |
| 3V3 | VCC (relé) |
| GND | GND (relé) |
| COM (relé) | Ânodo do LED (via resistor) |
| NC (relé) | GND |

## ⚙️ Funcionamento
O módulo relé usado é ativo em nível baixo: enviar `0` para o pino de controle liga o relé, e `1` desliga. O script mantém a lâmpada acesa por 3s e apagada por 3s, em loop contínuo.

## ▶️ Como simular
- Projeto original no Wokwi: https://wokwi.com/projects/441640786959216641
- Ou crie um novo projeto ESP32/MicroPython no [Wokwi](https://wokwi.com) e importe `main.py` e `diagram.json` deste repositório.

## 📁 Arquivos
- `main.py` — código MicroPython
- `diagram.json` — esquema de ligação (Wokwi)
- `wokwi-project.txt` — referência do projeto original
