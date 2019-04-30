import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
tag_dict = {
    "mashable.com":'section',
    "www.wired.com":'article',
    "www.digitaltrends.com":'article',
    "www.rockpapershotgun.com":'article',
    "www.fastcompany.com":'article',
    "www.thisisinsider.com":'section',
    "variety.com":'article',
    "digiday.com":"article",
    "www.fool.com":'section'
    #"www.businessinsider.com":"section"
}
class_dict = {
    'www.theverge.com':['c-entry-content'],
    'techcrunch.com':['article-content'],
    "www.nytimes.com":["StoryBodyCompanionColumn"],
    "www.bbc.co.uk":["story-body__inner","vxp-media__summary"],
    "www.nextbigfuture.com":["thecontent"],
    "www.engadget.com":["article-text"],
    "mashable.com":['article-content'],
    "gizmodo.com":['post-content'],
    "www.reuters.com":['StandardArticleBody_body'],
    "www.cnet.com":['article-main-body'],
    "venturebeat.com":['article-content'],
    "www.androidcentral.com":['article-body'],
    "makezine.com":['article-body'],
    "www.businessinsider.com":['slide-module',"col-12","news-content","collapse-container"], #'slide-module',"col-12","news-content",
    "arstechnica.com":['article-content'],
    "www.wired.com":['article-body'],
    "hackaday.com":['entry-content'],
    "news.yahoo.com":["body"],
    "thenextweb.com":['c-post-content','post-body'],
    "hardware.slashdot.org":['article'],
    "lifehacker.com":['post-content'],
    "www.digitaltrends.com":['m-content'],
    "reindernijhoff.net":['entry-content'],
    "www.entrepreneur.com":['art-v2-body'],
    "www.anandtech.com":['articleContent'],
    "www.nvidia.com":['body-text description'],
    "www.rockpapershotgun.com":['article'],
    "www.marketwatch.com":['article-body'],
    "www.diyphotography.net":['entry-content'],
    "www.windowscentral.com":['article-body__section--narrow narrow'],
    "androidcommunity.com":['td-post-content'],
    'www.theregister.co.uk':['body'],
    "www.thehansindia.com":['story_content'],
    "blog.hubspot.com":['post-content'],
    "markets.businessinsider.com":['news-content'],
    "www.fastcompany.com":['post__article'],
    "www.thisisinsider.com":['post-content'],
    "www.makeuseof.com":['single-post-content'],
    "hypebeast.com":['post-body-content'],
    "www.recode.net":['c-entry-content'],
    "www.androidpolice.com":['post-content'],
    "www.gamasutra.com":['page_data_1'],
    "adage.com":['article-copy'],
    "www.telegraph.co.uk":['article-body-text component'],
    "www.xda-developers.com":['entry_content'],
    "variety.com":['c-content'],
    "bgr.com":['entry-content'],
    "pjmedia.com":['pages'],
    "japantoday.com":['text-large mb'],
    "news.trust.org":['body-text'],
    "www.orilliamatters.com":['details-body'],
    "digiday.com":[""],
    "www.fool.com":["article-body"],
    "boingboing.net":['story'],
    "fashionista.com":['m-detail--body'],
    "www.knoxnews.com":['truncationWrap'],
    "www.gadgetsnow.com":['article-txt'],
    "www.slashgear.com":['content'],
    "indianexpress.com":['o-story-content__main'],
    'finance.yahoo.com':['canvas-body'],
    "ca.finance.yahoo.com":['body'],
    "ca.sports.yahoo.com":['caas-body'],
    "sg.finance.yahoo.com":['body'],
    "www.yahoo.com":['body'],
    "sports.yahoo.com":['caas-body']

}
key_word = {'BA':'Boeing','FB':'Facebook','TSLA':'Tesla','NFLX':'Netflix'}
def parse_url_file(filename,key):
    df = pd.read_csv(filename)
    urls = df.iloc[:,2].values
    title = df.iloc[:,1].values
    dates =df.iloc[:,0].values
    d,u,contents,t,p = parse_all_urls(title,urls,dates,key)
    return d, u, contents, t,p


def parse_all_urls(t,urls,d,key):
    contents = []
    i = 0
    dates = []
    titles = []
    first_para = []
    for url in urls:
        #url = "https://www.businessinsider.com/tesla-model-y-design-and-specs-details-2019-3"
        sources = url.split("/")
        if sources[2] not in class_dict:
            print(d[i],'rare website:',url)
            continue
        sources = sources[2]
        con, p = parse_url(sources, url,key)
        if con == "":
            print(d[i])
            continue
        res = t[i] + "\n" + con
        contents.append(res)
        dates.append(d[i])
        titles.append(t[i])
        first_para.append(p)
        i+=1
        if i % 20 == 0:
            print("Have parsed %d urls" %i)
    return dates,urls,contents,titles,first_para


