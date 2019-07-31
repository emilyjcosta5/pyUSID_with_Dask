function clone_pull {
  DIRECTORY=$(basename "$1" .git)
  if [ -d "$DIRECTORY" ]; then
    cd "$DIRECTORY"
    git pull
    cd ../
  else
    git clone "$1"
  fi
}
clone_pull https://github.com/emilyjcosta5/pyUSID_with_Dask.git
export PATH=/gpfs/alpine/gen011/world-shared/native-build/anaconda3/bin:$PATH
source activate WML161
jupyter-lab --ip=0.0.0.0 --no-browser --NotebookApp.token='' --port 8887
