import os
import pandas as pd
import matplotlib.pyplot as plt


class SalesDashboard:
    REQUIRED_COLUMNS = ["Date", "Product", "Sales"]

    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.filename)
            self.data.columns = self.data.columns.str.strip()  # remove stray spaces in headers

            missing = [c for c in self.REQUIRED_COLUMNS if c not in self.data.columns]
            if missing:
                print(f"Missing column(s): {', '.join(missing)}")
                return False

            # Clean types once, up front
            self.data["Date"] = pd.to_datetime(self.data["Date"], errors="coerce")
            self.data["Sales"] = pd.to_numeric(self.data["Sales"], errors="coerce")
            self.data = self.data.dropna(subset=["Date", "Sales"])

            if self.data.empty:
                print("No valid rows found in the file.")
                return False

            print("Sales Data Loaded Successfully!")
            return True

        except FileNotFoundError:
            print(f"Error: '{self.filename}' not found!")
            return False
        except Exception as e:
            print("Error loading CSV:", e)
            return False

    def display_data(self):
        print("\nRetail Sales Data:")
        print(self.data.to_string(index=False))

    def line_graph(self):
        daily_sales = self.data.groupby("Date")["Sales"].sum().sort_index()
        plt.figure(figsize=(10, 5))
        plt.plot(daily_sales.index, daily_sales.values, marker="o")
        plt.title("Daily Retail Sales")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def bar_chart(self):
        product_sales = self.data.groupby("Product")["Sales"].sum().sort_values(ascending=False)
        plt.figure(figsize=(10, 5))
        plt.bar(product_sales.index, product_sales.values)
        plt.title("Product-wise Sales")
        plt.xlabel("Product")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def main():
    # Works both as a script and in the Interactive Window / notebook
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        base_dir = os.getcwd()

    dashboard = SalesDashboard(os.path.join(base_dir, "sales.csv"))

    if dashboard.load_data():
        dashboard.display_data()
        dashboard.line_graph()
        dashboard.bar_chart()


if __name__ == "__main__":
    main()