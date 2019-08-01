# Set up environment
export PATH=/gpfs/alpine/world-shared/gen011/native-build/anaconda3/bin:$PATH

# Make sure repo it there and up-to-date
function clone_pull {
  DIRECTORY=$(basename "$1" .git)
  if [ -d "$DIRECTORY" ] | [ -d "../../$DIRECTORY"]; then
    cd "$DIRECTORY"
    git pull
    cd ../
  else
    git clone "$1"
  fi
}
clone_pull https://github.com/emilyjcosta5/pyUSID_with_Dask.git

# Start JupyterLab
export PATH=/gpfs/alpine/gen011/world-shared/native-build/anaconda3/bin:$PATH
source activate WML161
jupyter-lab --ip=0.0.0.0 --no-browser --NotebookApp.token='' --port 8887
