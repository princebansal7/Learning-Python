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