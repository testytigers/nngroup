# 7 Ways to Improve Your Website’s or Intranet’s Built-In Search Engine - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">8</span>

<div class="article-header">

<h1 class="article-h1">7 Ways to Improve Your Website’s or Intranet’s Built-In Search Engine</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Page Laubheimer</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2022-portrait-page-3.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Page Laubheimer

</span>

<p class="publication-date">

March 13, 2016

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2016-03-13</span>

</p>

</div>

</div>

</div>

<div class="article-share">

<a class="article-share-title ga-share" href="#">

<span class="article-share-icon"></span>

<p class="article-share-label body-medium">Share</p>

</a>

<div class="share-links tooltip">

<div class="tip-arrow"></div>

<ul>

<li class="body-medium">

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: 7 Ways to Improve Your Website’s or Intranet’s Built-In Search Engine&amp;body=https://www.nngroup.com/articles/internal-website-search/" data-share-type="Email">

<svg

width="24"

viewbox="0 0 24 24"

fill="none"

xmlns="http://www.w3.org/2000/svg"

class="icon"

>

<rect x="2.375" y="5" width="19.25" height="14" rx="0.65625" stroke="currentColor" stroke-width="1.3125"/>

<path d="M21.625 6.75L12.4156 14.285C12.1738 14.4828 11.8262 14.4828 11.5844 14.285L2.375 6.75" stroke="currentColor" stroke-width="1.3125"/>

</svg>Email article

</a>

</li>

<li class="body-medium">

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/internal-website-search/&amp;title=7 Ways to Improve Your Website’s or Intranet’s Built-In Search Engine&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/internal-website-search/&amp;text=7 Ways to Improve Your Website’s or Intranet’s Built-In Search Engine&amp;via=nngroup" data-share-type="Twitter">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-x" />

</svg>

Share on Twitter

</a>

</li>

</ul>

</div>

</div>

</div>

<div class="article-container">

<div class="article-content">

<div class="article-summary article-heading-small-light">

<span class="article-summary-label">

Summary:&nbsp;

</span>The accuracy of site search benefits when user queries are altered to allow for user typos or misspelling, vague search terms, and word choice that does not precisely match the terminology on the site.

</div>

<div class="article-body">

<p>Contemporary websites focus on optimization for external search engines like Google, Baidu, and Yandex. While search-engine optimization (SEO) is certainly important for bringing visitors to your website, the quality of the <em>built-in</em> search is often overlooked. Users do engage with the site search to find products, content, and other key assets; failing to provide a good search experience can lose <a href="https://www.nngroup.com/articles/conversion-rates/">conversions</a>, sales, and ultimately customers.</p>

<p>There are a few standard practices that can be used to strengthen your site search. Before discussing them, we define two key information-retrieval terms used for evaluating the performance of a search engine: precision and recall. These can help you better understand the implications and tradeoffs of the techniques below.</p>

<div class="table-of-contents">

<div class="content">

<div class="header">

<div class="toc-header">

<h2 class="toc-title article-heading-small">

In This Article:

</h2>

<span class="expand-icon"></span>

</div>

<a class="current-element" href="#"></a>

</div>

<ul class="toc-items">

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-two-metrics-for-search-performance-precision-and-recall-1">Two Metrics for Search Performance: Precision and Recall</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-7-techniques-for-improving-site-search-2">7 Techniques for Improving Site Search</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-summary-3">Summary</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-references-4">References</a>

</li>

</ul>

</div>

</div><h2 id="toc-two-metrics-for-search-performance-precision-and-recall-1">Two Metrics for Search Performance: Precision and Recall</h2>

<ul>

<li><strong>Precision</strong> is the percentage of <strong>retrieved search results that are relevant</strong>.</li>

<li><strong>Recall</strong> is the <strong>percentage of all relevant results</strong> that the search system actually retrieves<strong>. </strong></li>

</ul>

