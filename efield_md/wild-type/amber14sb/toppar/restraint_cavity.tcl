mol load gro ../pmwi.gro
set sel [atomselect top "resname ACE NME and noh"]
foreach ndx [$sel get index] {
	puts "[expr $ndx + 1]\t1\tPOSRES_FC_TER\tPOSRES_FC_TER\tPOSRES_FC_TER"
}
set sel [atomselect top "protein and resid 113 238 363 488 109 234 359 484 and noh"]
foreach ndx [$sel get index] {
	puts "[expr $ndx + 1]\t1\tPOSRES_FC_CAV\tPOSRES_FC_CAV\tPOSRES_FC_CAV"
}
exit
