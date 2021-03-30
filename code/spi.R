"
SPI-12 calculation
Sandy Herho <herho@umd.edu>
2021/03/31
"

rm(list = ls())


library(SPEI)
library(TSstudio)
library(tidyverse)

p <- read.csv("../data/precipWestPapua.csv")

spi12 <- spi(p$tp, 12)
spi12 <- spi12$fitted
spi12 <- na.omit(as.data.frame(spi12))
dates <- seq.Date(from = as.Date("1979-12-01"),
                  to = as.Date("2020-12-01"),
                  by = "month")
spi12 <- tibble(cbind.data.frame(dates, spi12), 
                .name_repair = ~ c("Dates", "SPI12"))


write.csv(spi12,"../data/spi12.csv")


SPI12 <- ts(data = spi12$SPI12,
            start = c(1979, 12),
            end = c(2020, 12),
            frequency = 12)

ts_plot(SPI12, line.mode = "lines+markers", 
        Xtitle = 'time (month)',
        Ytitle = "Standardized Precipitation Index - 12",
        title = ' ',
        Xgrid = TRUE,
        Ygrid = TRUE,
        color = '#924034')
