#= 11/08/2019 - este programa irá exportar os dados de geração tabular do ORGANON.
=#

function Gen(path)
#----------Variáveis de entrada-------------------------
    PATH_ORGANON = path


#----------Variáveis auxiliares------------------------
  cfg    = readdlm(PATH_ORGANON*"Flw_Summary.csv", ',', comments=false,skipstart=1) #este arquivo contem nas colunas 2 (etapa), coluna 3(série) e coluna 4 (bloco) referente a ordem dos arquivos do netplan
    nCases = size(cfg)[1] #número de casos
    println(string("Total de Casos: ",nCases))
    cases = cfg[:,1]
    dictCases  = Dict()

    auxZeros    = "00000"
    sptDinamica = ""
j = "NTW03"

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
        sptDinamica = sptDinamica*"NEWTON"*"\n"
        sptDinamica = sptDinamica*"NEWTON"*"\n"
        sptDinamica = sptDinamica*"CSV "*j*"\n"
        sptDinamica = sptDinamica*"COPY "*PATH_ORGANON*j*".csv "*PATH_ORGANON*j*"_"*string(i)*".csv\n"
        sptDinamica = sptDinamica*"DEL "*PATH_ORGANON*j*".csv "*"\n"
        next!(p)
    end

#------------Finalizacao-----------------------------------------
    arq  = PATH_ORGANON*"script.spt"
    narq = open(arq,"w")
    write(narq,sptDinamica)
    write(narq,"\nEND/")
    close(narq)
    println("Script Organon Finalizado")
    return(cases,nCases,dictCases)
end

function ReadGen(path,cases, nCases, dictCases,nGen)

        NTW03 = Array{Any}(1+nGen*nCases,7)
        NTW03[1,1]    = "Casos" #a coluna é a identificação dos casos
        NTW03[1,2]    = "Bus" #a coluna é a identificação dos casos
        NTW03[1,3]    = "Name" #a coluna é a identificação dos casos
        NTW03[1,4]    = "Status" #a coluna é a identificação dos casos
        NTW03[1,5]    = "Pg" #a coluna é a identificação dos casos
        NTW03[1,6]    = "Qg" #a coluna é a identificação dos casos
        NTW03[1,7]    = "Pmax" #a coluna é a identificação dos casos

        p = Progress(nCases, 1, "Escrevendo Arquivo de Resumo das Análises Dinâmicas...")
        aux = 0
        for i in cases
            aux = aux + 1
            NTW03[2+(aux-1)*nGen:nGen*aux+1,1] = string(i)
            arq = readdlm(PATH_ORGANON*"NTW03_"*string(i)*".csv",',',skipblanks=false,skipstart=1,comments=false,skipstart=1,header=true)[1]
            NTW03[2+(aux-1)*nGen:nGen*aux+1,2] = arq[:,1]
            NTW03[2+(aux-1)*nGen:nGen*aux+1,3] = arq[:,2]
            NTW03[2+(aux-1)*nGen:nGen*aux+1,4] = arq[:,4]
            NTW03[2+(aux-1)*nGen:nGen*aux+1,5] = arq[:,6]
            NTW03[2+(aux-1)*nGen:nGen*aux+1,6] = arq[:,7]
            NTW03[2+(aux-1)*nGen:nGen*aux+1,7] = arq[:,9]
            next!(p)
        end

        writedlm(PATH_ORGANON*"NTW03Completo.csv",NTW03,',')
        println("Arquivo NTW03 Salvo")
end