<p>Imagine that on a recipes website, we have 1000 recipes, of which 300 are for Indian dishes. Assume that when we search for Indian dishes, we get 500 results on the search-results page. Of those 500 search results, only 100 of them are actually Indian dishes; the remainder 400 are actually nonIndian recipes that are not relevant to our search. That means the <strong>precision</strong> is 100/500 or 20%. The <strong>recall</strong> would be 100/300 or 33%, as the search engine only found 100 of the 300 Indian recipes available on the site, which means that 200 Indian recipes didn’t show up on our search-results page at all. A perfect search engine would give us only 300 results total, corresponding to the 300 Indian recipes available on the site, so it would have 300/300 or 100% precision and recall. However, in the real world, that rarely happens. Different techniques that we discuss below trade off precision for recall, or vice versa, so it’s important to understand the conceptual difference.</p>

<p>One of the great insights of the original Google team was that precision is more important than recall for most web searches: there’s so much information available on the Internet that nobody would even <em>want</em> to see all the relevant results. For web-wide search, it’s much more important to focus on high precision: to make sure that all the top 10 hits are as highly relevant as possible to the user’s current problem.</p>

<p>In contrast, for internal searches on a single website or intranet, recall can be quite important. For example, if you search an engineering company’s intranet for information about all suspension bridges the company has consulted on in the past, it would be unfortunate to miss one or two bridges and leave them out of the <em>References</em> section of a new bridge proposal. Or, on an ecommerce site, if a search misses a relevant product, the customer will assume that the site doesn’t carry it and go elsewhere to buy it.</p>

<h2 id="toc-7-techniques-for-improving-site-search-2">7 Techniques for Improving Site Search</h2>

<p> </p>

<p><strong>1. Manually improve results for common queries </strong></p>

<p>Many typical commercial search engines that are available for integration with websites and intranets offer features for manually improving common search queries. In order to make better use of these features, you’ll want to routinely review search logs and evaluate the results returned by your site search to frequent user queries. When your relevance algorithm fails to return items that you consider highly relevant, you can manually indicate those items and surface them to the top of the search-results list for certain queries. However, be cautious about separating the manually promoted items into a “promoted” or “best bets” list when presenting the results, <a href="https://www.nngroup.com/reports/intranet-searching/">as users often ignore these</a>, like they ignore pay-per-click ads on web search engines. Instead, just integrate the manual hits with the search-engine–generated hits and present a single list to the users.</p>

<p><strong>2. Provide curated search suggestions</strong></p>

<p>Search-term suggestion (also called predictive search) refers to displaying suggested queries right below the search box while users are typing. However, an unedited list of common queries from the search logs will not be helpful. Remember, user queries may be misleading, inappropriate, or contain terms that have no results. Instead, suggest <em>curated</em> query terms that retrieve useful results. The suggestions can be based on your search logs or on your content’s descriptive metadata (more on this in our full-day <a href="https://www.nngroup.com/courses/information-architecture/">Information Architecture seminar</a>). It is also critical that you highlight those suggested-query terms that match the input query, so users can easily identify the similarity (if, for example, the typed word appears in the middle of a suggested query).</p>

<figure class="caption"><img alt="Ebay uses bolding to indicate search suggestions" border="0" height="241" loading="lazy" src="https://media.nngroup.com/media/editor/2016/02/03/ebayseachsuggestions.png" width="720"/>

<figcaption><em>Ebay uses bolding to indicate how the user’s typed query relates to the query suggestions.</em></figcaption>

</figure>

<p><span style="line-height: 1.6;">On ecommerce sites the predictive box should also show </span><em style="line-height: 1.6;">product</em><span style="line-height: 1.6;"> </span><em style="line-height: 1.6;">results</em><span style="line-height: 1.6;"> with photos to help users evaluate products quickly. (For more information and additional guidelines for ecommerce search, see our report </span><a href="https://www.nngroup.com/reports/ecommerce-ux-search-including-faceted-search/" style="line-height: 1.6;">Ecommerce User Experience: Search</a><span style="line-height: 1.6;">.)</span></p>

