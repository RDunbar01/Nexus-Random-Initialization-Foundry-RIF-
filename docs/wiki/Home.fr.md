# Nexus Random Initialization Foundry — Accueil

## [Essayer dans le navigateur](<https://rdunbar01.github.io/Nexus-Random-Initialization-Foundry-RIF-/Nexus_Random_Initialization_Foundry_v2_9_Browser.html>) · accès navigateur publié

La page HTTPS est publiée et son écran initial a été vérifié. Cela ne constitue pas une qualification complète des charges WebGPU, Windows ou Radeon. L’affichage du HTML dans GitHub n’exécute pas l’application.

Le paquet natif **2.9.1** est publié sur main. Ce correctif de démarrage empêche les mises à jour du titre natif de monopoliser les minuteries de l’interface. L’essai navigateur reste l’**édition 2.9 inchangée**. Les anciennes versions restent disponibles ; ne mélangez pas leurs composants. La revue du paquet et les contrôles d’extraction ont réussi, mais la qualification Windows, WebView2, Radeon et des modèles complets sur matériel réel reste à réaliser.

Ouvrez le lien et choisissez **Check WebGPU adapter**. L’objectif des dix premières secondes est d’examiner l’interface et les capacités du navigateur, pas de télécharger un modèle ni de garantir l’entraînement ou l’inférence. Le chargement dépend de la connexion et de l’appareil.

**L’essai HTML ne nécessite pas Python. Le moteur PyTorch natif exige le téléchargement complet.** Gardez l’installateur Python et toutes les parties de données de la même version ensemble. Python et PyTorch ne s’exécutent pas dans le HTML. La prise en charge de WebGPU, les fichiers locaux et les contrôles de compatibilité du modèle restent nécessaires.

## Versions de Python et environnement natif

- **Interpréteur conseillé : CPython 3.12 standard, 64 bits.** L’installateur annonce **Python 3.11–3.14**, sans imposer cette plage dans son programme de démarrage. L’ouverture avec une autre version ne valide pas le moteur natif.
- **L’installateur Foundry réutilise uniquement un environnement PyTorch compatible existant**, sélectionné avec `--runtime`. Il n’installe pas automatiquement un nouvel environnement de calcul. Le Python choisi doit correspondre à ses paquets PyTorch et réussir le test natif ; cette réutilisation n’applique pas de plage numérique distincte à Python. Le code seul ne permet pas d’affirmer qu’une version plus ancienne fonctionne.
- Le test exige **PyTorch 2.14.0+rocm10.1.0**, HIP et le RX 7900 XT/XTX configuré, puis contrôle des résultats FP32 avant/arrière finis. L’utilitaire de dépendances fourni, s’il est invoqué séparément, exige pour une nouvelle installation CPython standard x64 **3.11–3.14**, sans mode free-threaded, et Windows 11 **25H2**. L’installateur normal Foundry n’installe ni Python, ni pilotes GPU, ni compilateurs. Voir la [matrice officielle AMD](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html).

La validation Windows, WebView2, Radeon et modèle complet reste en attente. Les restrictions de l’utilitaire et la réussite du test ne prouvent pas la prise en charge de toutes les charges de travail.

**2.9.1 · Français**

Documentation de la version publiée. Consultez les preuves et limites ci-dessous.

[English](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ko)

## Objectif

Initialisez des modèles expérimentaux, entraînez-les sur des données locales et suivez leur progression. Les statistiques vertes translucides et le journal unifié exportable sont conservés. Enregistrez le journal avant de fermer la page.

## Choisir une édition

### Édition navigateur

[HTML](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/Nexus_Random_Initialization_Foundry_v2_9_Browser.html) · [README](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/README.md)

Utilisez un navigateur compatible WebGPU en HTTPS ou sur une origine localhost sécurisée prise en charge. Le fichier HTML unique contient le moteur JavaScript/WGSL personnalisé. Importez des fichiers locaux compatibles. Python, PyTorch, les services natifs, le téléchargement de jeux de données en ligne et la télémétrie GPU native ne sont pas disponibles ; les requêtes réseau de l’application sont bloquées. L’affichage du code sur GitHub n’exécute pas l’application.

### Édition installée

Téléchargez ensemble tous les fichiers du [paquet 2.9.1](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/tree/main/releases/2.9.1), en conservant leur disposition. Gardez toutes les parties de données `.nxd` numérotées à côté de [Start_Nexus.py](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/releases/2.9.1/Start_Nexus.py), puis lancez `python Start_Nexus.py` avec l’interpréteur compatible. Lisez le [guide correspondant](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/releases/2.9.1/README.md) et le récapitulatif avant de confirmer. Chaque partie `.nxd` fait au plus **10 000 000 octets** ; chaque fichier distribué, avant installation, fait moins de **20 000 000 octets**. L’archive complète, l’application reconstruite, les fichiers installés et les modèles téléchargés peuvent être plus volumineux. Ne mélangez pas les versions. Les réglages et tests PyTorch natifs concernent l’édition installée, pas l’essai HTML seul.

## Mesures et limites

Les tests CPU et les contrôles statiques/DOM ne valident pas l’exécution sur du matériel Windows/Radeon/WebGPU réel. Comparez uniquement des conditions équivalentes : modèle, corpus, contexte, lot, précision et moteur. Les débits d’entraînement, de récupération, de traitement des invites et de génération sont des mesures différentes. Aucune compatibilité universelle ni vitesse maximale n’est garantie.

Pic de débit d’entraînement déclaré par le développeur : **32 000 jetons/seconde sur Radeon RX 7900 XT**. Il n’a pas été reproduit indépendamment ici, ne garantit pas un débit soutenu et ne mesure pas la génération conversationnelle.

## Crédits et licences

Rich Dunbar / Nexus Emerging Technology, avec l’aide d’outils de codage par IA. Les licences existantes et les conditions applicables aux recherches, au code, aux modèles et aux données tiers restent en vigueur. Cette page n’accorde aucune licence supplémentaire.

## Licence de la version actuelle

Cette version de Nexus n’est pas proposée sous la licence Apache 2.0. Le logiciel appartenant à Nexus ne peut être utilisé qu’à des fins personnelles et non commerciales. Toute autre utilisation, y compris commerciale, ainsi que toute modification ou redistribution, nécessite le consentement écrit exprès du titulaire des droits. Les codes, modèles, jeux de données tiers et composants sous licence distincte conservent leurs propres licences et mentions. Les droits déjà accordés et les droits qui ne peuvent légalement être restreints restent inchangés.

