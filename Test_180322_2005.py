import xml.etree.ElementTree as ET
import collections


def read_xml(xml_file, len_words=6, top_words=10):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(xml_file, parser)
    root = tree.getroot()
    words_list = []
    description = root.findall('channel/item/description')
    for item in description:
        words_list.extend(item.text.split())
    words_list = [word for word in words_list if len(word) > len_words]
    counter_words = collections.Counter(words_list)    
    # print(words_list)
    # print(counter_words)
    print(counter_words.most_common(top_words))

if __name__ == '__main__':
    read_xml('test.xml')