<p>For Intranets, one of the most impactful guidelines that has huge <a href="https://www.nngroup.com/articles/return-on-investment-for-usability">ROI</a> is implementing <a href="https://www.nngroup.com/articles/suggested-employee-search/">employee suggestions for search</a>:  queries that match to employee names show contact information, photos, and links to employee-specific pages as the user types. Presenting employee contact info as a “zero-click” result (where users don’t even have to click on a search result to find the information they seek) can save an enormous amount of employee time, and company money. (For more intranet-specific considerations, see our <a href="https://www.nngroup.com/reports/intranet-searching/">Intranet Search Guidelines Report</a>.)</p>

<p><strong>3. Recognize synonyms and alternative terms</strong></p>

<p>Users often don’t formulate perfect queries. Perhaps they don’t know the appropriate phrases or <a href="https://www.nngroup.com/articles/specialized-words-specialized-audience/">industry jargon</a>, or maybe they don’t know exactly what they’re looking for yet, and start with vague search terms.</p>

<figure class="caption"><img alt="Best Buy's search doesn't allow for synonyms" border="0" height="706" loading="lazy" src="https://media.nngroup.com/media/editor/2016/02/03/bestbuysynonyms.png" width="720"/>

<figcaption><em>Searching BestBuy.com for “soundbar cable” brings up tons of soundbars, but no matches for the actual cable needed to plug a soundbar into a TV. BestBuy’s search engine only accommodates the technical name for that cable, “optical cable”, without assisting users who aren’t AV experts. This lack of flexibility can send users to competitors with a more accommodating site search.</em></figcaption>

</figure>

<p><span style="line-height: 1.6;">Your site search should accommodate realistic user synonyms and alternative terminology, especially if your content is jargon heavy, industry specific, or technical. Remember, your users likely don’t know the carefully crafted lingo that everyone in your office uses on a daily basis. Review your search logs and look for synonyms that you don’t currently have in your content. Then you can create synonym tables in your search engine where user search terms map to existing terminology that returns appropriate results.</span></p>

<p><strong>4. Accommodate variant word forms with stemming</strong></p>

<p>Here’s another common scenario: imagine that you searched for the term “marketing automation” on a website. If the writers had only used terms such as “automated marketing solutions”, your search wouldn’t have any results, even though lots of relevant articles on the site did match your information need (but did not match your exact query). You might assume that the website didn’t have any pertinent content and leave.</p>

<p>This issue could be avoided by using a process called stemming. Stemming <strong>refers to removing endings (like suffixes) from words, and reducing them to their morphological ‘stem.’ </strong>For example, in English, the words <em>reduction</em>, <em>reduce</em>, and <em>reducing</em> would all be stemmed to <em>reduc</em>. If a search engine uses stemming, a search for <em>reduction</em> will also return results containing the word <em>reducing</em>.</p>

<p>Many commercial search products have a stemming feature available (such as the gold-standard <a href="http://tartarus.org/martin/PorterStemmer/">Porter stemmer</a>). By default, this feature is often not enabled; turning it on is easy and thus a low-cost search improvement.</p>

<p>Although stemming will boost recall, it can also lower precision by returning results that are not relevant, but happen to include the stem of a query word. For example, a search for “university” may also return “universal” because the two words share the same stem. Decide whether stemming is right for your site by analyzing search logs and checking how many user search terms are variants of words used on your site.</p>

<p><strong>5.  Handle misspellings gracefully</strong></p>

<p>Typos and misspellings are extraordinarily common, which is why all big search engines offer a form of <em>Did you mean</em> spelling corrections. Although spelling suggestions are recognized as critical, many site-search systems don’t support them. Especially when your content includes a lot of complex jargon (such as on B2B websites), spelling suggestions are key to helping your users find what they need. Oftentimes query suggestions will assist users in adjusting spelling errors <em>while </em>they are typing the query. However, sometimes users will forge ahead with a misspelled query, and you’ll need to gracefully handle the problem on your search-results page by offering a <em>Did you mean</em> link.</p>

