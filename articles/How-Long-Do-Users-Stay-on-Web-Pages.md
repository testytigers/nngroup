# How Long Do Users Stay on Web Pages? - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">How Long Do Users Stay on Web Pages?</h1>

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

September 11, 2011

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2011-09-11</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: How Long Do Users Stay on Web Pages?&amp;body=https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/&amp;title=How Long Do Users Stay on Web Pages?&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/&amp;text=How Long Do Users Stay on Web Pages?&amp;via=nngroup" data-share-type="Twitter">

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

</span>Users often leave Web pages in 10–20 seconds, but pages with a clear value proposition can hold people&#x27;s attention for much longer. To gain several minutes of user attention, you must clearly communicate your value proposition within 10 seconds.

</div>

<div class="article-body">

<p>How long will users stay on a web page before leaving? It's a perennial question, yet the answer has always been the same:</p>

<ul>

<li><em>Not very long. </em></li>

</ul>

<p>The average page visit lasts a little less than a minute.</p>

<p>As users rush through web pages, they have <a class="old" href="https://www.nngroup.com/articles/how-little-do-users-read/" title="Alertbox: How Little Do Users Read?"> time to read only a quarter of the text</a> on the pages they actually visit (let alone all those they don't). So, unless your writing is extraordinarily clear and focused, little of what you say on your website will get through to customers.</p>

<p>However, while users are always in a hurry on the web, the time they spend on individual page visits varies widely: sometimes people <a class="old" href="https://www.nngroup.com/articles/reduce-bounce-rates/" title="Alertbox: Reduce Bounce Rates: Fight for the Second Click"> bounce away</a> immediately, other times they linger for far longer than a minute. Given this, <strong> the average is not the most fruitful way of analyzing </strong> user behaviors. Users are human beings — their <a class="old" href="https://www.nngroup.com/articles/variability-in-user-performance/" title="Alertbox: Variability in User Performance"> behaviors are highly variable</a> and are <a class="old" href="https://www.nngroup.com/articles/interaction-elasticity/" title="Alertbox: Interaction Elasticity"> not captured fully by a single number</a>.</p>

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

<a class="ga-article-toc-item" href="#toc-leaving-web-pages-the-weibull-hazard-function-1">Leaving Web Pages: The Weibull Hazard Function</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-negative-aging-leave-quick-or-stay-long-2">Negative Aging: Leave Quick or Stay Long</a>

</li>

</ul>

</div>

</div><h2 id="toc-leaving-web-pages-the-weibull-hazard-function-1">Leaving Web Pages: The Weibull Hazard Function</h2>

<p><a class="out" href="https://dl.acm.org/citation.cfm?doid=1835449.1835513" title="ACM Digital Library: Chao Liu, Ryen W. White, and Susan Dumais. 2010. Understanding web browsing behaviors through Weibull analysis of dwell time. In Proceedings of the 33rd international ACM SIGIR conference on Research and development in information retrieval (SIGIR '10)">Research by Chao Liu and colleagues</a> from Microsoft Research now provides a mathematical understanding of users' page-leaving behaviors. The scientists collected data from "a popular web browser plug-in," analyzing page-visit durations for <strong> 205,873 different web pages </strong> for which they had captured upwards of <strong> 10,000 visits</strong>.<strong> </strong> Suffice it to say: these guys crunched <em> a lot </em> of data (more than 2 billion dwell times).</p>

<ul>

<li>The result: <strong> the time users spend on a web page follows a Weibull distribution</strong>.</li>

</ul>

<p>99.9% of readers will now ask: <em> What's a Weibull distribution? </em></p>

<p><strong>Weibull is a reliability-engineering concept that's used to analyze the time-to-failure for components</strong>. The model's <em> hazard function </em> indicates the probability that a component will fail at time <em> t</em>, given that it has worked fine up until time <em> t</em>.</p>

<p>So, after replacing a spare part in a piece of equipment, Weibull analysis predicts when you'll have to replace it again. It also lets you conduct risk analysis beyond simplistic mean-time to failure. And, if you own a lot of equipment, you can use aggregate analysis to, say, manage your spare parts inventory.</p>

<p>Of course, <strong>when analyzing Web visits, we simply replace "component failure" with "user leaving the page."</strong> In their research paper, Liu and colleagues provide intensive statistical analysis to show that the Weibull model closely matches users' empirically observed behavior.</p>

<p>According to earlier research, there are 2 different kinds of Weibull distributions:</p>

<ul>

<li><strong>Positive aging</strong>: The longer the component has been in service, the <strong> more likely </strong> it is to fail. In other words, the hazard function increases for larger values of <em> t</em>. This makes intuitive sense, because the longer stuff is used, the more it wears down. Thus, something that has been in use for a long time will be approaching its breaking point.</li>

<li><strong>Negative aging</strong>: The longer the component has been in service, the <strong> less likely </strong> it is to fail. Here, the hazard function decreases for larger values of <em> t</em>. This makes sense when individual components vary in quality: poorly made components usually fail early, so anything that has been in service for a long time is likely to be particularly robust and will usually survive even longer.</li>

</ul>

<h2 id="toc-negative-aging-leave-quick-or-stay-long-2">Negative Aging: Leave Quick or Stay Long</h2>

<p>The researchers discovered <strong> that 99% of web pages have a negative aging effect</strong>. In human–computer interaction (HCI) research, it's extremely rare to get this strong a finding, and Liu and colleagues should be credited with discovering a major new insight.</p>

<p>Why negative aging? Because web pages are indeed of highly variable quality. Users know this and spend their initial time on a page in ruthless triage to abandon the dross ASAP. It's rare for people to linger on web pages, but when users do decide that a page is valuable, they may stay for a bit.</p>

<p>The following chart shows the hazard function — that is, the likelihood of leaving — for the median Weibull parameters fitted across the scientists' humongous dataset:</p>

<p> </p>

<p style="text-align:center"><img alt="Weibull hazard function showing the probability that users will leave a Web page at time t if they have already stayed for t seconds." height="443" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/weibull-hazard-function-leaving-web-pages.png" width="665"/></p>

<p> </p>

<p>It's clear from the chart that the <strong> first 10 seconds of the page visit are critical </strong> for users' decision to stay or leave. The probability of leaving is very high during these first few seconds because users are extremely skeptical, having suffered countless poorly designed web pages in the past. People know that most web pages are useless, and they behave accordingly to avoid wasting more time than absolutely necessary on bad pages.</p>

<p>If the web page survives this first — extremely harsh — 10-second judgment, users will look around a bit. However, they're still highly likely to leave during the subsequent 20 seconds of their visit. Only after people have stayed on a page for about 30 seconds does the curve become relatively flat. People continue to leave every second, but at a much slower rate than during the first 30 seconds.</p>

<p>So, if you can convince users to stay on your page for half a minute, there's a fair chance that they'll stay much longer — often 2 minutes or more, which is an eternity on the web.</p>

<p>So, roughly speaking, there are two cases here:</p>

<ul>

<li><strong>bad pages</strong>, which get the chop in a few seconds; and</li>

<li><strong>good pages</strong>, which might be allocated a few minutes.</li>

</ul>

<p>Note: <strong> "good" vs. "bad" is a decision that each individual user makes </strong> within those first few seconds of arriving. The design implications are clear:</p>

<ul>

<li>To gain several minutes of user attention, you must clearly <strong> communicate your value proposition within 10 seconds</strong>.</li>

</ul>

<h3>Reference and Related Reading</h3>

<p><a href="https://dl.acm.org/citation.cfm?doid=1835449.1835513">Chao Liu, Ryen W. White, and Susan Dumais. 2010. Understanding web browsing behaviors through Weibull analysis of dwell time.</a> In Proceedings of the 33rd international ACM SIGIR conference on Research and development in information retrieval (SIGIR '10)</p>

<p><a href="https://www.nngroup.com/articles/return-visits-not-bounce/">Optimize for Return Visits, Not Bounce Rate</a></p>

<p><a href="https://www.nngroup.com/articles/related-content-pageviews/">Related Content Boosts Pageviews, When Done Right</a></p>

<p><a href="https://www.nngroup.com/articles/why-site-tourists-are-worthless/">Why Site Tourists are Worthless</a></p>

<p> </p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=how-long-do-users-stay-on-web-pages&amp;pt=article">

<h4 class="title heading-small">The Human Mind and Usability</h4>

<p id="the-human-mind-and-usability" class="description body-small">

Use psychology to predict and explain how your customers think and act

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

<li>

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=how-long-do-users-stay-on-web-pages&amp;pt=article">

<h4 class="title heading-small">Web Page UX Design</h4>

<p id="web-page-ux-design" class="description body-small">

Strategically combine content, visuals, and interactive components to design successful web pages

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Human Computer Interaction,Web Usability,timing</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>