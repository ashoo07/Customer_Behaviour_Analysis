import os
import sys
import time
import traceback
from pathlib import Path

# Always work from the project folder, even when started by Task Scheduler
PROJECT_DIR = Path(__file__).resolve().parent
os.chdir(PROJECT_DIR)
sys.path.insert(0, str(PROJECT_DIR / "etl"))

from logger import get_logger
from extract import extract_all
from transform import transform_all
from quality import run_quality_checks
from load import load_all

log = get_logger()


def run(load=True):
    start = time.time()
    log.info("=== Pipeline started ===")
    try:
        raw = extract_all()
        log.info(f"Extract done: {sum(len(df) for df in raw.values())} rows read")

        cleaned = transform_all(raw)
        log.info("Transform done")

        good = run_quality_checks(cleaned)
        kept = len(good["purchases"])
        log.info(f"Quality checks done: {kept} purchase rows kept")

        if load:
            load_all(good)
            log.info(f"Load done: {kept} rows in fact_purchases")
        else:
            log.info("Dry run: load step skipped")

        log.info(f"=== Pipeline finished successfully in {time.time() - start:.1f}s ===")
        return 0
    except Exception:
        log.error("Pipeline FAILED:\n" + traceback.format_exc())
        return 1


if __name__ == "__main__":
    # "python run_pipeline.py --no-load" runs everything except the database step
    sys.exit(run(load="--no-load" not in sys.argv))