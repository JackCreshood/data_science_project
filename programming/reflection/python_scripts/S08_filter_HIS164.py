cmd.delete("all")
import pandas as pd

# basic settings
cmd.delete("all")
cmd.load("F:/structures/S08/structure.pdb")
cmd.select("CA_S08", "/////CA")
cmd.show("spheres", "CA_S08")
cmd.set("sphere_scale", 0.5, "CA_S08")
cmd.hide("cartoon")

target_ca = "CA_164"
ca_group = "HIS_164"
HIS_data = pd.read_csv("F:/Bristol/courses/DSP/codes/filter/S08_filter_HIS164.csv", index_col=0)
HIS_index = list(HIS_data.index)
HIS_corr = list(HIS_data['HIS_164'])
atom_type = "CA_"
basic_path_pre = "/CA_S08///"
basic_path_sub = "/CA"
cmd.select(target_ca, "/CA_S08///164/CA")
cmd.group(ca_group, target_ca)

for i in range(len(HIS_index)):
    temp_idx = HIS_index[i]
    temp_corr = HIS_corr[i]
    temp_abs_corr = abs(temp_corr)
    temp_order = temp_idx[4:]
    temp_sele = atom_type + temp_order
    temp_path = basic_path_pre + temp_order + basic_path_sub
    cmd.select(temp_sele, temp_path)
    cmd.bond(target_ca, temp_sele)
    cmd.set_bond("stick_radius", temp_abs_corr, target_ca, temp_sele)
    # use different colors due to whether the correlation is positive or negative
    if temp_corr > 0:
        cmd.set_bond("stick_color", "blue", target_ca, temp_sele)
    elif temp_corr < 0:
        cmd.set_bond("stick_color", "red", target_ca, temp_sele)
    cmd.group(ca_group, temp_sele, "add")

cmd.color("yellow", target_ca)
cmd.show("stick", ca_group)
cmd.bg_color("white")