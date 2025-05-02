import requests
import logging

logger = logging.getLogger(__name__)

def send_alert(webhook_url: str, payload: dict) -> bool:
    try:
        resp = requests.post(webhook_url, json=payload, timeout=5)
        resp.raise_for_status()
        return True
    except requests.RequestException as e:
        logger.error(f"alert failed: {e}")
        return False