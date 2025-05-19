import pandas as pd
import os

# #  dzielnice
# def generate_districts_inserts(input_csv = "districts.csv", output_sql = "insert_districts.sql"):
#     districts = pd.read_csv(input_csv, encoding="UTF-8", sep=';')
#     districts.columns = districts.columns.str.strip()

#     insert_districts = (
#         "INSERT INTO districts (district_id, district_name, district_area, registered_residents)"
#         "VALUES ({district_id}, '{district_name}', {district_area}, {registered_residents});")

#     insert_districts_values = []
#     for _, row in districts.iterrows():
#         values = insert_districts.format(
#             district_id=row["district_id"],
#             district_name=row["district_name"].replace("'", "''"),
#             district_area=row["area"],
#             registered_residents=row["registered_residents"]
#         )
#         insert_districts_values.append(values)


#     with open(output_sql, "w", encoding="utf-8") as f:
#         f.write("\n".join(insert_districts_values))
#         f.write("\n")
#     print("Dzielnice dodane", districts.head(2))

# #  demografia
# def generate_demographics_inserts(input_csv = "demographics.csv", output_sql = "insert_demographics.sql"):
#     demographics = pd.read_csv(input_csv, encoding= "UTF-8", sep=';')
#     demographics.columns = demographics.columns.str.strip()

#     insert_demographics = (
#         "INSERT INTO demographics (demographic_id, district_id, gender, age_from, age_to, count)"
#         "VALUES ({demographic_id}, {district_id}, '{gender}', {age_from}, {age_to}, {count});")

#     insert_demographics_values = []
#     for _, row in demographics.iterrows():
#         values = insert_demographics.format(
#             demographic_id=row["demographic_id"],
#             district_id=row["district_id"],
#             gender=row["gender"],
#             age_from=row["age_from"],
#             age_to=row["age_to"],
#             count=row["count"]
#         )
#         insert_demographics_values.append(values)


#     with open(output_sql, "w", encoding="utf-8") as f:
#         f.write("\n".join(insert_demographics_values))
#         f.write("\n")
#     print(demographics.head(2))

# #  działki
# def geberate_plots_inserts(input_csv = "plots.csv", output_sql = "insert_plots.sql"):
#     plots = pd.read_csv(input_csv, encoding= "UTF-8", sep=';')
#     plots.columns = plots.columns.str.strip()

#     insert_plots = (
#         "INSERT INTO plots (plot_id, district_id, identifier, plot_number, plot_area_ha)"
#         "VALUES ({plot_id}, {district_id}, '{identifier}', {plot_number}, {plot_area_ha});")

#     insert_plots_values = []
#     for _, row in plots.iterrows():
#         values = insert_plots.format(
#             plot_id=row["plot_id"],
#             district_id=row["district_id"],
#             identifier=row["identifier"],
#             plot_number=row["plot_number"],
#             plot_area_ha=row["plot_area_ha"]
#         )
#         insert_plots_values.append(values)


#     with open(output_sql, "w", encoding="utf-8") as f:
#         f.write("\n".join(insert_plots_values))
#         f.write("\n")
#     print(plots.head(2))


# #  piramida wieku
# def generate_age_pyramid_inserts(input_csv = "age_piramid.csv", output_sql = "insert_age_pyramid.sql"):
#     age_pyramid = pd.read_csv(input_csv, encoding="UTF-8", sep=';')
#     age_pyramid.columns = age_pyramid.columns.str.strip()  # usunięcie spacji z nazw kolumn

#     insert_age_pyramid = (
#         "INSERT INTO age_pyramid (pyramid_id, district_id, f_0_2, m_0_2, f_3_6, m_3_6, "
#         "f_7_14, m_7_14, f_15_18, m_15_18, f_19_24, m_19_24, f_25_34, m_25_34, "
#         "f_35_44, m_35_44, f_45_59_64, m_45_59_64, f_60_65_79, m_60_65_79, "
#         "f_over_80, m_over_80) "
#         "VALUES ({pyramid_id}, {district_id}, {f_0_2}, {m_0_2}, {f_3_6}, {m_3_6}, "
#         "{f_7_14}, {m_7_14}, {f_15_18}, {m_15_18}, {f_19_24}, {m_19_24}, "
#         "{f_25_34}, {m_25_34}, {f_35_44}, {m_35_44}, {f_45_59_64}, {m_45_59_64}, "
#         "{f_60_65_79}, {m_60_65_79}, {f_over_80}, {m_over_80});"
#     )

