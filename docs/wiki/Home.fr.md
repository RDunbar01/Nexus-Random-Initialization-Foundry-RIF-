# Nexus Random Initialization Foundry — Accueil

**2.9.0 · Français**

Cette page est la source du wiki à relire pour la prochaine version. Elle ne signifie pas que le wiki public ou la version d’essai en ligne est déjà publié.

[English](Home.md) · [Français](Home.fr.md) · [日本語](Home.ja.md) · [한국어](Home.ko.md)

## Objectif

Initialisez des modèles expérimentaux, entraînez-les sur des données locales et suivez leur progression. Les statistiques vertes translucides et le journal unifié exportable sont conservés. Enregistrez le journal avant de fermer la page.

## Choisir une édition

### Édition navigateur

[HTML](../../Nexus_Random_Initialization_Foundry_v2_9_Browser.html) · [README](../../README.md)

Utilisez un navigateur compatible WebGPU en HTTPS ou sur une origine localhost sécurisée prise en charge. Le fichier HTML unique contient le moteur JavaScript/WGSL personnalisé. Importez des fichiers locaux compatibles. Python, PyTorch, les services natifs, le téléchargement de jeux de données en ligne et la télémétrie GPU native ne sont pas disponibles ; les requêtes réseau de l’application sont bloquées. L’affichage du code sur GitHub n’exécute pas l’application.

### Édition installée

Extrayez le ZIP complet et gardez l’installateur avec toutes ses parties de données. Chaque composant distribué doit faire moins de 20 000 000 octets ; les fichiers reconstruits et les modèles téléchargés peuvent être plus volumineux. Suivez le manifeste et le récapitulatif de l’installateur de cette version. Les réglages et tests PyTorch natifs concernent l’édition installée, pas l’édition HTML seule.

## Mesures et limites

Les tests CPU et les contrôles statiques/DOM ne valident pas l’exécution sur du matériel Windows/Radeon/WebGPU réel. Comparez uniquement des conditions équivalentes : modèle, corpus, contexte, lot, précision et moteur. Les débits d’entraînement, de récupération, de traitement des invites et de génération sont des mesures différentes. Aucune compatibilité universelle ni vitesse maximale n’est garantie.

Pic de débit d’entraînement déclaré par le développeur : **32 000 jetons/seconde sur Radeon RX 7900 XT**. Il n’a pas été reproduit indépendamment ici, ne garantit pas un débit soutenu et ne mesure pas la génération conversationnelle.

## Crédits et licences

Rich Dunbar / Nexus Emerging Technology, avec l’aide d’outils de codage par IA. Les licences existantes et les conditions applicables aux recherches, au code, aux modèles et aux données tiers restent en vigueur. Cette page n’accorde aucune licence supplémentaire.

## Licence de la version actuelle

Cette version de Nexus n’est pas proposée sous la licence Apache 2.0. Le logiciel appartenant à Nexus ne peut être utilisé qu’à des fins personnelles et non commerciales. Toute autre utilisation, y compris commerciale, ainsi que toute modification ou redistribution, nécessite le consentement écrit exprès du titulaire des droits. Les codes, modèles, jeux de données tiers et composants sous licence distincte conservent leurs propres licences et mentions. Les droits déjà accordés et les droits qui ne peuvent légalement être restreints restent inchangés.
