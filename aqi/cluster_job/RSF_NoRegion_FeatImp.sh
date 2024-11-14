#!/bin/bash
#SBATCH --account=def-monti
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=124G
#SBATCH --time=5:00:00
#SBATCH --mail-user=fraser_franco.maxime@courrier.uqam.ca
#SBATCH --mail-type=ALL

module load python/3.11.5
python RSF_NoRegion_FeatImp.py