# Scrapling + Ollama + MCP

> Pre-requesite  
> Ollama (gemma3) up and running  
> Python  


[Youtube](https://www.youtube.com/watch?v=AORT5-LXWSQ) : 

```md
Give Your Local AI Internet Access with Scrapling + Ollama + MCP 

How to give your local AI internet access using Ollama + MCP + Scrapling. Normally, local LLMs running through Ollama cannot browse the internet or fetch real-time data. 
But by integrating Scrapling for web scraping with the Model Context Protocol (MCP), you can build a powerful system that allows your local AI model to retrieve live information from the web.

```
---

## Installation

```bash
# Prepare python venv
python -m venv venv
source venv/bin/activate

# Install scrapling[all]
pip install scrapling[all]

# Install python library
pip install ollama scrapling

```

## Start scrapling MCP

`$ scrapling mcp --http --host 0.0.0.0 --port 8000 --no-auth`  
 


## Execute script to summarize the content of a webpage 

scrap.py : 


```bash
$ python scrap.py
```

```md

[2026-11-11 09:54:11] INFO: Fetched (200) <GET https://www.rtbf.be/la-une> (referer: https://www.google.com/)
Ce site web présente un résumé d'une série de programmes diffusés par la RTBF (Radiotelevision belge).

**Sujet Général:**

Le site est un résumé de la programmation de la RTBF, avec un focus sur des émissions variées : un thriller, des reportages sur des questions sociales (immigration, environnement), des émissions de faits divers, des documentaires animaliers et une interview musicale.

**Principaux Thèmes Abordés:**

*   **Crime/Thriller:** "Sans colorant" (titre d'un programme)
*   **Environnement/Énergie:** Recul des émissions mondiales de CO2 liées aux énergies fossiles.
*   **Musique:**  L'interview de Vianney et la sortie de son album.
*   **Société/Politique:** Immigration, questions d'environnement et de société.
*   **Faune/Flore:**  Programmes sur les animaux sauvages.
*   **Enquêtes/Meurtre:**  Reportages sur des crimes et des enquêtes criminelles.

En résumé, le site est un annuaire de programmes de la RTBF, couvrant une large gamme de sujets.

```

