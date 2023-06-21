
(base) C:\Users\ASUS>conda --version
conda 23.3.1

(base) C:\Users\ASUS>conda update conda
Retrieving notices: ...working... done
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\ASUS\miniconda3

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2023.05.30 |       haa95532_0         120 KB
    certifi-2023.5.7           |  py310haa95532_0         153 KB
    conda-23.5.0               |  py310haa95532_0         1.0 MB
    conda-package-handling-2.1.0|  py310haa95532_0         287 KB
    conda-package-streaming-0.8.0|  py310haa95532_0          28 KB
    cryptography-39.0.1        |  py310h21b164f_2         1.0 MB
    intel-openmp-2023.1.0      |   h59b6b97_46319         2.7 MB
    joblib-1.2.0               |  py310haa95532_0         392 KB
    libffi-3.4.4               |       hd77b12b_0         113 KB
    mkl-2023.1.0               |   h8bd8f75_46356       155.6 MB
    mkl-service-2.4.0          |  py310h2bbff1b_1          44 KB
    mkl_fft-1.3.6              |  py310h4ed8f06_1         157 KB
    mkl_random-1.2.2           |  py310h4ed8f06_1         210 KB
    numexpr-2.8.4              |  py310h2cd9be0_1         128 KB
    numpy-1.24.3               |  py310h055cbcc_1          11 KB
    numpy-base-1.24.3          |  py310h65a83cf_1         5.2 MB
    openssl-3.0.8              |       h2bbff1b_0         7.4 MB
    pyopenssl-23.0.0           |  py310haa95532_0          98 KB
    python-3.10.11             |       he1021f5_3        15.8 MB
    sqlite-3.41.2              |       h2bbff1b_0         894 KB
    tbb-2021.8.0               |       h59b6b97_0         149 KB
    tqdm-4.65.0                |  py310h9909e9c_0         149 KB
    tzdata-2023c               |       h04d1e81_0         116 KB
    urllib3-1.26.16            |  py310haa95532_0         202 KB
    xz-5.4.2                   |       h8cc25b3_0         592 KB
    zstandard-0.19.0           |  py310h2bbff1b_0         340 KB
    ------------------------------------------------------------
                                           Total:       192.7 MB

The following NEW packages will be INSTALLED:

  tbb                pkgs/main/win-64::tbb-2021.8.0-h59b6b97_0

The following packages will be UPDATED:

  ca-certificates                     2023.01.10-haa95532_0 --> 2023.05.30-haa95532_0
  certifi                         2022.12.7-py310haa95532_0 --> 2023.5.7-py310haa95532_0
  conda                              23.3.1-py310haa95532_0 --> 23.5.0-py310haa95532_0
  conda-package-han~                  2.0.2-py310haa95532_0 --> 2.1.0-py310haa95532_0
  conda-package-str~                  0.7.0-py310haa95532_0 --> 0.8.0-py310haa95532_0
  cryptography                       38.0.4-py310h21b164f_0 --> 39.0.1-py310h21b164f_2
  intel-openmp                       2021.4.0-haa95532_3556 --> 2023.1.0-h59b6b97_46319
  joblib                              1.1.1-py310haa95532_0 --> 1.2.0-py310haa95532_0
  libffi                                   3.4.2-hd77b12b_6 --> 3.4.4-hd77b12b_0
  mkl                                 2021.4.0-haa95532_640 --> 2023.1.0-h8bd8f75_46356
  mkl-service                         2.4.0-py310h2bbff1b_0 --> 2.4.0-py310h2bbff1b_1
  mkl_fft                             1.3.1-py310ha0764ea_0 --> 1.3.6-py310h4ed8f06_1
  mkl_random                          1.2.2-py310h4ed8f06_0 --> 1.2.2-py310h4ed8f06_1
  numexpr                             2.8.4-py310hd213c9f_0 --> 2.8.4-py310h2cd9be0_1
  numpy                              1.23.5-py310h60c9a35_0 --> 1.24.3-py310h055cbcc_1
  numpy-base                         1.23.5-py310h04254f7_0 --> 1.24.3-py310h65a83cf_1
  openssl                                 1.1.1t-h2bbff1b_0 --> 3.0.8-h2bbff1b_0
  pyopenssl          pkgs/main/noarch::pyopenssl-22.0.0-py~ --> pkgs/main/win-64::pyopenssl-23.0.0-py310haa95532_0
  python                                  3.10.9-h966fe2a_0 --> 3.10.11-he1021f5_3
  sqlite                                  3.40.1-h2bbff1b_0 --> 3.41.2-h2bbff1b_0
  tqdm                               4.64.1-py310haa95532_0 --> 4.65.0-py310h9909e9c_0
  tzdata                                   2022g-h04d1e81_0 --> 2023c-h04d1e81_0
  urllib3                           1.26.14-py310haa95532_0 --> 1.26.16-py310haa95532_0
  xz                                      5.2.10-h8cc25b3_1 --> 5.4.2-h8cc25b3_0
  zstandard                          0.18.0-py310h2bbff1b_0 --> 0.19.0-py310h2bbff1b_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
