install.packages('httr')
install.packages('jsonlite')
install.packages('glue')

library(httr)
library(jsonlite)
library(glue)

clima <- function(city) {   

    city <- gsub(" ", "-", city)

    response_geoCoding <- GET(glue("http://api.openweathermap.org/geo/1.0/direct?q={city},Rio-de-Janeiro,BR&appid=d8dddb1bcad0dd2c12e6a141f4e558d4"))

    if (status_code(response_geoCoding) == 200) {
        json_data <- content(response_geoCoding, as = "text")
        content_geoCoding <- fromJSON(json_data)
        
        lat <- round(content_geoCoding["lat"], 2)
        lon <- round(content_geoCoding["lon"], 2)

        response_weather <- GET(glue("https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=d8dddb1bcad0dd2c12e6a141f4e558d4&units=metric"))

        if (status_code(response_weather) == 200) {
            content_weather <- fromJSON(content(response_weather, as = "text"))
            # print(content_weather)
            # print(paste0("Temperatura: ", content_weather$main$temp, "°C"))
            # print(paste0("Umidade: ", content_weather$main$humidity, "%"))
            # print(paste0("Vento: ", content_weather$wind$speed, " km/h"))

            return (
                data.frame(
                    item = c("Temperatura: ", "Umidade: ", "Vento: "),
                    valor = c(
                        round(content_weather$main$temp), 
                        round(content_weather$main$humidity), 
                        content_weather$wind$speed),
                    unid_medida = c("°C", "%", "km/h")
                )
            )

        } else {
            print(paste("Erro:", status_code(response_weather)))
        }

    } else {
        print(paste("Erro:", status_code(response_geoCoding)))
    }
}

# city <- gsub(" ", "-", readline(prompt = "Digite sua cidade: "))

# print(clima("Pinheiral"))