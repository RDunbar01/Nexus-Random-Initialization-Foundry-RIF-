# Nexus Random Initialization Foundry

**Version 2.9.1**

Initialiser des modèles de langage expérimentaux, les entraîner sur des données locales et exporter les points de contrôle pris en charge.

**[Essayer dans le navigateur](https://rdunbar01.github.io/Nexus-Random-Initialization-Foundry-RIF-/Nexus_Random_Initialization_Foundry_v2_9_Browser.html)** · [Télécharger les composants de bureau](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/tree/main/releases/2.9.1) · [README](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/README.md)

Ouvrez la version d’essai pour examiner l’interface et choisissez **Check WebGPU adapter**. Aucune installation de Python n’est nécessaire. L’objectif est un premier aperçu rapide ; le chargement d’un modèle et l’exécution d’une tâche dépendent des données et de l’appareil.

Paquet natif 2.9.1 ; édition navigateur 2.9.

## Fonctionnalités

- Initialisation des modèles et commandes d’entraînement sur corpus local.
- Statistiques d’entraînement en direct dans un tableau de bord vert translucide.
- Journal de progression unifié, enregistrable avant de fermer la page.
- Parcours d’entraînement distincts : WebGPU personnalisé et PyTorch installé.

## Contribution technique

Un parcours local et inspectable reliant l’initialisation, le suivi de l’entraînement et l’export des points de contrôle. Il permet d’expérimenter avec de petits modèles de langage sans imposer un service d’entraînement dans le cloud.

## Pourquoi un seul fichier HTML ?

L’édition navigateur réunit l’interface, JavaScript, CSS et les noyaux WGSL dans un seul fichier HTML. Ce choix facilite les essais en ligne, le partage du lien et l’inspection, sans compilation ni CDN à l’exécution. Le fichier contient le moteur navigateur, pas les poids des modèles ni le backend PyTorch natif.

Utilisez un navigateur compatible WebGPU en HTTPS. Les requêtes réseau à l’exécution, la surveillance matérielle native et les passerelles vers un serveur local sont désactivées. L’entraînement ou l’évaluation exige des entrées prises en charge. Le backend PyTorch natif nécessite le téléchargement complet.

[English](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ko)

## Versions de Python et environnement natif

- **Interpréteur conseillé : CPython 3.12 standard, 64 bits.** L’installateur annonce **Python 3.11–3.14**, sans imposer cette plage dans son programme de démarrage. L’ouverture avec une autre version ne valide pas le moteur natif.
- **L’installateur Foundry réutilise uniquement un environnement PyTorch compatible existant**, sélectionné avec `--runtime`. Il n’installe pas automatiquement un nouvel environnement de calcul. Le Python choisi doit correspondre à ses paquets PyTorch et réussir le test natif ; cette réutilisation n’applique pas de plage numérique distincte à Python. Le code seul ne permet pas d’affirmer qu’une version plus ancienne fonctionne.
- Le test exige **PyTorch 2.14.0+rocm10.1.0**, HIP et le RX 7900 XT/XTX configuré, puis contrôle des résultats FP32 avant/arrière finis. L’utilitaire de dépendances fourni, s’il est invoqué séparément, exige pour une nouvelle installation CPython standard x64 **3.11–3.14**, sans mode free-threaded, et Windows 11 **25H2**. L’installateur normal Foundry n’installe ni Python, ni pilotes GPU, ni compilateurs. Voir la [matrice officielle AMD](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html).

La validation Windows, WebView2, Radeon et modèle complet reste en attente. Les restrictions de l’utilitaire et la réussite du test ne prouvent pas la prise en charge de toutes les charges de travail.


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

## Utilisation et attribution

Rich Dunbar / Nexus Emerging Technology. L’usage personnel ainsi que les tests et évaluations commerciaux internes sont autorisés pour les éléments appartenant à Nexus. La distribution, la modification, le déploiement en production et les autres usages commerciaux nécessitent un consentement écrit exprès. Les licences tierces et les droits déjà accordés restent inchangés. [licence](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/LICENSE) · [autorisation d’évaluation (en anglais)](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).
