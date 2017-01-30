#funnybot

This is an attempt to create a funny bot trained on a corpus of jokes. The goal of the project is to draw samples from a character level LSTM model, which should actually be funny. 

## Datasets

* **Jokes**: Variety of jokes are crawled from online websites using python crawler scripts (can be found at `utils/crawlers/`). Jokes from each website are compiled into a csv file with the format: “serial number, joke” which can be found in the `data/` folder. All these csv files are compiled into one `data/all-jokes.csv` using `utils/combine_data.py` script. Hence the final dataset (`data/all-jokes.csv`) consists of 32728 jokes. For the language model, it is trimmed and written into a separate text file `data/all-jokes.txt` using `utils/csv_to_text.py` script.  

* **F.R.I.E.N.D.S**: As a fun task, transcripts of all the episodes of TV Series F.R.I.E.N.D.S are compiled into a single text file of 4.6MB (`/data/friends.txt`) using `utils/friends.py` script. The intent is to generate funny text similar to the dialogues in the series. The script is ad-hoc as of now, so contributions are welcome. 

## Dependencies

* **Python**  - Crawling websites and preprocessing.
* **Torch** - Language model is written in Torch. 
* **BeautifulSoup** - A Python package for parsing HTML pages.

## Running Model

Navigate to `/src/` folder and run the following commands: 
```bash
python scripts/preprocess.py --input_txt ../data/all-jokes.txt  --output_h5 my_data.h5  --output_json my_data.json
th train.lua -input_h5 my_data.h5 -input_json my_data.json -model_type lstm -num_layers 3 -rnn_size 512
```
This will start the training session of 50 epochs on jokes dataset and checkpoints are saved in `src/cv/` folder every 1000 iterations with names like `cv/checkpoint_1000.t7`. 

To sample data with 2000 characters from the trained checkpoint (say after 3000 iterations), run the following command:

```bash
th sample.lua -checkpoint cv/checkpoint_3000.t7 -length 2000
````

In case of any errors, missing dependencies or more info, refer to [torch-rnn](https://github.com/jcjohnson/torch-rnn). 

## Results

A 3-layer character level LSTM network with 512 hidden units in each layer is trained on the jokes dataset for 24 hours (~30 epochs and 109000 iterations) with NVIDIA Tesla K40 GPU. Samples can be drawn using the trained checkpoint file available at `src/saved_checkpoints/`. 


## Contributions and TODOs
* Data compiled from `utils/friends.py` contains many extra headers, which were [manually removed](https://github.com/abhinavmoudgil95/funnybot/commit/f2e901bb1f597b1966ac4033d447f86fc951e438). It would be great if this task could be automated. 
* It has been attempted to keep the dataset as clean as possible. So, relevant additions to the jokes dataset are welcome. 
* Currently results are sampled using a 3 hidden layer LSTM network with 512 hidden units in each layer. However, if there exists a more optimal model that generates better results, please feel free to report or send a pull request.

