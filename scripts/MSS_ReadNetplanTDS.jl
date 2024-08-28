#= 04/05/2019 - este programa irá executar a análise dinâmica para contigências simples para os cenários do OptFlow exportados para PWF. Dessa forma, o próprio Netplan irá fazer as leituras dos cenários do SDDP e gerar um ponto de operação sem precisar passar pelo comando SCD do Organon

Andamento
17/07/2019 - O Módulo Logging não funciona adequadamente

A Fazer:
Substituir os prints pelo logging.

=#

function TDS(path,results,dyn,evt,plv)
#----------Variáveis de entrada-------------------------
    PATH_ORGANON = path
    results      = results #lista de saídas
    dynFile      = string(dyn,".dyn") #arquivo dinâmico
    println("Arquivo Dinâmico: "*dynFile)
    evtFile      = string(evt,".evt") #lista de contigências
    println("Arquivo de Contigências: "*evtFile)
    plvFile = fill("",size(plv)[1])
    for i in 1:size(plv)[1]
        plvFile[i] = plv[i]*".plv"
        println("Arquivo de gráfico: "*plvFile[i])
    end


#----------Variáveis auxiliares------------------------
  cfg    = readdlm(PATH_ORGANON*"Flw_Summary.csv", ',', comments=false,skipstart=1) #este arquivo contem nas colunas 2 (etapa), coluna 3(série) e coluna 4 (bloco) referente a ordem dos arquivos do netplan
    nCases = size(cfg)[1] #número de casos
    println(string("Total de Casos: ",nCases))
    cases = cfg[:,1]
    dictCases  = Dict()

    auxZeros    = "00000"
    sptDinamica = ""

    evt        = readdlm(PATH_ORGANON*evtFile, comments=false,skipstart=1)
    auxCtg     = find(x->(x==-99),evt)
    nCtg       = size(auxCtg)[1] #numero de contigências
    codeCtg    = Array{String}(nCtg,1) #código das contigências
    codeCtg[1] = string(evt[1,1])
    nameCtg    = Array{String}(nCtg,1) #nome das contigências
    nameCtg[1] = split(evt[1,2],"'")[2]
    for i in 2:nCtg
        pos        = auxCtg[i-1] + 1
        codeCtg[i] = string(evt[pos,1])
        nameCtg[i] = split(evt[pos,2],"'")[2]
    end
    println(string("Total de Contingências: ",nCtg))

#----------Código Principal------------------------
    #Escreve o código do Organon
    p = Progress(nCases, 1, "Escrevendo Código Organon...")
    aux = 0
    for i in cfg[:,1]
        aux = aux+1
        dictCases[i]    = [cfg[aux,2],cfg[aux,3],cfg[aux,4]] #dicionario com etapa,serie e bloco
        strI        = string(i)
        key         = "ANAR_"*auxZeros[1:5-length(strI)]*strI*".PWF" #arquivo do netplan
        sptDinamica = sptDinamica*"OPEN "*key*"\n"
        sptDinamica = sptDinamica*"OPEN "*dynFile*"\n"
        sptDinamica = sptDinamica*"OPEN "*evtFile*"\n"
        for l in plvFile
            sptDinamica = sptDinamica*"OPEN "*l*"\n"
        end
        sptDinamica = sptDinamica*"NEWTON"*"\n"
        sptDinamica = sptDinamica*"NEWTON"*"\n"
        for k in codeCtg
            sptDinamica = sptDinamica*"TDS CTG ="*k*"\n"
            sptDinamica = sptDinamica*"SAVE "*"caso"*string(i)*"_ctg"k*"_frequency"*".PLT"*"\n"
        end
        for j in results
            sptDinamica = sptDinamica*"CSV "*j*"\n"
            sptDinamica = sptDinamica*"COPY "*PATH_ORGANON*j*".csv "*PATH_ORGANON*j*"_"*string(i)*".csv\n"
            sptDinamica = sptDinamica*"DEL "*PATH_ORGANON*j*".csv "*"\n"
        end
        next!(p)
    end

#------------Finalizacao-----------------------------------------
    arq  = PATH_ORGANON*"script.spt"
    narq = open(arq,"w")
    write(narq,sptDinamica)
    write(narq,"\nEND/")
    close(narq)
    println("Script Organon Finalizado")
    return(cases,nCases, dictCases,nCtg,nameCtg)
#==========Rodando com mais de um processador=======================
    for i in 1:73
        strI = string(i)
        key = PATH_ORGANON1*"ANAR_"*auxZeros[1:5-length(strI)]*strI*".PWF" #arquivo do netplan
        sptDinamica = sptDinamica*"OPEN "*key*"\n"
        sptDinamica = sptDinamica*"OPEN "*dynFile*"\n"
        sptDinamica = sptDinamica*"OPEN "*evtFile*"\n"
        for k in codeCtg
            sptDinamica = sptDinamica*"TDS CTG ="*k*"\n"
        end
        for j in results
            sptDinamica = sptDinamica*"CSV "*j*"\n"
            sptDinamica = sptDinamica*"COPY "*PATH_ORGANON1*j*".csv "*PATH_ORGANON1*j*"_"*string(i)*"_ctg"*k*".csv\n"
            sptDinamica = sptDinamica*"DEL "*PATH_ORGANON1*j*".csv "*"\n"

        end
    end
    #Salva o Script
    arq  = PATH_ORGANON1*"script.spt"
    narq = open(arq,"w")
    write(narq,sptDinamica)
    write(narq,"\nEND/")
    close(narq)


    sptDinamica = ""
    for i in 74:144
        strI = string(i)
        key = PATH_ORGANON2*"ANAR_"*auxZeros[1:5-length(strI)]*strI*".PWF" #arquivo do netplan
        sptDinamica = sptDinamica*"OPEN "*key*"\n"
        sptDinamica = sptDinamica*"OPEN "*dynFile*"\n"
        sptDinamica = sptDinamica*"OPEN "*evtFile*"\n"
        for k in codeCtg
            sptDinamica = sptDinamica*"TDS CTG ="*k*"\n"
        end
        for j in results
            sptDinamica = sptDinamica*"CSV "*j*"\n"
            sptDinamica = sptDinamica*"COPY "*PATH_ORGANON2*j*".csv "*PATH_ORGANON2*j*"_"*string(i)*".csv\n"
            sptDinamica = sptDinamica*"DEL "*PATH_ORGANON2*j*".csv "*"\n"
        end
    end
    arq  = PATH_ORGANON2*"script.spt"
    narq = open(arq,"w")
    write(narq,sptDinamica)
    write(narq,"\nEND/")
    close(narq)

    ====================================#

end
