def load_disposable_domains(file_path="data/disposable_domains.txt"):
    try:
        with open(file_path, "r") as f:
            domains = set(line.strip().lower() for line in f if line.strip())
        return domains
    except FileNotFoundError:
        return set()