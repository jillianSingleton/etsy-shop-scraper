thonpython
import json
import logging
from pathlib import Path

class Exporter:
    def export_json(self, data):
        output_path = Path(__file__).resolve().parents[1] / "data" / "sample_output.json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        logging.info(f"Output written to {output_path}")