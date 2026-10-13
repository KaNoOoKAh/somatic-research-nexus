import json
import os
import sys
from datetime import datetime, timezone, timedelta
import urllib.request

# ============================================================
# SOMATIC RESEARCH NEXUS: HYPER-LOCAL TELEMETRY LOGGER
# Signature: ICeI3 | Reference Marker: htps:/192.168.1.12
# Location Target: 3741 Poka Place, Honolulu, HI 96816
# ============================================================

IDENTITY_SIGNATURE = "ICeI3"
REFERENCE_MARKER = "htps:/192.168.1.12"
LATITUDE = 21.2858
LONGITUDE = -157.8025
DEFAULT_TRIAL_DIR = os.path.join("trials", "Trial_001")

def get_environmental_telemetry():
    """Pulls atmospheric & satellite solar variables for 3741 Poka Place."""
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}&longitude={LONGITUDE}&"
        f"current=temperature_2m,relative_humidity_2m,surface_pressure,"
        f"cloud_cover,wind_speed_10m,wind_gusts_10m,direct_radiation"
    )
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            curr = data.get("current", {})
            
            temp_c = curr.get("temperature_2m", 28.0)
            temp_f = round((temp_c * 9/5) + 32, 1)
            
            wind_kmh = curr.get("wind_speed_10m", 0)
            gust_kmh = curr.get("wind_gusts_10m", 0)
            
            return {
                "temperature_f": temp_f,
                "relative_humidity_percent": curr.get("relative_humidity_2m"),
                "surface_pressure_hpa": curr.get("surface_pressure"),
                "solar_radiation_w_m2": curr.get("direct_radiation"),
                "cloud_cover_percent": curr.get("cloud_cover"),
                "wind_speed_mph": round(wind_kmh * 0.621371, 1),
                "wind_gust_mph": round(gust_kmh * 0.621371, 1),
                "data_source": "Open-Meteo Environmental Reanalysis API"
            }
    except Exception as e:
        return {
            "temperature_f": 85.0,
            "relative_humidity_percent": 55,
            "surface_pressure_hpa": 1015.2,
            "solar_radiation_w_m2": 800.0,
            "cloud_cover_percent": 20,
            "wind_speed_mph": 12.0,
            "wind_gust_mph": 17.0,
            "data_source": "Fallback Oahu Baseline",
            "error_note": str(e)
        }

def collect_somatic_input():
    """Prompts for trial event type and subjective somatic state."""
    print("\n" + "="*60)
    print("      SOMATIC RESEARCH NEXUS: DUAL-STATE TELEMETRY LOGGER      ")
    print("="*60)
    
    event_type = input("\n[1] Enter Event Type (START / STOP) [Default: START]: ").strip().upper()
    if not event_type:
        event_type = "START"
        
    try:
        energy_level = int(input("[2] Energy Level (1-10): ").strip())
    except ValueError:
        energy_level = 5
        
    try:
        focus_clarity = int(input("[3] Focus / Clarity (1-10): ").strip())
    except ValueError:
        focus_clarity = 5
        
    observational_state = input("[4] Primary Observational State (Detailed somatic description):\n> ").strip()
    
    return event_type, energy_level, focus_clarity, observational_state

def main():
    event_type, energy, focus, state_desc = collect_somatic_input()
    
    # Time calculation (HST = UTC-10)
    now_utc = datetime.now(timezone.utc)
    hst_tz = timezone(timedelta(hours=-10))
    now_local = now_utc.astimezone(hst_tz)
    
    timestamp_utc_str = now_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    timestamp_local_str = now_local.strftime("%Y-%m-%dT%H:%M:%S-10:00")
    file_timestamp = now_local.strftime("%Y%m%d_%H%M")
    
    env_data = get_environmental_telemetry()
    
    telemetry_packet = {
        "header": {
            "protocol_version": "1.1",
            "signature": IDENTITY_SIGNATURE,
            "reference_marker": REFERENCE_MARKER,
            "timestamp_utc": timestamp_utc_str,
            "timestamp_local": timestamp_local_str,
            "location": {
                "address": "3741 Poka Place, Honolulu, HI 96816",
                "coordinates": f"{LATITUDE}, {LONGITUDE}"
            }
        },
        "trial_metadata": {
            "trial_id": "Trial_001",
            "event_type": event_type,
            "target_directory": DEFAULT_TRIAL_DIR
        },
        "objective_telemetry": {
            "environmental_influences": env_data,
            "system_state": {
                "platform": sys.platform,
                "python_version": sys.version.split()[0],
                "pipeline_status": "ACTIVE"
            }
        },
        "subjective_somatic": {
            "energy_level": energy,
            "focus_clarity": focus,
            "observational_state": state_desc
        }
    }
    
    os.makedirs(DEFAULT_TRIAL_DIR, exist_ok=True)
    
    filename = f"telemetry_{file_timestamp}_{event_type.lower()}.json"
    filepath = os.path.join(DEFAULT_TRIAL_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(telemetry_packet, f, indent=2)
        
    print("\n" + "-"*60)
    print(f"[+] SUCCESS: Hyper-Local Telemetry Packet Generated!")
    print(f"[+] Saved to: {filepath}")
    print("-"*60)

if __name__ == "__main__":
    main()
