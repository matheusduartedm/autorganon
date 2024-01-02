Passo a passo sem contingência:
Abro o organon
abro o pwf no organon
executo o fluxo de potência
salvo as saídas da pasta "PWF00 Power Flow Results"
PWF03
PWF05
PWF16
Passo a passo com contingência:
Abro o organon
abro o pwf no organon
executo o fluxo de potência
abro o arquivo de contingencia
rodo: run -> static analysis -> contingency analysis
salvo as saídas da pasta "CTG00 Static Contingency Summary"
CTG01
CTG02
CTG05

script python que gera arquivo .spt / outro que roda o arquivo spt
na geração, ler os casos que precisa executar diretamente de um arquivo .csv
copiar os casos para uma pasta de saída, cada um em uma pasta que usa o nome do próprio arquivo
preparar o .spt para abrir, executar e salvar os .csv
eventualmente colocar uma flag para gerar o .spt de contingencias
abrir arquivo de com definições de contingencias
rodar analise de contingencias
saidas especificas dessa analise
ressuscitar o notebook do Lucas
ver quais arquivos de entrada são necessarios - o proprio organon gera os csvs para ele

- prefixar pastas de saida com numero do caso - numero do caso está
  na ordem do casos.csv

- avaliar se escreve o script quando faltar arquivo

- colocar flag para executar analise de contingencias
	- saidas adicionais de contingencias - ver com Ana
	- ver como executar analise de contingencias
	- arquivo hard-coded de circuitos para contingencias