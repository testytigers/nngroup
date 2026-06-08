# Designing Web Ads Using Click-Through Data - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Designing Web Ads Using Click-Through Data</h1>

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

September 1, 2001

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2001-09-01</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Designing Web Ads Using Click-Through Data&amp;body=https://www.nngroup.com/articles/designing-web-ads-using-click-through-data/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/designing-web-ads-using-click-through-data/&amp;title=Designing Web Ads Using Click-Through Data&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/designing-web-ads-using-click-through-data/&amp;text=Designing Web Ads Using Click-Through Data&amp;via=nngroup" data-share-type="Twitter">

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

</span>Search engine ads are one type of Web advertising that can actually work. To create the best ads, do quick experiments and redesign ads based on usability principles for online writing. Doing so helped us increase ad click-through by 55% to 310%.

</div>

<div class="article-body">

<p>I recently found myself making two purchases after clicking through advertisements on Google. Given that I've been saying for four years that <a class="old" href="/articles/why-advertising-doesnt-work-on-the-web/" title="Alertbox Sept. 1997: Why advertising doesn't work on the Web"> advertising on the Web doesn't work</a>, this might seem like a contradiction.</p>

<p>However, I have always maintained that <strong> search engines are the exception to the Web advertising rule</strong>. There are two reasons for this:</p>

<ul>

<li>Search engines are the only type of site that users visit with the explicit intention of finding somewhere else to go as quickly as possible.</li>

<li>Because they know what users are looking for, search engines can target ads to a user's current navigation goals. Displaying an ad for something that the user immediately wants is much more powerful than targeting ads based on general user profiling and demographics.</li>

</ul>

<p>Google's ads are even better: <strong> Because the ads are <a class="new" href="/articles/will-plain-text-ads-continue-to-rule/" title="Alertbox April 2003: Will Plain-Text Ads Continue to Rule?"> text-only</a>, there's a chance that users will actually see them</strong>, rather than ignore them due to banner blindness. Also, because the text is short, Google ads force a <strong> focus on crisp and plain content </strong> that might actually communicate something in the second or two users typically allocate to reading ads.</p>

<p>I've recently been running ads for one of our own projects, and the click-through statistics provide interesting insights into advertising design. With a few simple changes, our ads' <strong> performance improvements ranged from 55% to 310%</strong>, which is within the <a class="new" href="/articles/usability-roi-declining-but-still-strong/" title="Alertbox Jan. 2003: Return on Investment for Usability"> improvement range we typically see</a> for usability-driven redesigns.</p>

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

<a class="ga-article-toc-item" href="#toc-keyword-targeting-1">Keyword Targeting</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-tune-the-text-2">Tune the Text</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-geographic-targeting-3">Geographic Targeting</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-rapid-experimentation-4">Rapid Experimentation</a>

</li>

</ul>

</div>

</div><h2 id="toc-keyword-targeting-1">Keyword Targeting</h2>

<p>Search engine advertising is keyword driven: You buy keywords and when users enter those words your ad appears. Buying the right keywords is thus a crucial step. It's easy to rapidly blow a budget on poorly targeted words.</p>

<p>For example, I bought the keywords "requirements specification" to run an advertisement for our field studies tutorial. Even after I tried several different wordings on the ad itself (two appear below), the <strong> click-through rate was exactly zero </strong> in the United States, although we did get a few clicks from other countries.</p>

<table align="center" border="0">

<tbody>

<tr>

<td valign="top">

<table>

<tbody>

<tr>

<td align="center" colspan="2">

<table border="0" cellpadding="3" cellspacing="0" width="100%">

<tbody>

<tr>

<td align="left" bgcolor="#ecf8ff" nowrap="nowrap"><font face="arial,sans-serif" size="-1"><a href="http://www.nngroup.com/courses/research-beyond-user-testing/">Practical Field Studies</a><br/>

<font color="#6f6f6f">Full-day course: fast method to get<br/>

user requirements from site visits.</font><br/>

