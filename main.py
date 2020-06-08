# import sys
import random


def get_alphas_and_non_alphas(word):

    alphas = []
    non_alphas = []

    for num, char in enumerate(word, start=0):
        if char.isalpha():
            alphas.append(char)
        else:
            non_alphas.append((num, char,))

    return (alphas, non_alphas)


def mix_characters_in_word(word):
    """ Mixis all but first and last character in a word"""

    alphas_from_non_alphas = get_alphas_and_non_alphas(word)
    alphas_only = alphas_from_non_alphas[0]
    non_alphas = alphas_from_non_alphas[1]

    # if string is shorter than 4 characters do nothing
    if len(alphas_only) < 3:
        return word

    # get first and last character
    fc = alphas_only[0]
    lc = alphas_only[-1]

    # get the string without head and tail
    mix_char_list = list(alphas_only[1: len(alphas_only)-1])
    # randomize the middle string
    mix_char_list = random.sample(mix_char_list, len(mix_char_list))
    # add first character to beginning of string
    mix_char_list.insert(0, fc)
    # add final character to end of string
    mix_char_list.append(lc)
    # place non alpha charactert to their position in list
    [mix_char_list.insert(element[0], element[1]) for element in non_alphas]
    # return the mixed string
    return "".join(mix_char_list)


def main():
    if __name__ == "__main__":
        sentence = """The Coachella Valley Music and Arts Festival (commonly called Coachella or the Coachella Festival) is an annual music 
                and arts festival held at the Empire Polo Club in Indio, California, in the Coachella Valley in the Colorado Desert. 
                It was co-founded by Paul Tollett and Rick Van Santen in 1999, and is organized by Goldenvoice, a subsidiary of AEG Presents.[1] 
                The event features musical artists from many genres of music, including rock, pop, indie, hip hop and electronic dance music,
                as well as art installations and sculptures. Across the grounds, several stages continuously host live music."""
        jibberish = []
        [jibberish.append(mix_characters_in_word(word))
         for word in sentence.split()]

        print(" ".join(jibberish))


main()
