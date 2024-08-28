#= 12/05/2019 - este programa irá fazer a leitura dos arquivos de resultados do Organon e salvá-las em um arquivo único
=#
#=
Andamento
16/07/2019 - função para ler os arquivos testadas. Além disso, para arquivos de margem vazios, o programa preenche com margem igual a 1
17/07/2019 - função testada e implementada com o retorno das variáveis

Faltando
Está faltando o cabeçalho dos arquivos TDS03, TDS14, TDS15
=#


function Results(PATH_ORGANON, cases, nCases, dictCases, nCtg,nameCtg)
    #=Entradas
    PATH_ORGANON - string com o path do caso - vem da função main
    cases - dicionário com a chave dos casos e correspondente etapa, série e bloc -  vem da função ReadNetplanTDS
    nCases - inteiro com a quantidade de casos -  vem da função ReadNetplanTDS
    nCtg - inteiro com a quantidade de contigênicas
    nameCtg - Array de strings com os nomes das contigências
    ,nCtg,nameCtg
    =#
    PATH_ORGANON = PATH_ORGANON
    cases        = cases
    casos        = dictCases
    nCases       = nCases
    nCtg         = nCtg
    nameCtg      = nameCtg


    #---------------------VARIÁVEIS AUXILIARES-----------------------------------------------------------
    TDS03 = Array{Any}(1,20) #damping
    TDS01 = Array{Any}(1+nCtg*nCases,22) #margem do caso - as dimensões do TDS01 jão são conhecidas
    TDS00 = Array{Any}(1+nCtg*nCases,32) #resumo do caso - as dimensões do TDS00 jão são conhecidas


    #----------Código Principal---------------------------------------------------------------------
    #ARQUIVO DE MARGEM------------------------------------------------------------------------------
    TDS01[1,1] = "Casos" #a coluna é a identificação dos casos
    TDS01[1,2] = "Etapa" #a coluna é a identificação das etapas
    TDS01[1,3] = "Serie" #a coluna é a identificação das séries
    TDS01[1,4] = "Bloco" #a coluna é a identificação dos blocos

    TDS01[1,5:22] = readdlm(PATH_ORGANON*"TDS01_"*string(cases[1])*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[2]

    p = Progress(nCases, 1, "Escrevendo Arquivo de Margem...")
    aux = 0
    for i in cases
        aux = aux + 1
        TDS01[2+(aux-1)*nCtg:nCtg*aux+1,1] = string(i)
        TDS01[2+(aux-1)*nCtg:nCtg*aux+1,2] = casos[i][1]
        TDS01[2+(aux-1)*nCtg:nCtg*aux+1,3] = casos[i][2]
        TDS01[2+(aux-1)*nCtg:nCtg*aux+1,4] = casos[i][3]
        try
            TDS01[2+(aux-1)*nCtg:nCtg*aux+1,5:22] =
            readdlm(PATH_ORGANON*"TDS01_"*string(i)*".csv",',',skipblanks=false, skipstart=1,comments=false,header=true)[1]
        catch
            ctgs = string.(readdlm(PATH_ORGANON*"TDS01_"*string(i)*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[1][:,1])
            totalR = size(readdlm(PATH_ORGANON*"TDS01_"*string(i)*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[1])[1]
            TDS01[2+(aux-1)*nCtg:1+(aux-1)*nCtg+totalR,5:22] =
            readdlm(PATH_ORGANON*"TDS01_"*string(i)*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[1]
            aux2=1
            for ct in 1:nCtg
                if nameCtg[ct] in ctgs
                    #O arquivo já foi preenchido com essas contigênicas
                else
                    println("Arquivo de margem incompleto ---> preenchido com margem igual a 1")
                    TDS01[1+(aux-1)*nCtg+totalR+aux2,5:22] = fill("",18)
                    TDS01[1+(aux-1)*nCtg+totalR+aux2,5]    = nameCtg[ct]
                    TDS01[1+(aux-1)*nCtg+totalR+aux2,9]    = "0"
                    TDS01[1+(aux-1)*nCtg+totalR+aux2,11]   = "1"
                    aux2= aux2+1
                end
            end
        end
        next!(p)
    end
    writedlm(PATH_ORGANON*"TDS01Completo.csv",TDS01,',')
    println("Arquivo TDS01 Salvo")


    #ARQUIVO DE Resumo da Análise dinâmica----------------------------------------------------------------
    TDS00[1,1]    = "Casos" #a coluna é a identificação dos casos
    TDS00[1,2]    = "Etapa" #a coluna é a identificação das etapas
    TDS00[1,3]    = "Serie" #a coluna é a identificação das séries
    TDS00[1,4]    = "Bloco" #a coluna é a identificação dos blocos

    TDS00[1,5:32] = readdlm(PATH_ORGANON*"TDS00_"*string(cases[1])*".csv",',',skipblanks=false,skipstart=1,comments=false,skipstart=1,header=true)[2]

    p = Progress(nCases, 1, "Escrevendo Arquivo de Resumo das Análises Dinâmicas...")
    aux = 0
    for i in cases
        aux = aux + 1
        TDS00[2+(aux-1)*nCtg:nCtg*aux+1,1] = string(i)
        TDS00[2+(aux-1)*nCtg:nCtg*aux+1,2] = casos[i][1]
        TDS00[2+(aux-1)*nCtg:nCtg*aux+1,3] = casos[i][2]
        TDS00[2+(aux-1)*nCtg:nCtg*aux+1,4] = casos[i][3]
        TDS00[2+(aux-1)*nCtg:nCtg*aux+1,5:32] = readdlm(PATH_ORGANON*"TDS00_"*string(i)*".csv",',',skipblanks=false,skipstart=1,comments=false,skipstart=1,header=true)[1]
        next!(p)
    end

    writedlm(PATH_ORGANON*"TDS00Completo.csv",TDS00,',')
    println("Arquivo TDS00 Salvo")

    #ARQUIVO DE DAMPING-------------------------------------------------------------------------------
    TDS03[1,1]    = "Casos" #a coluna é a identificação dos casos
    TDS03[1,2]    = "Etapa" #a coluna é a identificação das etapas
    TDS03[1,3]    = "Serie" #a coluna é a identificação das séries
    TDS03[1,4]    = "Bloco" #a coluna é a identificação dos blocos
    TDS03[1,5:20] = readdlm(PATH_ORGANON*"\\TDS03_"*string(cases[1])*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[2]

    p = Progress(nCases, 1, "Escrevendo Arquivo de Damping...")
    aux = 0
    for i in cases
        aux = aux + 1
        auxCases  = readdlm(PATH_ORGANON*"TDS03_"*string(i)*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[1]
        vecCases  =  Array{Any}(size(auxCases)[1],1)
        vecEtapas =  Array{Any}(size(auxCases)[1],1)
        vecSeries =  Array{Any}(size(auxCases)[1],1)
        vecBlocos =  Array{Any}(size(auxCases)[1],1)

        vecCases[1:size(auxCases)[1],1]  = string(i)
        vecEtapas[1:size(auxCases)[1],1] = casos[i][1]
        vecSeries[1:size(auxCases)[1],1] = casos[i][2]
        vecBlocos[1:size(auxCases)[1],1] = casos[i][3]

        TDS03 = vcat(TDS03,hcat(vecCases,vecEtapas,vecSeries,vecBlocos,auxCases))
        next!(p)
    end
    writedlm(PATH_ORGANON*"TDS03Completo.csv",TDS03,',')
    println("Arquivo TDS03 Salvo")

    #ARQUIVO DE SUB-FREQUÊNCIA-----------------------------------------------------------------
    TDS14         = Array{Any}(1,11)
    TDS14[1,1]    = "Casos" #a coluna é a identificação dos casos
    TDS14[1,2]    = "Etapa" #a coluna é a identificação das etapas
    TDS14[1,3]    = "Serie" #a coluna é a identificação das séries
    TDS14[1,4]    = "Bloco" #a coluna é a identificação dos blocos
    TDS14[1,5:11] = readdlm(PATH_ORGANON*"\\TDS14_"*string(cases[1])*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[2]
    aux           = 1

    p = Progress(nCases, 1, "Escrevendo Arquivo de Subfrequência...")
    for i in cases
        auxCases  = readdlm(PATH_ORGANON*"TDS14_"*string(i)*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[1]
        vecCases  =  Array{Any}(size(auxCases)[1],1)
        vecEtapas =  Array{Any}(size(auxCases)[1],1)
        vecSeries =  Array{Any}(size(auxCases)[1],1)
        vecBlocos =  Array{Any}(size(auxCases)[1],1)

        vecCases[1:size(auxCases)[1],1]  = string(i)
        vecEtapas[1:size(auxCases)[1],1] = casos[i][1]
        vecSeries[1:size(auxCases)[1],1] = casos[i][2]
        vecBlocos[1:size(auxCases)[1],1] = casos[i][3]

        TDS14 = vcat(TDS14,hcat(vecCases,vecEtapas,vecSeries,vecBlocos,auxCases))
        next!(p)
    end
    writedlm(PATH_ORGANON*"TDS14Completo.csv",TDS14,',')
    println("Arquivo TDS15 Salvo")

    # ARQUIVO DE SOBRE-FREQUÊNCIA
    TDS15         = Array{Any}(1,11)
    TDS15[1,1]    = "Casos" #a coluna é a identificação dos casos
    TDS15[1,2]    = "Etapa" #a coluna é a identificação das etapas
    TDS15[1,3]    = "Serie" #a coluna é a identificação das séries
    TDS15[1,4]    = "Bloco" #a coluna é a identificação dos blocos
    TDS15[1,5:11] = readdlm(PATH_ORGANON*"\\TDS15_"*string(cases[1])*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[2]
    aux           = 1

    p = Progress(nCases, 1, "Escrevendo Arquivo de Sobrefrequência...")
    for i in cases
        auxCases  = readdlm(PATH_ORGANON*"TDS15_"*string(i)*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[1]
        vecCases  =  Array{Any}(size(auxCases)[1],1)
        vecEtapas =  Array{Any}(size(auxCases)[1],1)
        vecSeries =  Array{Any}(size(auxCases)[1],1)
        vecBlocos =  Array{Any}(size(auxCases)[1],1)

        vecCases[1:size(auxCases)[1],1]  = string(i)
        vecEtapas[1:size(auxCases)[1],1] = casos[i][1]
        vecSeries[1:size(auxCases)[1],1] = casos[i][2]
        vecBlocos[1:size(auxCases)[1],1] = casos[i][3]

        TDS15 = vcat(TDS15,hcat(vecCases,vecEtapas,vecSeries,vecBlocos,auxCases))
        next!(p)
    end
    writedlm(PATH_ORGANON*"TDS15Completo.csv",TDS15,',')
    println("Arquivo TDS15 Salvo")

    return(TDS01,TDS00,TDS03,TDS14,TDS15)
end

#=Funções importantes
mkdir()
readdir()
mkpath() - cria diretorios e subdiretorios
rm() - deleta arquivos
    rm("C:\\Users\\amand\\Desktop\\TCC\\04-Resultados_Organon\\PARTE2\\teste",recursive=true)
isdir() - verifica se o diretório existe
=#

#=Lista de todos os arquivos .csvs da pasta
for file in files
    if file[end-2:end] == "csv"
        println(file)
    end
end
=#

#=TDS14         = Array{Any}(size(TDS03)[1],11) #sub_frequencia
TDS14[1,1]    = "Casos" #a coluna é a identificação dos casos
TDS14[1,2]    = "Etapa" #a coluna é a identificação das etapas
TDS14[1,3]    = "Serie" #a coluna é a identificação das séries
TDS14[1,4]    = "Bloco" #a coluna é a identificação dos blocos
TDS14[1,5:11] = readdlm(PATH_ORGANON*"\\TDS14_"*string(cases[1])*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[2]

p = Progress(nCases, 1, "Escrevendo Arquivo de subfrequencia...")
aux = 1
for i in cases
    dados                   = readdlm(PATH_ORGANON*"TDS14_"*string(i)*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[1]
    (l,c)                   = size(dados)
    TDS14[aux+1:aux+l,5:11] = readdlm(PATH_ORGANON*"TDS14_"*string(i)*".csv",',',skipblanks=false,skipstart=1,comments=false,header=true)[1]
    TDS14[aux+1:aux+l,1]    = string(i)
    TDS14[aux+1:aux+l,2]    = casos[i][1]
    TDS14[aux+1:aux+l,3]    = casos[i][2]
    TDS14[aux+1:aux+l,4]    = casos[i][3]
    aux                     = aux + 1
    next!(p)
end
writedlm(PATH_ORGANON*"TDS14Completo.csv",TDS14,',')
println("Arquivo TDS14 Salvo")=#
