import numpy as np

input_file = r"D:\input_data"###
output_file = r"D:\output_data"
A = 316.7807  # size

R = np.array([
    [0.408248, 0.408248, -0.816497],
    [-0.707107, 0.707107, 0],
    [0.57735, 0.57735, 0.57735],
], dtype=np.float32)#11-2 -110 111


max_rep = 2

# read_data
def read_lammps(filename):
    atoms = []
    box = []
    masses = []
    atom_types = 0

    with open(filename) as f:
        lines = f.readlines()

    read_atoms = False
    read_masses = False

    for line in lines:
        if "atom types" in line:
            atom_types = int(line.split()[0])

        if "xlo xhi" in line or "ylo yhi" in line or "zlo zhi" in line:
            box.append(list(map(float, line.split()[:2])))

        if "Masses" in line:
            read_masses = True
            continue

        if "Atoms" in line:
            read_atoms = True
            read_masses = False
            continue

        if read_masses and line.strip():
            masses.append(line.strip())

        if read_atoms:
            parts = line.split()
            if len(parts) >= 5:
                atoms.append([
                    int(parts[0]),
                    int(parts[1]),
                    float(parts[2]),
                    float(parts[3]),
                    float(parts[4])
                ])

    return np.array(atoms, dtype=np.float32), np.array(box), masses, atom_types


# judge_atom
def is_outside_block(shift, coords_rot, box):
    min_c = coords_rot.min(axis=0) + shift
    max_c = coords_rot.max(axis=0) + shift

    if (max_c[0] < box[0][0] or min_c[0] > box[0][1] or
        max_c[1] < box[1][0] or min_c[1] > box[1][1] or
        max_c[2] < box[2][0] or min_c[2] > box[2][1]):
        return True
    return False


atoms, box, masses, atom_types = read_lammps(input_file)

coords = atoms[:, 2:5]

coords_rot = coords @ R.T

lx = box[0][1] - box[0][0]
ly = box[1][1] - box[1][0]
lz = box[2][1] - box[2][0]

a1 = R @ np.array([lx, 0, 0], dtype=np.float32)
a2 = R @ np.array([0, ly, 0], dtype=np.float32)
a3 = R @ np.array([0, 0, lz], dtype=np.float32)

new_box = np.array([
    [-A/2, A/2],
    [-A/2, A/2],
    [-A/2, A/2]
], dtype=np.float32)

print("total atom...")

count = 0

for i in range(-max_rep, max_rep+1):
    for j in range(-max_rep, max_rep+1):
        for k in range(-max_rep, max_rep+1):

            shift = i*a1 + j*a2 + k*a3

            if is_outside_block(shift, coords_rot, new_box):
                continue

            for idx in range(len(coords_rot)):
                new_coord = coords_rot[idx] + shift

                if (new_box[0][0] <= new_coord[0] <= new_box[0][1] and
                    new_box[1][0] <= new_coord[1] <= new_box[1][1] and
                    new_box[2][0] <= new_coord[2] <= new_box[2][1]):

                    count += 1

print(f"原子数 = {count}")

print("output ing...")

with open(output_file, "w") as f:
   
    f.write("LAMMPS data file\n\n")
    f.write(f"{count} atoms\n")
    f.write(f"{atom_types} atom types\n\n")

    f.write(f"{new_box[0][0]} {new_box[0][1]} xlo xhi\n")
    f.write(f"{new_box[1][0]} {new_box[1][1]} ylo yhi\n")
    f.write(f"{new_box[2][0]} {new_box[2][1]} zlo zhi\n\n")

    f.write("Masses\n\n")
    for m in masses:
        f.write(m + "\n")

    f.write("\nAtoms\n\n")

    atom_id = 1

    for i in range(-max_rep, max_rep+1):
        for j in range(-max_rep, max_rep+1):
            for k in range(-max_rep, max_rep+1):

                shift = i*a1 + j*a2 + k*a3

                if is_outside_block(shift, coords_rot, new_box):
                    continue

                for idx, atom in enumerate(atoms):
                    new_coord = coords_rot[idx] + shift

                    if (new_box[0][0] <= new_coord[0] <= new_box[0][1] and
                        new_box[1][0] <= new_coord[1] <= new_box[1][1] and
                        new_box[2][0] <= new_coord[2] <= new_box[2][1]):

                        f.write(f"{atom_id} {int(atom[1])} "
                                f"{new_coord[0]:.6f} {new_coord[1]:.6f} {new_coord[2]}:.6f\n")

                        atom_id += 1

                        
                        if atom_id % 100000 == 0:
                            f.flush()

print("done!")