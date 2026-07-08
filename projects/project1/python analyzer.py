import pandas as pd
import matplotlib.pyplot as plt


class TitanicAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def clean_data(self):
        # Condensed cleaning logic
        self.df['Age'] = self.df['Age'].fillna(self.df["Age"].median())
        self.df = self.df.drop(columns=['Cabin'])
        self.df["Embarked"] = self.df["Embarked"].fillna(self.df["Embarked"].mode()[0])

    def engineer_features(self):
        self.df["FamilySize"] = self.df["SibSp"].add(self.df["Parch"], fill_value=0) + 1

    def generate_report(self):
        total_passengers = len(self.df)
        overall_survival = self.df["Survived"].mean() * 100

        # THE UPGRADE: 24 lines of code reduced to 2 lines using Groupby
        gender_survival = self.df.groupby("Sex")["Survived"].mean() * 100
        class_survival = self.df.groupby("Pclass")["Survived"].mean() * 100

        report = f"""=======================================
TITANIC SURVIVAL ANALYSIS REPORT
=======================================
[INFO] Data loaded successfully.
[INFO] Data cleaned and features engineered.

--- OVERALL STATS ---
Total Passengers: {total_passengers}
Overall Survival Rate: {overall_survival:.2f}%

--- GENDER ANALYSIS ---
Female Survival Rate: {gender_survival.get('female', 0):.2f}%
Male Survival Rate: {gender_survival.get('male', 0):.2f}%

--- CLASS ANALYSIS ---
Class 1 Survival Rate: {class_survival.get(1, 0):.2f}%
Class 2 Survival Rate: {class_survival.get(2, 0):.2f}%
Class 3 Survival Rate: {class_survival.get(3, 0):.2f}%
======================================="""
        print(report)

    def generate_visualizations(self):
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))

        # Plot 1: Age Distribution
        axes[0].hist(self.df['Age'], bins=20, color='lightgrey', edgecolor='black', linewidth=2)
        axes[0].set_xlabel("Age")
        axes[0].set_ylabel("Number of Passengers")
        axes[0].set_title("Passenger Age Distribution")
        axes[0].grid(True, linestyle="--", alpha=0.7)

        classes = ["Class 1", "Class 2", "Class 3"]
        rates = self.df.groupby("Pclass")["Survived"].mean() * 100

        axes[1].bar(classes, rates, color=["#4CAF50", "#FF9800", "#F44336"], edgecolor="black", width=0.6)
        axes[1].set_ylabel("Survival Rate (%)")
        axes[1].set_title("Survival Rate by Passenger Class")
        axes[1].set_ylim(0, 100)

        plt.tight_layout()

        plt.savefig("visualizations.png", dpi=300)
        plt.close()


if __name__ == "__main__":
    analyzer = TitanicAnalyzer("train.csv")
    analyzer.clean_data()
    analyzer.engineer_features()
    analyzer.generate_report()
    analyzer.generate_visualizations()
    print("[INFO] Process complete. Visualizations saved to disk as 'visualizations.png'.")