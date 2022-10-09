from pathlib import Path
DATA_DIR = Path("C:/Users/kaust/fitbit/data")
Model_DIR = Path("C:/Users/kaust/fitbit/models")

fitbitdailyActivity_merged = DATA_DIR/'fitbitdailyActivity_merged.csv'

fitdailyCalories_merged = DATA_DIR/'fitdailyCalories_merged.csv'
heartrate_seconds_merged = DATA_DIR/'heartrate_seconds_merged.csv'
load_model= Model_DIR/'fitbit_time.hs'