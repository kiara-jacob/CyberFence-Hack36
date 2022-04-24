import infer
import pandas as pd

def final_predictions(type):

    data = infer.predict(type)

    if type == 'hatespeech':
        data = data[data['Label'] == 'Hate Speech']
    else:
        data = data[data['Label'] == 'Bullying']

    final_df = pd.DataFrame()

    final_df['created_at'] = data['created_at']
    final_df['username'] = data['username']
    final_df['tweet'] = data['tweet']

    
    value_counts = final_df['username'].value_counts(dropna=True, sort=True)
    value_df = pd.DataFrame(value_counts)
    value_df.reset_index(drop = True, inplace=True)
    value_df.columns = ['username', 'counts']

    return final_df, value_df

if __name__ == "__main__":
    final_predictions("hatespeech")
    print("Script Sucessful")

