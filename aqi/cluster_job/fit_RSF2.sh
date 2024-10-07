#!/bin/bash
#SBATCH --account=def-monti
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --time=10:00:00
#SBATCH --mail-user=fraser_franco.maxime@courrier.uqam.ca
#SBATCH --mail-type=ALL

module load python/3.11.5
python fit_RSF2.py