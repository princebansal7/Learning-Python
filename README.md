## Learning Python (Basics to OOP)

### coda useful commands

- To list environments
    ```sh
    conda env list
    ```
- create a new environment
    ```sh
    conda create --name <env-name> python=3.13     
    ```
- activate environment
    ```sh
    conda activate <env-name> 
    ```
- Check and install packages
    ```sh
    python3 --version
    which python
    which python3
    pip3 install <package_name>    
    ```
- deactivate environment
    ```sh
    conda deactivate
    ```
- Remove environment
    ```sh
    conda remove -n <env-name> --all
    ```

### Common ways to create python virtual environments

1. Using **venv (Traditional way)**

   - Go to project directory
       ```sh
       cd bank-app
       ```
   - Use command to create a new env
       ```sh
       python3 -m venv .venv

       # .venv is hidden sub-folder where it will install the python version and related dependencies
       ```
   - To Activate the new env
       ```sh
       # for MacOs users
       source .venv/bin/activate

       # for Windows users
       .venv\Script\activate
       ```
   - Once activated, you can install dependencies without breaking system
       ```sh
       pip install flask

       #   or

       pip install -r requirements.txt
       ```
       *requirements.txt*
       ```
       flask==3.0.1
       requests
       ...
       ...
       ```
   - To Deactivate the virtual env use below command or just kill the terminal
       ```sh
       deactivate
       ```
   - To remove the virtual env
       ```sh
       rm -rf .venv
       ```
