#funnybot

This is an attempt to create a funny bot trained on a corpus of jokes. The goal of the project is to draw samples from a character level LSTM model, which should actually be funny. 

Read my [blog post](https://abhinavmoudgil95.github.io/2017-03-01/funnybot/) for detailed analysis and results. 

## Datasets

* **[Short Jokes](https://www.kaggle.com/abhinavmoudgil95/short-jokes)**: It contains 231,657 short jokes and oneliners. For the language model, csv file of the dataset is processed and written to a seperate text file `data/shortjokes.txt` with `utils/csv_to_text.py`. 

* **F.R.I.E.N.D.S**: As a fun task, transcripts of all the episodes of TV Series F.R.I.E.N.D.S are compiled into a single text file of 4.79MB (`/data/friends.txt`) using `utils/friends.py` script. The intent is to generate funny text similar to the dialogues in the series. The script is ad-hoc as of now, so contributions are welcome. 

## Dependencies

* **Python**  - Preprocessing the dataset.
* **Torch** - Language model is written in Torch. 

## Running Model

Navigate to `/src/` folder and run the following commands: 
```bash
python scripts/preprocess.py --input_txt ../data/shortjokes.txt  --output_h5 my_data.h5  --output_json my_data.json
th train.lua -input_h5 my_data.h5 -input_json my_data.json -model_type lstm -num_layers 3 -rnn_size 512
```
This will start the training session of 50 epochs on jokes dataset and checkpoints are saved in `src/cv/` folder every 1000 iterations with names like `cv/checkpoint_1000.t7`. 

To sample data with 2000 characters from the trained checkpoint (say after 3000 iterations), run the following command:

```bash
th sample.lua -checkpoint cv/checkpoint_3000.t7 -length 2000
````

In case of any errors, missing dependencies or more info, refer to [torch-rnn](https://github.com/jcjohnson/torch-rnn). 

## Contributions and TODOs
* Data compiled from `utils/friends.py` contains many extra headers, which were manually removed. It would be great if this task could be automated. 
* It has been attempted to keep the dataset as clean as possible. So, relevant additions to the jokes dataset are welcome. 

