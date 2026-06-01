import pandas as pd
import matplotlib.pyplot as plt


class TitanicAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def clean_data(self):
        median_age = self.df["Age"].median()
        self.df['Age'] = self.df['Age'].fillna(median_age)
        self.df = self.df.drop(columns=['Cabin'])
        mode_embarked = self.df["Embarked"].mode()[0]
        self.df["Embarked"] = self.df["Embarked"].fillna(mode_embarked)

    def engineer_features(self):
        self.df["FamilySize"] = self.df["SibSp"].add(self.df["Parch"], fill_value=0) + 1

    def generate_report(self):
        total_passengers = len(self.df)
        total_survived = self.df["Survived"].sum()
        survived_percent = (total_survived / total_passengers) * 100

        female_df = self.df[self.df['Sex'] == 'female']
        total_female = len(female_df)
        survived_female = female_df["Survived"].sum()
        survived_female_percent = (survived_female / total_female) * 100

        male_df = self.df[self.df["Sex"] == 'male']
        total_male = len(male_df)
        survived_male = male_df["Survived"].sum()
        survived_male_percent = (survived_male / total_male) * 100

        Pclass1_df = self.df[self.df["Pclass"] == 1]
        total_Pclass1 = len(Pclass1_df)
        survived_Pclass1 = Pclass1_df["Survived"].sum()
        survived_Pclass1_percent = (survived_Pclass1 / total_Pclass1) * 100

        Pclass2_df = self.df[self.df["Pclass"] == 2]
        total_Pclass2 = len(Pclass2_df)
        survived_Pclass2 = Pclass2_df["Survived"].sum()
        survived_Pclass2_percent = (survived_Pclass2 / total_Pclass2) * 100

        Pclass3_df = self.df[self.df["Pclass"] == 3]
        total_Pclass3 = len(Pclass3_df)
        survived_Pclass3 = Pclass3_df["Survived"].sum()
        survived_Pclass3_percent = (survived_Pclass3 / total_Pclass3) * 100

        report = f"""=======================================
TITANIC SURVIVAL ANALYSIS REPORT
=======================================
[INFO] Data loaded successfully.
[INFO] Data cleaned and features engineered.

--- OVERALL STATS ---
Total Passengers: {total_passengers}
Overall Survival Rate: {survived_percent:.2f}%

--- GENDER ANALYSIS ---
Female Survival Rate: {survived_female_percent:.2f}%
Male Survival Rate: {survived_male_percent:.2f}%

--- CLASS ANALYSIS ---
Class 1 Survival Rate: {survived_Pclass1_percent:.2f}%
Class 2 Survival Rate: {survived_Pclass2_percent:.2f}%
Class 3 Survival Rate: {survived_Pclass3_percent:.2f}%
======================================="""

        print(report)

    def generate_visualizations(self):
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))


        axes[0].hist(self.df['Age'], bins=20, color='lightgrey', edgecolor='black', linewidth=2)
        axes[0].set_xlabel("Age")
        axes[0].set_ylabel("Number of Passengers")
        axes[0].set_title("Passenger Age Distribution")
        axes[0].grid(True, linestyle="--", alpha=0.7)

        classes = ["Class 1", "Class 2", "Class 3"]


        rates = [
            self.df[self.df["Pclass"] == 1]["Survived"].mean() * 100,
            self.df[self.df["Pclass"] == 2]["Survived"].mean() * 100,
            self.df[self.df["Pclass"] == 3]["Survived"].mean() * 100
        ]

        axes[1].bar(classes, rates, color=["#4CAF50", "#FF9800", "#F44336"], edgecolor="black", width=0.6)
        axes[1].set_ylabel("Survival Rate (%)")
        axes[1].set_title("Survival Rate by Passenger Class")
        axes[1].set_ylim(0, 100)

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    analyzer = TitanicAnalyzer("train.csv")

    analyzer.clean_data()
    analyzer.engineer_features()
    analyzer.generate_report()

    analyzer.generate_visualizations()
    print("[INFO] Process complete. Visualizations displayed on screen.")