pyopenssl-23.0.0     | 98 KB     | ############################################################################ | 100%
joblib-1.2.0         | 392 KB    | ############################################################################ | 100%
libffi-3.4.4         | 113 KB    | ############################################################################ | 100%
xz-5.4.2             | 592 KB    | ############################################################################ | 100%
zstandard-0.19.0     | 340 KB    | ############################################################################ | 100%
intel-openmp-2023.1. | 2.7 MB    | ############################################################################ | 100%
sqlite-3.41.2        | 894 KB    | ############################################################################ | 100%
numpy-base-1.24.3    | 5.2 MB    | ###########################4                                                 |  36%
conda-package-handli | 287 KB    | ############################################################################ | 100%
mkl_fft-1.3.6        | 157 KB    | ############################################################################ | 100%
tqdm-4.65.0          | 149 KB    | ############################################################################ | 100%
tbb-2021.8.0         | 149 KB    | ############################################################################ | 100%
cryptography-39.0.1  | 1.0 MB    | ############################################################################ | 100%
ca-certificates-2023 | 120 KB    | ############################################################################ | 100%
urllib3-1.26.16      | 202 KB    | ############################################################################ | 100%
mkl-2023.1.0         | 155.6 MB  | ###                                                                          |   4%
tzdata-2023c         | 116 KB    | ############################################################################ | 100%
conda-23.5.0         | 1.0 MB    | ############################################################################ | 100%
numpy-1.24.3         | 11 KB     | ############################################################################ | 100%
mkl_random-1.2.2     | 210 KB    | ############################################################################ | 100%
conda-package-stream | 28 KB     | ############################################################################ | 100%
python-3.10.11       | 15.8 MB   | #################                                                            |  22%
mkl-service-2.4.0    | 44 KB     | ############################################################################ | 100%
numexpr-2.8.4        | 128 KB    | ############################################################################ | 100%
openssl-3.0.8        | 7.4 MB    | ############5                                                                |  17%
certifi-2023.5.7     | 153 KB    | ############################################################################ | 100%






numpy-base-1.24.3    | 5.2 MB    | ############################################################################ | 100%







mkl-2023.1.0         | 155.6 MB  | ##########################                                                   |  34%





python-3.10.11       | 15.8 MB   | ############################################################################ | 100%


openssl-3.0.8        | 7.4 MB    | ############################################################################ | 100%














mkl-2023.1.0         | 155.6 MB  | ##################################################2                          |  66%
mkl-2023.1.0         | 155.6 MB  | ##################################################3                          |  66%





mkl-2023.1.0         | 155.6 MB  | ##################################################3                          |  66%


