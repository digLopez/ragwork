from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter

chunk_size = 100
chunk_overlap = 20

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap)

c_splitter = CharacterTextSplitter(
    separator=' ', chunk_size=chunk_size, chunk_overlap=chunk_overlap)


if __name__ == '__main__':
    text = ("hello world, how about you? thanks, I am fine.  the machine learning class. "
            "So what I wanna do today is just spend a little time going over the logistics of the class, "
            "and then we'll start to talk a bit about machine learning")
    # s = r_splitter.split_text(text)
    s = c_splitter.split_text(text)
    print(type(s))
    print(len(s))
    for item in s:
        print(item)