<p>If the original query doesn’t have any results, it’s a good practice to also go ahead and automatically retrieve the results for the alternative-spelling suggestion, without requiring the user to click the <em>Did you mean</em> link. Just be sure to make it clear that you retrieved results for a variation of the user’s spelling</p>

<figure class="caption"><img alt="Google indicates when it has shown results for a spelling suggestion " border="0" height="226" loading="lazy" src="https://media.nngroup.com/media/editor/2016/02/03/googlemispellings.png" width="720"/>

<figcaption><em>Google indicates when it has chosen to retrieve an alternative spelling for a user’s query, and gives a clear option to force a search with the original spelling.</em></figcaption>

</figure>

<p><strong style="line-height: 1.6;">6.  Support homophones</strong></p>

<p>Sometimes users may type in a homophone instead of the word they actually mean. (Homophones are words that sound the same, but are spelled differently – such as “peace” and “piece”, or “Stuart” and “Stewart”.) For these situations, a useful tool is Soundex, which is an algorithm used to find similarly sounding words that are spelled differently. Soundex converts search terms (and words from indexed content) into their phonetic representations, and enables your site search to retrieve results that are spelled completely differently from the query words, but are pronounced in the same way. Soundex is widely available and can benefit searches for proper names, jargon terms, foreign words, and more. It’s even built into programming languages like PHP, and into MySQL databases, so it’s relatively easy for your development team to integrate it into the search engine.</p>

<p>Both spelling suggestions and the use of homophones improve the recall, but they can lower precision, by returning results that may not be relevant, but happen to sound like the query word.</p>

<p><strong>7. Ignore stop words</strong></p>

<p>The majority of words that fill out even the best written content on the web are <strong>stop words. </strong>Stop words include function words such as articles (“a”, “the”), prepositions (“of”, “for”), or conjunctions (“but”, “and”), but also other high-frequency words (“be”, “seem”) that appear in most documents and are unlikely to be distinctive for any one of them. These words can negatively affect search relevance.</p>

<p>The easiest way to manage this problem is to have your website’s search engine use a list of excluded <strong>stop words</strong>, ignored in users’ queries. If your search engine doesn’t do a lot of complex language modeling to determine relevance ranking, removing stop words from the users’ queries can have two benefits: (1) it can speed up the search performance, and (2) it can help to suppress irrelevant results that contain these common words. Many stop-word lists are available for most languages, but, before using one, do make sure that it does not include any terms that are uniquely important in your industry or on your website.</p>

<p>Ignoring stop words will boost precision, but lower recall, especially in edge cases like the famous example of “to be or not to be”, which is made <em>entirely of </em>stop words. However, if your search engine already does complex phrase matching and natural-language processing (much like Google does), do <em>not </em>exclude stop words, since those offer additional context that can improve the search results.</p>

<h2 id="toc-summary-3">Summary</h2>

<p>While the major web search engines have grown ever more sophisticated, the built-in search on many websites has been neglected. Stemming, excluding stop words, showing curated query suggestions, and using homophones and spelling suggestions all modify the search query either to  accommodate <a href="https://www.nngroup.com/articles/slips/">user errors</a> or to address possible variations in word choice, and may improve the quality or the number of search results without requiring a major development investment.</p>

<h2 id="toc-references-4">References</h2>

<p>Dan Jurafsky, “Stanford Natural Language Processing: Word Normalization and Stemming” (<a href="https://class.coursera.org/nlp/lecture">link</a>)</p>

<p>W. Bruce Croft, Donald Metzler, Trevor Strohman, <em>Search Engines: Information Retrieval in Practice</em>, Addison-Wesley, 2010.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Information Architecture" href="/courses/information-architecture/?lm=internal-website-search&amp;pt=article">

<h4 class="title heading-small">Information Architecture</h4>

<p id="information-architecture" class="description body-small">

Organize and structure information to improve findability and discoverability

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-interaction" />

</svg>

<p class="ux-specialty interaction-design">Interaction</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Search</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Search</span>

<a class="ga-article-related-topic" href="/topic/search/">Search</a>

</li>

</ul>

</div>

</div>

</div>

</div>