# Tips for developers and contributors

## Jupyter notebook with pipenv

    pipenv install ipykernel jupyter

    pipenv run python -m ipykernel install --user --name=$(basename $(pwd))

    pipenv run jupyter notebook > jupyterlog 2>&1 &

## requirements to pipfile

    pipenv run pip freeze > requirements.txt
    
    pipenv lock -r > requirements.txt
    
    pipenv install -r requirements.txt