import logging
from pathlib import Path

# Kreiraj logs folder ako ne postoji
logs_dir = Path(__file__).parent.parent / "logs"
logs_dir.mkdir(exist_ok=True)


def get_logger(name: str) -> logging.Logger:
    """Kreiraj i konfiguriši logger sa imenom `name`."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Loša praksa: višestruko dodavanje handlera
    # Svaki put kada se pozove funkcija dodaje se novi handler!
    # To može dovesti do duplih log poruka.
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    return logger

print("Pokrećem primer sa duplim handlerima...")
print("Loša praksa: svaki poziv get_logger dodaje novi handler.")
print("Zato ćeš videti svaku log poruku više puta u konzoli.")

# Primer korišćenja loše prakse -> pozovati više puta
for i in range(3):
    log = get_logger(name="duplicate_logger")
    log.info(f"Log poruka broj {i + 1}")

print("Pokrenuto je više log poruka sa duplim handlerima.")
print("Zbog loše prakse, svaka log poruka se pojavila više puta u konzoli.")
print(
    "Reši problem tako što ćeš proveriti da li logger već ima"
    " handlere pre dodavanja novih."
)

# Rešenje problema: proveri da li logger već ima handlere
def get_logger_fixed(name: str) -> logging.Logger:
    """Kreiraj i konfiguriši logger sa imenom `name`."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Dobra praksa: proveri da li logger već ima handlere, dodaj samo ako ih nema!
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S")
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Primer korišćenja ispravljenog koda
for i in range(3):
    log_fixed = get_logger_fixed(name="fixed_logger")
    log_fixed.info(f"Ispravljena log poruka broj {i + 1}")
