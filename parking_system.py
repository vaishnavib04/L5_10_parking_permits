"""Manage parking permits and identify vehicles with invalid permits."""

import json
import secrets
from datetime import datetime, timedelta

# Global state
permits = {}
ZONES = ["A", "B", "C"]


def register_permit(vehicle_plate, zone_id, zone_records=None):
    """Register a vehicle for a valid parking zone."""
    if not isinstance(vehicle_plate, str) or not vehicle_plate.strip():
        return None

    if zone_id not in ZONES:
        return None

    if zone_records is None:
        zone_records = []

    permit_no = "P" + str(secrets.randbelow(90000) + 10000)
    expiry = datetime.now() + timedelta(days=180)
    permits[vehicle_plate] = {
        "zone": zone_id,
        "permit": permit_no,
        "expiry": expiry.strftime("%Y-%m-%d"),
    }
    zone_records.append((vehicle_plate, zone_id))
    return permit_no


def revoke_permit(vehicle_plate):
    """Revoke a vehicle's permit if one exists."""
    try:
        del permits[vehicle_plate]
    except KeyError:
        pass


def is_expired(vehicle_plate):
    """Return whether a vehicle's permit has expired."""
    try:
        expiry = datetime.strptime(
            permits[vehicle_plate]["expiry"], "%Y-%m-%d"
        )
    except (KeyError, TypeError, ValueError):
        return False

    return expiry < datetime.now()


def scan_zone(zone_id, plates_seen):
    """Return plates without a valid permit for the scanned zone."""
    flagged = []
    for plate in plates_seen:
        if (
            plate not in permits
            or permits[plate]["zone"] != zone_id
            or is_expired(plate)
        ):
            flagged.append(plate)
    return flagged


def load_permit_database(file="permits.json"):
    """Load saved permits and update the in-memory database."""
    try:
        with open(file, "r", encoding="utf-8") as database_file:
            loaded_permits = json.load(database_file)
        if not isinstance(loaded_permits, dict):
            raise ValueError("Permit database must contain a JSON object.")
    except (OSError, json.JSONDecodeError, ValueError):
        loaded_permits = {}

    permits.clear()
    permits.update(loaded_permits)


def save_permit_database(file="permits.json"):
    """Save all permits to a JSON file."""
    with open(file, "w", encoding="utf-8") as database_file:
        json.dump(permits, database_file, indent=4)


def set_expiry(vehicle_plate, date_text):
    """Set a permit's expiry date using YYYY-MM-DD format."""
    expiry = datetime.strptime(date_text, "%Y-%m-%d")
    permits[vehicle_plate]["expiry"] = expiry.strftime("%Y-%m-%d")


def main():
    """Run a demonstration of the parking permit system."""
    load_permit_database()
    register_permit("KA01AB1234", "A")
    register_permit("KA05XY9999", "Z")
    register_permit("", "B")
    register_permit(None, "C")
    set_expiry("KA01AB1234", "2020-01-01")
    revoke_permit("MH12ZZ0000")

    print(
        "Flagged in zone A:",
        scan_zone("A", ["KA01AB1234", "KA05XY9999", "TN09QQ1111"]),
    )
    plate = input("Plate to revoke (Enter to skip): ")
    if plate:
        revoke_permit(plate)

    save_permit_database()
    print("Permits on file:", len(permits))


if __name__ == "__main__":
    main()
