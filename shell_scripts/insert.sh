#!/bin/bash
#SBATCH -N 1
#SBATCH -n 24



source /etc/profile
source $HOME/gromacs/gromacs-2021/install/bin/GMXRC
./etc/profile.d/modules.sh
module load mpi/openmpi-4.0
module load anaconda/2021b
gmx_mpi insert-molecules -f fens.gro -o fens_mcaniso.gro -ip mcaniso_pos.dat -dr 9 9 1.25 -radius 0.01 -nmol 40 -try 1000000 -ci MC.pdb -rot z
gmx_mpi insert-molecules -f fens_mcaniso.gro -o fens_m.gro -ip mciso_pos.dat -dr 9 9 1.25 -radius 0.01 -nmol 40 -try 1000000 -ci MC.pdb
gmx_mpi insert-molecules -f fens_m.gro -o fens_mt.gro -ip tw80_pos.dat -dr 10 10 1.25 -radius 0.01 -nmol 86 -try 1000000 -ci tw80.pdb

exit;