<font color="green">www.NNgroup.com</font><br/>

<font color="#6f6f6f">Interest:</font> <img align="absmiddle" alt="" border="0" height="4" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/20010902_interestbar.gif" width="40"/> </font></td>

</tr>

</tbody>

</table>

</td>

</tr>

<tr>

<td>USA:</td>

<td>0.00%</td>

</tr>

</tbody>

</table>

</td>

<td>   </td>

<td valign="top">

<table>

<tbody>

<tr>

<td align="center" colspan="2">

<table border="0" cellpadding="3" cellspacing="0" width="100%">

<tbody>

<tr>

<td align="left" bgcolor="#ecf8ff" nowrap="nowrap"><font face="arial,sans-serif" size="-1"><a href="http://www.nngroup.com/courses/research-beyond-user-testing/">Practical Field Studies</a><br/>

<font color="#6f6f6f">Base your design on the features<br/>

users really need. Full-day course.</font><br/>

<font color="green">www.NNgroup.com</font><br/>

<font color="#6f6f6f">Interest:</font> <img align="absmiddle" alt="" border="0" height="4" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/20010902_interestbar.gif" width="40"/> </font></td>

</tr>

</tbody>

</table>

</td>

</tr>

<tr>

<td>USA:</td>

<td>0.00%</td>

</tr>

</tbody>

</table>

</td>

</tr>

</tbody>

</table>

<p>I finally had to acknowledge the real problem: However much I believe that field studies of real users in their natural habitat are a great way to gather requirement specifications, if people into requirement specifications disagree, I'm not going to convince them otherwise in three lines.</p>

<p>All mediums have their benefits. The <strong> Web is not a great platform for changing people's minds</strong>. Typically, users are <strong> clicking so quickly on the things they want </strong> that they don't consider alternatives.</p>

<p>It's thus important to understand the context of your product. People typically have strong opinions about requirements engineering. When I have them safely in their seats and can spend an hour or more wowing them with data and striking examples, I'm more likely to convince them to base feature designs on user data. But in three lines, I'm not going to change the way people run projects. It's foolish to try.</p>

<h2 id="toc-tune-the-text-2">Tune the Text</h2>

<p>Selecting the right wording for your ad is crucial to click-through. The following examples show the initial and revised wordings of an ad we ran in Europe, along with the click-through rates (we ran a different ad for the American conference). The results? Users were 55% more likely to click on the revised ad.</p>

<table align="center" border="0">

<tbody>

<tr>

<td valign="top">

<table>

<tbody>

<tr>

<td align="center" colspan="2">

<table border="0" cellpadding="3" cellspacing="0" width="100%">

<tbody>

<tr>

<td align="left" bgcolor="#ecf8ff" nowrap="nowrap"><font face="arial,sans-serif" size="-1"><a href="http://www.nngroup.com/training/">Usability Conference</a><br/>

<font color="#6f6f6f">The leading international experts<br/>

in user experience visit London</font><br/>

<font color="green">www.NNgroup.com/events</font><br/>

<font color="#6f6f6f">Interest:</font> <img align="absmiddle" alt="" border="0" height="4" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/20010902_interestbar.gif" width="40"/> </font></td>

</tr>

</tbody>

</table>

</td>

</tr>

<tr>

<td>Europe:</td>

<td>0.85%</td>

</tr>

</tbody>

</table>

</td>

<td>   </td>

<td valign="top">

<table>

<tbody>

<tr>

<td align="center" colspan="2">

<table border="0" cellpadding="3" cellspacing="0" width="100%">

<tbody>

<tr>

<td align="left" bgcolor="#ecf8ff" nowrap="nowrap"><font face="arial,sans-serif" size="-1"><a href="http://www.nngroup.com/training/">Jakob Nielsen in Europe</a><br/>

<font color="#6f6f6f">4-day usability conference<br/>

London, Nov. 4-7, 2001</font><br/>

<font color="green">www.NNgroup.com/events</font><br/>

