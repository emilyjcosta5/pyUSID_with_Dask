# Start JupyterLab
export PATH=/gpfs/alpine/gen011/world-shared/native-build/anaconda3/bin:$PATH
source activate WML161
jupyter-lab --ip=0.0.0.0 --no-browser --NotebookApp.token='' --port 8887
