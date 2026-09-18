def estrai_indici_per_categoria(itp_file, categorie, forze):
    """
    Estrae gli indici degli atomi da un file .itp per categorie e ordina gli indici
    all'interno di ogni categoria.
    """
    indici_categorie = {cat: [] for cat in categorie}

    in_atoms = False
    with open(itp_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(";"):
                continue

            if line.startswith("[ atoms ]"):
                in_atoms = True
                continue
            if in_atoms and line.startswith("["):
                break

            if in_atoms:
                campi = line.split()
                if len(campi) < 5:
                    continue

                nr = int(campi[0])
                type = campi[1]
                resnr = campi[2]
                residue = campi[3]
                atom = campi[4]

                residuo_full = residue if residue in ["ACE", "NME"] else f"{residue} {resnr}"

                # controlla a quale categoria appartiene il residuo
                categoria = next((cat for cat, reslist in categorie.items() if residuo_full in reslist), None)
                if categoria is None:
                    continue

                # selezione atomi
                if categoria == "SF" and atom not in ["N", "CA", "C", "O"]:
                    continue
                elif categoria != "SF" and type[0] not in ["C", "O", "N"]:
                    continue

                indici_categorie[categoria].append(nr)

    # ordina gli indici all'interno di ciascuna categoria
    for cat in indici_categorie:
        indici_categorie[cat].sort()

    return indici_categorie


if __name__ == "__main__":
    file_itp = "PRO.itp"

    categorie = {
        "TER": ["ACE", "NME"],
        "CAV": ["TYR 652", "PHE 656"],
        "SF": ["SER 624", "VAL 625", "GLY 626", "PHE 627", "GLY 628"]
    }

    forze = {
        "TER": "POSRES_FC_TER",
        "CAV": "POSRES_FC_CAV",
        "SF": "POSRES_FC_SF"
    }

    indici_per_categoria = estrai_indici_per_categoria(file_itp, categorie, forze)

    print("\n[ position_restraints ]")
    # stampa in ordine TER → CAV → SF
    for cat in ["TER", "CAV", "SF"]:
        forza = forze[cat]
        for nr in indici_per_categoria[cat]:
            print(f"{nr}\t1\t{forza}\t{forza}\t{forza}")
