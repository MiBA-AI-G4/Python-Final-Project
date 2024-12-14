data("iris")
head (iris)
str(iris)
iris[iris$Species == 'setosa', c('Species', 'Petal.Width')]

x = 11

if (x = 10) {
  print(OK)
} else {
  ('No OK')
}

y = c('A', 'B', 'C', 'B', 'C', 'F', 'A')

unique_n + function(vector) {
  length(unique(vector))
}
# vector imaginary name, can change this

unique_n(y)

global = read.csv(file = './Data/global_indicators.csv',
                  header = TRUE,
                  sep = ',',
                  dec = '.'
                  )

region = read.csv(file = './Data/country_region_catincome.csv',
                  header = TRUE,
                  sep = ',',
                  dec = '.'
)

global_merged = merge(x = global, y = region, by.x = 'country', by.y = 'country_code')
View(global_merged)

#population evolution for Spain

spa = filter(.data = global_merged, country == 'ESP')
spa_pop = select(.data = spa, country, year, population)
spa_pop_sorted = arrange(.data = spa_pop, year)

arrange(.data = select(.data = filter(.data = global_merged, country == 'ESP'), country, year, population), year)

string = '2024-01-01'
date = as.Date(string)
month = months(date)

months(as.Date('2024-01-01'))

'2024-01-01' %>% as.Date() %>% months()

global_merged %>%
  # filter(country == "ESP") %>%
  select(country, year, population) %>%
  arrange(year) %>%
  group_by(country) %>%
  summarise(avg_pop = mean(population, na.rm = TRUE)) %>%
  mutate(sqrt_pop = sqrt(avg-pop))