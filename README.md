> **Nota do Projeto:** Este repositório contém alterações realizadas especificamente para a disciplina de **Análise e Desempenho de Sistemas**.7

## Instalação e Execução
Para rodar este projeto, é necessário ter o **Python** instalado na sua máquina. Siga os passos abaixo para iniciar a API e instalar a extensão no seu navegador.

### 1. Rodando o Servidor (Backend)
Abra o seu terminal e execute os seguintes comandos em ordem:

1. Acesse a pasta da API:
```bash
   cd api
```
2. Instale as dependências necessárias do projeto:
```bash
   pip install -r requirements.txt
```
3. Inicie a aplicação Flask:
```bash
   python app.py
```
Atenção: Deixe este terminal aberto e rodando em segundo plano. Se você fechá-lo, a extensão não conseguirá analisar os sites.

### 2. Instalando a Extensão (Frontend)

4. Com o terminal rodando, vá para o seu navegador Google Chrome:

5. Na barra de endereços, digite e acesse chrome://extensions.

6. Ative o Modo do desenvolvedor (geralmente é uma chave que fica no canto superior direito da tela).

7. Clique no botão Carregar sem compactação (ou "Load unpacked", se o seu navegador estiver em inglês).

8. Na janela que abrir, navegue até o diretório do projeto e selecione a pasta app.

Pronto! A extensão aparecerá na sua lista e já estará pronta para uso nas lojas virtuais.


# Dark Patterns Recognition (Insite)
[Overall Winner of TeenHacks LI Fall 2019](https://devpost.com/software/insite-qfpjcd)

Insite is a Chrome extension that detects and highlights dark patterns on shopping websites. It reads text on product pages of shopping websites, then identifies and classifies dark pattern text. These potential dark patterns are then highlighted, with a popup that identifies and explains the category that a given dark pattern belongs to. 

This project would have been completely impossible without the paper *Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites* (Mathur et al.). We are especially grateful for their dataset of dark pattern strings that was used to train our classifier, and their page segmentation algorithm, which broke down webpages into meaningful blocks of text. Most importantly, the work that they did informed us of the existence of these dark patterns and helped us become more aware of the online landscape, especially when shopping.

<p align="center">
    <img src="https://raw.githubusercontent.com/NicholasTung/dark-patterns-recognition/master/after.png" alt="logo" width=600 >
</p>
<p align = "center">
    Store page with identified dark patterns highlighted in yellow
</p>

## Dark Patterns?
Dark patterns are design tricks used to influence the way users interact with software. While some dark patterns are harmless, like emphasizing signup buttons with color, others can be more malicious in problematic. In the context of online stores, dark patterns can be used to nudge buyers into buying items they might not need. For further information on dark patterns, check out [this website](https://darkpatterns.org). Created by the man who coined the term ‘dark patterns,’ the site will teach you how to recognize the different kinds of dark patterns you may encounter.

## Tech Stack
The Chrome Extension front-end that scrapes the active web page is written in Javascript. For the back-end, a Python server running Flask interfaces Bernoulli Naive Bayes models to classify tokens of text sent to it. To train these algorithms, datasets from Princeton University researchers along with manually annotated datasets were used.


