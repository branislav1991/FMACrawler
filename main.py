from fma_crawler import FMACrawler
import json

def main():
    fma_crawler = FMACrawler()

    eu_richtlinien = {'url': 'https://www.fma.gv.at/eu/eu-richtlinien/', 'folder': 'eu_richtlinien'}
    eu_verordnungen = {'url': 'https://www.fma.gv.at/eu/eu-verordnungen/', 'folder': 'eu_verordnungen'}
    eba_leitlinien = {'url': 'https://www.fma.gv.at/eu/eba-leitlinien/', 'folder': 'eba_leitlinien'}
    eiopa_leitlinien = {'url': 'https://www.fma.gv.at/eu/eiopa-leitlinien/', 'folder': 'eiopa_leitlinien'}
    esma_leitlinien = {'url': 'https://www.fma.gv.at/eu/esma-leitlinien/', 'folder': 'esma_leitlinien'}
    aufsichtsgesetze = {'url': 'https://www.fma.gv.at/national/gesetze/', 'folder': 'aufsichtsgesetze'}
    fma_verordnungen = {'url': 'https://www.fma.gv.at/national/fma-verordnungen/', 'folder': 'fma_verordnungen'}
    fma_mindeststandards = {'url': 'https://www.fma.gv.at/fma/fma-mindeststandards/', 'folder': 'fma_mindeststandards'}
    fma_rundschreiben = {'url': 'https://www.fma.gv.at/fma/fma-rundschreiben/', 'folder': 'fma_rundschreiben'}
    fma_leitfaeden = {'url': 'https://www.fma.gv.at/fma/fma-leitfaeden/', 'folder': 'fma_leitfaeden'}
    fma_stellungnahmen = {'url': 'https://www.fma.gv.at/fma/fma-stellungnahmen/', 'folder': 'fma_stellungnahmen'}
    fma_konsultationen = {'url': 'https://www.fma.gv.at/fma/fma-konsultationen/', 'folder': 'fma_konsultationen'}

    docs = fma_crawler.crawl_eu_docs(eu_richtlinien['url'])
    no_url = []
    for doc in docs:
        if doc['url'] == '':
            no_url.append(doc['filename'])
        else:
            fma_crawler.download_doc(doc, eu_richtlinien['folder'])
    with open('no_url_eu_richtlinien.json', 'w') as fp:
        json.dump(no_url, fp)

    docs = fma_crawler.crawl_eu_docs(eu_verordnungen['url'])
    no_url = []
    for doc in docs:
        if doc['url'] == '':
            no_url.append(doc['filename'])
        else:
            fma_crawler.download_doc(doc, eu_verordnungen['folder'])
    with open('no_url_eu_verordnungen.json', 'w') as fp:
        json.dump(no_url, fp)

if __name__ == '__main__':
    main()