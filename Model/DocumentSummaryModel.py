from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

tokenizer = PreTrainedTokenizerFast.from_pretrained("ainize/kobart-news")
model = BartForConditionalGeneration.from_pretrained("ainize/kobart-news")

def summary(result : list[str]):
    summaryResult = []
    for res in result:
        input_ids = tokenizer.encode(res, return_tensors="pt")
        # Generate Summary Text Ids
        summary_text_ids = model.generate(
            input_ids=input_ids,
            bos_token_id=model.config.bos_token_id,
            eos_token_id=model.config.eos_token_id,
            length_penalty=2.0,
            max_length=142,
            min_length=56,
            num_beams=4,
            no_repeat_ngram_size=2
        )
        # Decoding Text
        summaryResult.append(tokenizer.decode(summary_text_ids[0], skip_special_tokens=True))

    return summaryResult

    # return f"question : {question} 에 대한 챗봇 답변입니다."