<font color="#6f6f6f">Interest:</font> <img align="absmiddle" alt="" border="0" height="4" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/20010902_interestbar.gif" width="40"/> </font></td>

</tr>

</tbody>

</table>

</td>

</tr>

<tr>

<td>Europe:</td>

<td>1.32%</td>

</tr>

</tbody>

</table>

</td>

</tr>

</tbody>

</table>

<p>Our original ad (on the left) was fairly generic and did not use <a class="old" href="/reports/ecommerce-ux-trust-and-credibility/" title="Nielsen Norman Group: 34 Design Guidelines for Trust"> trust-enhancing design</a>. Most conferences boast "leading international experts" <em> (says who?) </em> and, in any case, Web users are too busy to bother with your general statements about how good you are. The revised ad is more specific: it names one of the speakers and provides concrete facts about the conference.</p>

<h2 id="toc-geographic-targeting-3">Geographic Targeting</h2>

<p>We know from many studies of international usability that people use the Web differently in different countries. Thus, it comes as no big surprise that the click-through rates can differ dramatically between regions.</p>

<p>For example, my initial ad for the conference's accessibility day (below, on the left) generated a horribly low click-through rate in Europe, though it did reasonably well in the U.S. When I revised it to target Europeans (right), the ad more than <strong> quadrupled the click-through rate</strong>. Well worth a few minutes of additional writing.</p>

<table align="center" border="0">

<tbody>

<tr>

<td valign="top">

<table>

<tbody>

<tr>

<td align="center" colspan="2">

<table border="0" cellpadding="3" cellspacing="0" width="100%">

<tbody>

<tr>

<td align="left" bgcolor="#ecf8ff" nowrap="nowrap"><font face="arial,sans-serif" size="-1"><a href="http://www.nngroup.com/reports/topic/accessibility/">Usability beyond ALT text</a><br/>

<font color="#6f6f6f">Full-day seminar in US &amp; Europe:<br/>

Design for users with disabilities</font><br/>

<font color="green">www.NNgroup.com/events</font><br/>

<font color="#6f6f6f">Interest:</font> <img align="absmiddle" alt="" border="0" height="4" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/20010902_interestbar.gif" width="40"/> </font></td>

</tr>

</tbody>

</table>

</td>

</tr>

<tr>

<td>Europe:</td>

<td>0.40%</td>

</tr>

<tr>

<td>USA:</td>

<td>0.96%</td>

</tr>

</tbody>

</table>

</td>

<td>   </td>

<td valign="top">

<table>

<tbody>

<tr>

<td align="center" colspan="2">

<table border="0" cellpadding="3" cellspacing="0" width="100%">

<tbody>

<tr>

<td align="left" bgcolor="#ecf8ff" nowrap="nowrap"><font face="arial,sans-serif" size="-1"><a href="http://www.nngroup.com/reports/topic/accessibility/">Usability beyond ALT text</a><br/>

<font color="#6f6f6f">Full-day seminar London Nov. 7:<br/>

Design for users with disabilities.</font><br/>

<font color="green">www.NNgroup.com/events</font><br/>

<font color="#6f6f6f">Interest:</font> <img align="absmiddle" alt="" border="0" height="4" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/20010902_interestbar.gif" width="40"/> </font></td>

</tr>

</tbody>

</table>

</td>

</tr>

<tr>

<td>Europe:</td>

<td>1.64%</td>

</tr>

</tbody>

</table>

</td>

</tr>

</tbody>

</table>

<p>Why didn't Europeans click on the first ad? I didn't run it through user testing, so I don't know for sure. However, my speculation is that the initial ad might have seemed too American. Although our accessibility seminar will present research from international studies of users with disabilities, the ad surely doesn't say that. And, while there's no room in the ad for that level of detail (and if there were, people wouldn't read it), retargetting the ad specifically to regional users definitely improved click-through.</p>

<h2 id="toc-rapid-experimentation-4">Rapid Experimentation</h2>

