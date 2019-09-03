#!/bin/bash
#SBATCH -N 1
#SBATCH -n 20
#SBATCH -t 2:00:00
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
#SBATCH --mail-user=ctokita@princeton.edu

module load anaconda3
cd InformationCascades/
srun python3 scripts/3_gammasweep-networkbreaking.py -1 1 0.1