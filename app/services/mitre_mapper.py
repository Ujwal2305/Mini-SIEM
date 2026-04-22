MITRE_MAP = {
    "BRUTE_FORCE": {
        "technique": "T1110",
        "tactic": "Credential Access"
    },
    "BRUTE_FORCE_SUCCESS": {
        "technique": "T1110",
        "tactic": "Credential Access"
    }
}

def map_to_mitre(alert_type):
    return MITRE_MAP.get(alert_type, {})