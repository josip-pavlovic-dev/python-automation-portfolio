from pathlib import Path

# from datetime import datetime

# === 1. ODREDI RADNI DIREKTORIJUM ===
# Skripta treba da se pokreće iz sandbox/basics/ direktorijuma
script_dir = Path(__file__).parent
print(f"📁 Script dir: {script_dir}")

# === 2. PROVERI POSTOJEĆI SYMLINK ===
link = script_dir / "logs/latest.log"  # ✅ Apsolutna putanja od script_dir
print(f"\n📂 Link putanja: {link}")
print(f"🔗 Da li je symlink? {link.is_symlink()}")
print(f"📁 Link postoji? {link.exists()}")

# === 3. VIDI TARGET (ako postoji) ===
if link.is_symlink():
    raw_target = link.readlink()  # Relativna putanja kako je sačuvana
    resolved = link.resolve()      # Apsolutna putanja
    print(f"\n🎯 Raw target (kako je sačuvan): {raw_target}")
    print(f"📍 Resolved (apsolutna putanja): {resolved}")
    print(f"✅ Target postoji? {resolved.exists()}")

# === 4. KREIRAJ TESTNE LOG FAJLOVE ===
log_dir = script_dir / "cli_logging_practice/logs"  # ✅ Apsolutna putanja
log_dir.mkdir(parents=True, exist_ok=True)

# Kreiraj nekoliko dnevnih log fajlova
log1 = log_dir / "app_2025-12-24.log"
log2 = log_dir / "app_2025-12-25.log"
log3 = log_dir / "app_2025-12-26.log"

log1.write_text("Log za 24. decembar - Testiranje symlinks\n")
log2.write_text("Log za 25. decembar - Više testova\n")
log3.write_text("Log za 26. decembar - NAJNOVIJI log!\n")

print("\n✅ Kreirani test log fajlovi:")
print(f"   - {log1.name}")
print(f"   - {log2.name}")
print(f"   - {log3.name}")

# === 5. KREIRAJ SYMLINK HELPER FUNKCIJU ===
def update_symlink(link: Path, target: Path, *, relative: bool = True) -> None:
    """Create/update symlink at `link` pointing to `target`."""
    if link.is_symlink():
        link.unlink()
    elif link.exists():
        raise FileExistsError(f"Cannot overwrite regular file: {link}")

    if relative:
        try:
            target_rel = target.relative_to(link.parent)
        except ValueError:
            target_rel = target
        link.symlink_to(target_rel)
    else:
        link.symlink_to(target)
    print(f"🔗 Updated: {link.name} → {target.name}")

# === 6. UPDATE SYMLINK DA POKAZUJE NA log1 ===
update_symlink(link, log1)

print("\n📖 Čitaj kroz symlink:")
print(f"   Sadržaj: {link.read_text()}")
print(f"   Target: {link.readlink()}")

# === 7. UPDATE SYMLINK DA POKAZUJE NA log2 ===
print("\n🔄 Promeni symlink da pokazuje na drugi fajl...")
update_symlink(link, log2)

print("📖 Čitaj ponovo kroz ISTI symlink:")
print(f"   Sadržaj: {link.read_text()}")
print(f"   Target: {link.readlink()}")

# === 8. UPDATE SYMLINK DA POKAZUJE NA log3 (najnoviji) ===
print("\n🔄 Promeni symlink da pokazuje na najnoviji log...")
update_symlink(link, log3)

print("📖 Čitaj ponovo (treći put) kroz ISTI symlink:")
print(f"   Sadržaj: {link.read_text()}")
print(f"   Target: {link.readlink()}")

# === 9. POENTA: Kod ne mora da se menja! ===
print("\n" + "="*60)
print("🎯 POENTA SYMLINKS-a:")
print("="*60)
print(f"✅ Tvoj kod UVEK čita: {link}")
print(f"✅ Ali zapravo čita iz: {link.resolve().name}")
print("✅ Možeš da menjaš target BEZ promene koda!")
print("✅ Perfektno za log rotation, config fajlove, data snapshots!")
print("="*60 + "\n")
print(f"📖 Finalni čitanje kroz symlink:"
      f"\n   Sadržaj: {link.read_text()}"
      f"\n   Target: {link.readlink()}"
      )
# === KRAJ ===

