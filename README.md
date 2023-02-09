# fairdivision
[Reading] (https://cs.binghamton.edu/~sikdar/papers/FSVX19equitable.pdf)
[Notes](https://www.notion.so/Equitable-allocations-4009ba1acc7f4b89ae57ff7d93d733a6)

### Activating venv
```
source venv/bin/activate
```

### Creating requiement.txt file
```
pip install pipreqs
python -m  pipreqs.pipreqs --encoding utf-8  /Users/anmolpal/projects/prof-sujoy-sikars-material/fairdivisionFork
```

### downloading all project requirements
check if requirement.txt was created
```
(venv) (base) anmolpal@Anmols-Air fairdivisionFork % ls -ltar requirements.txt 
-rw-r--r--  1 anmolpal  staff  76 Feb  2 13:39 requirements.txtpip3 install -r requirements.txt
```

```
pip3 install -r requirements.txt
```

###Installing gurobi
1. Create an academic account on gurobi [website](https://www.gurobi.com/downloads/gurobi-software/) and install download respective version. [for steps by gurobi] (https://www.gurobi.com/features/academic-named-user-license/)
2. Installation
```
 >conda config --add channels https://conda.anaconda.org/gurobi
 >conda install gurobi
 Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /opt/homebrew/Caskroom/miniforge/base

  added / updated specs:
    - gurobi


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    gurobi-10.0.1              |          py310_0        39.2 MB  gurobi
    ------------------------------------------------------------
                                           Total:        39.2 MB

The following NEW packages will be INSTALLED:

  gurobi             gurobi/osx-64::gurobi-10.0.1-py310_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages
                                                                                                       
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```


Follow - file:///Library/gurobi1001/macos_universal2/docs/quickstart/cs_python_installation_opt.html

file:///Library/gurobi1001/macos_universal2/docs/quickstart/retrieving_and_setting_up_.html#section:RetrieveLicense

### gurobi liscence written to 
```
License 929083 written to file /Users/anmolpal/gurobi.lic
```


## Code Structure
#### 1. [data.py] (data.py)
Generate Functions 
Load Funtions 

#### 2. [main.py] (main.py)
Calls a function to generate equitable allocations - eq_goods()

#### 3. 
Will run some experiments on differnet allocation methods eg[Maximize nash welfare or leximin](solution.py) whether or not the defined properties are met
