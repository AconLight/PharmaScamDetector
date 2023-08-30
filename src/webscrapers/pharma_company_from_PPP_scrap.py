from src.webscrapers.utils.website_link_tree_scraper import website_link_tree_scrapper


def pharma_company_from_PPP_scrap(web_link, pharma_company_data_objects, link_filter_matches, depth=2):
    website_contents, next_page_links = website_link_tree_scrapper(web_link, web_link)
    found_pharma_company_data_objects = set()

    for times in range(depth-1):
        new_next_page_links = []
        next_page_links = list(filter(lambda link: any([match in link for match in link_filter_matches]), next_page_links))
        for next_page_link in next_page_links:
            temp_website_contents, temp_next_page_links = website_link_tree_scrapper(web_link, next_page_link)
            new_next_page_links += temp_next_page_links
            for temp_website_content in temp_website_contents:
                text = temp_website_content.lower()
                for pharma_company_data_object in pharma_company_data_objects:
                    for company_name_phrase in pharma_company_data_object.data_dict['company_name_phrases']:
                        if company_name_phrase in text:
                            found_pharma_company_data_objects.add(pharma_company_data_object)
                            break

        next_page_links = new_next_page_links

    return list(found_pharma_company_data_objects)
