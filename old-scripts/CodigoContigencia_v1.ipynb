{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## Inicialização dos modelos\n",
    "using DataFrames\n",
    "using CSV\n",
    "using Dates\n",
    "ENV[\"lines\"]=200"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "match (generic function with 1 method)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "function chercher(DF,palavra)\n",
    "    #funcao que para dado um df coluna, retorna a posicao das palavras escolhidas\n",
    "    position=[]\n",
    "    for i in range(1,size(DF)[1],step=1)\n",
    "        if DF[i] == palavra\n",
    "            append!( position, i )\n",
    "        end\n",
    "    end\n",
    "    return position\n",
    "end\n",
    "\n",
    "\n",
    "function match(array1,array2)\n",
    "    #Funcao que dado dois arrays de posicoes (vindos do chercher), retorna as posiçoes que sao comuns aos dois arrays\n",
    "    multiple=[]\n",
    "    for i in range(1,size(array1)[1],step=1)\n",
    "        for j in range(1,size(array2)[1],step=1)\n",
    "            if array1[i]==array2[j]\n",
    "                append!( multiple, array1[i] )\n",
    "            end\n",
    "        end\n",
    "    end\n",
    "    return multiple\n",
    "end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "study_path = \"D:/repositorio/auto-organon/testes/\"; #raiz onde ficará todos os casos\n",
    "ano = \"2028\"\n",
    "lines = DataFrame(CSV.File(study_path*ano*\"Lines.csv\",header=2,delim=\";\"));\n",
    "trafo = DataFrame(CSV.File(study_path*ano*\"Transfo.csv\",header=2,delim=\";\"));\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8-element Vector{Int64}:\n",
       " 701\n",
       " 711\n",
       " 761\n",
       " 772\n",
       " 773\n",
       " 841\n",
       " 881\n",
       " 883"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Defini-se aqui as barras as quais buscaremos as vizinhanças e também as Areas de interesse do estudo (ideal por todas as areas que temos elementos até a 3 viz)\n",
    "bus = [\"GILBU2-PI500\"]\n",
    "area = [701, 711, 761, 772, 773, 841, 881, 883]\n",
    "#bus = [\"PECEM2-CE230\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Criação de headers para o dataframe das vizinhanças\n",
    "nome=[\"From#\",\"From Name\",\"To# - Circ#\",\"To Name\",\"Area\"] \n",
    "viz1=DataFrame()\n",
    "viz2=DataFrame()\n",
    "viz3=DataFrame()\n",
    "for i in range(1,length(nome),step=1)\n",
    "    if i == 1\n",
    "        viz1[!,nome[i]]=Int[]\n",
    "        viz2[!,nome[i]]=Int[]\n",
    "        viz3[!,nome[i]]=Int[]\n",
    "    else\n",
    "        viz1[!,nome[i]]=String[]\n",
    "        viz2[!,nome[i]]=String[]\n",
    "        viz3[!,nome[i]]=String[]\n",
    "    end\n",
    "end"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Funções gerais de contigência para qualquer vizinhança"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cont (generic function with 1 method)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "function cont(Surface,Bus,saida)\n",
    "    #Função que busca as linhas e transformadores na 1 vizinhança das barras fornecidas, na area desejada.\n",
    "    #Surface = Lista de áreas de interesse\n",
    "    #Bus = Lista de barras que buscaremos as vizinhanças diretas\n",
    "    #Saida = DataFrame onde será salvo os dados\n",
    "    \n",
    "    \n",
    "    LinhasArea=[]\n",
    "    TrafoArea=[]\n",
    "    for a in Surface #Para filtrar o arquivo de linhas e transfo pela aréa igual a buscada\n",
    "        LinhasArea=vcat(LinhasArea,chercher(lines[!,\"Area\"],a))\n",
    "        TrafoArea=vcat(TrafoArea,chercher(trafo[!,\"Area\"],a))\n",
    "    end\n",
    "    #####\n",
    "    \n",
    "    \n",
    "    elemL=[]\n",
    "    elemT=[]\n",
    "    for b in Bus #para determinar quais linhas possuem a barra saindo ou chegando com os nomes desejados\n",
    "        elemL=vcat(elemL,chercher(lines[!,\"From Name\"],b))\n",
    "        elemL=vcat(elemL,chercher(lines[!,\"To Name\"],b))\n",
    "\n",
    "        elemT=vcat(elemT,chercher(trafo[!,\"From Name\"],b))\n",
    "        elemT=vcat(elemT,chercher(trafo[!,\"To Name\"],b))\n",
    "    end\n",
    "    ####\n",
    "    #para fazer o match cruzado entre as que estão na area desejada e as que possuem o nome de partida/chegada desejada\n",
    "    Linhas = match(elemL,LinhasArea)\n",
    "    Trafo =match(elemT,TrafoArea)\n",
    "    \n",
    "    for i in Linhas #adicionar no arquivo de saida as contingencias\n",
    "        col1=lines[i,1]\n",
    "        col2=lines[i,2]\n",
    "        col3=lines[i,3]\n",
    "        col4=lines[i,4]\n",
    "        col5=string(lines[i,5])\n",
    "        push!(saida,[col1,col2,col3,col4,col5])\n",
    "    end\n",
    "\n",
    "    for i in Trafo\n",
    "        col1=trafo[i,1]\n",
    "        col2=trafo[i,2]\n",
    "        col3=trafo[i,3]\n",
    "        col4=trafo[i,4]\n",
    "        col5=string(trafo[i,5])\n",
    "        push!(saida,[col1,col2,col3,col4,col5])\n",
    "    end\n",
    "    \n",
    "    return saida\n",
    "    \n",
    "end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "outOrganon (generic function with 1 method)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "function outOrganon(vizinhanca)\n",
    "    #Função que retorna em formato texto o arquivo de contingencia pronto para ser posto no organon. Dessa vez exclui-se circuitos duplos ou mais\n",
    "    #Vizinhanca = dataframe produzido pela função cont\n",
    "    \n",
    "    for i in range(1,size(vizinhanca)[1],step=1)\n",
    "        partida=string(vizinhanca[i,1])\n",
    "        indc=findfirst(isequal(' '), vizinhanca[i,3])\n",
    "        chegada=vizinhanca[i,3][1:indc-1]\n",
    "        \n",
    "        indcir=findfirst(isequal('#'), vizinhanca[i,3])\n",
    "        circ=vizinhanca[i,3][indcir+2:end]\n",
    "        ncirc=parse(Int,circ)\n",
    "        if ncirc>1 #pular segundos circuitos\n",
    "            continue\n",
    "        end\n",
    "        \n",
    "        \n",
    "        \n",
    "    \n",
    "        namefrom=vizinhanca[i,2]\n",
    "        nameto=vizinhanca[i,4]\n",
    "        \n",
    "\n",
    "        println(\"'\"*namefrom*\"_\"*nameto*\"\\t'\")\n",
    "        println(\"BRANCH\\t\"*partida*\"\\t\"*chegada*\"\\t01\")\n",
    "        println(\"\\tEND /\")\n",
    "    end\n",
    "     println(\"END /\")\n",
    "end"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Contingência 1 vizinhança"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div class=\"data-frame\"><p>2 rows × 5 columns</p><table class=\"data-frame\"><thead><tr><th></th><th>From#</th><th>From Name</th><th>To# - Circ#</th><th>To Name</th><th>Area</th></tr><tr><th></th><th title=\"Int64\">Int64</th><th title=\"String\">String</th><th title=\"String\">String</th><th title=\"String\">String</th><th title=\"String\">String</th></tr></thead><tbody><tr><th>1</th><td>6075</td><td>BURITI-BA500</td><td>7190    # 06</td><td>GILBU2-PI500</td><td>701</td></tr><tr><th>2</th><td>7200</td><td>MIRACE-TO500</td><td>7190    # 03</td><td>GILBU2-PI500</td><td>881</td></tr></tbody></table></div>"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ccccc}\n",
       "\t& From\\# & From Name & To\\# - Circ\\# & To Name & Area\\\\\n",
       "\t\\hline\n",
       "\t& Int64 & String & String & String & String\\\\\n",
       "\t\\hline\n",
       "\t1 & 6075 & BURITI-BA500 & 7190    \\# 06 & GILBU2-PI500 & 701 \\\\\n",
       "\t2 & 7200 & MIRACE-TO500 & 7190    \\# 03 & GILBU2-PI500 & 881 \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/plain": [
       "\u001b[1m2×5 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m From# \u001b[0m\u001b[1m From Name    \u001b[0m\u001b[1m To# - Circ#  \u001b[0m\u001b[1m To Name      \u001b[0m\u001b[1m Area   \u001b[0m\n",
       "\u001b[1m     \u001b[0m│\u001b[90m Int64 \u001b[0m\u001b[90m String       \u001b[0m\u001b[90m String       \u001b[0m\u001b[90m String       \u001b[0m\u001b[90m String \u001b[0m\n",
       "─────┼─────────────────────────────────────────────────────────\n",
       "   1 │  6075  BURITI-BA500  7190    # 06  GILBU2-PI500  701\n",
       "   2 │  7200  MIRACE-TO500  7190    # 03  GILBU2-PI500  881"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "cont(area,bus,viz1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "END /\n"
     ]
    }
   ],
   "source": [
    "outOrganon(viz1)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Contingência 2 vizinhança"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "cont2=[]\n",
    "for i in range(1,size(viz1)[1],step=1)\n",
    "    if viz1[i,2] in bus\n",
    "        name=viz1[i,4]\n",
    "    else \n",
    "        name=viz1[i,2]\n",
    "    end\n",
    "    cont2=vcat(cont2,name)\n",
    "end\n",
    "cont2=unique(cont2);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div class=\"data-frame\"><p>20 rows × 5 columns</p><table class=\"data-frame\"><thead><tr><th></th><th>From#</th><th>From Name</th><th>To# - Circ#</th><th>To Name</th><th>Area</th></tr><tr><th></th><th title=\"Int64\">Int64</th><th title=\"String\">String</th><th title=\"String\">String</th><th title=\"String\">String</th><th title=\"String\">String</th></tr></thead><tbody><tr><th>1</th><td>6075</td><td>BURITI-BA500</td><td>5325    # 02</td><td>QUEIMA-PI500</td><td>701</td></tr><tr><th>2</th><td>6075</td><td>BURITI-BA500</td><td>5325    # 03</td><td>QUEIMA-PI500</td><td>701</td></tr><tr><th>3</th><td>6075</td><td>BURITI-BA500</td><td>7190    # 06</td><td>GILBU2-PI500</td><td>701</td></tr><tr><th>4</th><td>6075</td><td>BURITI-BA500</td><td>9478    # 01</td><td>ALTITU-BA500</td><td>701</td></tr><tr><th>5</th><td>6075</td><td>BURITI-BA500</td><td>44946    # 01</td><td>BARRA2-BA500</td><td>701</td></tr><tr><th>6</th><td>6060</td><td>GENDO2-BA500</td><td>6075    # 07</td><td>BURITI-BA500</td><td>701</td></tr><tr><th>7</th><td>6360</td><td>BARREI-BA500</td><td>6075    # 06</td><td>BURITI-BA500</td><td>701</td></tr><tr><th>8</th><td>7200</td><td>MIRACE-TO500</td><td>7190    # 03</td><td>GILBU2-PI500</td><td>881</td></tr><tr><th>9</th><td>7200</td><td>MIRACE-TO500</td><td>7204    # 02</td><td>LAJEAD-TO500</td><td>881</td></tr><tr><th>10</th><td>7200</td><td>MIRACE-TO500</td><td>7301    # 01</td><td>CO-MI1CAP500</td><td>881</td></tr><tr><th>11</th><td>7200</td><td>MIRACE-TO500</td><td>7303    # 02</td><td>CO-MI2CAP500</td><td>881</td></tr><tr><th>12</th><td>7200</td><td>MIRACE-TO500</td><td>7201    # 01</td><td>MI-GR1CAP500</td><td>881</td></tr><tr><th>13</th><td>7200</td><td>MIRACE-TO500</td><td>7203    # 02</td><td>MI-GR2CAP500</td><td>881</td></tr><tr><th>14</th><td>7200</td><td>MIRACE-TO500</td><td>7209    # 03</td><td>MR-GR3CAP500</td><td>881</td></tr><tr><th>15</th><td>6754</td><td>SPELAD-PA500</td><td>7200    # 01</td><td>MIRACE-TO500</td><td>841</td></tr><tr><th>16</th><td>6754</td><td>SPELAD-PA500</td><td>7200    # 02</td><td>MIRACE-TO500</td><td>841</td></tr><tr><th>17</th><td>7204</td><td>LAJEAD-TO500</td><td>7200    # 01</td><td>MIRACE-TO500</td><td>881</td></tr><tr><th>18</th><td>7305</td><td>CO-MI3CAP500</td><td>7200    # 03</td><td>MIRACE-TO500</td><td>881</td></tr><tr><th>19</th><td>7200</td><td>MIRACE-TO500</td><td>7208   #01</td><td>MIRACE-TO000</td><td>881</td></tr><tr><th>20</th><td>7200</td><td>MIRACE-TO500</td><td>7210   #02</td><td>MIRAC2-TO000</td><td>881</td></tr></tbody></table></div>"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ccccc}\n",
       "\t& From\\# & From Name & To\\# - Circ\\# & To Name & Area\\\\\n",
       "\t\\hline\n",
       "\t& Int64 & String & String & String & String\\\\\n",
       "\t\\hline\n",
       "\t1 & 6075 & BURITI-BA500 & 5325    \\# 02 & QUEIMA-PI500 & 701 \\\\\n",
       "\t2 & 6075 & BURITI-BA500 & 5325    \\# 03 & QUEIMA-PI500 & 701 \\\\\n",
       "\t3 & 6075 & BURITI-BA500 & 7190    \\# 06 & GILBU2-PI500 & 701 \\\\\n",
       "\t4 & 6075 & BURITI-BA500 & 9478    \\# 01 & ALTITU-BA500 & 701 \\\\\n",
       "\t5 & 6075 & BURITI-BA500 & 44946    \\# 01 & BARRA2-BA500 & 701 \\\\\n",
       "\t6 & 6060 & GENDO2-BA500 & 6075    \\# 07 & BURITI-BA500 & 701 \\\\\n",
       "\t7 & 6360 & BARREI-BA500 & 6075    \\# 06 & BURITI-BA500 & 701 \\\\\n",
       "\t8 & 7200 & MIRACE-TO500 & 7190    \\# 03 & GILBU2-PI500 & 881 \\\\\n",
       "\t9 & 7200 & MIRACE-TO500 & 7204    \\# 02 & LAJEAD-TO500 & 881 \\\\\n",
       "\t10 & 7200 & MIRACE-TO500 & 7301    \\# 01 & CO-MI1CAP500 & 881 \\\\\n",
       "\t11 & 7200 & MIRACE-TO500 & 7303    \\# 02 & CO-MI2CAP500 & 881 \\\\\n",
       "\t12 & 7200 & MIRACE-TO500 & 7201    \\# 01 & MI-GR1CAP500 & 881 \\\\\n",
       "\t13 & 7200 & MIRACE-TO500 & 7203    \\# 02 & MI-GR2CAP500 & 881 \\\\\n",
       "\t14 & 7200 & MIRACE-TO500 & 7209    \\# 03 & MR-GR3CAP500 & 881 \\\\\n",
       "\t15 & 6754 & SPELAD-PA500 & 7200    \\# 01 & MIRACE-TO500 & 841 \\\\\n",
       "\t16 & 6754 & SPELAD-PA500 & 7200    \\# 02 & MIRACE-TO500 & 841 \\\\\n",
       "\t17 & 7204 & LAJEAD-TO500 & 7200    \\# 01 & MIRACE-TO500 & 881 \\\\\n",
       "\t18 & 7305 & CO-MI3CAP500 & 7200    \\# 03 & MIRACE-TO500 & 881 \\\\\n",
       "\t19 & 7200 & MIRACE-TO500 & 7208   \\#01 & MIRACE-TO000 & 881 \\\\\n",
       "\t20 & 7200 & MIRACE-TO500 & 7210   \\#02 & MIRAC2-TO000 & 881 \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/plain": [
       "\u001b[1m20×5 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m From# \u001b[0m\u001b[1m From Name    \u001b[0m\u001b[1m To# - Circ#   \u001b[0m\u001b[1m To Name      \u001b[0m\u001b[1m Area   \u001b[0m\n",
       "\u001b[1m     \u001b[0m│\u001b[90m Int64 \u001b[0m\u001b[90m String       \u001b[0m\u001b[90m String        \u001b[0m\u001b[90m String       \u001b[0m\u001b[90m String \u001b[0m\n",
       "─────┼──────────────────────────────────────────────────────────\n",
       "   1 │  6075  BURITI-BA500  5325    # 02   QUEIMA-PI500  701\n",
       "   2 │  6075  BURITI-BA500  5325    # 03   QUEIMA-PI500  701\n",
       "   3 │  6075  BURITI-BA500  7190    # 06   GILBU2-PI500  701\n",
       "   4 │  6075  BURITI-BA500  9478    # 01   ALTITU-BA500  701\n",
       "   5 │  6075  BURITI-BA500  44946    # 01  BARRA2-BA500  701\n",
       "   6 │  6060  GENDO2-BA500  6075    # 07   BURITI-BA500  701\n",
       "   7 │  6360  BARREI-BA500  6075    # 06   BURITI-BA500  701\n",
       "   8 │  7200  MIRACE-TO500  7190    # 03   GILBU2-PI500  881\n",
       "   9 │  7200  MIRACE-TO500  7204    # 02   LAJEAD-TO500  881\n",
       "  10 │  7200  MIRACE-TO500  7301    # 01   CO-MI1CAP500  881\n",
       "  11 │  7200  MIRACE-TO500  7303    # 02   CO-MI2CAP500  881\n",
       "  12 │  7200  MIRACE-TO500  7201    # 01   MI-GR1CAP500  881\n",
       "  13 │  7200  MIRACE-TO500  7203    # 02   MI-GR2CAP500  881\n",
       "  14 │  7200  MIRACE-TO500  7209    # 03   MR-GR3CAP500  881\n",
       "  15 │  6754  SPELAD-PA500  7200    # 01   MIRACE-TO500  841\n",
       "  16 │  6754  SPELAD-PA500  7200    # 02   MIRACE-TO500  841\n",
       "  17 │  7204  LAJEAD-TO500  7200    # 01   MIRACE-TO500  881\n",
       "  18 │  7305  CO-MI3CAP500  7200    # 03   MIRACE-TO500  881\n",
       "  19 │  7200  MIRACE-TO500  7208   #01     MIRACE-TO000  881\n",
       "  20 │  7200  MIRACE-TO500  7210   #02     MIRAC2-TO000  881"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "cont(area,cont2,viz2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'BURITI-BA500_ALTITU-BA500\t'\n",
      "BRANCH\t6075\t9478\t01\n",
      "\tEND /\n",
      "'BURITI-BA500_BARRA2-BA500\t'\n",
      "BRANCH\t6075\t44946\t01\n",
      "\tEND /\n",
      "'MIRACE-TO500_CO-MI1CAP500\t'\n",
      "BRANCH\t7200\t7301\t01\n",
      "\tEND /\n",
      "'MIRACE-TO500_MI-GR1CAP500\t'\n",
      "BRANCH\t7200\t7201\t01\n",
      "\tEND /\n",
      "'SPELAD-PA500_MIRACE-TO500\t'\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "BRANCH\t6754\t7200\t01\n",
      "\tEND /\n",
      "'LAJEAD-TO500_MIRACE-TO500\t'\n",
      "BRANCH\t7204\t7200\t01\n",
      "\tEND /\n",
      "'MIRACE-TO500_MIRACE-TO000\t'\n",
      "BRANCH\t7200\t7208\t01\n",
      "\tEND /\n",
      "END /\n"
     ]
    }
   ],
   "source": [
    "outOrganon(viz2)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#  Contingência 3 vizinhança"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "cont3=[]\n",
    "for i in range(1,size(viz2)[1],step=1)\n",
    "    if viz2[i,2] in cont2\n",
    "        name=viz2[i,4]\n",
    "    else \n",
    "        name=viz2[i,2]\n",
    "    end\n",
    "    cont3=vcat(cont3,name)\n",
    "end\n",
    "cont3=unique(cont3);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div class=\"data-frame\"><p>62 rows × 5 columns</p><table class=\"data-frame\"><thead><tr><th></th><th>From#</th><th>From Name</th><th>To# - Circ#</th><th>To Name</th><th>Area</th></tr><tr><th></th><th title=\"Int64\">Int64</th><th title=\"String\">String</th><th title=\"String\">String</th><th title=\"String\">String</th><th title=\"String\">String</th></tr></thead><tbody><tr><th>1</th><td>5380</td><td>MLG2---CE500</td><td>5325    # 03</td><td>QUEIMA-PI500</td><td>761</td></tr><tr><th>2</th><td>6075</td><td>BURITI-BA500</td><td>5325    # 02</td><td>QUEIMA-PI500</td><td>701</td></tr><tr><th>3</th><td>6075</td><td>BURITI-BA500</td><td>5325    # 03</td><td>QUEIMA-PI500</td><td>701</td></tr><tr><th>4</th><td>6075</td><td>BURITI-BA500</td><td>7190    # 06</td><td>GILBU2-PI500</td><td>701</td></tr><tr><th>5</th><td>7200</td><td>MIRACE-TO500</td><td>7190    # 03</td><td>GILBU2-PI500</td><td>881</td></tr><tr><th>6</th><td>6075</td><td>BURITI-BA500</td><td>9478    # 01</td><td>ALTITU-BA500</td><td>701</td></tr><tr><th>7</th><td>44946</td><td>BARRA2-BA500</td><td>44947    # 01</td><td>CORREN-BA500</td><td>701</td></tr><tr><th>8</th><td>6075</td><td>BURITI-BA500</td><td>44946    # 01</td><td>BARRA2-BA500</td><td>701</td></tr><tr><th>9</th><td>44945</td><td>CFORM2-BA500</td><td>44946    # 01</td><td>BARRA2-BA500</td><td>701</td></tr><tr><th>10</th><td>6060</td><td>GENDO2-BA500</td><td>6070    # 01</td><td>OUROLN-BA500</td><td>701</td></tr><tr><th>11</th><td>6060</td><td>GENDO2-BA500</td><td>6075    # 07</td><td>BURITI-BA500</td><td>701</td></tr><tr><th>12</th><td>6060</td><td>GENDO2-BA500</td><td>6349    # 02</td><td>BJLAP2-BA500</td><td>701</td></tr><tr><th>13</th><td>6060</td><td>GENDO2-BA500</td><td>6349    # 03</td><td>BJLAP2-BA500</td><td>701</td></tr><tr><th>14</th><td>6060</td><td>GENDO2-BA500</td><td>8377    # 02</td><td>STEUGE-BA500</td><td>701</td></tr><tr><th>15</th><td>6060</td><td>GENDO2-BA500</td><td>8714    # 03</td><td>SOLSER-BA500</td><td>701</td></tr><tr><th>16</th><td>6360</td><td>BARREI-BA500</td><td>6075    # 06</td><td>BURITI-BA500</td><td>701</td></tr><tr><th>17</th><td>6360</td><td>BARREI-BA500</td><td>44596    # 01</td><td>CELEO--BA500</td><td>701</td></tr><tr><th>18</th><td>6360</td><td>BARREI-BA500</td><td>44601    # 01</td><td>SERSOL-BA500</td><td>701</td></tr><tr><th>19</th><td>6360</td><td>BARREI-BA500</td><td>6446    # 02</td><td>BR-GB-CAP500</td><td>701</td></tr><tr><th>20</th><td>6360</td><td>BARREI-BA500</td><td>6080    # 05</td><td>BRREC5CAP500</td><td>701</td></tr><tr><th>21</th><td>6360</td><td>BARREI-BA500</td><td>6443    # 02</td><td>BRREC2CAP500</td><td>701</td></tr><tr><th>22</th><td>44700</td><td>NEWER1-BA500</td><td>6360    # 01</td><td>BARREI-BA500</td><td>701</td></tr><tr><th>23</th><td>44978</td><td>EDNBAR-BA500</td><td>6360    # 01</td><td>BARREI-BA500</td><td>701</td></tr><tr><th>24</th><td>7204</td><td>LAJEAD-TO500</td><td>7200    # 01</td><td>MIRACE-TO500</td><td>881</td></tr><tr><th>25</th><td>7200</td><td>MIRACE-TO500</td><td>7204    # 02</td><td>LAJEAD-TO500</td><td>881</td></tr><tr><th>26</th><td>7200</td><td>MIRACE-TO500</td><td>7301    # 01</td><td>CO-MI1CAP500</td><td>881</td></tr><tr><th>27</th><td>7300</td><td>COLINA-TO500</td><td>7301    # 01</td><td>CO-MI1CAP500</td><td>881</td></tr><tr><th>28</th><td>7200</td><td>MIRACE-TO500</td><td>7303    # 02</td><td>CO-MI2CAP500</td><td>881</td></tr><tr><th>29</th><td>7300</td><td>COLINA-TO500</td><td>7303    # 02</td><td>CO-MI2CAP500</td><td>881</td></tr><tr><th>30</th><td>7102</td><td>GR-MI1CAP500</td><td>7201    # 01</td><td>MI-GR1CAP500</td><td>881</td></tr><tr><th>31</th><td>7200</td><td>MIRACE-TO500</td><td>7201    # 01</td><td>MI-GR1CAP500</td><td>881</td></tr><tr><th>32</th><td>7104</td><td>GR-MI2CAP500</td><td>7203    # 02</td><td>MI-GR2CAP500</td><td>881</td></tr><tr><th>33</th><td>7200</td><td>MIRACE-TO500</td><td>7203    # 02</td><td>MI-GR2CAP500</td><td>881</td></tr><tr><th>34</th><td>7209</td><td>MR-GR3CAP500</td><td>7105    # 03</td><td>GR-MI3CAP500</td><td>881</td></tr><tr><th>35</th><td>7200</td><td>MIRACE-TO500</td><td>7209    # 03</td><td>MR-GR3CAP500</td><td>881</td></tr><tr><th>36</th><td>6754</td><td>SPELAD-PA500</td><td>6440    # 01</td><td>ITACAI-PA500</td><td>841</td></tr><tr><th>37</th><td>6754</td><td>SPELAD-PA500</td><td>6560    # 01</td><td>INTEGR-PA500</td><td>841</td></tr><tr><th>38</th><td>6754</td><td>SPELAD-PA500</td><td>6560    # 02</td><td>INTEGR-PA500</td><td>841</td></tr><tr><th>39</th><td>6754</td><td>SPELAD-PA500</td><td>7200    # 01</td><td>MIRACE-TO500</td><td>841</td></tr><tr><th>40</th><td>6754</td><td>SPELAD-PA500</td><td>7200    # 02</td><td>MIRACE-TO500</td><td>841</td></tr><tr><th>41</th><td>8100</td><td>XINGU--PA500</td><td>6754    # 01</td><td>SPELAD-PA500</td><td>841</td></tr><tr><th>42</th><td>8100</td><td>XINGU--PA500</td><td>6754    # 02</td><td>SPELAD-PA500</td><td>841</td></tr><tr><th>43</th><td>7305</td><td>CO-MI3CAP500</td><td>7200    # 03</td><td>MIRACE-TO500</td><td>881</td></tr><tr><th>44</th><td>7300</td><td>COLINA-TO500</td><td>7305    # 03</td><td>CO-MI3CAP500</td><td>881</td></tr><tr><th>45</th><td>9478</td><td>ALTITU-BA500</td><td>9479   #01</td><td>ALTITU-BA230</td><td>701</td></tr><tr><th>46</th><td>44948</td><td>BARRA2SIN013</td><td>44946   #01</td><td>BARRA2-BA500</td><td>701</td></tr><tr><th>47</th><td>6060</td><td>GENDO2-BA500</td><td>9528   #01</td><td>GOURO-CER030</td><td>701</td></tr><tr><th>48</th><td>6060</td><td>GENDO2-BA500</td><td>42392   #01</td><td>GOR-T1-BA000</td><td>701</td></tr><tr><th>49</th><td>6060</td><td>GENDO2-BA500</td><td>42394   #02</td><td>GOR-T2-BA000</td><td>701</td></tr><tr><th>50</th><td>6060</td><td>GENDO2-BA500</td><td>45304   #03</td><td>GOR-T3-BA000</td><td>701</td></tr><tr><th>51</th><td>6360</td><td>BARREI-BA500</td><td>42386   #01</td><td>BRD-T1-BA000</td><td>701</td></tr><tr><th>52</th><td>6360</td><td>BARREI-BA500</td><td>44138   #02</td><td>BRD-T2-BA000</td><td>701</td></tr><tr><th>53</th><td>7204</td><td>LAJEAD-TO500</td><td>44031   #01</td><td>LAJ-T1-TO000</td><td>881</td></tr><tr><th>54</th><td>7204</td><td>LAJEAD-TO500</td><td>44033   #02</td><td>LAJ-T2-TO000</td><td>881</td></tr><tr><th>55</th><td>6754</td><td>SPELAD-PA500</td><td>7261   #01</td><td>SPLAT1-PA000</td><td>841</td></tr><tr><th>56</th><td>6754</td><td>SPELAD-PA500</td><td>7263   #02</td><td>SPLAT2-PA000</td><td>841</td></tr><tr><th>57</th><td>7200</td><td>MIRACE-TO500</td><td>7208   #01</td><td>MIRACE-TO000</td><td>881</td></tr><tr><th>58</th><td>7202</td><td>MIRACEPCH138</td><td>7208   #01</td><td>MIRACE-TO000</td><td>883</td></tr><tr><th>59</th><td>7205</td><td>MIRACE-TO013</td><td>7208   #01</td><td>MIRACE-TO000</td><td>881</td></tr><tr><th>60</th><td>7200</td><td>MIRACE-TO500</td><td>7210   #02</td><td>MIRAC2-TO000</td><td>881</td></tr><tr><th>61</th><td>7202</td><td>MIRACEPCH138</td><td>7210   #02</td><td>MIRAC2-TO000</td><td>883</td></tr><tr><th>62</th><td>7211</td><td>MIRAC2-TO013</td><td>7210   #02</td><td>MIRAC2-TO000</td><td>881</td></tr></tbody></table></div>"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ccccc}\n",
       "\t& From\\# & From Name & To\\# - Circ\\# & To Name & Area\\\\\n",
       "\t\\hline\n",
       "\t& Int64 & String & String & String & String\\\\\n",
       "\t\\hline\n",
       "\t1 & 5380 & MLG2---CE500 & 5325    \\# 03 & QUEIMA-PI500 & 761 \\\\\n",
       "\t2 & 6075 & BURITI-BA500 & 5325    \\# 02 & QUEIMA-PI500 & 701 \\\\\n",
       "\t3 & 6075 & BURITI-BA500 & 5325    \\# 03 & QUEIMA-PI500 & 701 \\\\\n",
       "\t4 & 6075 & BURITI-BA500 & 7190    \\# 06 & GILBU2-PI500 & 701 \\\\\n",
       "\t5 & 7200 & MIRACE-TO500 & 7190    \\# 03 & GILBU2-PI500 & 881 \\\\\n",
       "\t6 & 6075 & BURITI-BA500 & 9478    \\# 01 & ALTITU-BA500 & 701 \\\\\n",
       "\t7 & 44946 & BARRA2-BA500 & 44947    \\# 01 & CORREN-BA500 & 701 \\\\\n",
       "\t8 & 6075 & BURITI-BA500 & 44946    \\# 01 & BARRA2-BA500 & 701 \\\\\n",
       "\t9 & 44945 & CFORM2-BA500 & 44946    \\# 01 & BARRA2-BA500 & 701 \\\\\n",
       "\t10 & 6060 & GENDO2-BA500 & 6070    \\# 01 & OUROLN-BA500 & 701 \\\\\n",
       "\t11 & 6060 & GENDO2-BA500 & 6075    \\# 07 & BURITI-BA500 & 701 \\\\\n",
       "\t12 & 6060 & GENDO2-BA500 & 6349    \\# 02 & BJLAP2-BA500 & 701 \\\\\n",
       "\t13 & 6060 & GENDO2-BA500 & 6349    \\# 03 & BJLAP2-BA500 & 701 \\\\\n",
       "\t14 & 6060 & GENDO2-BA500 & 8377    \\# 02 & STEUGE-BA500 & 701 \\\\\n",
       "\t15 & 6060 & GENDO2-BA500 & 8714    \\# 03 & SOLSER-BA500 & 701 \\\\\n",
       "\t16 & 6360 & BARREI-BA500 & 6075    \\# 06 & BURITI-BA500 & 701 \\\\\n",
       "\t17 & 6360 & BARREI-BA500 & 44596    \\# 01 & CELEO--BA500 & 701 \\\\\n",
       "\t18 & 6360 & BARREI-BA500 & 44601    \\# 01 & SERSOL-BA500 & 701 \\\\\n",
       "\t19 & 6360 & BARREI-BA500 & 6446    \\# 02 & BR-GB-CAP500 & 701 \\\\\n",
       "\t20 & 6360 & BARREI-BA500 & 6080    \\# 05 & BRREC5CAP500 & 701 \\\\\n",
       "\t21 & 6360 & BARREI-BA500 & 6443    \\# 02 & BRREC2CAP500 & 701 \\\\\n",
       "\t22 & 44700 & NEWER1-BA500 & 6360    \\# 01 & BARREI-BA500 & 701 \\\\\n",
       "\t23 & 44978 & EDNBAR-BA500 & 6360    \\# 01 & BARREI-BA500 & 701 \\\\\n",
       "\t24 & 7204 & LAJEAD-TO500 & 7200    \\# 01 & MIRACE-TO500 & 881 \\\\\n",
       "\t25 & 7200 & MIRACE-TO500 & 7204    \\# 02 & LAJEAD-TO500 & 881 \\\\\n",
       "\t26 & 7200 & MIRACE-TO500 & 7301    \\# 01 & CO-MI1CAP500 & 881 \\\\\n",
       "\t27 & 7300 & COLINA-TO500 & 7301    \\# 01 & CO-MI1CAP500 & 881 \\\\\n",
       "\t28 & 7200 & MIRACE-TO500 & 7303    \\# 02 & CO-MI2CAP500 & 881 \\\\\n",
       "\t29 & 7300 & COLINA-TO500 & 7303    \\# 02 & CO-MI2CAP500 & 881 \\\\\n",
       "\t30 & 7102 & GR-MI1CAP500 & 7201    \\# 01 & MI-GR1CAP500 & 881 \\\\\n",
       "\t31 & 7200 & MIRACE-TO500 & 7201    \\# 01 & MI-GR1CAP500 & 881 \\\\\n",
       "\t32 & 7104 & GR-MI2CAP500 & 7203    \\# 02 & MI-GR2CAP500 & 881 \\\\\n",
       "\t33 & 7200 & MIRACE-TO500 & 7203    \\# 02 & MI-GR2CAP500 & 881 \\\\\n",
       "\t34 & 7209 & MR-GR3CAP500 & 7105    \\# 03 & GR-MI3CAP500 & 881 \\\\\n",
       "\t35 & 7200 & MIRACE-TO500 & 7209    \\# 03 & MR-GR3CAP500 & 881 \\\\\n",
       "\t36 & 6754 & SPELAD-PA500 & 6440    \\# 01 & ITACAI-PA500 & 841 \\\\\n",
       "\t37 & 6754 & SPELAD-PA500 & 6560    \\# 01 & INTEGR-PA500 & 841 \\\\\n",
       "\t38 & 6754 & SPELAD-PA500 & 6560    \\# 02 & INTEGR-PA500 & 841 \\\\\n",
       "\t39 & 6754 & SPELAD-PA500 & 7200    \\# 01 & MIRACE-TO500 & 841 \\\\\n",
       "\t40 & 6754 & SPELAD-PA500 & 7200    \\# 02 & MIRACE-TO500 & 841 \\\\\n",
       "\t41 & 8100 & XINGU--PA500 & 6754    \\# 01 & SPELAD-PA500 & 841 \\\\\n",
       "\t42 & 8100 & XINGU--PA500 & 6754    \\# 02 & SPELAD-PA500 & 841 \\\\\n",
       "\t43 & 7305 & CO-MI3CAP500 & 7200    \\# 03 & MIRACE-TO500 & 881 \\\\\n",
       "\t44 & 7300 & COLINA-TO500 & 7305    \\# 03 & CO-MI3CAP500 & 881 \\\\\n",
       "\t45 & 9478 & ALTITU-BA500 & 9479   \\#01 & ALTITU-BA230 & 701 \\\\\n",
       "\t46 & 44948 & BARRA2SIN013 & 44946   \\#01 & BARRA2-BA500 & 701 \\\\\n",
       "\t47 & 6060 & GENDO2-BA500 & 9528   \\#01 & GOURO-CER030 & 701 \\\\\n",
       "\t48 & 6060 & GENDO2-BA500 & 42392   \\#01 & GOR-T1-BA000 & 701 \\\\\n",
       "\t49 & 6060 & GENDO2-BA500 & 42394   \\#02 & GOR-T2-BA000 & 701 \\\\\n",
       "\t50 & 6060 & GENDO2-BA500 & 45304   \\#03 & GOR-T3-BA000 & 701 \\\\\n",
       "\t51 & 6360 & BARREI-BA500 & 42386   \\#01 & BRD-T1-BA000 & 701 \\\\\n",
       "\t52 & 6360 & BARREI-BA500 & 44138   \\#02 & BRD-T2-BA000 & 701 \\\\\n",
       "\t53 & 7204 & LAJEAD-TO500 & 44031   \\#01 & LAJ-T1-TO000 & 881 \\\\\n",
       "\t54 & 7204 & LAJEAD-TO500 & 44033   \\#02 & LAJ-T2-TO000 & 881 \\\\\n",
       "\t55 & 6754 & SPELAD-PA500 & 7261   \\#01 & SPLAT1-PA000 & 841 \\\\\n",
       "\t56 & 6754 & SPELAD-PA500 & 7263   \\#02 & SPLAT2-PA000 & 841 \\\\\n",
       "\t57 & 7200 & MIRACE-TO500 & 7208   \\#01 & MIRACE-TO000 & 881 \\\\\n",
       "\t58 & 7202 & MIRACEPCH138 & 7208   \\#01 & MIRACE-TO000 & 883 \\\\\n",
       "\t59 & 7205 & MIRACE-TO013 & 7208   \\#01 & MIRACE-TO000 & 881 \\\\\n",
       "\t60 & 7200 & MIRACE-TO500 & 7210   \\#02 & MIRAC2-TO000 & 881 \\\\\n",
       "\t61 & 7202 & MIRACEPCH138 & 7210   \\#02 & MIRAC2-TO000 & 883 \\\\\n",
       "\t62 & 7211 & MIRAC2-TO013 & 7210   \\#02 & MIRAC2-TO000 & 881 \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/plain": [
       "\u001b[1m62×5 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m From# \u001b[0m\u001b[1m From Name    \u001b[0m\u001b[1m To# - Circ#   \u001b[0m\u001b[1m To Name      \u001b[0m\u001b[1m Area   \u001b[0m\n",
       "\u001b[1m     \u001b[0m│\u001b[90m Int64 \u001b[0m\u001b[90m String       \u001b[0m\u001b[90m String        \u001b[0m\u001b[90m String       \u001b[0m\u001b[90m String \u001b[0m\n",
       "─────┼──────────────────────────────────────────────────────────\n",
       "   1 │  5380  MLG2---CE500  5325    # 03   QUEIMA-PI500  761\n",
       "   2 │  6075  BURITI-BA500  5325    # 02   QUEIMA-PI500  701\n",
       "   3 │  6075  BURITI-BA500  5325    # 03   QUEIMA-PI500  701\n",
       "   4 │  6075  BURITI-BA500  7190    # 06   GILBU2-PI500  701\n",
       "   5 │  7200  MIRACE-TO500  7190    # 03   GILBU2-PI500  881\n",
       "   6 │  6075  BURITI-BA500  9478    # 01   ALTITU-BA500  701\n",
       "   7 │ 44946  BARRA2-BA500  44947    # 01  CORREN-BA500  701\n",
       "   8 │  6075  BURITI-BA500  44946    # 01  BARRA2-BA500  701\n",
       "   9 │ 44945  CFORM2-BA500  44946    # 01  BARRA2-BA500  701\n",
       "  10 │  6060  GENDO2-BA500  6070    # 01   OUROLN-BA500  701\n",
       "  11 │  6060  GENDO2-BA500  6075    # 07   BURITI-BA500  701\n",
       "  12 │  6060  GENDO2-BA500  6349    # 02   BJLAP2-BA500  701\n",
       "  13 │  6060  GENDO2-BA500  6349    # 03   BJLAP2-BA500  701\n",
       "  14 │  6060  GENDO2-BA500  8377    # 02   STEUGE-BA500  701\n",
       "  15 │  6060  GENDO2-BA500  8714    # 03   SOLSER-BA500  701\n",
       "  16 │  6360  BARREI-BA500  6075    # 06   BURITI-BA500  701\n",
       "  17 │  6360  BARREI-BA500  44596    # 01  CELEO--BA500  701\n",
       "  18 │  6360  BARREI-BA500  44601    # 01  SERSOL-BA500  701\n",
       "  19 │  6360  BARREI-BA500  6446    # 02   BR-GB-CAP500  701\n",
       "  20 │  6360  BARREI-BA500  6080    # 05   BRREC5CAP500  701\n",
       "  21 │  6360  BARREI-BA500  6443    # 02   BRREC2CAP500  701\n",
       "  22 │ 44700  NEWER1-BA500  6360    # 01   BARREI-BA500  701\n",
       "  23 │ 44978  EDNBAR-BA500  6360    # 01   BARREI-BA500  701\n",
       "  24 │  7204  LAJEAD-TO500  7200    # 01   MIRACE-TO500  881\n",
       "  25 │  7200  MIRACE-TO500  7204    # 02   LAJEAD-TO500  881\n",
       "  26 │  7200  MIRACE-TO500  7301    # 01   CO-MI1CAP500  881\n",
       "  27 │  7300  COLINA-TO500  7301    # 01   CO-MI1CAP500  881\n",
       "  28 │  7200  MIRACE-TO500  7303    # 02   CO-MI2CAP500  881\n",
       "  29 │  7300  COLINA-TO500  7303    # 02   CO-MI2CAP500  881\n",
       "  30 │  7102  GR-MI1CAP500  7201    # 01   MI-GR1CAP500  881\n",
       "  31 │  7200  MIRACE-TO500  7201    # 01   MI-GR1CAP500  881\n",
       "  32 │  7104  GR-MI2CAP500  7203    # 02   MI-GR2CAP500  881\n",
       "  33 │  7200  MIRACE-TO500  7203    # 02   MI-GR2CAP500  881\n",
       "  34 │  7209  MR-GR3CAP500  7105    # 03   GR-MI3CAP500  881\n",
       "  35 │  7200  MIRACE-TO500  7209    # 03   MR-GR3CAP500  881\n",
       "  36 │  6754  SPELAD-PA500  6440    # 01   ITACAI-PA500  841\n",
       "  37 │  6754  SPELAD-PA500  6560    # 01   INTEGR-PA500  841\n",
       "  38 │  6754  SPELAD-PA500  6560    # 02   INTEGR-PA500  841\n",
       "  39 │  6754  SPELAD-PA500  7200    # 01   MIRACE-TO500  841\n",
       "  40 │  6754  SPELAD-PA500  7200    # 02   MIRACE-TO500  841\n",
       "  41 │  8100  XINGU--PA500  6754    # 01   SPELAD-PA500  841\n",
       "  42 │  8100  XINGU--PA500  6754    # 02   SPELAD-PA500  841\n",
       "  43 │  7305  CO-MI3CAP500  7200    # 03   MIRACE-TO500  881\n",
       "  44 │  7300  COLINA-TO500  7305    # 03   CO-MI3CAP500  881\n",
       "  45 │  9478  ALTITU-BA500  9479   #01     ALTITU-BA230  701\n",
       "  46 │ 44948  BARRA2SIN013  44946   #01    BARRA2-BA500  701\n",
       "  47 │  6060  GENDO2-BA500  9528   #01     GOURO-CER030  701\n",
       "  48 │  6060  GENDO2-BA500  42392   #01    GOR-T1-BA000  701\n",
       "  49 │  6060  GENDO2-BA500  42394   #02    GOR-T2-BA000  701\n",
       "  50 │  6060  GENDO2-BA500  45304   #03    GOR-T3-BA000  701\n",
       "  51 │  6360  BARREI-BA500  42386   #01    BRD-T1-BA000  701\n",
       "  52 │  6360  BARREI-BA500  44138   #02    BRD-T2-BA000  701\n",
       "  53 │  7204  LAJEAD-TO500  44031   #01    LAJ-T1-TO000  881\n",
       "  54 │  7204  LAJEAD-TO500  44033   #02    LAJ-T2-TO000  881\n",
       "  55 │  6754  SPELAD-PA500  7261   #01     SPLAT1-PA000  841\n",
       "  56 │  6754  SPELAD-PA500  7263   #02     SPLAT2-PA000  841\n",
       "  57 │  7200  MIRACE-TO500  7208   #01     MIRACE-TO000  881\n",
       "  58 │  7202  MIRACEPCH138  7208   #01     MIRACE-TO000  883\n",
       "  59 │  7205  MIRACE-TO013  7208   #01     MIRACE-TO000  881\n",
       "  60 │  7200  MIRACE-TO500  7210   #02     MIRAC2-TO000  881\n",
       "  61 │  7202  MIRACEPCH138  7210   #02     MIRAC2-TO000  883\n",
       "  62 │  7211  MIRAC2-TO013  7210   #02     MIRAC2-TO000  881"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "cont(area,cont3,viz3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'BURITI-BA500_ALTITU-BA500\t'\n",
      "BRANCH\t6075\t9478\t01\n",
      "\tEND /\n",
      "'BARRA2-BA500_CORREN-BA500\t'\n",
      "BRANCH\t44946\t44947\t01"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\tEND /\n",
      "'BURITI-BA500_BARRA2-BA500\t'\n",
      "BRANCH\t6075\t44946\t01"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\tEND /\n",
      "'CFORM2-BA500_BARRA2-BA500\t'\n",
      "BRANCH\t44945\t44946\t01\n",
      "\tEND /\n",
      "'GENDO2-BA500_OUROLN-BA500\t'\n",
      "BRANCH\t6060\t6070\t01\n",
      "\tEND /\n",
      "'BARREI-BA500_CELEO--BA500\t'\n",
      "BRANCH\t6360\t44596\t01\n",
      "\tEND /\n",
      "'BARREI-BA500_SERSOL-BA500\t'\n",
      "BRANCH\t6360\t44601\t01\n",
      "\tEND /\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'NEWER1-BA500_BARREI-BA500\t'\n",
      "BRANCH\t44700\t6360\t01\n",
      "\tEND /\n",
      "'EDNBAR-BA500_BARREI-BA500\t'\n",
      "BRANCH\t44978\t6360\t01\n",
      "\tEND /\n",
      "'LAJEAD-TO500_MIRACE-TO500\t'\n",
      "BRANCH\t7204\t7200\t01\n",
      "\tEND /\n",
      "'MIRACE-TO500_CO-MI1CAP500\t'\n",
      "BRANCH\t7200\t7301\t01\n",
      "\tEND /\n",
      "'COLINA-TO500_CO-MI1CAP500\t'\n",
      "BRANCH\t7300\t7301\t01\n",
      "\tEND /\n",
      "'GR-MI1CAP500_MI-GR1CAP500\t'\n",
      "BRANCH\t7102\t7201\t01\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\tEND /\n",
      "'MIRACE-TO500_MI-GR1CAP500\t'\n",
      "BRANCH\t7200\t7201\t01\n",
      "\tEND /\n",
      "'SPELAD-PA500_ITACAI-PA500\t'\n",
      "BRANCH\t6754\t6440\t01\n",
      "\tEND /\n",
      "'SPELAD-PA500_INTEGR-PA500\t'\n",
      "BRANCH\t6754\t6560\t01\n",
      "\tEND /\n",
      "'SPELAD-PA500_MIRACE-TO500\t'\n",
      "BRANCH\t6754\t7200\t01\n",
      "\tEND /\n",
      "'XINGU--PA500_SPELAD-PA500\t'\n",
      "BRANCH\t8100\t6754\t01\n",
      "\tEND /\n",
      "'ALTITU-BA500_ALTITU-BA230\t'\n",
      "BRANCH\t9478\t9479\t01\n",
      "\tEND /\n",
      "'BARRA2SIN013_BARRA2-BA500\t'\n",
      "BRANCH\t44948\t44946\t01\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\tEND /\n",
      "'GENDO2-BA500_GOURO-CER030\t'\n",
      "BRANCH\t6060\t9528\t01\n",
      "\tEND /\n",
      "'GENDO2-BA500_GOR-T1-BA000\t'\n",
      "BRANCH\t6060\t42392\t01\n",
      "\tEND /\n",
      "'BARREI-BA500_BRD-T1-BA000\t'\n",
      "BRANCH\t6360\t42386\t01\n",
      "\tEND /\n",
      "'LAJEAD-TO500_LAJ-T1-TO000\t'\n",
      "BRANCH\t7204\t44031\t01\n",
      "\tEND /\n",
      "'SPELAD-PA500_SPLAT1-PA000\t'\n",
      "BRANCH\t6754\t7261\t01\n",
      "\tEND /\n",
      "'MIRACE-TO500_MIRACE-TO000\t'\n",
      "BRANCH\t7200\t7208\t01\n",
      "\tEND /\n",
      "'MIRACEPCH138_MIRACE-TO000\t'\n",
      "BRANCH\t7202\t7208\t01\n",
      "\tEND /\n",
      "'MIRACE-TO013_MIRACE-TO000\t'\n",
      "BRANCH\t7205\t7208\t01\n",
      "\tEND /\n",
      "END /\n"
     ]
    }
   ],
   "source": [
    "outOrganon(viz3)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Contingências totais"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div class=\"data-frame\"><p>22 rows × 5 columns</p><table class=\"data-frame\"><thead><tr><th></th><th>From#</th><th>From Name</th><th>To# - Circ#</th><th>To Name</th><th>Area</th></tr><tr><th></th><th title=\"Int64\">Int64</th><th title=\"String\">String</th><th title=\"String\">String</th><th title=\"String\">String</th><th title=\"String\">String</th></tr></thead><tbody><tr><th>1</th><td>6060</td><td>GENDO2-BA500</td><td>6075    # 07</td><td>BURITI-BA500</td><td>701</td></tr><tr><th>2</th><td>6075</td><td>BURITI-BA500</td><td>44946    # 01</td><td>BARRA2-BA500</td><td>701</td></tr><tr><th>3</th><td>6075</td><td>BURITI-BA500</td><td>5325    # 02</td><td>QUEIMA-PI500</td><td>701</td></tr><tr><th>4</th><td>6075</td><td>BURITI-BA500</td><td>5325    # 03</td><td>QUEIMA-PI500</td><td>701</td></tr><tr><th>5</th><td>6075</td><td>BURITI-BA500</td><td>7190    # 06</td><td>GILBU2-PI500</td><td>701</td></tr><tr><th>6</th><td>6075</td><td>BURITI-BA500</td><td>7190    # 06</td><td>GILBU2-PI500</td><td>701</td></tr><tr><th>7</th><td>6075</td><td>BURITI-BA500</td><td>9478    # 01</td><td>ALTITU-BA500</td><td>701</td></tr><tr><th>8</th><td>6360</td><td>BARREI-BA500</td><td>6075    # 06</td><td>BURITI-BA500</td><td>701</td></tr><tr><th>9</th><td>6754</td><td>SPELAD-PA500</td><td>7200    # 01</td><td>MIRACE-TO500</td><td>841</td></tr><tr><th>10</th><td>6754</td><td>SPELAD-PA500</td><td>7200    # 02</td><td>MIRACE-TO500</td><td>841</td></tr><tr><th>11</th><td>7200</td><td>MIRACE-TO500</td><td>7190    # 03</td><td>GILBU2-PI500</td><td>881</td></tr><tr><th>12</th><td>7200</td><td>MIRACE-TO500</td><td>7190    # 03</td><td>GILBU2-PI500</td><td>881</td></tr><tr><th>13</th><td>7200</td><td>MIRACE-TO500</td><td>7201    # 01</td><td>MI-GR1CAP500</td><td>881</td></tr><tr><th>14</th><td>7200</td><td>MIRACE-TO500</td><td>7203    # 02</td><td>MI-GR2CAP500</td><td>881</td></tr><tr><th>15</th><td>7200</td><td>MIRACE-TO500</td><td>7204    # 02</td><td>LAJEAD-TO500</td><td>881</td></tr><tr><th>16</th><td>7200</td><td>MIRACE-TO500</td><td>7208   #01</td><td>MIRACE-TO000</td><td>881</td></tr><tr><th>17</th><td>7200</td><td>MIRACE-TO500</td><td>7209    # 03</td><td>MR-GR3CAP500</td><td>881</td></tr><tr><th>18</th><td>7200</td><td>MIRACE-TO500</td><td>7210   #02</td><td>MIRAC2-TO000</td><td>881</td></tr><tr><th>19</th><td>7200</td><td>MIRACE-TO500</td><td>7301    # 01</td><td>CO-MI1CAP500</td><td>881</td></tr><tr><th>20</th><td>7200</td><td>MIRACE-TO500</td><td>7303    # 02</td><td>CO-MI2CAP500</td><td>881</td></tr><tr><th>21</th><td>7204</td><td>LAJEAD-TO500</td><td>7200    # 01</td><td>MIRACE-TO500</td><td>881</td></tr><tr><th>22</th><td>7305</td><td>CO-MI3CAP500</td><td>7200    # 03</td><td>MIRACE-TO500</td><td>881</td></tr></tbody></table></div>"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ccccc}\n",
       "\t& From\\# & From Name & To\\# - Circ\\# & To Name & Area\\\\\n",
       "\t\\hline\n",
       "\t& Int64 & String & String & String & String\\\\\n",
       "\t\\hline\n",
       "\t1 & 6060 & GENDO2-BA500 & 6075    \\# 07 & BURITI-BA500 & 701 \\\\\n",
       "\t2 & 6075 & BURITI-BA500 & 44946    \\# 01 & BARRA2-BA500 & 701 \\\\\n",
       "\t3 & 6075 & BURITI-BA500 & 5325    \\# 02 & QUEIMA-PI500 & 701 \\\\\n",
       "\t4 & 6075 & BURITI-BA500 & 5325    \\# 03 & QUEIMA-PI500 & 701 \\\\\n",
       "\t5 & 6075 & BURITI-BA500 & 7190    \\# 06 & GILBU2-PI500 & 701 \\\\\n",
       "\t6 & 6075 & BURITI-BA500 & 7190    \\# 06 & GILBU2-PI500 & 701 \\\\\n",
       "\t7 & 6075 & BURITI-BA500 & 9478    \\# 01 & ALTITU-BA500 & 701 \\\\\n",
       "\t8 & 6360 & BARREI-BA500 & 6075    \\# 06 & BURITI-BA500 & 701 \\\\\n",
       "\t9 & 6754 & SPELAD-PA500 & 7200    \\# 01 & MIRACE-TO500 & 841 \\\\\n",
       "\t10 & 6754 & SPELAD-PA500 & 7200    \\# 02 & MIRACE-TO500 & 841 \\\\\n",
       "\t11 & 7200 & MIRACE-TO500 & 7190    \\# 03 & GILBU2-PI500 & 881 \\\\\n",
       "\t12 & 7200 & MIRACE-TO500 & 7190    \\# 03 & GILBU2-PI500 & 881 \\\\\n",
       "\t13 & 7200 & MIRACE-TO500 & 7201    \\# 01 & MI-GR1CAP500 & 881 \\\\\n",
       "\t14 & 7200 & MIRACE-TO500 & 7203    \\# 02 & MI-GR2CAP500 & 881 \\\\\n",
       "\t15 & 7200 & MIRACE-TO500 & 7204    \\# 02 & LAJEAD-TO500 & 881 \\\\\n",
       "\t16 & 7200 & MIRACE-TO500 & 7208   \\#01 & MIRACE-TO000 & 881 \\\\\n",
       "\t17 & 7200 & MIRACE-TO500 & 7209    \\# 03 & MR-GR3CAP500 & 881 \\\\\n",
       "\t18 & 7200 & MIRACE-TO500 & 7210   \\#02 & MIRAC2-TO000 & 881 \\\\\n",
       "\t19 & 7200 & MIRACE-TO500 & 7301    \\# 01 & CO-MI1CAP500 & 881 \\\\\n",
       "\t20 & 7200 & MIRACE-TO500 & 7303    \\# 02 & CO-MI2CAP500 & 881 \\\\\n",
       "\t21 & 7204 & LAJEAD-TO500 & 7200    \\# 01 & MIRACE-TO500 & 881 \\\\\n",
       "\t22 & 7305 & CO-MI3CAP500 & 7200    \\# 03 & MIRACE-TO500 & 881 \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/plain": [
       "\u001b[1m22×5 DataFrame\u001b[0m\n",
       "\u001b[1m Row \u001b[0m│\u001b[1m From# \u001b[0m\u001b[1m From Name    \u001b[0m\u001b[1m To# - Circ#   \u001b[0m\u001b[1m To Name      \u001b[0m\u001b[1m Area   \u001b[0m\n",
       "\u001b[1m     \u001b[0m│\u001b[90m Int64 \u001b[0m\u001b[90m String       \u001b[0m\u001b[90m String        \u001b[0m\u001b[90m String       \u001b[0m\u001b[90m String \u001b[0m\n",
       "─────┼──────────────────────────────────────────────────────────\n",
       "   1 │  6060  GENDO2-BA500  6075    # 07   BURITI-BA500  701\n",
       "   2 │  6075  BURITI-BA500  44946    # 01  BARRA2-BA500  701\n",
       "   3 │  6075  BURITI-BA500  5325    # 02   QUEIMA-PI500  701\n",
       "   4 │  6075  BURITI-BA500  5325    # 03   QUEIMA-PI500  701\n",
       "   5 │  6075  BURITI-BA500  7190    # 06   GILBU2-PI500  701\n",
       "   6 │  6075  BURITI-BA500  7190    # 06   GILBU2-PI500  701\n",
       "   7 │  6075  BURITI-BA500  9478    # 01   ALTITU-BA500  701\n",
       "   8 │  6360  BARREI-BA500  6075    # 06   BURITI-BA500  701\n",
       "   9 │  6754  SPELAD-PA500  7200    # 01   MIRACE-TO500  841\n",
       "  10 │  6754  SPELAD-PA500  7200    # 02   MIRACE-TO500  841\n",
       "  11 │  7200  MIRACE-TO500  7190    # 03   GILBU2-PI500  881\n",
       "  12 │  7200  MIRACE-TO500  7190    # 03   GILBU2-PI500  881\n",
       "  13 │  7200  MIRACE-TO500  7201    # 01   MI-GR1CAP500  881\n",
       "  14 │  7200  MIRACE-TO500  7203    # 02   MI-GR2CAP500  881\n",
       "  15 │  7200  MIRACE-TO500  7204    # 02   LAJEAD-TO500  881\n",
       "  16 │  7200  MIRACE-TO500  7208   #01     MIRACE-TO000  881\n",
       "  17 │  7200  MIRACE-TO500  7209    # 03   MR-GR3CAP500  881\n",
       "  18 │  7200  MIRACE-TO500  7210   #02     MIRAC2-TO000  881\n",
       "  19 │  7200  MIRACE-TO500  7301    # 01   CO-MI1CAP500  881\n",
       "  20 │  7200  MIRACE-TO500  7303    # 02   CO-MI2CAP500  881\n",
       "  21 │  7204  LAJEAD-TO500  7200    # 01   MIRACE-TO500  881\n",
       "  22 │  7305  CO-MI3CAP500  7200    # 03   MIRACE-TO500  881"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "contingencias=vcat(viz1,viz2)\n",
    "#contingencias=vcat(contingencias,viz3) #Caso deseja-se incluir 3 vizinhança. porém para a 3 melhor fazer na mão\n",
    "sort!(contingencias,[1,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Remoção de elementos que se repetem. ex: se temos 2 buses de interesse, a msm linha é primeira vizinhança dos 2 buses\n",
    "sum=0\n",
    "for i in findall(nonunique(contingencias))\n",
    "    delete!(contingencias,i-sum)\n",
    "    sum+=1\n",
    "end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'BURITI-BA500_BARRA2-BA500\t'\n",
      "BRANCH\t6075\t44946\t01\n",
      "\tEND /\n",
      "'BURITI-BA500_ALTITU-BA500\t'\n",
      "BRANCH\t6075\t9478\t01\n",
      "\tEND /\n",
      "'SPELAD-PA500_MIRACE-TO500\t'\n",
      "BRANCH\t6754\t7200\t01\n",
      "\tEND /\n",
      "'MIRACE-TO500_MI-GR1CAP500\t'\n",
      "BRANCH\t7200\t7201\t01\n",
      "\tEND /\n",
      "'MIRACE-TO500_MIRACE-TO000\t'\n",
      "BRANCH\t7200\t7208\t01\n",
      "\tEND /\n",
      "'MIRACE-TO500_CO-MI1CAP500\t'\n",
      "BRANCH\t7200\t7301\t01\n",
      "\tEND /\n",
      "'LAJEAD-TO500_MIRACE-TO500\t'\n",
      "BRANCH\t7204\t7200\t01\n",
      "\tEND /\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "END /\n"
     ]
    }
   ],
   "source": [
    "outOrganon(contingencias)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Julia 1.6.7",
   "language": "julia",
   "name": "julia-1.6"
  },
  "language_info": {
   "file_extension": ".jl",
   "mimetype": "application/julia",
   "name": "julia",
   "version": "1.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
