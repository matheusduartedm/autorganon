#Pacotes
using DataFrames
using CSV
using ProgressMeter
using Gtk
using Plots
using StatPlots
using Plotly
using PyPlot


#Funções
include("MSS_OrganonExe.jl")
include("MSS_ReadNetplanTDS.jl")
include("MSS_ReadResults.jl")
include("MSS_AnalyseResults.jl")
include("MSS_ReadGenOrganon.jl")

#Entradas
PATH_ORGANON = "D:\\GoogleDrive\\ufrj\\TCC\\02-Base_Dados\\17-Colombia_2030_Damping_v2\\analise\\" #caminho do estudo
results      = ["TDS00","TDS01","TDS03","TDS14","TDS15"] #lista de saídas
dynFile      = "maquinas_2030_damping_v2" #arquivo dinâmico
evtFile      = "eventos_2030" #lista de contigências
plvfile      = ["frequency"]


#Execução das Rodadas
(cases,nCases,dictCases,nCtg,nameCtg) = TDS(PATH_ORGANON,results,dynFile,evtFile,plvfile)
OrganonExe(PATH_ORGANON)
(TDS01,TDS00,TDS03,TDS14,TDS15) = Results(PATH_ORGANON, cases, nCases, dictCases, nCtg,nameCtg)

TDS01 = readdlm(PATH_ORGANON*"\\TDS01Completo"*".csv",',',skipblanks=false,comments=false)
TDS00 = readdlm(PATH_ORGANON*"\\TDS00Completo"*".csv",',',skipblanks=false,comments=false)

nCases = 180
nCtg = 59
Convergencia(nCases,nCtg,TDS00)

(heat, xs,ys,indiceStab) = IndiceStab(nCases,nCtg,TDS01)
plotStab = heatmap(xs, ys, indiceStab, colorbar = true, clim=(58.8,60),color = :Spectral, title = "Estabilidade dos casos",xlabel = "# Contingência",ylabel = "# Cenário")

plotStab = heatmap(title = "Estabilidade dos casos",xlabel = "# Contingência",ylabel = "# Cenário")

surfStap = plot!(indiceStab, st = [:surface], color=:YlGnBu,zlabel = "Índice de Estabilidade")

    nVariaveis = 101
    caso = "53240"
    ctg = "23"
    exportPlot = 1 #1 para exportar e 0 para não.

(plotf, plota) = plotOrganon(PATH_ORGANON, nVariaveis, caso, ctg, exportPlot)
(plotfrequency) = plotFreq(PATH_ORGANON, nVariaveis, caso, ctg, exportPlot)
(plota) = plotA(PATH_ORGANON, nVariaveis, caso, ctg, exportPlot)

 plot(plota,palette=:Spectral, line = 2,  xlabel = "Tempo (s)",ylabel = "Ângulo (Graus) - " *"Caso "*string(caso) *" -  Ctg "*string(ctg),clim=(-40,40))

(cases,nCases,dictCases) = Gen(PATH_ORGANON)
OrganonExe(PATH_ORGANON)
nGen = 229
ReadGen(PATH_ORGANON,cases, nCases, dictCases,nGen)

nCtg = 59
nCases = 180
PATH = "D:\\GoogleDrive\\ufrj\\TCC\\02-Base_Dados\\17-Colombia_2030_Damping_v2\\Analise\\"
file = "frequencia_contingencia.csv"

function VarCvarContingencia(PATH,file, nCtg,nCases)
    freqContingencia = readdlm(PATH*file,',',skipblanks=false,comments=false,skipstart=1)
    result           = Array{Any}(nCtg,3)
    for i in 1:nCtg
        freq        = (freqContingencia[(i-1)*180+1: 180*i,2])
        result[i,1] = freqContingencia[(i-1)*180+1,1]
        (var,cVar)  = VarCvar(freq)
        result[i,2] = var
        result[i,3] = cVar
    end
    writedlm(PATH*"VarCvar_.csv",result,',')
end


function VarCvar(freq, alpha=5)
    dist = sort(freq)
    casos = size(dist)[1]
    pos = alpha*casos ÷ 100
    var = dist[pos]
    cVar = mean(dist[1:pos])
    return(var,cVar)
end

VarCvarContingencia(PATH,file, nCtg,nCases)
