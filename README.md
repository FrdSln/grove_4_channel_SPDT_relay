# grove_4_channel_SPDT_relay

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

Bibliothèques et exemples d'utilisation pour [Grove - 4 channel SPDT Relay](https://wiki.seeedstudio.com/Grove-4-Channel_SPDT_Relay/)

## Utilisation

### Matériel nécessaire

- 1 Carte micro:bit V1 ou V2
- 1 Shield
- 1 Grove - 4 channel SPDT Telay
- Logiciel Mu

### Installation

- **Copier** la bibliothèque mb_4SPDTRelay_grove.py avec l'outil _fichiers_ de Mu.

- **Lancer** le fichier exemple mb_4SPDTRelay_grove_example1.py

Les relais sont commandés successivement ou simultanément. Le module Grove a son adresse I2C par défaut (0x11).

- **Lancer** le fichier exemple mb_4SPDTRelay_grove_example2.py

Le module GRove est paramétré pour occuper l'addresse 0x31.

### Fonctions supportées

- Initialisation : relais = mb_4SPDTRelay_grove(0x11)
- Activation d'un relais : relais.turn_on_channel(n) avec n compris entre 1 et 4
- Désactivation d'un relais : relais.turn_off_channel(n) avec n compris entre 1 et 4
- Commande des 4 relais : relais.channel_control(k) avec k quartet des états des 4 relais
- Affichage de la version du firmware : relais.getFirmwareVersion()
- Modification de l'addresse I2C : relais.

## Versions

**Dernière version :** 2

Version à venir : écriture des version ESP32

[Liste des versions](https://github.com/FrdSln/ grove_i2c_driver_motor/tags)

## Auteur

* **F. SAULIN** ([FrdSln](https://github.com/FrdSln))

## Licence

Ce projet est sous licence ``GNU General Public License v3.0`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations

