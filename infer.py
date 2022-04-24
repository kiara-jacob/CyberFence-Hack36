import preprocess
import pandas as pd
import numpy as np
import torch
from tqdm.notebook import tqdm
from torch.utils.data import TensorDataset

from torch.utils.data import DataLoader, SequentialSampler

from transformers import BertTokenizer, BertForSequenceClassification

import warnings
warnings.filterwarnings('ignore')

def make_predictions(model, dataloader_test):

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model.eval()
    
    predictions = []
    
    for batch in dataloader_test:
        
        batch = tuple(b.to(device) for b in batch)
        
        inputs = {'input_ids':      batch[0],
                  'attention_mask': batch[1]
                 }

        with torch.no_grad():        
            outputs = model(**inputs)
            
        logits = outputs[0]
        logits = logits.detach().cpu().numpy()

        predictions.append(logits)
     
    predictions = np.concatenate(predictions, axis=0)
    return predictions

def predict(type):

    model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                      num_labels=2,
                                                      output_attentions=False,
                                                      output_hidden_states=False)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    if type == 'hatespeech':
        data = pd.read_csv('./data/hatespeech.csv', index_col = 0)
        label_dict = {1:'No Hate Speech', 0:'Hate Speech'}
        model.load_state_dict(torch.load('./models/finetuned_BERT_hatespeech.model', map_location=torch.device('cpu')))

    else:
        data = pd.read_csv('./data/bullying.csv', index_col = 0)
        label_dict = {1 :'Bullying', 0 : 'Non-Bullying'}
        model.load_state_dict(torch.load('./models/finetuned_BERT_bullying.model', map_location=torch.device('cpu')))

    data = preprocess.preprocessing(data)

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', 
                                          do_lower_case=True)  
    
    encoded_data_test = tokenizer.batch_encode_plus(
        data['tweet_text'].values, 
        add_special_tokens=True, 
        return_attention_mask=True, 
        pad_to_max_length=True, 
        max_length=256, 
        return_tensors='pt'
    )

    input_ids_test = encoded_data_test['input_ids']

    attention_masks_test = encoded_data_test['attention_mask']

    dataset_test = TensorDataset(input_ids_test, attention_masks_test)

    dataloader_test = DataLoader(dataset_test, 
                                    sampler=SequentialSampler(dataset_test), 
                                    batch_size=8)

    predictions = make_predictions(model, dataloader_test)
    predictions = np.argmax(predictions, axis = 1)
    predictions = predictions.tolist()
    data['Label'] = predictions
    data['Label'] = data['Label'].replace(label_dict)

    return data

    
