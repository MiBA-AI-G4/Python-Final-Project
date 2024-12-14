load('./DATA/sales_pharmacy.RData')
load('./DATA/adress_pharmacy.RData')

pediatric_sales <- sales_pharmacy[sales_pharmacy$classification_id == 8, ]

library(dplyr)

pharmacy_sales <- pediatric_sales %>%
  group_by(pharmacy_id) %>%
  summarise(total_units = sum(units))

pharmacy_data <- merge(pharmacy_sales, adress_pharmacy, by = "pharmacy_id")

catalonia_pharmacies <- pharmacy_data %>%
  filter(province_id %in% c('08', '25', '17', '43'))

top_20_pharmacies <- catalonia_pharmacies %>%
  group_by(province) %>%
  arrange(desc(total_units)) %>%
  mutate(rank = row_number()) %>%
  filter(rank <= 0.2 * n())

eligible_pharmacies_per_province <- top_20_pharmacies %>%
  group_by(province) %>%
  summarise(eligible_pharmacies = n())

write.csv(top_20_pharmacies, "top_20_pharmacies.csv", row.names = FALSE)
