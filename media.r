# install.packages('glue')

library(glue)

insumos_gastos <- data.frame(
  Mes = 1:12,
  Sulfato_de_Amonio    = c(10.5, 11.2, 9.8, 12.1, 10.9, 11.5, 10.0, 9.7, 10.8, 11.3, 10.1, 12.0),
  Superfosfato_Simples = c(7.2, 7.5, 6.8, 7.9, 7.0, 7.3, 6.9, 7.1, 7.4, 7.0, 6.7, 7.8),
  Cloreto_de_Potassio  = c(5.5, 5.8, 5.2, 6.0, 5.6, 5.9, 5.3, 5.4, 5.7, 5.5, 5.1, 6.1)
)

# Calcular a média para cada insumo
media_sulfato      <- round(mean(insumos_gastos$Sulfato_de_Amonio), 2)
media_superfosfato <- round(mean(insumos_gastos$Superfosfato_Simples), 2)
media_cloreto      <- round(mean(insumos_gastos$Cloreto_de_Potassio), 2)

# Calcular o desvio padrão para cada insumo
desvio_sulfato      <- round(sd(insumos_gastos$Sulfato_de_Amonio), 2)
desvio_superfosfato <- round(sd(insumos_gastos$Superfosfato_Simples), 2)
desvio_cloreto      <- round(sd(insumos_gastos$Cloreto_de_Potassio), 2)

print(glue("--- Sulfato de Amônio --- \nMédia: {media_sulfato}t \nDesvio Padrão: {desvio_sulfato}t \n\n"))
print(glue("--- Superfosfato Simples --- \nMédia: {media_superfosfato}t \nDesvio Padrão: {desvio_superfosfato}t \n\n"))
print(glue("--- Cloreto de Potássio --- \nMédia: {media_cloreto}t \nDesvio Padrão: {desvio_cloreto}t \n"))
