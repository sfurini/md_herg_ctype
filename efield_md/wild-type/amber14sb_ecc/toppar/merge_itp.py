n_chains = 4
delta_chain = 1905

fin = open('PROA.itp', 'rt')
fout = open('PRO.itp', 'wt')

l = fin.readline()
while l:
    if l:
        if l[0] == ';' or l =='\n':
            fout.write(l)
        elif l[0] == '[':
            fout.write(l)
            if l.split()[1] == 'moleculetype':
                l = fin.readline()
                fout.write(l)
                l = fin.readline()
                fout.write('PRO 	     3\n')
            elif l.split()[1] == 'atoms':
                l = fin.readline()
                fout.write(l)
                l = fin.readline()
                atoms = []
                while l != '\n':
                    l = l.strip()
                    if l[0] != ';':
                        atoms.append(l.split())
                    l = fin.readline()
                for i_chain in range(n_chains):
                    for i_atom, atom in enumerate(atoms):
                        print(atom)
                        nr = int(atom[0])
                        kind = atom[1]
                        resnr = atom[2]
                        residu = atom[3]
                        name = atom[4]
                        cgnr = atom[5]
                        charge = atom[6]
                        mass = atom[7]
                        fout.write('{}\t\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t; qtot  {}\n'.format(nr+i_chain*delta_chain, kind, resnr, residu, name, nr+i_chain*delta_chain, charge, mass, atom[-1]))
                fout.write('\n')
            elif l.split()[1] == 'bonds':
                l = fin.readline()
                fout.write(l)
                l = fin.readline()
                bonds = []
                while l != '\n':
                    l = l.strip()
                    bonds.append(l.split())
                    l = fin.readline()
                for i_chain in range(n_chains):
                    for i_bond, bond in enumerate(bonds):
                        n1 = int(bond[0])
                        n2 = int(bond[1])
                        f = bond[2]
                        fout.write('{}\t{}\t{}\n'.format(n1+i_chain*delta_chain, n2+i_chain*delta_chain, f))
                fout.write('\n')
            elif l.split()[1] == 'pairs':
                l = fin.readline()
                fout.write(l)
                l = fin.readline()
                fout.write(l)
                l = fin.readline()
                pairs = []
                while l != '\n':
                    l = l.strip()
                    pairs.append(l.split())
                    l = fin.readline()
                for i_chain in range(n_chains):
                    for i_pair, pair in enumerate(pairs):
                        n1 = int(pair[0])
                        n2 = int(pair[1])
                        f = pair[2]
                        fout.write('{}\t{}\t{}\n'.format(n1+i_chain*delta_chain, n2+i_chain*delta_chain, f))
                fout.write('\n')
            elif l.split()[1] == 'angles':
                l = fin.readline()
                fout.write(l)
                l = fin.readline()
                angles = []
                while l != '\n':
                    l = l.strip()
                    angles.append(l.split())
                    l = fin.readline()
                for i_chain in range(n_chains):
                    for i_angle, angle in enumerate(angles):
                        n1 = int(angle[0])
                        n2 = int(angle[1])
                        n3 = int(angle[2])
                        f = angle[3]
                        fout.write('{}\t{}\t{}\t{}\n'.format(n1+i_chain*delta_chain, n2+i_chain*delta_chain, n3+i_chain*delta_chain, f))
                fout.write('\n')
            elif l.split()[1] == 'dihedrals':
                l = fin.readline()
                fout.write(l)
                l = fin.readline()
                dihedrals = []
                while l and l != '\n':
                    l = l.strip()
                    if l:
                        if l[0] != ';':
                            dihedrals.append(l.split())
                    print(l)
                    l = fin.readline()
                for i_chain in range(n_chains):
                    for i_dihedral, dihedral in enumerate(dihedrals):
                        n1 = int(dihedral[0])
                        n2 = int(dihedral[1])
                        n3 = int(dihedral[2])
                        n4 = int(dihedral[3])
                        f = dihedral[4]
                        fout.write('{}\t{}\t{}\t{}\t{}\n'.format(n1+i_chain*delta_chain, n2+i_chain*delta_chain, n3+i_chain*delta_chain, n4+i_chain*delta_chain, f))
                fout.write('\n')
        elif l == '#ifdef POSRES\n':
            fout.write(l)
            l = fin.readline()
            fout.write(l)
            l = fin.readline()
            posress = []
            while l != '#endif\n':
                l = l.strip()
                posress.append(l.split())
                l = fin.readline()
            for i_chain in range(n_chains):
                for i_posres, posres in enumerate(posress):
                    n1 = int(posres[0])
                    fout.write('{}\t{}\t{}\t{}\t{}\n'.format(n1+i_chain*delta_chain, posres[1], posres[2], posres[3], posres[4]))
            fout.write('#endif\n')
    l = fin.readline()

fin.close()
fout.close()
