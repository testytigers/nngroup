# Nielsen Norman Group: UX Research, Training, and Consulting - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">When the UI Is Too Fast</h1>

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

July 8, 2013

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2013-07-08</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: When the UI Is Too Fast&amp;body=https://www.nngroup.com/articles/too-fast-ux/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/too-fast-ux/&amp;title=When the UI Is Too Fast&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/too-fast-ux/&amp;text=When the UI Is Too Fast&amp;via=nngroup" data-share-type="Twitter">

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

</span>Users might overlook things that change too fast — and even when they do notice, changeable screen elements are harder to understand in a limited timeframe.

</div>

<div class="article-body">

<p>Given that 99% of all <a href="https://www.nngroup.com/articles/website-response-times/" title="Website Response Times, article">usability problems related to response times</a> are caused by user interfaces being too <em>slow</em>, it might be dangerous for me to write about those few cases where the computer is too <em>fast</em>. After all,</p>

<ul>

<li><strong>computers are usually too slow</strong>, and</li>

<li>snappy response times enhance usability. <a href="https://www.nngroup.com/articles/short-term-memory-and-web-usability/" title="Short-Term Memory and Web Usability, article">Human memory decays</a> rapidly, so people might forget some of what they were doing while waiting for a slow computer.</li>

</ul>

<p>Further, while <a href="https://www.nngroup.com/topic/young-users/" title="Usability research with children, teenagers, and college students">young users</a> are notoriously impatient, even older users won’t linger long on a slow site.</p>

<p>Caveats enough, I hope; a snappier user experience is almost always better.</p>

<p>That said, there is such a thing as <strong>too fast</strong>. My latest example came a few days ago (2013) when we were user-testing tablet applications for the next update of our <a href="https://www.nngroup.com/courses/usability-mobile-websites-apps/" title="Nielsen Norman Group: full-day training course">Mobile User Experience</a> course: The user repeatedly failed to connect to the correct WiFi network, because she repeatedly touched the wrong entry in the list.</p>

<p>Making such a mistake once might be excused as an example of the inherent problem in gestural interfaces — that people sometimes touch a spot that’s a bit off the target.</p>

<p>But this user hit the wrong target several times. Why? The intended <strong>target kept moving</strong> without her noticing it because the tablet was continually scanning the airwaves and adding or removing entries on its list of available WiFi networks.</p>

<p>The interaction went as follows:</p>

<ol>

<li>The user scanned the list to locate the intended network (for which she had the proper login info).</li>

<li>She started moving her hand toward the target, intending to touch the line for the network found in step 1.</li>

<li><em>During the fraction of a second</em> that her finger was moving toward the tablet surface, the list would gain or lose an entry, causing the intended target to jump to a different place on the screen.</li>

<li>The user <strong>selected a different target than intended</strong> because the new network was now occupying the spot of the one she wanted (and <strong>she didn’t notice</strong> that she was touching the wrong name because her finger obscured the target).</li>

<li>The user attempted to log in to the selected network, but was refused because she was using credentials from a different network.</li>

</ol>

<p>Although these steps occurred in rapid succession, the poor user repeated the exact same sequence so many times that I figured out what was happening without needing to replay the usability video.</p>

<p>(Of course, obeying a <a href="https://www.nngroup.com/articles/authentic-behavior-in-user-testing/" title="Authentic Behavior in User Testing, article">basic tenet of usability testing</a>, we couldn’t tell the unfortunate test participant what she was doing wrong; we had to sit in silence and watch her fail repeatedly until she finally got lucky enough to select the network during a period in which the WiFi software didn’t detect any updates to the list.)</p>

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

<a class="ga-article-toc-item" href="#toc-fast-might-be-missed-1">Fast Might Be Missed</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-fast-might-be-difficult-2">Fast Might Be Difficult</a>

</li>

</ul>

</div>

</div><h2 id="toc-fast-might-be-missed-1">Fast Might Be Missed</h2>

<p>When the screen changes in the proverbial blink of an eye, users might blink and <a href="/articles/change-blindness/">miss the change</a>. Or, as in my WiFi example, they might not be looking at that particular part of the screen during the brief interval in which the change occurs.</p>

<p>When changes happen on their own — without any user prompting — people don’t even know to look for them and are likely to miss things that change rapidly. To alleviate this problem, one useful tactic is to slow down the change, using, for example, an animation that lasts a second or two. But don’t over signal; there’s nothing more annoying than an aggressively blinking screen.</p>

<p>Rapid screen updates are great when they’re the result of <strong>user-initiated actions</strong>. When you touch a slider on a tablet, for example, you want it to highlight immediately to indicate that it has been activated. And, as you move the slider, you want the corresponding screen elements to update immediately.</p>

<p>As long as <em>users</em> do something, they know to look for the result. But even in these cases, there’s a potential usability issue if <a href="https://www.nngroup.com/articles/auto-forwarding/" title="Closeness of Actions and Objects in GUI Design, article">the update is far removed from the action</a>. Changes outside the user’s field of vision might be overlooked and require stronger signaling than simply replacing the old information with something new. A classic example is <a href="https://www.nngroup.com/reports/ecommerce-ux-shopping-carts-checkout-registration/" title="E-Commerce User Experience Design Guidelines, Vol. 04: Shopping Carts, Checkout and Registration - Nielsen Norman Group research report">ecommerce shopping carts</a> that are positioned in the screen’s far corner and simply count up when the user clicks <em>Add to Cart</em>. In testing, we often find that users overlook such subtle updates when they occur far away from the button they clicked.</p>

<h2 id="toc-fast-might-be-difficult-2">Fast Might Be Difficult</h2>

<p>A second class of usability problems occurs when users do notice a rapid change, but <strong>can’t understand what happened quickly enough</strong>. This often happens in <a href="https://www.nngroup.com/articles/auto-forwarding/" title="Auto-Forwarding Carousels and Accordions Annoy Users and Reduce Visibility, article">carousel, rotators, and other auto-forwarding design elements</a>. Once you decide that something might be of interest, it’s yanked off the screen — replaced by something you don’t want.</p>

<p>This is particularly problematic for slower users, such as <a href="https://www.nngroup.com/topic/international-users/" title="Articles about usability for international users">international customers</a> who don’t read your language well or <a href="https://www.nngroup.com/articles/usability-for-senior-citizens/" title="Seniors as Web Users, article">old</a> or <a href="https://www.nngroup.com/topic/accessibility/" title="Articles about accessibility">disabled</a> users who might need extra time dealing with the user interface and are thus disproportionally harmed by rapidly changing screens.</p>

<p>Let’s establish a simple usability principle: <strong>avoid taunting the customers</strong>.</p>

<p>And, to circle back to the beginning, it’s important to remember that, as problems go, being too fast is far less common than being too slow. Whether fast or slow, the point is to pay attention to the <a href="https://www.nngroup.com/articles/powers-of-10-time-scales-in-ux/" title="Powers of 10: Time Scales in User Experience, article">time aspect of the user experience</a>. After all, a key differentiator of interaction design compared to most other forms of design is that we deal with time-changing phenomena.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Human Computer Interaction,timing,response time,performance</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

</ul>

</div>

</div>

</div>

</div>