mkl-2023.1.0         | 155.6 MB  | ##################################################7                          |  67%
mkl-2023.1.0         | 155.6 MB  | ##################################################8                          |  67%


mkl-2023.1.0         | 155.6 MB  | ##################################################8                          |  67%


mkl-2023.1.0         | 155.6 MB  | ###################################################                          |  67%
mkl-2023.1.0         | 155.6 MB  | ###################################################1                         |  67%
mkl-2023.1.0         | 155.6 MB  | ###################################################1                         |  67%



mkl-2023.1.0         | 155.6 MB  | ###################################################2                         |  67%


mkl-2023.1.0         | 155.6 MB  | ###################################################2                         |  67%


mkl-2023.1.0         | 155.6 MB  | ###################################################3                         |  68%
mkl-2023.1.0         | 155.6 MB  | ###################################################5                         |  68%
mkl-2023.1.0         | 155.6 MB  | ###################################################7                         |  68%
mkl-2023.1.0         | 155.6 MB  | ###################################################7                         |  68%

mkl-2023.1.0         | 155.6 MB  | ###################################################8                         |  68%



mkl-2023.1.0         | 155.6 MB  | ###################################################8                         |  68%

Preparing transaction: done
Verifying transaction: done
Executing transaction: done

(base) C:\Users\ASUS>conda activate snowflakes

EnvironmentNameNotFound: Could not find conda environment: snowflakes
You can list all discoverable environments with `conda info --envs`.



(base) C:\Users\ASUS>conda create --name snowflakes biopython
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\ASUS\miniconda3\envs\snowflakes

  added / updated specs:
    - biopython


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    biopython-1.78             |  py311h2bbff1b_0         2.6 MB
    mkl-service-2.4.0          |  py311h2bbff1b_1          44 KB
    mkl_fft-1.3.6              |  py311hf62ec03_1         164 KB
    mkl_random-1.2.2           |  py311hf62ec03_1         218 KB
    numpy-1.24.3               |  py311hdab7c0b_1          11 KB
    numpy-base-1.24.3          |  py311hd01c5d8_1         6.1 MB
    pip-23.1.2                 |  py311haa95532_0         3.4 MB
    python-3.11.3              |       he1021f5_1        17.9 MB
    setuptools-67.8.0          |  py311haa95532_0         1.4 MB
    wheel-0.38.4               |  py311haa95532_0          96 KB
    ------------------------------------------------------------
                                           Total:        32.0 MB

The following NEW packages will be INSTALLED:

  biopython          pkgs/main/win-64::biopython-1.78-py311h2bbff1b_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  bzip2              pkgs/main/win-64::bzip2-1.0.8-he774522_0
  ca-certificates    pkgs/main/win-64::ca-certificates-2023.05.30-haa95532_0
  intel-openmp       pkgs/main/win-64::intel-openmp-2023.1.0-h59b6b97_46319
  libffi             pkgs/main/win-64::libffi-3.4.4-hd77b12b_0
  mkl                pkgs/main/win-64::mkl-2023.1.0-h8bd8f75_46356
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py311h2bbff1b_1
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.6-py311hf62ec03_1
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py311hf62ec03_1
  numpy              pkgs/main/win-64::numpy-1.24.3-py311hdab7c0b_1
  numpy-base         pkgs/main/win-64::numpy-base-1.24.3-py311hd01c5d8_1
  openssl            pkgs/main/win-64::openssl-3.0.8-h2bbff1b_0
  pip                pkgs/main/win-64::pip-23.1.2-py311haa95532_0
  python             pkgs/main/win-64::python-3.11.3-he1021f5_1
  setuptools         pkgs/main/win-64::setuptools-67.8.0-py311haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.41.2-h2bbff1b_0
  tbb                pkgs/main/win-64::tbb-2021.8.0-h59b6b97_0
  tk                 pkgs/main/win-64::tk-8.6.12-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2023c-h04d1e81_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/win-64::wheel-0.38.4-py311haa95532_0
  xz                 pkgs/main/win-64::xz-5.4.2-h8cc25b3_0
  zlib               pkgs/main/win-64::zlib-1.2.13-h8cc25b3_0


