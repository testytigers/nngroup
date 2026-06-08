# Deferred Hypertext: The Virtues of Delayed Gratification - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">Deferred Hypertext: The Virtues of Delayed Gratification</h1>

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

September 29, 2001

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2001-09-29</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Deferred Hypertext: The Virtues of Delayed Gratification&amp;body=https://www.nngroup.com/articles/deferred-hypertext-the-virtues-of-delayed-gratification/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/deferred-hypertext-the-virtues-of-delayed-gratification/&amp;title=Deferred Hypertext: The Virtues of Delayed Gratification&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/deferred-hypertext-the-virtues-of-delayed-gratification/&amp;text=Deferred Hypertext: The Virtues of Delayed Gratification&amp;via=nngroup" data-share-type="Twitter">

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

</span>Navigating a full browsing session to find information can be unpleasant and slow, particularly on mobile devices. Instead, issue a deferred request and have the information arrive later, as done by some SMS systems.

</div>

<div class="article-body">

<p>Although users typically click a link and expect an immediate response, this scenario is not always convenient. Several systems now use hypertext links that do not generate an immediate page view, but instead defer the results.</p>

<p>Users might prefer deferred hypertext when they have:</p>

<ul>

<li><strong>Bad user interfaces </strong> that prevent efficient user interactions. With deferred hypertext, users submit simple requests for a single, well-defined unit of information rather than interacting with complicated screens and forms.</li>

<li><strong>Bad displays </strong> that make in-depth reading unpleasant. By deferring hypertext in this scenario, users can read the full text at a later time on a better display.</li>

</ul>

<p>Currently, most deferred hypertext systems work through e-mail to compensate for the bad browsing interfaces on existing mobile devices. However, I also expect an increase in services to support bad displays and lack of reading time.</p>

<p>For example, readers browsing on mobile devices might find it especially valuable to mark certain articles or websites and have them show up later on full-screen displays at the office or at home. Another application might let users issue a deferred request for an article and have it automatically print out on the office computer so that it's waiting for them when they arrive. These are just a few ideas that indicate the need for tighter integration between low-end, mobile computing and stationary computing devices.</p>

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

<a class="ga-article-toc-item" href="#toc-the-sms-solution-1">The SMS Solution</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-usability-issues-2">Usability Issues</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-deferred-or-half-dead-3">Deferred or Half Dead?</a>

</li>

</ul>

</div>

</div><h2 id="toc-the-sms-solution-1">The SMS Solution</h2>

<p>Deferred hypertext is currently very popular among mobile phone users in Europe. Given that it is so <a class="old" href="http://www.nngroup.com/reports/wap/" title="Nielsen Norman Group: WAP usability report"> painful to navigate through WAP screens </a> to find information interactively, most users prefer instead to <strong> send an SMS message </strong> and have the answer returned in a subsequent message. (SMS is short emails sent to and from cell phones.)</p>

<p>Say, for example, that you are in Zurich and need departure times for trains to Geneva. Using SMS, you can send a train information service a message consisting of the word "Geneva." The service then sends you a reply listing the next several trains departing for that city. The system assumes several things to reduce your typing burden: that you want only a few departure times, that you want them for the next few trains, and that you want only trains departing from Zurich (although I've only used this service in Zurich, I assume other big cities provide it as well).</p>

<p>Blackberry offers similar services, many of which let users interact with complex corporate databases and sales automation systems.</p>

<h2 id="toc-usability-issues-2">Usability Issues</h2>

<p>SMS information retrieval has no user interface in the modern sense, since all the user can do is type out a command and send it off. Of course, a command language <em> is </em> a user interface in its own right; SMS interactions are very similar to batch processing computers that used punch card commands in the 1950s.</p>

<p>There are four basic usability guidelines for dealing with SMS and other email-style commands.</p>

<ul>

<li><strong>Offer great flexibility in command recognition. </strong> There is nothing more annoying than getting a "command not recognized" response in a batch processing system, where turn taking between human and computer is very slow. To achieve this flexibility:

<ul>

<li>recognize both noun-verb syntax and verb-noun syntax for all commands,</li>

<li>allow for as many synonyms as possible, and</li>

<li>correct typos using a spelling checker.</li>

</ul>

</li>

<li><strong>Support abbreviations, but also support full commands. </strong> One of the stupidities of Unix was that you had to type <em> ls </em> ; you couldn't type <em> list </em> (which is easier to remember).</li>

<li><strong>Guess where appropriate. </strong> If there is no downside to misinterpreting the user's command, err on the side of wild guessing for correcting typos or interpreting abbreviations. For example, if the user asks for the "Chigaco" weather forecast, just send off the Chicago weather. On the other hand, if the user asks to buy 10,000 shares of a stock symbol that's not in the database, simply buying the closest match is not a good idea.</li>

<li><strong>Return multiple responses when necessary. </strong> If multiple interpretations are possible, it is sometimes better to return responses corresponding to all possibilities rather than asking the user for clarification. If such a response would be too big for easy transmission or reading, send both the best guess and a menu of secondary guesses that the user can choose from.</li>

</ul>

<p>Supporting all the possible ways a user might type a command on a crummy phone keypad sounds like a tall order, but it is eminently possible to support at least 98% of the variations. You can predict many of the alternatives by simply thinking about the problem; you can discover many more in a basic user test. For example, simply ask 10 people to write down how they would query the service in question. Finally, continually review your log files for real-world user inputs. In my experience, you quickly achieve an asymptote of high-recognition performance as you add the ability to handle empirically observed variations.</p>

<h2 id="toc-deferred-or-half-dead-3">Deferred or Half Dead?</h2>

<p>In my 1995 <a class="old" href="http://www.nngroup.com/books/multimedia-and-hypertext/" title="Jakob Nielsen: 'Multimedia and Hypertext: The Internet and Beyond'"> book on the theory behind the Web </a> , I used the term "half-dead hypertext" to differentiate deferred links from both <strong> live links </strong> and completely <strong> dead links </strong> (inactive references). A half-dead link indicated that manual user labor was required. For example, if I wrote the title of my book above, but provided no link, the user would have to go to a bookstore site or the local library to find it. Although offering the title is better than offering no reference at all, the half-dead link offers no possibility for live and immediate computer interaction, and thus I called it "half-dead."</p>

<p>The live vs. dead metaphor does have some value, even if the terminology never caught on. However, I now prefer the term "deferred hypertext" over "half-dead hypertext." The new term does raise an important question, however: Deferred for how long?</p>

<p>Even though deferred hypertext is not a live interaction, the length of delay in delivery impacts the service's usefulness. Given too long a delay, users might forget the request altogether, requiring that the response either reestablish context or render itself meaningless. At that point, the information is likely to be more dead than deferred.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet,timing</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

</ul>

</div>

</div>

</div>

</div>