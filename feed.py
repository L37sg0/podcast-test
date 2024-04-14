import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss', {
        'version':'2.0',
        'xmlns:itunes':'https://www.itunes.com/dtds/podcast-1.0.dtg',
        'xmlns:content':'https://purl.org/rss/1.0/modules/content'
    })

    channel_element = xml_tree.SubElement(rss_element, 'channel')

    link_prefix = yaml_data['link']
    for k in yaml_data:
        
        match k:
            case 'author':
                element_title = 'itunes:author'
                break
            case 'image':
                element_title = 'itunes:image'
                break
            case default:
                element_title = k

        if k == 'item':
            for x in yaml_data[k]:
                item_element = xml_tree.SubElement(channel_element, 'item')
                item_data = x
                for y in item_data:
                    xml_tree.SubElement(item_element, y).text = item_data[y]
        else:
            xml_tree.SubElement(channel_element, element_title).text = yaml_data[k]

output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast', encoding='UTF-8', xml_declaration=True)