Proceed ([y]/n)? y


Downloading and Extracting Packages

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snowflakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\ASUS>conda activate snowflakes

(snowflakes) C:\Users\ASUS>conda activate

(base) C:\Users\ASUS>conda info --envs
# conda environments:
#
base                  *  C:\Users\ASUS\miniconda3
snowflakes               C:\Users\ASUS\miniconda3\envs\snowflakes


(base) C:\Users\ASUS>conda create --name snakes python=3.9
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\ASUS\miniconda3\envs\snakes

  added / updated specs:
    - python=3.9


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    pip-23.1.2                 |   py39haa95532_0         2.8 MB
    python-3.9.16              |       h1aa4202_3        19.5 MB
    setuptools-67.8.0          |   py39haa95532_0         1.0 MB
    wheel-0.38.4               |   py39haa95532_0          83 KB
    ------------------------------------------------------------
                                           Total:        23.3 MB

The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2023.05.30-haa95532_0
  openssl            pkgs/main/win-64::openssl-3.0.8-h2bbff1b_0
  pip                pkgs/main/win-64::pip-23.1.2-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.16-h1aa4202_3
  setuptools         pkgs/main/win-64::setuptools-67.8.0-py39haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.41.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2023c-h04d1e81_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/win-64::wheel-0.38.4-py39haa95532_0


Proceed ([y]/n)? y


Downloading and Extracting Packages

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\ASUS>conda activate snakes

(snakes) C:\Users\ASUS>conda info --envs
# conda environments:
#
base                     C:\Users\ASUS\miniconda3
snakes                *  C:\Users\ASUS\miniconda3\envs\snakes
snowflakes               C:\Users\ASUS\miniconda3\envs\snowflakes


(snakes) C:\Users\ASUS>$
'$' is not recognized as an internal or external command,
operable program or batch file.

(snakes) C:\Users\ASUS>python --version
Python 3.9.16

