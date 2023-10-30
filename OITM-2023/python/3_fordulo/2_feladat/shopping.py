import os
import pandas as pd

shopping_list = {
    "Komló": 2,
    "Maláta": 10,
    "Sörélesztő": 1,
    "Víz": 100,
    "Üveg": 48
}


def load_data(file_name: str) -> dict[str, dict[str, int]]:
    return pd.read_excel(os.path.join(os.getcwd(), file_name), engine="openpyxl")


def get_cheapest_store(shopping_list: dict[str, int], stores: pd.DataFrame) -> [str, int]:
    """Return the cheapest store
    (where the total cost of the items * amount in the shopping list is the minimum),
    and the total price of the shopping list."""
    # TODO: implement this function properly


if __name__ == "__main__":
    stores = load_data("ingredients.xlsx")
    print(get_cheapest_store(shopping_list, stores))