<p>With online ads, you can experiment rapidly. With the field studies ad appearing for "requirement specification" keywords, I pulled the ad after only 355 impressions. If the ad were going to attract a 1% click-through rate in the long run, then there would be a less than 3% probability of experiencing 355 exposures without a single click. This is more than enough proof. Of course, there is a 3% chance of canning an ad that might ultimately work, but so what? Better to try something else rather than continue an experiment that would be a waste of money in 97% of the cases.</p>

<p>I'm usually opposed to the strategy of simply <a class="old" href="/articles/the-mud-throwing-theory-of-usability/" title="Alertbox April 2000:The mud-throwing theory of usability"> throwing a design at the wall to see if it sticks</a>. For interaction design projects, it is much better to test a prototype design with a few users before implementing and launching the full design.</p>

<p>Ads are different for several reasons:</p>

<ul>

<li>There is a <strong> clear-cut metric </strong> for whether an ad works: the click-through rate. If it's less than your target (say, 1%), kill the ad. Doesn't matter why the ad doesn't work, it's toast. In contrast, with a full user interface, such as a website, there is substantial complexity. To improve its design, you need more detailed insights beyond "the site is too hard to use."</li>

<li>It is very <strong> cheap to generate alternative ads</strong>, especially for text-only ads that you can write in a few minutes. It's better to write more versions and see which one works than to agonize forever over a single ad.</li>

<li>It's also <strong> cheap to run a few hundred exposures </strong> to test an ad's click-through rate. The 355 exposures of the field study ad cost $5, which is cheaper than having a staff member even <em> think </em> about whether to run the ad or not. And, if you're willing to suffer a 10% probability of being wrong, you can differentiate between a 1% and 0% click-through rate in 229 exposures. With a few thousand exposures (costing less than $50), you can make much more accurate assessments. <em> (Update 2004: I wrote this column back when search engines still charged for exposure. Now that you pay for performance, you pay almost nothing for those ads that turned out not to work, making experimentation even more cost-effective.) </em></li>

<li><strong>No harm is done </strong> if you run a few ads that don't work. Nobody clicked, but also nobody got burned by your site or got a bad impression of your company. (This obviously assumes that you are not running offensive ads; just ads that people ignored.)</li>

</ul>

<p>Finally, it's not literally true that click-through is all that matters. You also have to account for the conversion rate of visitors into paying customers. Some ads might attract lots of clicks from a type of user unwilling to pay for your product. Ideally, you should track clicks through to the point of sale.</p>

<p>Whether you track click-through or sales, the point remains: You can try out many different ads and many different keyword purchases, and simply keep the ones that work.</p>

<p>This same method applies to a few other areas where there is a similar binary distinction between designs that work and designs that fail. One example is <a class="new" href="/reports/email-newsletter-design/" title="Nielsen Norman Group Report: Email Newsletter Usability -79 design guidelines for subscription, newsletter content and account maintenance based on usability studies"> having site visitors sign up for a newsletter</a>: either they do it, or they don't. The outcome is clearly defined and measurable at the time of use. As with ads, you can easily try two alternative designs and keep the one that attracts the most subscribers.</p>

<p>Although finding what works and what doesn't can be easy with these types of design, guessing why users don't behave the way you want is less straightforward. This complicates the choice of alternative designs, because you don't get the qualitative insights that come from usability methods that go beyond the simple numbers. For more complex design problems, simply looking at clicks is not enough.</p>

<p><strong>Find out more </strong> about designing search ads from this good book on how to use Google AdWords (same principles apply for Yahoo/Microsoft ads and other text-based search advertising): <a href="http://www.amazon.com/dp/0071496564?tag=useitcomusablein"> Buy from Amazon.com</a> or, if you are based in Europe <a href="http://www.amazon.co.uk/dp/0071496564?tag=useit-21"> buy from Amazon.co.uk</a>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Writing for the Web,advertising</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Writing for the Web</span>

<a class="ga-article-related-topic" href="/topic/writing-web/">Writing for the Web</a>

</li>

</ul>

</div>

</div>

</div>

</div>