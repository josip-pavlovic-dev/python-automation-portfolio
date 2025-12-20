import logging
from pathlib import Path

# Kreiraj logs folder ako ne postoji
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Kreiraj i konfiguriši logger
logger = logging.getLogger("file_logger")
logger.setLevel(logging.DEBUG)

# Kreiraj formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Kreiraj stream handler (konsola)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Kreiraj file handler (fajl)
file_handler = logging.FileHandler(log_dir / "file_logger.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Dodaj handlere loggeru
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

# Primer log poruka
logger.debug("Ovo je debug poruka - detaljne informacije za dijagnostiku.")
logger.info("Ovo je info poruka - opšte informacije o radu aplikacije.")
logger.warning(
    "Ovo je warning poruka - nešto neočekivano se desilo,"
    "ali aplikacija nastavlja sa radom."
)
logger.error(
    "Ovo je error poruka - došlo je do greške koja je uticala na rad aplikacije."
)
logger.critical(
    "Ovo je critical poruka - ozbiljna greška," \
    "aplikacija možda neće moći da nastavi sa radom."
)

print("Log poruke su zabeležene u konzoli i u fajlu 'logs/file_logger.log'.")
