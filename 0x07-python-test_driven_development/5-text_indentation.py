def text_indentation(text):
    """
    Print text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    # Split the text into sentences using '.', '?', and ':'
    sentences = [sentence.strip() for sentence in text.split('.') + text.split('?') + text.split(':')]

    # Filter out empty sentences
    sentences = [sentence for sentence in sentences if sentence]

    # Print each sentence with 2 new lines
    print("\n\n".join(sentences))

# Example usage:
# text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
# Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
# Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
# Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
# Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
# rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
# stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
# cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
# beatiorem! Iam ruinas videres""")

