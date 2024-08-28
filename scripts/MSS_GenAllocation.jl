#=
Como o programa irá ler direto do Netplan, não será necessário esse código por ora.
Essa função deverá permitir alocar os geradores em um arquivo de rede do organon.ntw de acordo com o arquivo dger.dat e acertar a área das barras de acordo com o regiao.dat
=#

function MSS_GenAllocation(Path, file)
    dictGerBus = Dict() #Este dicionário irá permitir mapear a geração/barra para a escrita dos cenários.
    for arquivo in file
        # Passo 1 - Lê arquivo ntw e localiza a parte dos geradores, das barras e da área
        rede      = readdlm(Path*"\\"*arquivo,'\n', comments=false)

        iniB      = 5
        fimB      = find(x->x==" 0  / END OF BUS DATA, BEGIN LOAD DATA", rede)[1]
        iniG      = find(x->x=="0  / END OF LOAD DATA, BEGIN GENERATOR DATA", rede)[1]
        fimG      = find(x->x=="0  / END OF GENERATOR DATA, BEGIN SHUNT DATA", rede)[1]
        iniA      = find(x->x=="0  / END OF VSC DATA, BEGIN AREA DATA", rede)[1]
        fimA      = find(x->x=="0  / END OF AREA DATA, BEGIN OF ZONE DATA", rede)[1]
        bus       = split.(rede[iniB:fimB-1],",")
        generator = split.(rede[iniG+2:fimG-1],",")
        linB      = fimB-iniB
        colB      = size(bus[1])[1]
        linG      = fimG-2-iniG
        colG      = size(generator[1])[1]

        auxB      = Array{String}(linB,colB)
        auxG      = Array{String}(linG,colG)
        tensaoB   = Array{String}(linB,2) #irá guardar a tensão e parâmetros de sequência dos geradores
        sincrono = []
        for i in 1:linG
            for j in 1:colG
                auxG[i,j] =rstrip(lstrip(generator[i][j]))
                if j == 15
                    pmax = parse(Float64,generator[i][j])
                    if pmax == 0.0
                        push!(sincrono, i+iniG+1)
                    end
                end

            end
        end

        for i in 1:linB
            for j in 1:colB
                auxB[i,j] = bus[i][j]
                if j == 1
                    tensaoB[i,1] = lstrip.(rstrip.(auxB[i,1]))
                elseif j == 10
                    tensaoB[i,2] = auxB[i,10]
                end
            end
        end


        #Passo 2 - Lê o arquivo dger.dat com a localização dos geradores e o regiao.dat com as áreas
        dger   = readdlm(Path*"/dger.dat", ',', comments=false)
        regiao = readdlm(Path*"/regiao.dat",',', comments=false)


        #Passo 3 - Acerta a área das barras

        for i in 1:linB #esse for está devagar
            auxB[i,8] = string(regiao[find(x->x==parse(Int64,auxB[i,1]), regiao[:,1]),6][1])
        end

        novaArea = unique(regiao[:,5])


        # Passo 4 - Aceta a localização dos geradores
        finalG     = Array{String}(size(dger)[1]-2,colG) # String  final padrão .NTW com os geradores

        for i in 3:size(dger)[1]
            l            = i-2
            barra        = string(dger[i,4])
            finalG[l,1]  = barra
            finalG[l,2]  = "'1'"
            finalG[l,3]  = "0.0"
            finalG[l,4]  = "0.0"
            qMax         = dger[i,11]
            finalG[l,5]  = string(qMax)
            finalG[l,6]  = string(dger[i,10])
            finalG[l,7]  = tensaoB[find(x->x==barra, tensaoB[:,1])[1],2]
            finalG[l,8]  = barra
            finalG[l,9]  = "0.0"
            finalG[l,10] = "0.00000"
            finalG[l,11] = "0.00000"
            finalG[l,12] = "1.00000"
            finalG[l,13] = "1"
            finalG[l,14] = "100.0"
            pMax         = dger[i,9]
            finalG[l,15] = string(pMax)
            finalG[l,16] = "0.0"
            finalG[l,17] = "10"
            finalG[l,18] = "0"
            finalG[l,19] = "1"
            finalG[l,20] = "1" #conexão estrela [padrão]
            finalG[l,21] = "0.000"
            S            = sqrt(pMax^2+qMax^2)
            X1           = 0.3/S
            finalG[l,22] = string(round(X1,8))
            finalG[l,23] = "0.000"
            X0           = 0.7*X1
            finalG[l,24] = string(X0)
            finalG[l,25] = "0.000"
            Xn           = (1 -2*X1)/(3*S)
            finalG[l,26] = string(round(Xn,8))
            gerador      = dger[i,2]
            finalG[l,27] = gerador
            dictGerBus = merge(dictGerBus,Dict(gerador=>barra))
        end



        #Passo 5 - Escreve arquivo modificado
        arq  = Path*"\\SDDP_"*arquivo
        narq = open(arq,"w")
        write(narq,string(rede[1]))
        write(narq,"\n")
        write(narq,rede[2])
        write(narq,"\n")
        write(narq,"Caso - geradores SDDP")
        write(narq,"\n")
        write(narq,rede[4])
        write(narq,"\n")
        writedlm(narq,auxB, ',')
        for i in fimB:iniG+1
            write(narq,rede[i])
            write(narq,"\n")
        end
        writedlm(narq,finalG, ',')
        for i in sincrono
            write(narq,rede[i])
            write(narq,"\n")
        end
        for i in fimG:iniA+1
            write(narq,rede[i])
            write(narq,"\n")
        end
        for i in 2:size(novaArea)[1]
            area = string(regiao[find(x->x==novaArea[i],regiao[:,5])[1],6])*",0,0.00,"*novaArea[i]
            write(narq,area)
            write(narq,"\n")
        end
        for i in fimA:size(rede)[1]
            write(narq,rede[i])
            write(narq,"\n")
        end
        close(narq)
    end
    return (dictGerBus)
end
#run(`D:/TCC/01-Base_Organon/ORGANONB.exe -1 cenario.spt`,   )
