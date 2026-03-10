"""
Questions database for all compliance frameworks.
Each question has: id, text_fr, text_en, category, weight, framework
"""

FRAMEWORKS = {
    "eu_ai_act": {"name_fr": "EU AI Act", "name_en": "EU AI Act", "icon": "🤖"},
    "nis2":      {"name_fr": "NIS2",      "name_en": "NIS2",      "icon": "🛡️"},
    "rgpd":      {"name_fr": "RGPD",      "name_en": "GDPR",      "icon": "🔒"},
    "iso27001":  {"name_fr": "ISO 27001", "name_en": "ISO 27001", "icon": "📋"},
    "soc2":      {"name_fr": "SOC 2",     "name_en": "SOC 2",     "icon": "✅"},
}

QUESTIONS = {

    # ─────────────────────────────────────────
    # EU AI ACT
    # ─────────────────────────────────────────
    "eu_ai_act": [
        {
            "id": "euai_01",
            "category_fr": "Classification du risque",
            "category_en": "Risk classification",
            "text_fr": "Votre organisation développe ou déploie-t-elle des systèmes d'IA ?",
            "text_en": "Does your organisation develop or deploy AI systems?",
            "weight": 3,
        },
        {
            "id": "euai_02",
            "category_fr": "Classification du risque",
            "category_en": "Risk classification",
            "text_fr": "Avez-vous classifié vos systèmes d'IA selon les niveaux de risque de l'EU AI Act (inacceptable, élevé, limité, minimal) ?",
            "text_en": "Have you classified your AI systems according to EU AI Act risk levels (unacceptable, high, limited, minimal)?",
            "weight": 5,
        },
        {
            "id": "euai_03",
            "category_fr": "Systèmes à haut risque",
            "category_en": "High-risk systems",
            "text_fr": "Si vous utilisez des systèmes IA à haut risque, avez-vous mis en place une évaluation de la conformité ?",
            "text_en": "If you use high-risk AI systems, have you conducted a conformity assessment?",
            "weight": 5,
        },
        {
            "id": "euai_04",
            "category_fr": "Transparence",
            "category_en": "Transparency",
            "text_fr": "Les utilisateurs sont-ils informés lorsqu'ils interagissent avec un système d'IA (ex : chatbot, système de décision automatisé) ?",
            "text_en": "Are users informed when they interact with an AI system (e.g. chatbot, automated decision system)?",
            "weight": 4,
        },
        {
            "id": "euai_05",
            "category_fr": "Gouvernance des données",
            "category_en": "Data governance",
            "text_fr": "Les données d'entraînement de vos modèles IA sont-elles documentées et auditables ?",
            "text_en": "Are the training datasets for your AI models documented and auditable?",
            "weight": 4,
        },
        {
            "id": "euai_06",
            "category_fr": "Supervision humaine",
            "category_en": "Human oversight",
            "text_fr": "Existe-t-il un mécanisme de supervision humaine pour les décisions critiques prises par l'IA ?",
            "text_en": "Is there a human oversight mechanism for critical decisions made by AI?",
            "weight": 5,
        },
        {
            "id": "euai_07",
            "category_fr": "Robustesse & sécurité",
            "category_en": "Robustness & security",
            "text_fr": "Vos systèmes IA ont-ils fait l'objet de tests de robustesse et de résistance aux attaques adversariales ?",
            "text_en": "Have your AI systems been tested for robustness and resistance to adversarial attacks?",
            "weight": 4,
        },
        {
            "id": "euai_08",
            "category_fr": "Enregistrement & traçabilité",
            "category_en": "Logging & traceability",
            "text_fr": "Les systèmes IA à haut risque génèrent-ils automatiquement des journaux d'événements traçables ?",
            "text_en": "Do high-risk AI systems automatically generate traceable event logs?",
            "weight": 3,
        },
    ],

    # ─────────────────────────────────────────
    # NIS2
    # ─────────────────────────────────────────
    "nis2": [
        {
            "id": "nis2_01",
            "category_fr": "Gouvernance",
            "category_en": "Governance",
            "text_fr": "La direction générale est-elle formellement responsable de la cybersécurité ?",
            "text_en": "Is senior management formally accountable for cybersecurity?",
            "weight": 5,
        },
        {
            "id": "nis2_02",
            "category_fr": "Gestion des risques",
            "category_en": "Risk management",
            "text_fr": "Votre organisation réalise-t-elle des évaluations régulières des risques cyber ?",
            "text_en": "Does your organisation conduct regular cybersecurity risk assessments?",
            "weight": 5,
        },
        {
            "id": "nis2_03",
            "category_fr": "Gestion des incidents",
            "category_en": "Incident management",
            "text_fr": "Avez-vous un plan de réponse aux incidents de sécurité documenté et testé ?",
            "text_en": "Do you have a documented and tested security incident response plan?",
            "weight": 5,
        },
        {
            "id": "nis2_04",
            "category_fr": "Gestion des incidents",
            "category_en": "Incident management",
            "text_fr": "Êtes-vous en mesure de notifier un incident significatif sous 24h aux autorités compétentes ?",
            "text_en": "Are you able to notify a significant incident to competent authorities within 24 hours?",
            "weight": 4,
        },
        {
            "id": "nis2_05",
            "category_fr": "Sécurité de la chaîne d'approvisionnement",
            "category_en": "Supply chain security",
            "text_fr": "Évaluez-vous la posture de sécurité de vos fournisseurs et prestataires critiques ?",
            "text_en": "Do you assess the security posture of your critical suppliers and service providers?",
            "weight": 4,
        },
        {
            "id": "nis2_06",
            "category_fr": "Continuité d'activité",
            "category_en": "Business continuity",
            "text_fr": "Disposez-vous d'un plan de continuité d'activité (PCA) et de reprise après sinistre (PRA) ?",
            "text_en": "Do you have a Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP)?",
            "weight": 4,
        },
        {
            "id": "nis2_07",
            "category_fr": "Sécurité technique",
            "category_en": "Technical security",
            "text_fr": "Utilisez-vous l'authentification multi-facteurs (MFA) pour les accès aux systèmes critiques ?",
            "text_en": "Do you use multi-factor authentication (MFA) for access to critical systems?",
            "weight": 4,
        },
        {
            "id": "nis2_08",
            "category_fr": "Formation & sensibilisation",
            "category_en": "Training & awareness",
            "text_fr": "Les employés reçoivent-ils une formation régulière en cybersécurité ?",
            "text_en": "Do employees receive regular cybersecurity training?",
            "weight": 3,
        },
    ],

    # ─────────────────────────────────────────
    # RGPD / GDPR
    # ─────────────────────────────────────────
    "rgpd": [
        {
            "id": "rgpd_01",
            "category_fr": "Base légale",
            "category_en": "Legal basis",
            "text_fr": "Chaque traitement de données personnelles repose-t-il sur une base légale identifiée (consentement, contrat, intérêt légitime…) ?",
            "text_en": "Does each personal data processing activity rely on an identified legal basis (consent, contract, legitimate interest…)?",
            "weight": 5,
        },
        {
            "id": "rgpd_02",
            "category_fr": "Registre des traitements",
            "category_en": "Records of processing",
            "text_fr": "Maintenez-vous un registre des activités de traitement (Article 30 RGPD) ?",
            "text_en": "Do you maintain a Record of Processing Activities (Article 30 GDPR)?",
            "weight": 4,
        },
        {
            "id": "rgpd_03",
            "category_fr": "Droits des personnes",
            "category_en": "Data subject rights",
            "text_fr": "Disposez-vous de procédures pour répondre aux demandes d'exercice des droits (accès, rectification, effacement) dans les délais légaux ?",
            "text_en": "Do you have procedures to respond to data subject rights requests (access, rectification, erasure) within legal deadlines?",
            "weight": 4,
        },
        {
            "id": "rgpd_04",
            "category_fr": "Violation de données",
            "category_en": "Data breach",
            "text_fr": "Avez-vous un processus pour détecter et notifier les violations de données à la CNIL dans les 72h ?",
            "text_en": "Do you have a process to detect and notify data breaches to the supervisory authority within 72 hours?",
            "weight": 5,
        },
        {
            "id": "rgpd_05",
            "category_fr": "Privacy by design",
            "category_en": "Privacy by design",
            "text_fr": "La protection des données est-elle intégrée dès la conception de vos projets (privacy by design) ?",
            "text_en": "Is data protection integrated from the design phase of your projects (privacy by design)?",
            "weight": 3,
        },
        {
            "id": "rgpd_06",
            "category_fr": "Transferts internationaux",
            "category_en": "International transfers",
            "text_fr": "Les transferts de données hors UE sont-ils encadrés par des mécanismes adéquats (clauses contractuelles types, décision d'adéquation) ?",
            "text_en": "Are data transfers outside the EU covered by adequate mechanisms (standard contractual clauses, adequacy decision)?",
            "weight": 4,
        },
        {
            "id": "rgpd_07",
            "category_fr": "DPO",
            "category_en": "DPO",
            "text_fr": "Avez-vous désigné un Délégué à la Protection des Données (DPO) si requis ?",
            "text_en": "Have you designated a Data Protection Officer (DPO) if required?",
            "weight": 3,
        },
    ],

    # ─────────────────────────────────────────
    # ISO 27001
    # ─────────────────────────────────────────
    "iso27001": [
        {
            "id": "iso_01",
            "category_fr": "Politique de sécurité",
            "category_en": "Security policy",
            "text_fr": "Disposez-vous d'une politique de sécurité de l'information formalisée et approuvée par la direction ?",
            "text_en": "Do you have a formal information security policy approved by management?",
            "weight": 4,
        },
        {
            "id": "iso_02",
            "category_fr": "Gestion des actifs",
            "category_en": "Asset management",
            "text_fr": "Maintenez-vous un inventaire complet de vos actifs informationnels (données, systèmes, applications) ?",
            "text_en": "Do you maintain a complete inventory of your information assets (data, systems, applications)?",
            "weight": 4,
        },
        {
            "id": "iso_03",
            "category_fr": "Contrôle d'accès",
            "category_en": "Access control",
            "text_fr": "Le principe du moindre privilège est-il appliqué pour les accès aux systèmes et aux données ?",
            "text_en": "Is the principle of least privilege applied for access to systems and data?",
            "weight": 5,
        },
        {
            "id": "iso_04",
            "category_fr": "Cryptographie",
            "category_en": "Cryptography",
            "text_fr": "Les données sensibles sont-elles chiffrées au repos et en transit ?",
            "text_en": "Is sensitive data encrypted at rest and in transit?",
            "weight": 4,
        },
        {
            "id": "iso_05",
            "category_fr": "Sécurité physique",
            "category_en": "Physical security",
            "text_fr": "L'accès physique aux locaux et équipements sensibles est-il contrôlé et journalisé ?",
            "text_en": "Is physical access to sensitive premises and equipment controlled and logged?",
            "weight": 3,
        },
        {
            "id": "iso_06",
            "category_fr": "Gestion des vulnérabilités",
            "category_en": "Vulnerability management",
            "text_fr": "Réalisez-vous des scans de vulnérabilités et des tests de pénétration réguliers ?",
            "text_en": "Do you conduct regular vulnerability scans and penetration tests?",
            "weight": 4,
        },
        {
            "id": "iso_07",
            "category_fr": "Audit interne",
            "category_en": "Internal audit",
            "text_fr": "Des audits internes du SMSI sont-ils réalisés à intervalles réguliers ?",
            "text_en": "Are internal ISMS audits conducted at regular intervals?",
            "weight": 3,
        },
        {
            "id": "iso_08",
            "category_fr": "Amélioration continue",
            "category_en": "Continual improvement",
            "text_fr": "Les non-conformités identifiées font-elles l'objet d'actions correctives documentées ?",
            "text_en": "Are identified non-conformities subject to documented corrective actions?",
            "weight": 3,
        },
    ],

    # ─────────────────────────────────────────
    # SOC 2
    # ─────────────────────────────────────────
    "soc2": [
        {
            "id": "soc2_01",
            "category_fr": "Disponibilité",
            "category_en": "Availability",
            "text_fr": "Disposez-vous d'engagements de disponibilité (SLA) documentés pour vos services ?",
            "text_en": "Do you have documented availability commitments (SLA) for your services?",
            "weight": 4,
        },
        {
            "id": "soc2_02",
            "category_fr": "Intégrité du traitement",
            "category_en": "Processing integrity",
            "text_fr": "Des contrôles sont-ils en place pour garantir que les traitements sont complets, valides et précis ?",
            "text_en": "Are controls in place to ensure processing is complete, valid and accurate?",
            "weight": 4,
        },
        {
            "id": "soc2_03",
            "category_fr": "Confidentialité",
            "category_en": "Confidentiality",
            "text_fr": "Les informations confidentielles sont-elles identifiées et protégées par des contrôles appropriés ?",
            "text_en": "Is confidential information identified and protected by appropriate controls?",
            "weight": 4,
        },
        {
            "id": "soc2_04",
            "category_fr": "Sécurité logique",
            "category_en": "Logical security",
            "text_fr": "Les accès logiques sont-ils restreints aux seules personnes autorisées et revus périodiquement ?",
            "text_en": "Are logical accesses restricted to authorised personnel only and reviewed periodically?",
            "weight": 5,
        },
        {
            "id": "soc2_05",
            "category_fr": "Surveillance",
            "category_en": "Monitoring",
            "text_fr": "Les systèmes sont-ils monitorés en continu pour détecter les incidents et anomalies ?",
            "text_en": "Are systems continuously monitored to detect incidents and anomalies?",
            "weight": 4,
        },
        {
            "id": "soc2_06",
            "category_fr": "Gestion du changement",
            "category_en": "Change management",
            "text_fr": "Un processus formel de gestion des changements est-il en place pour les systèmes en production ?",
            "text_en": "Is a formal change management process in place for production systems?",
            "weight": 3,
        },
        {
            "id": "soc2_07",
            "category_fr": "Sous-traitants",
            "category_en": "Subprocessors",
            "text_fr": "Les risques liés aux sous-traitants et fournisseurs cloud sont-ils évalués et contractualisés ?",
            "text_en": "Are risks related to subcontractors and cloud providers assessed and contractualised?",
            "weight": 3,
        },
    ],
}
