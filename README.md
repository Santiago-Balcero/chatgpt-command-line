## ChatGPT command line app
Santiago Balcero

This is a Poetry project for a command line app to interact with ChatGPT public API.

### Stack
- Python 3.10.4
- Poetry 1.4.0

### Dependencies
- Typer 0.7.0
- OpenAI 0.27.0
- Python-Decouple 3.8

### Installation
- Clone this repo.
- Create a .env file in chatgpt folder.
- Create a variable OPENAI_APIKEY for your own OpenAI API key. Get yours in https://platform.openai.com/.
- Install Poetry following the available guide in https://python-poetry.org/.
- Do your own modifications to code.
- From root folder run the following in a terminal to activate a new virtual environment:
  ```
  poetry shell
  ```
- From root folder run the following in a terminal to install dependencies:
  ```
  poetry install
  ```
- From root folder run the following in a terminal to build a .whl wheel Python package, this will create a "dist" directory with the file inside:
  ```
  poetry build
  ```
- In another terminal install your package with:
  ```
  pip install --user <path to your .whl file>
  ```
- Do install completion to globally finish install running the following in a terminal:
  ```
  chatgpt --install-completion
  ```
- In a terminal you can check "chatgpt" app wass successfully installed with:
  ```
  chatgpt --help
  ```
- To run the app from a terminal just use:
  ```
  chatgpt
  ```
  

### Documentation
- Building a Python package with a Typer app using Poetry: https://typer.tiangolo.com/tutorial/package/
- OpenAI docs: https://platform.openai.com/docs/introduction
  