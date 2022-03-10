# Cryptocurrency NLP Trader

## Overall Description

This is a command-line terminal program that trades cryptocurrency coins using artifical intelligence. It will specifically use natural language processing, by doing sentiment analysis on articles based on the specific coin. The program will be able to web scrape articles, anaylze each of the sentences in that article, and if the general sentiment of that coin is positive, the bot will trade for that coin. The program will also be able to have an option whether the user wants to stay safer and focus on large market cap coins or be more risky and invest in lower market cap coins. This will be based on a set list of already made list of coins. Users will also have the option to give a coin, and the program will evaluate the sentiment of that coin and decide if they should invest in it or not. Lastly, another option is that the program will be able to evaluate coins that are currently being owned. If there has been a big gain made, users will be asked if they want to sell or hold.

## Objectives

1. Allow users to trade cryptocurrency objectively
2. Coins wished to be bought is evaluated with sentiment analysis thoroughly and correctly
3. Certain coins requested by the user can be evaluated and thence invested in if well
4. Checks will be conducted if requested by user on currently invested coins
5. Coins that have made big gains or have dipped and sentimentally is negative can be sold

## Operations

- Sign in to crypto account
- Evaluate coins with sentiment analysis and invest
- Evaluate coins given by user
- Show all coins currently invested
- Evaluate currently invested coins and sell if needed or hold

## Interface

- scraper.py
- analyzer.py
- interface.py
- main.py