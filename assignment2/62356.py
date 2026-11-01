def split_sentences(text):
    """Split text into sentences while retaining punctuation."""

    sentences = []
    current = ""

    for char in text.strip():
        current += char

        if char in ".!?":
            sentence = current.strip()
            if sentence:
                sentences.append(sentence)
            current = ""

    remaining = current.strip()
    if remaining:
        sentences.append(remaining)

    return sentences
