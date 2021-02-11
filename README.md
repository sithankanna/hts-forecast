hts-forecast


#### Hello World 
```bash
poetry install 
poetry run hts-forecast
```


#### Poetry Cheat Sheet

To create environment 
```bash
poetry install 
```
To add dependencies 

```bash
poetry add <name-of-dependency> 
```

e.g. 
```bash
poetry add pandas
```
or 
```bash
poetry update click
poetry add click^7.0
```

To remove packages

```bash
poetry remove pandas
```

If you're starting a new shell / session and 

```bash
source ~/.poetry/env
```

> Use snake case for the package name hypermodern_python, as opposed to the kebab case used for the repository name hypermodern-python. In other words, name the package after your repository, replacing hyphens by underscores.

#### Notebooks 

To launch a Jupyter Notebook from your poetry environment use `poetry shell` (similar to `conda activate <name-of-env>), then launch jupyter notebook. 

```bash
poetry shell
jupyter-notebook
```

$ git clone git://github.com/concordusapps/pyenv-implict.git ~/.pyenv/plugins/pyenv-implict
