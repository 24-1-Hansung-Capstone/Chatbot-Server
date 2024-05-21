from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

tokenizer = PreTrainedTokenizerFast.from_pretrained("ainize/kobart-news")
model = BartForConditionalGeneration.from_pretrained("ainize/kobart-news")

def summary(result : str):
    summaryResult = ""

    result = result[:1024]
    input_ids = tokenizer.encode(result, return_tensors="pt")
    # Generate Summary Text Ids
    summary_text_ids = model.generate(
        input_ids=input_ids,
        bos_token_id=model.config.bos_token_id,
        eos_token_id=model.config.eos_token_id,
        length_penalty=2.0,
        max_length=100,
        min_length=30,
        num_beams=4,
        no_repeat_ngram_size=2
    )
    # Decoding Text
    summaryResult = (tokenizer.decode(summary_text_ids[0], skip_special_tokens=True))
    return summaryResult