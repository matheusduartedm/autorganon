#= 26/05/2019 - este programa irá analisar os resultados do Organon para o usuário como uma espécie de graficador para resultados macros
=#


#=Ideia 1 - verificar as rodadas
1 - indica que o caso foi rodado
0 - indica que teve problema de convergência - "Not Checked" ou "Severe Error"
=#
function Convergencia(nCases,nCtg,TDS00)
    nCases  = nCases
    nCtg    = nCtg
    TDS00   = TDS00
    if nCtg == 1
        converg = ones(nCases,2)
    else
        converg = ones(nCases,nCtg)
    end



    p = Progress(nCases*nCtg, 1, "Verificando os casos...")
    for i in 1:nCases
        for j in 1:nCtg
            if TDS00[(i-1)*nCtg + j + 1,6] == " Not Checked" || TDS00[(i-1)*nCtg + j,6] == " Severe Error"
                converg[i,j] = 0
            end
        end
        next!(p)
    end
    plotly()

    ys = [string(i) for i = 1:nCases]
    if nCtg == 1
        xs = [string(i) for i = 1:2]
    else
        xs = [string(i) for i = 1:nCtg]
    end
    plotConverg = heatmap(xs, ys, converg, colorbar = true, clim=(0,1),color = :Spectral, title = "Convergência dos casos", xlabel = "# Ctg",ylabel = "# Cenário")
    return plotConverg
end



#=Ideia 2 - mapa de calor com os indíces de estabilidade do arquivo margem
=#
function IndiceStab(nCases,nCtg,TDS01)
    nCases  = nCases
    nCtg    = nCtg
    TDS01   = TDS01
    if nCtg == 1
        indiceStab = ones(nCases,2)
    else
        indiceStab = ones(nCases,nCtg)
    end


    p = Progress(nCases*nCtg, 1, "Verificando os casos...")
    for i in 1:nCases
        for j in 1:nCtg
            try
                indiceStab[i,j] = TDS01[(i-1)*nCtg + j + 1,11]
            catch
                indiceStab[i,j] = parse(TDS01[(i-1)*nCtg + j + 1,11])
            end
        end
        next!(p)
    end
    plotly()

    ys = [string(i) for i = 1:nCases]
    if nCtg == 1
        xs = [string(i) for i = 1:2]
    else
        xs = [string(i) for i = 1:nCtg]
    end



    plotStab = heatmap(xs, ys, indiceStab, colorbar = true, clim=(0.6,1),color = :tempo, title = "Estabilidade dos casos")
    #surfStap = plot3d(xs,ys,indiceStab)
    #surfStap = plot(xs,ys,indiceStab, st = [:surface, :contourf])
    return (plotStab,xs,ys,indiceStab)
end

#=Ideia 3 - mapa com a frequencia por barra e variação angular
lê os arquivos .plt com as saídas do Organon=#

function plotOrganon(PATH_ORGANON, nVariaveis, caso, ctg, exportPlot)
    PATH_ORGANON = PATH_ORGANON
    nVariaveis =  nVariaveis #número de varíaveis do gráfico
    caso = caso
    ctg = ctg
    variaveis = Array{Any}(1,nVariaveis)
    exportPlot = exportPlot
    graph2   = readdlm(PATH_ORGANON*"caso"*caso*"_ctg"*ctg*".PLT",skipblanks=false,skipstart=2+2*nVariaveis,comments=false,header=false)
    open(PATH_ORGANON*"caso"*string(caso)*"_ctg"*string(ctg)*".PLT") do file
         for (i, ln) in enumerate(eachline(file))
            if i <= nVariaveis + 2
                if i >2
                    variaveis[1,i-2] = split(split(ln,":",)[2]," ")[3]
                end
            else
                break
            end
        end
    end


    nLinhas = div(2*nVariaveis,5)+1 #indica o número de linhas + 1 que as variáveis ocupam
    dataFrequency = zeros(size(graph2)[1]/(nLinhas),nVariaveis+1)
    dataAngle = zeros(size(graph2)[1]/(nLinhas),nVariaveis+1)
    for i in 1:Int(size(graph2)[1]/(nLinhas))
        dataFrequency[i,1] =  graph2[1+(i-1)*(nLinhas),1]
        dataAngle[i,1]     =  dataFrequency[i,1]
        for j in 1:nVariaveis
            dataFrequency[i,j+1] = graph2[div(j,5)+1+(i-1)*(nLinhas),1+j-div(j,5)*5]
            jAngle = j + nVariaveis
            dataAngle[i,j+1]  = graph2[div(jAngle,5)+1+(i-1)*(nLinhas),1+jAngle-div(jAngle,5)*5]
        end
    end
    plotly()

    fmin = fill(59.8,Int(size(graph2)[1]/(nLinhas)))
    fmax = fill(60.2,Int(size(graph2)[1]/(nLinhas)))
    plotf = plot(dataFrequency[:,1],hcat(fmin,fmax,dataFrequency[:,2:nVariaveis+1]), label = hcat(["fMin" "fMax"],variaveis),hover = hcat(["fMin" "fMax"],variaveis), palette=:Spectral, line = 2, xlabel = "Tempo (s)", ylabel = "Frequência (Hz) - "*"Caso "*string(caso) *" -  Ctg "*string(ctg))
    plota = plot(plotAngle[:,1],dataAngle[:,2:nVariaveis+1], palette=:Spectral, line = 2, label = variaveis, hover=variaveis,palette=:Spectral, line = 2,  xlabel = "Tempo (s)",ylabel = "Ângulo (Graus) - " *"Caso "*string(caso) *" -  Ctg "*string(ctg))

    if exportPlot == 1
        writedlm(PATH_ORGANON*"Frequencia_"*"Caso"*string(caso)*"_Ctg"*string(ctg)*".csv",dataFrequency,',')
        writedlm(PATH_ORGANON*"Angulo_"*"Caso"*string(caso)*"_Ctg"*string(ctg)*".csv",dataAngle,',')
        println("Arquivos com os dados dos gráficos exportados com sucesso")
    end
    return plotf, plota