def parse_url(sources, url,key):
    # Make the request to a url
    r = requests.get(url)
    if r.status_code != 200:
        print("not access:",url)
        return "", ""
    # Create soup from content of request
    c = r.content

    soup = BeautifulSoup(c, "html.parser")
    main_content = []
    tag = tag_dict[sources] if sources in tag_dict else 'div'
    # Find the element on the webpage
    if sources in ['www.marketwatch.com','www.theregister.co.uk',"boingboing.net"]:
        main_content = soup.find_all(tag, id = re.compile(".*" + class_dict[sources][0] + ".*"))
    elif sources in ['digiday.com']:
        main_content = soup.find_all ( tag )
    else:
        for classname in class_dict[sources]:
            main_content = soup.find_all (tag, class_=re.compile ( ".*" + classname + ".*" ) )
            if len(main_content) > 0:
                break
    if len(main_content) == 0:
        print("cannot find class:",url)
        return "",""
    # Init
    content = ""

    # Extract content
    if sources in ['www.engadget.com','www.windowscentral.com','www.businessinsider.com','news.yahoo.com','ca.finance.yahoo.com','www.yahoo.com','sg.finance.yahoo.com']:
        paragraphs = []
        for each in main_content:
            paragraphs.extend(each.find_all('p'))
    else:
        paragraphs = main_content[0].find_all('p')

    if not paragraphs:
        print("no paragraph:", url)
        return "",""
    isFound = False
    first_para = ""
    for p in paragraphs:
        if p.text and p.text != 'Advertisement':
            if not isFound and key_word[key] in p.text and len(p.text) > 5:
                first_para = p.text
                isFound = True
            content += (p.text + " ")
    if first_para == "":
        for p in paragraphs:
            if len(p.text) > 5:
                first_para = p.text
                break
    if first_para == "":
        print("no first paragraph:",url)
        return "",""
    return content, first_para

def main():
    # Parse file
    file_list = os.listdir('Prediction')
    for f in file_list:
        #f = 'BA_yahoo.com_urls.csv'
        if f == ".DS_Store":
            continue
        key_word = f.split('_')[0]
        dates,urls,contents,titles,first_para = parse_url_file("Prediction/"+ f,key_word)
        articles = contents

        sid = SentimentIntensityAnalyzer()
        final_data = {}
        for i in range(len(articles)):
            sentences = []
            sentences_p = []
            lines_list = tokenize.sent_tokenize(articles[i])
            lines_list_p = tokenize.sent_tokenize(first_para[i])
            sentences.extend(lines_list)
            sentences_p.extend(lines_list_p)

            scores = {}
            scores['pos'] = 0
            scores['neg'] = 0
            scores['neu'] = 0
            scores['compound'] = 0
            p_scores = {}
            p_scores['pos'] = 0
            p_scores['neg'] = 0
            p_scores['neu'] = 0
            p_scores['compound'] = 0
            t_scores = sid.polarity_scores(titles[i])


            for sentence in sentences_p:
                ss = sid.polarity_scores(sentence)

                p_scores['pos'] += ss['pos']
                p_scores['neg'] += ss['neg']
                p_scores['neu'] += ss['neu']
                p_scores['compound'] += ss['compound']
            for k in sorted(p_scores):
                if len(sentences_p) == 0:
                    p_scores[k] = 0.0
                else:
                    p_scores[k] /= len(sentences_p)


            for sentence in sentences:
                ss = sid.polarity_scores(sentence)

                scores['pos'] += ss['pos']
                scores['neg'] += ss['neg']
                scores['neu'] += ss['neu']
                scores['compound'] += ss['compound']

            for k in sorted(scores):
                scores[k] /= len(sentences)

            final_data['dates'] = final_data.get('dates',[])+[dates[i]]
            final_data['url'] = final_data.get("url",[])+ [urls[i]]
            final_data['title'] = final_data.get ( 'title', [] ) + [titles[i]]
            final_data['title_score'] = final_data.get('title_score',[]) + [t_scores['compound']]
            final_data['first_para'] = final_data.get('first_para',[]) + [first_para[i]]
            final_data['firstP_score'] = final_data.get('firstP_score',[]) + [p_scores['compound']]
            final_data['content_scores'] = final_data.get('content_scores', []) + [scores['compound']]
        data = pd.DataFrame.from_dict(final_data)
        data.to_csv('Prediction/'+ f ,index=False)
        print('finish with',f)
if __name__ == '__main__':
    main()