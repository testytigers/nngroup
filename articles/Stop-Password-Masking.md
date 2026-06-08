# Stop Password Masking - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">2</span>

<div class="article-header">

<h1 class="article-h1">Stop Password Masking</h1>

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

June 22, 2009

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2009-06-22</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Stop Password Masking&amp;body=https://www.nngroup.com/articles/stop-password-masking/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/stop-password-masking/&amp;title=Stop Password Masking&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/stop-password-masking/&amp;text=Stop Password Masking&amp;via=nngroup" data-share-type="Twitter">

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

</span>Usability suffers when users type in passwords and the only feedback they get is a row of bullets. Typically, masking passwords doesn&#x27;t even increase security, but it does cost you business due to login failures.

</div>

<div class="article-body">

<p>It's time to show most passwords in clear text as users type them. <strong> Providing feedback </strong> and visualizing the system's status have always been among the most <a class="old" href="http://www.nngroup.com/articles/ten-usability-heuristics/" title="Jakob Nielsen: 10 Usability Heuristics"> basic usability principles</a>. Showing undifferentiated bullets while users enter complex codes definitely fails to comply.</p>

<p>Most websites (and many other applications) mask passwords as users type them, and thereby theoretically prevent miscreants from looking over users' shoulders. Of course, a truly skilled criminal can simply look at the keyboard and note which keys are being pressed. So, password masking doesn't even protect fully against snoopers.</p>

<p>More importantly, there's usually nobody looking over your shoulder when you log in to a website. It's just you, sitting all alone in your office, suffering reduced usability to protect against a non-issue.</p>

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

<a class="ga-article-toc-item" href="#toc-the-costs-of-masking-1">The Costs of Masking</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-abandon-legacy-design-2">Abandon Legacy Design</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-update-microsoft-listens-3">Update: Microsoft Listens</a>

</li>

</ul>

</div>

</div><h2 id="toc-the-costs-of-masking-1">The Costs of Masking</h2>

<p>Password masking has proven to be a particularly nasty usability problem in our <a class="old" href="/articles/mobile-usability-update/" title="Alertbox: Mobile Web 2009 = Desktop Web 1998"> testing of mobile devices</a>, where typing is difficult and typos are common. But the problem exists for desktop users as well.</p>

<p>When you make it hard for users to enter passwords you create two problems — one of which actually lowers security:</p>

<ul>

<li>Users <strong> make more errors </strong> when they can't see what they're typing while filling in a form. They therefore <strong> feel less confident</strong>. This double degradation of the user experience means that people are more likely to give up and never log in to your site at all, leading to <strong> lost business</strong>. (Or, in the case of intranets, increased support calls.)</li>

<li>The more uncertain users feel about typing passwords, the more likely they are to (a) employ <strong> overly simple passwords </strong> and/or (b) <strong> copy-paste passwords </strong> from a file on their computer. Both behaviors lead to a true <strong> loss of security</strong>.</li>

</ul>

<p>Yes, users are sometimes truly at risk of having bystanders spy on their passwords, such as when they're using an Internet cafe. It's therefore worth offering them a <a class="old" href="/articles/checkboxes-vs-radio-buttons/" title="Alertbox: Checkboxes vs. Radio Buttons"> checkbox </a> to have their passwords masked; for high-risk applications, such as bank accounts, you might even check this box by default. In cases where there's a <a class="old" href="/articles/security-and-human-factors/" title="Alertbox: Security &amp; Human Factors"> tension between security and usability</a>, sometimes security should win.</p>

<p>In most cases, however, users will appreciate getting clear-text feedback as they enter passwords. Your business will increase, and security will even improve a tiny bit as well.</p>

<h2 id="toc-abandon-legacy-design-2">Abandon Legacy Design</h2>

<p>Password masking has become common for no reasons other than (a) it's easy to do, and (b) it was the default in the Web's early days. In this respect, it's similar to another usability problem — <a class="old" href="http://www.nngroup.com/articles/reset-and-cancel-buttons/" title="Alertbox: Reset and Cancel Buttons"> having <em> Reset </em> buttons on forms</a>, which is also something that should die.</p>

<p>Generally, I recommend <a class="old" href="/articles/the-need-for-web-design-standards/" title="Alertbox: The Need for Web Design Standards"> adhering to conventions</a>. Do what users expect, and they can concentrate their brainpower on understanding your products and offers instead of struggling with the user interface.</p>

<p>But password masking and <em> Reset </em> buttons are not something users actively seek out. Losing these features won't cause confusion, nor will their replacements: the new features will simply be clear text (in the first case) and a blank area where the destroy-my-work button used to be (in the second).</p>

<p>This is very different from removing something users look for or introducing something they don't understand.</p>

<p>Let's clean up the Web's cobwebs and remove stuff that's there only because it's always been there.</p>

<h2 id="toc-update-microsoft-listens-3">Update: Microsoft Listens</h2>

<p>The release of Internet Explorer 10 in 2013 added a neat new feature: view password in cleartext while clicking a small icon in a field with otherwise-masked characters. Looks like this:</p>

<p style="text-align:center"><img alt='A password field as shown in IE10, including the "view as cleartext" icon' loading="lazy" src="//media.nngroup.com/media/editor/2013/03/15/ie10-cleartext-view.png" style="width: 137px; height: 31px;"/></p>

<p>This is not quite what I wanted when I asked websites to stop password masking. But this is a good example of how browser vendors can help users overcome usability problems in web design. Nice work Microsoft.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">password,Human Computer Interaction,standards &amp; conventions,errors</span>

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