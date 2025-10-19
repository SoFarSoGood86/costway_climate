# COSTWAY Mobil Climate Réversible 

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz)
[![License](https://img.shields.io/github/license/SoFarSoGood86/costway_climate)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/SoFarSoGood86/costway_climate)](https://github.com/SoFarSoGood86/costway_climate/releases)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Integration-41BDF5)](https://www.home-assistant.io/)

**COSTWAY** mobil climate intégration for Home Assistant.
Working witj **Tuya local** protocol - libray [tinytuya](https://github.com/jasonacox/tinytuya).

---

## Features :

- ✅ Allumer / éteindre le climatiseur  
- 🌡️ Régler la température cible  
- 🔄 Mode chaud / froid  
- 🌀 Vitesse du ventilateur (Low / Medium / High)  
- 📡 Lecture d’état en temps réel (local)  
- 🧭 Ajout via l’interface Home Assistant ou YAML

---

## Installation :

### Option 1 — via [HACS](https://hacs.xyz) (recommandé)

1. Dans HACS → **Custom Repositories**, ajoute :  
   ```
   https://github.com/SoFarSoGood86/costway_climate
   ```
   Type : `Integration`
2. Installe **COSTWAY Climate (Tuya Local)** depuis HACS.
3. Redémarre Home Assistant.

### Option 2 — Manuel

1. Télécharge la dernière [release](https://github.com/SoFarSoGood86/costway_climate/releases).  
2. Copie le dossier `custom_components/costway_climate` dans le dossier `config/custom_components` de ton installation Home Assistant.  
3. Redémarre Home Assistant.

---

## Configuration

### 📲 Via Interface graphique (config flow)

1. Paramètres → Appareils & services → Ajouter une intégration.  
2. Rechercher `COSTWAY Climate`.  
3. Saisir les informations :
   - **Device ID**
   - **Local Key**
   - **Adresse IP locale**

📝 Ces informations peuvent être récupérées via la librairie [`tinytuya`](https://github.com/jasonacox/tinytuya) ou la [Tuya IoT Platform](https://iot.tuya.com).

---

### 🧾 Via `configuration.yaml` (optionnel)

```yaml
climate:
  - platform: costway_climate
    device_id: "xxxxxxxxxxxxxxxxxxxx"
    local_key: "xxxxxxxxxxxxxx"
    ip: "192.168.1.50"
```

---

## 🧪 Exigences

- Compte Tuya configuré avec le climatiseur.  
- Connexion locale (pas besoin de cloud une fois configuré).  
- Informations de connexion extraites avec `tinytuya` :
  ```bash
  python -m tinytuya wizard
  ```

---

## 🧰 Dépannage

- Assurez-vous que le climatiseur est connecté au **même réseau local** que Home Assistant.  
- Vérifiez que l’adresse IP est fixe ou réservée dans votre routeur.  
- Si aucune réponse n’est reçue : essayez de définir la **version du protocole 3.3** dans TinyTuya.  
- Vérifiez que le port TCP du module Tuya n’est pas bloqué.

---

## 🚀 Feuille de route (Roadmap)

- [ ] Mode Auto
- [ ] Gestion de l’humidité (si disponible)
- [ ] Auto-discovery MQTT (optionnel)
- [ ] Support multi-appareils
- [ ] Diagnostic UI

---

## 🧑‍💻 Développement

```bash
# Cloner le dépôt
git clone https://github.com/SoFarSoGood86/costway_climate.git
cd costway_climate

# Installer les dépendances
pip install tinytuya

# Tester localement avec Home Assistant Core
```

---

✨ *Si cette intégration t’a été utile, pense à laisser une étoile sur le dépôt GitHub pour la soutenir !* ⭐
