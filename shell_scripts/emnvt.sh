#!/bin/bash
#SBATCH -N 1
#SBATCH -n 20



source /etc/profile
source $HOME/gromacs/gromacs-2021/install/bin/GMXRC
./etc/profile.d/modules.sh
module load mpi/openmpi-4.0
module load anaconda/2021b
gmx_mpi grompp -f em.mdp -c fens_mt.gro -n index.ndx -p fens.top -o em.tpr -r fens_mt.gro
gmx_mpi mdrun -v -deffnm em -ntomp 20
gmx_mpi grompp -f nvt.mdp -c em.gro -n index.ndx -p fens.top -o nvt.tpr -r em.gro
gmx_mpi mdrun -v -deffnm nvt -ntomp 20
exit;
