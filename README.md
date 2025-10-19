![71vARL+q8TL _AC_SL1500_](https://github.com/user-attachments/assets/355e22d2-4e82-4c45-9610-25af26be7597)

# COSTWAY reversible mobile air conditioner 

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz)
[![License](https://img.shields.io/github/license/SoFarSoGood86/costway_climate)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/SoFarSoGood86/costway_climate)](https://github.com/SoFarSoGood86/costway_climate/releases)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Integration-41BDF5)](https://www.home-assistant.io/)

**COSTWAY** air conditioner intégration for Home Assistant.
Working with **Tuya local** protocol - libray [tinytuya](https://github.com/jasonacox/tinytuya).

---

## Features :

- ✅ Device control (ON / OFF).
- 🌡️ Set temperature.
- 🔄 Heat / Cool mode.
- 🌀 Fan speed (Low / Medium / High).
- 📡 Real time status (local)  
- 🧭 Add. via Home Assistant ou YAML

---

## Installation :

### Option 1 — via [HACS](https://hacs.xyz) (recommended)

1. In HACS → **Custom Repositories**, add :  
   ```
   https://github.com/SoFarSoGood86/costway_climate
   ```
   Type : `Integration`
2. Install **COSTWAY Climate (Tuya Local)** from HACS.
3. Restart Home Assistant.

### Option 2 — Manual

1. Download last [![GitHub Release](https://img.shields.io/github/v/release/SoFarSoGood86/costway_climate)](https://github.com/SoFarSoGood86/costway_climate/releases)
2. Copie folder `custom_components/costway_climate` inside folder `config/custom_components` of your Home Assistant.  
3. Restart Home Assistant.

---

## Configuration :

### Via Graphic Interface (config flow)

1. Settings → Devices & Services → Add. intégration.  
2. Research `COSTWAY Climate`.  
3. Enter the informations :
   - **Device ID**
   - **Local Key**
   - **Adresse IP locale**

This information can be retrieved via the library [`tinytuya`](https://github.com/jasonacox/tinytuya) or [Tuya IoT Platform](https://iot.tuya.com).

---

### Via `configuration.yaml` (optionnal)

```yaml
climate:
  - platform: costway_climate
    device_id: "xxxxxxxxxxxxxxxxxxxx"
    local_key: "xxxxxxxxxxxxxx"
    ip: "192.168.1.50"
```

---

## Required :

- Tuya accont configured with COSWAY air conditioner.  
- Local connexion (no cloud needed once setup).  
- Connexions informations from `tinytuya` :
  ```bash
  python -m tinytuya wizard
  ```

---

## Need help ! :

- Assurez-vous que le climatiseur est connecté au **même réseau local** que Home Assistant.  
- Vérifiez que l’adresse IP est fixe ou réservée dans votre routeur.  
- Si aucune réponse n’est reçue : essayez de définir la **version du protocole 3.3** dans TinyTuya.  
- Vérifiez que le port TCP du module Tuya n’est pas bloqué.

---

## Roadmap :

- [ ] Mode Auto
- [ ] Gestion de l’humidité (si disponible)
- [ ] Auto-discovery MQTT (optionnel)
- [ ] Support multi-appareils
- [ ] Diagnostic UI

---

## Development :

```bash
# Cloner le dépôt
git clone https://github.com/SoFarSoGood86/costway_climate.git
cd costway_climate

# Installer les dépendances
pip install tinytuya

# Tester localement avec Home Assistant Core
```

---

✨ *If you found this integration useful, please consider leaving a star on the GitHub repository to support it. !* ⭐
