library(tidyverse)

data(band_members)
data(band_instruments)

left_join(x = band_members, y = band_instruments, by = 'name')

full_join(x = band_members, y = band_instruments, by = 'name')

anti_join(x = band_members, y = band_instruments, by = 'name')

global = read.csv('./DATA/glabal_indicators.csv')