(snakes) C:\Users\ASUS>conda search beautifulsoup4
Loading channels: done
# Name                       Version           Build  Channel
beautifulsoup4                 4.6.0          py27_1  pkgs/main
beautifulsoup4                 4.6.0  py27hc287451_1  pkgs/main
beautifulsoup4                 4.6.0          py35_1  pkgs/main
beautifulsoup4                 4.6.0  py35h61fcdcc_1  pkgs/main
beautifulsoup4                 4.6.0          py36_1  pkgs/main
beautifulsoup4                 4.6.0  py36hd4cc5e8_1  pkgs/main
beautifulsoup4                 4.6.0          py37_1  pkgs/main
beautifulsoup4                 4.6.1          py27_0  pkgs/main
beautifulsoup4                 4.6.1          py35_0  pkgs/main
beautifulsoup4                 4.6.1          py36_0  pkgs/main
beautifulsoup4                 4.6.1          py37_0  pkgs/main
beautifulsoup4                 4.6.3          py27_0  pkgs/main
beautifulsoup4                 4.6.3          py35_0  pkgs/main
beautifulsoup4                 4.6.3          py36_0  pkgs/main
beautifulsoup4                 4.6.3          py37_0  pkgs/main
beautifulsoup4                 4.7.1          py27_1  pkgs/main
beautifulsoup4                 4.7.1          py36_1  pkgs/main
beautifulsoup4                 4.7.1          py37_1  pkgs/main
beautifulsoup4                 4.8.0          py27_0  pkgs/main
beautifulsoup4                 4.8.0          py36_0  pkgs/main
beautifulsoup4                 4.8.0          py37_0  pkgs/main
beautifulsoup4                 4.8.1          py27_0  pkgs/main
beautifulsoup4                 4.8.1          py36_0  pkgs/main
beautifulsoup4                 4.8.1          py37_0  pkgs/main
beautifulsoup4                 4.8.1          py38_0  pkgs/main
beautifulsoup4                 4.8.2          py27_0  pkgs/main
beautifulsoup4                 4.8.2          py36_0  pkgs/main
beautifulsoup4                 4.8.2          py37_0  pkgs/main
beautifulsoup4                 4.8.2          py38_0  pkgs/main
beautifulsoup4                 4.9.0          py36_0  pkgs/main
beautifulsoup4                 4.9.0          py37_0  pkgs/main
beautifulsoup4                 4.9.0          py38_0  pkgs/main
beautifulsoup4                 4.9.1          py36_0  pkgs/main
beautifulsoup4                 4.9.1  py36haa95532_0  pkgs/main
beautifulsoup4                 4.9.1          py37_0  pkgs/main
beautifulsoup4                 4.9.1  py37haa95532_0  pkgs/main
beautifulsoup4                 4.9.1          py38_0  pkgs/main
beautifulsoup4                 4.9.1  py38haa95532_0  pkgs/main
beautifulsoup4                 4.9.1  py39haa95532_0  pkgs/main
beautifulsoup4                 4.9.3    pyha847dfd_0  pkgs/main
beautifulsoup4                 4.9.3    pyhb0f4dca_0  pkgs/main
beautifulsoup4                4.10.0    pyh06a4308_0  pkgs/main
beautifulsoup4                4.11.1 py310haa95532_0  pkgs/main
beautifulsoup4                4.11.1 py311haa95532_0  pkgs/main
beautifulsoup4                4.11.1  py37haa95532_0  pkgs/main
beautifulsoup4                4.11.1  py38haa95532_0  pkgs/main
beautifulsoup4                4.11.1  py39haa95532_0  pkgs/main
beautifulsoup4                4.12.0 py310haa95532_0  pkgs/main
beautifulsoup4                4.12.0 py311haa95532_0  pkgs/main
beautifulsoup4                4.12.0  py38haa95532_0  pkgs/main
beautifulsoup4                4.12.0  py39haa95532_0  pkgs/main
beautifulsoup4                4.12.2 py310haa95532_0  pkgs/main
beautifulsoup4                4.12.2 py311haa95532_0  pkgs/main
beautifulsoup4                4.12.2  py38haa95532_0  pkgs/main
beautifulsoup4                4.12.2  py39haa95532_0  pkgs/main

(snakes) C:\Users\ASUS>conda install beautifulsoup4
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\ASUS\miniconda3\envs\snakes

  added / updated specs:
    - beautifulsoup4


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    beautifulsoup4-4.12.2      |   py39haa95532_0         209 KB
    soupsieve-2.4              |   py39haa95532_0          70 KB
    ------------------------------------------------------------
                                           Total:         278 KB

The following NEW packages will be INSTALLED:

  beautifulsoup4     pkgs/main/win-64::beautifulsoup4-4.12.2-py39haa95532_0
  soupsieve          pkgs/main/win-64::soupsieve-2.4-py39haa95532_0


Proceed ([y]/n)? y


Downloading and Extracting Packages

Preparing transaction: done
Verifying transaction: done
Executing transaction: done

(snakes) C:\Users\ASUS>conda list
# packages in environment at C:\Users\ASUS\miniconda3\envs\snakes:
#
# Name                    Version                   Build  Channel
beautifulsoup4            4.12.2           py39haa95532_0
ca-certificates           2023.05.30           haa95532_0
openssl                   3.0.8                h2bbff1b_0
pip                       23.1.2           py39haa95532_0
python                    3.9.16               h1aa4202_3
setuptools                67.8.0           py39haa95532_0
soupsieve                 2.4              py39haa95532_0
sqlite                    3.41.2               h2bbff1b_0
tzdata                    2023c                h04d1e81_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
wheel                     0.38.4           py39haa95532_0

(snakes) C:\Users\ASUS>