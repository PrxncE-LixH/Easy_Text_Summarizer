
# Text Summarization with Pegasus

This project focuses on text summarization using the Google Pegasus model, fine-tuned on the SAMSum dataset. The SAMSum dataset consists of a variety of conversational data and corresponding summaries, making it ideal for summarizing chat and dialogue-based text. With the help Pegasus, the resultant model is able generate concise and coherent summaries of dialogues, preserving the essential information and context.

## Demo
```
https://firebasestorage.googleapis.com/v0/b/tomatoguard-2110e.appspot.com/o/Recording%20summarizer.mp4?alt=media&token=abd09c8f-a564-4d5a-8423-3bff83990222
```

![image](https://firebasestorage.googleapis.com/v0/b/tomatoguard-2110e.appspot.com/o/Screenshot%20II.png?alt=media&token=f7f095ec-fa60-4808-98aa-d32d672a744a)





## License


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Authors

- [PrxncE-LixH](https://github.com/PrxncE-LixH)


## Build for yourself
```
cd root directory
```
 - Install required packages
   ``` 
   pip install -r requirements.txt
   ```

 - Train the model
   - Training params [model trainer](https://github.com/PrxncE-LixH/Text_Summarizer_HF_Pegasus/blob/main/src/text_summarizer/components/model_trainer.py)
   ```
   python .\main.py
   ```
  
 - Run the model
   ```
   streamlit run .\homepage.py
   ```
## Additional Information 

- The  SAMSum dataset used for the training can be found at     https://huggingface.co/datasets/Samsung/samsum
- Initial training took about 45mins, and was completed with a 7900XTX graphics card with ROCM enabled. It trained for 3 epochs and was represented in fractional parts. 
- To add more context to the generated summary, modify the length penalty in the summary params in the [homepage.py](homepage.py)


