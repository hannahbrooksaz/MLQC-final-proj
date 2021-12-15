# MLQC-final-proj
Final Project - CSCI3340, Boston College, Fall 2021

### Setup
The libraries we needed to run `janggu` are listed in `final-proj-env.yml`. To set up an equivalent environment:
1. Download `final-proj-env.yml`
2. Edit `prefix:` in the last row to match where you normally install libraries
3. Create the environment. We used conda: `conda env create -f final-proj-env.yml`
4. Activate the environment. Again, we used conda: `conda activate final-proj`

### Troubleshooting
If `bedtools`-related issues arise (i.e., `janggu` cannot run `bedtools` via `pybedtools` internally), put the following lines in your `~/.bashrc` file, substituting the fields contained in `<>` with the actual paths:

`
export PATH="<where-janggu-is-installed>/lib:$PATH"
`

`
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$<where-janggu-is-installed>/lib"
`

`
export C_INCLUDE_PATH="<where-janggu-is-installed>/include"
`

`
export CPLUS_INCLUDE_PATH="<where-janggu-is-installed>/include"
`

### Questions?
This is a work in progress. Please be in touch with any questions: weissjy@bc.edu