end


function plotFreq(PATH_ORGANON, nVariaveis, caso, ctg, exportPlot)
    PATH_ORGANON = PATH_ORGANON
    nVariaveis =  nVariaveis #número de varíaveis do gráfico
    caso = caso
    ctg = ctg
    variaveis = Array{Any}(1,nVariaveis)
    exportPlot = exportPlot
    graph2   = readdlm(PATH_ORGANON*"caso"*caso*"_ctg"*ctg*"_frequency"*".PLT",skipblanks=false,skipstart=2+nVariaveis,comments=false,header=false)
    open(PATH_ORGANON*"caso"*string(caso)*"_ctg"*string(ctg)*"_frequency"*".PLT") do file
         for (i, ln) in enumerate(eachline(file))
            if i <= nVariaveis + 2
                if i >2
                    variaveis[1,i-2] = split(split(ln,":",)[2]," ")[3]
                end
            else
                break
            end
        end
    end


    nLinhas = div(nVariaveis,5)+1 #indica o número de linhas + 1 que as variáveis ocupam
    plotFrequency = zeros(size(graph2)[1]/(nLinhas),nVariaveis+1)
    for i in 1:Int(size(graph2)[1]/(nLinhas))
        plotFrequency[i,1] =  graph2[1+(i-1)*(nLinhas),1]
        for j in 1:nVariaveis
            plotFrequency[i,j+1] = graph2[div(j,5)+1+(i-1)*(nLinhas),1+j-div(j,5)*5]
        end
    end
    plotly()

    fmin = fill(59.4,Int(size(graph2)[1]/(nLinhas)))
    fmax = fill(60.2,Int(size(graph2)[1]/(nLinhas)))
    Plots.plot()
    plotfrequency = plot!(plotFrequency[:,1],hcat(fmin,fmax,plotFrequency[:,2:nVariaveis+1]), label = hcat(["fMin" "fMax"],variaveis),hover = hcat(["fMin" "fMax"],variaveis), palette=:Spectral, line = 2, xlabel = "Tempo (s)", ylabel = "Frequência (Hz) - "*"Caso "*string(caso) *" -  Ctg "*string(ctg))

    if exportPlot == 1
        writedlm(PATH_ORGANON*"Frequencia_"*"Caso"*string(caso)*"_Ctg"*string(ctg)*".csv",vcat(hcat(["tempo"],variaveis),plotFrequency),',')
        println("Arquivos com os dados dos gráficos exportados com sucesso")
    end
    return plotfrequency
end

function plotA(PATH_ORGANON, nVariaveis, caso, ctg, exportPlot)
    PATH_ORGANON = PATH_ORGANON
    nVariaveis =  nVariaveis #número de varíaveis do gráfico
    caso = caso
    ctg = ctg
    variaveis = Array{Any}(1,nVariaveis)
    exportPlot = exportPlot
    graph2   = readdlm(PATH_ORGANON*"caso"*caso*"_ctg"*ctg*"_angle"*".PLT",skipblanks=false,skipstart=2+nVariaveis,comments=false,header=false)
    open(PATH_ORGANON*"caso"*string(caso)*"_ctg"*string(ctg)*"_angle"*".PLT") do file
         for (i, ln) in enumerate(eachline(file))
            if i <= nVariaveis + 2
                if i >2
                    variaveis[1,i-2] = split(split(ln,":",)[2]," ")[3]
                end
            else
                break
            end
        end
    end


    nLinhas = div(nVariaveis,5)+1 #indica o número de linhas + 1 que as variáveis ocupam
    plotAngle = zeros(size(graph2)[1]/(nLinhas),nVariaveis+1)
    for i in 1:Int(size(graph2)[1]/(nLinhas))
        plotAngle[i,1] =  graph2[1+(i-1)*(nLinhas),1]
        for j in 1:nVariaveis
            plotAngle[i,j+1] = graph2[div(j,5)+1+(i-1)*(nLinhas),1+j-div(j,5)*5]
        end
    end
    plotly()

    plotangle = plot(plotAngle[:,1],plotAngle[:,2:nVariaveis+1], palette=:Spectral, line = 2, label = variaveis, hover=variaveis,palette=:Spectral, line = 2,  xlabel = "Tempo (s)",ylabel = "Ângulo (Graus) - " *"Caso "*string(caso) *" -  Ctg "*string(ctg))

    if exportPlot == 1
        writedlm(PATH_ORGANON*"Angulo_"*"Caso"*string(caso)*"_Ctg"*string(ctg)*".csv",vcat(hcat(["tempo"],variaveis),plotAngle),',')
        println("Arquivos com os dados dos gráficos exportados com sucesso")
    end
    return plotangle
end