#     insert_age_pyramid_values = []

#     for _, row in age_pyramid.iterrows():

#         values = insert_age_pyramid.format(
#             pyramid_id=int(row["pyramid_id"]) if row["pyramid_id"] != "NULL" else "NULL",
#             district_id=int(row["district_id"]) if row["district_id"] != "NULL" else "NULL",
#             f_0_2=row["f_0_2"],
#             m_0_2=row["m_0_2"],
#             f_3_6=row["f_3_6"],
#             m_3_6=row["m_3_6"],
#             f_7_14=row["f_7_14"],
#             m_7_14=row["m_7_14"],
#             f_15_18=row["f_15_18"],
#             m_15_18=row["m_15_18"],
#             f_19_24=row["f_19_24"],
#             m_19_24=row["m_19_24"],
#             f_25_34=row["f_25_34"],
#             m_25_34=row["m_25_34"],
#             f_35_44=row["f_35_44"],
#             m_35_44=row["m_35_44"],
#             f_45_59_64=row["f_45_59_64"],
#             m_45_59_64=row["m_45_59_64"],
#             f_60_65_79=row["f_60_65_79"],
#             m_60_65_79=row["m_60_65_79"],
#             f_over_80=row["f_over_80"],
#             m_over_80=row["m_over_80"]
#         )
#         insert_age_pyramid_values.append(values)

#     with open(output_sql, "w", encoding="utf-8") as f:
#         f.write("\n".join(insert_age_pyramid_values))
#         f.write("\n")

#     print(f"Wygenerowano {len(insert_age_pyramid_values)} INSERTów do tabeli age_pyramid.")

    # # przystanki
# def generate_stops_inserts(input_csv = "stops.csv", output_sql = "insert_stops.sql"):
#     stops = pd.read_csv(input_csv, encoding="UTF-8", sep=';')
#     stops.columns = stops.columns.str.strip()

#     insert_stops = (
#     "INSERT INTO stops (stop_id, district_id, stop_name, lines, stop_type, longitude, latitude) "
#     "VALUES ({stop_id}, {district_id}, '{stop_name}', '{lines}', '{stop_type}', {longitude}, {latitude});"
#     )

#     insert_stops_values = []
#     for _, row in stops.iterrows():
#         values = insert_stops.format(
#             stop_id=row["stop_id"],
#             district_id=row["district_id"],
#             stop_name=row["stop_name"],
#             lines=row["lines"],
#             stop_type=row["stop_type"],
#             longitude=row["longitude"],
#             latitude=row["latitude"]
#         )
#         insert_stops_values.append(values)

#     # Zapisz do pliku
#     with open(output_sql, "w", encoding="utf-8") as f:
#         f.write("\n".join(insert_stops_values))
#         f.write("\n")

#     print(f"Wygenerowano {len(insert_stops_values)} INSERTów do tabeli stops.")

# budynki
# def generate_buildings_inserts(input_csv = "buildings.csv", output_sql = "insert_buildings.sql"):
# buildings = pd.read_csv(input_csv, encoding="UTF-8", sep=';')
# buildings.columns = buildings.columns.str.strip()

# insert_buildings = (
#     "INSERT INTO buildings (building_id, district_id, plot_number, index_type, building_type, building_area_ha) "
#     "VALUES ({building_id}, {district_id}, '{plot_number}', '{index_type}', '{building_type}', {building_area_ha});")

# insert_buildings_values = []
# for _, row in buildings.iterrows():
#     values = insert_buildings.format(
#         building_id=row["building_id"],
#         district_id=row["district_id"],
#         plot_number=row["plot_number"],
#         index_type=row["index_type"],
#         building_type=row["building_type"],
#         building_area_ha=row["building_area_ha"]
#     )
#     insert_buildings_values.append(values)

# with open(output_sql, "w", encoding="utf-8") as f:
#     f.write("\n".join(insert_buildings_values))
#     f.write("\n")

# print(buildings.head(2))
# print(f"Wygenerowano {len(insert_buildings_values)} INSERTów do tabeli buildings.")

