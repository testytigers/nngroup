# The Reputation Manager - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">The Reputation Manager</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Jakob Nielsen</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Jakob-Nielsen-tie-800x800.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/jakob-nielsen/">

Jakob Nielsen</a></span>

<p class="publication-date">

February 7, 1998

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1998-02-07</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: The Reputation Manager&amp;body=https://www.nngroup.com/articles/the-reputation-manager/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/the-reputation-manager/&amp;title=The Reputation Manager&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/the-reputation-manager/&amp;text=The Reputation Manager&amp;via=nngroup" data-share-type="Twitter">

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

<div class="article-body">

<p>There are two ways for users to know which of the two million websites to visit:</p>

<ul>

<li><strong>Brand</strong>: the user knows that a site usually provides certain qualities; if the user likes these qualities, then it will probably be worth visiting more pages on that site</li>

<li><strong>Reputation</strong>: the user follows the advice of <em> other </em> users who know that a site has quality</li>

</ul>

<p>Branding is the focus of most current Web projects: the theory is that building a powerful brand while the Web is still relatively small will allow a site to be profitable when the Web gets larger. A example of a good Web brand is <strong> news.com</strong>: when you want to know what's happening in the information industry, you will usually be able to find recent news at news.com.</p>

<p>Even though brands work well for a few, large sites, they are not a good mechanism to help users handle millions of sites. On the contrary, the nature of the Web encourages the formation of many smaller sites, and most of its <a class="old" href="/articles/do-websites-have-increasing-returns/" title="Alertbox Apr. 1997: the Web follows a Zipf distribution"> value comes from such specialized sites</a>. Thus, the Web needs a mechanism for making sense of <strong> overwhelming diversity </strong> .</p>

<p>Since there is no way for computers to automatically measure quality, we have to rely on human judgment for Web quality ratings. The reputation manager is a way to automate the processing of such human judgments; not a way to make the judgments themselves. In other words, <strong> quality needs to become an explicit attribute </strong> of Web objects.</p>

<p>My vision for a reputation manager involves the coordination of billions of individual quality judgments by hundreds of millions of users. Every time you encounter an information source on the Internet, your Web client software will present you with an opportunity to vote on its quality. Typically, this would be done by adding two buttons to the interface: a <strong> thumbs-up </strong> button and a <strong> thumbs-down </strong> button. A neutral rating would be given by <em> doing nothing </em> (since we want to minimize overhead in the user interface), but when a user encounters something particularly good, he or she would hit the "good" button. Similarly, disappointing services would be punished by a click on "bad."</p>

<p>The simplest reputation manager would compute the average rating for each information source, but more advanced services would use ideas from <a class="out" href="http://sims.berkeley.edu/resources/collab/" title="Univ. Calif. Berkeley: overview of collaborative filtering research and projects"> collaborative filtering</a> and compute different ratings for different users. Basically, the reputation manager would find <strong> other users whose tastes are very similar to your own </strong> and give added weight to these users' ratings. Since the Web will have half a billion users in five years, it will always be possible to find other users who match your interests, no matter how obscure they are. Thus, the reputation manager can deal differently with people who love the Spice Girls and people who don't.</p>

<p>The reputation manager will collect ratings for entire websites, for individual pages, and for people who contribute comments to discussion groups or chat rooms. The resulting reputation can be used to direct users to sites that will be helpful or interesting, and it can be used to filter out the less valuable contributors in chat rooms and online discussions. In this way, the reputation manager becomes a more powerful version of the <strong> bozo filter </strong> .</p>

<p>Reputation management will be especially valuable when combined with <a class="old" href="/articles/the-case-for-micropayments/" title="Alertbox Jan. 1998: why micropayments are needed for good Web content"> micro-payments</a>: once you have to pay for clicks, you will be motivated to find out <em> in advance </em> whether the destination website is any good.</p>

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

<a class="ga-article-toc-item" href="#toc-implementing-reputation-on-the-web-1">Implementing Reputation on the Web</a>

</li>

</ul>

</div>

</div><h2 id="toc-implementing-reputation-on-the-web-1">Implementing Reputation on the Web</h2>

<p>Initially, I expect reputation managers to become embedded in proxy servers for large corporations and offered as a value-added service by larger Internet Service Providers. In both cases, it is possible to collect data about the behavior of a large number of users at a single point. In about three years reputation management will become an Internet-wide service that users can subscribe to by paying a small micro-payment for each recommendation.</p>

<p>There is already an independent reputation manager available on the Internet: Alexa —  which unfortunately is a browser add-on and thus not fully integrated with the user's Web client software (of course, right now, browsers serve as a weak type of Web access clients). [Note 2020: the "Alexa" referred to here was a website ranking service, not Amazon's much later voice assistant by the same name.] The most relevant features of Alexa relative to this column are:</p>

<ul>

<li><strong>Reputation statistics </strong> for most sites on the Web showing how frequently they are visited and how popular they are. <!--For example, &lt;A HREF="http://widener.alexa.com/sitedata/www.useit.com" TITLE="Alexa Internet's summary of useit.com's reputation"&gt;Alexa's page about www.useit.com&lt;/A&gt; shows how many of Alexa's users like my site and how many don't like it.--></li>

<li><strong>Recommendation links </strong> to good other sites that are related to the current page.</li>

</ul>

<p>Even without any fancy statistics, <strong> most websites could benefit from explicit use of quality ratings </strong> in their interface. A simple logfile analysis will show you what parts of your site are the most popular, and it would be reasonable to give these pages special prominence in search results and in listings. For example, my own <a href="./"> list of old Alertbox columns</a> highlights those columns that have attracted the largest readership in the past. Doing so prevents new readers from being overwhelmed by choices and allows them to focus on the links that are most likely to be of interest. A site with an even larger set of old material could provide a single <a href="http://www.scripting.com/davenet/best.html" title="DaveNet's list of best columns since 1994"> page listing nothing but its top hits</a>.</p>

<p>I have posted <a class="new" href="/articles/readers-comments-on-the-reputation-manager/" title="Sidebar: readers' comments"> several reader comments</a>, including a suggestion to use a user's bookmarks as an initial set of positive votes and a warning against an oligopoly of rating services.</p>

<p>See also: <a href="/articles/reputation-managers-are-happening/" title="Alertbox Sept. 1999"> Reputation managers are <strong> happening</strong></a> (this topic revisited 1.5 years later).</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Persuasive Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Persuasive Design</span>

<a class="ga-article-related-topic" href="/topic/persuasive-design/">Persuasive Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>