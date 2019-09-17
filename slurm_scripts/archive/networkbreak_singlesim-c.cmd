#!/bin/bash
#SBATCH -N 1
#SBATCH -c 20
#SBATCH --time=9:59:00
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
#SBATCH --mail-user=ctokita@princeton.edu

module load anaconda3
module load 
cd InformationCascades/
srun python3 scripts/2_parallel-networkbreaking_simple.py