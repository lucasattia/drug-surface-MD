#!/bin/bash
#SBATCH -N 1
#SBATCH -n 20

source /etc/profile
source $HOME/gromacs/gromacs-2021/install/bin/GMXRC
./etc/profile.d/modules.sh
module load mpi/openmpi-4.0
module load anaconda/2021b

dup_backupext() {
result=${PWD##*/} 
result2="${result}_backupext"
cd ../
cp -r $result  $result2
cd $result 
}

dup_backupext
gmx_mpi convert-tpr -s nvt.tpr -extend 9625 -o nvt_extend.tpr
gmx_mpi mdrun -v -deffnm nvt_extend -cpi nvt.cpt -noappend -ntomp 20
gmx_mpi trjcat -f nvt.xtc nvt_extend.part0002.xtc -o nvtboth.xtc
gmx_mpi eneconv -f nvt.edr nvt_extend.part0002.edr -o nvtboth.edr
sbatch rdf.sh
exit;