# #  zieleń
# def generate_green_areas_inserts(input_csv = "green_areas.csv", output_sql = "insert_green_areas.csv"):
#     green_areas = pd.read_csv(input_csv, encoding="UTF-8", sep=';')
#     green_areas.columns = green_areas.columns.str.strip()

#     insert_green_areas = (
#         "INSERT INTO green_areas (green_area_id, district_id, green_type, area_ha) "
#         "VALUES ({green_area_id}, {district_id}, '{green_type}', {area_ha});")

#     insert_green_areas_values = []
#     for _, row in green_areas.iterrows():
#         values = insert_green_areas.format(
#             green_area_id=row["green_area_id"],
#             district_id=row["district_id"],
#             green_type=row["green_type"],
#             area_ha=row["area_ha"]
#         )
#         insert_green_areas_values.append(values)

#     with open(output_sql, "w", encoding="utf-8") as f:
#         f.write("\n".join(insert_green_areas_values))
#         f.write("\n")

#     print(f"Wygenerowano {len(insert_green_areas_values)} INSERTów do tabeli green_areas.")

#  ceny
# def generate_price_registry_inserts(input_csv = "price_registry.csv", output_sql = "insert_price_registry.sql"):
#     price_registry = pd.read_csv("price_registry.csv", encoding = "UTF-8", sep=";")
#     price_registry.columns = price_registry.columns.str.strip()
#     insert_price_registry =(
#         "INSERT INTO price_registry (price_registry_id, purchase_year, purchase_month, market_type, avg_price, avg_area, avg_price_per_m2, object_count, district_id) "
#         "VALUES ({price_registry_id}, {purchase_year}, {purchase_month}, '{market_type}', {avg_price}, {avg_area}, {avg_price_per_m2}, {object_count}, {district_id});"
#     )

#     insert_price_registry_values = []
#     for _, row in price_registry.iterrows():
#         values = insert_price_registry.format(
#             price_registry_id=row["price_registry_id"],
#             purchase_year=row["purchase_year"],
#             purchase_month=row["purchase_month"],
#             market_type=row["market_type"],
#             avg_price=row["avg_price"],
#             avg_area=row["avg_area"],
#             avg_price_per_m2=row["avg_price_per_m2"],
#             object_count=row["object_count"],
#             district_id=row["district_id"]
#         )
#         insert_price_registry_values.append(values)

#     with open(output_sql, "w", encoding="utf-8") as f: 
#         f.write("\n".join(insert_price_registry_values))
#         f.write("\n")

#     print(f"Wygenerowano {len(insert_price_registry_values)} INSERTów do tabeli price_registry.")

# #  dostępność   
# def generate_facility_access_inserts(input_csv = "facility_access.csv", output_sql = "insert_facility_access.sql"):
#     facility_access = pd.read_csv(input_csv, encoding = "UTF-8", sep=";")
#     facility_access.columns = facility_access.columns.str.strip()

#     insert_facility_access = (
#         "INSERT INTO facility_access (facility_id, facility_name, facility_type, facility_code, street, longitude, latitude, district_id) "
#         "VALUES ({facility_id}, '{facility_name}', '{facility_type}', {facility_code}, '{street}', {longitude}, {latitude}, {district_id});"
#     )
#     insert_facility_access_values = []
#     for _, row in facility_access.iterrows():
#         values = insert_facility_access.format(
#             facility_id=row["facility_id"],
#             facility_name=row["facility_name"],
#             facility_type=row["facility_type"],
#             facility_code=row["facility_code"],
#             street=row["street"],
#             longitude=row["longitude"],
#             latitude=row["latitude"],
#             district_id=row["district_id"]
#         )
#         insert_facility_access_values.append(values)

#     with open(output_sql, "w", encoding="utf-8") as f:
#         f.write("\n".join(insert_facility_access_values))
#         f.write("\n")

#     print(f"Wygenerowano {len(insert_facility_access_values)} INSERTów do tabeli facility_access.")



# wyswollanie funkcji

# generate_districts_inserts()
# generate_demographics_inserts()
# generate_plots_inserts()
# generate_age_pyramid_inserts()
# generate_stops_inserts()
# generate_buildings_inserts()
# generate_green_areas_inserts()
# generate_price_registry_inserts()
# generate_facility_access_inserts()