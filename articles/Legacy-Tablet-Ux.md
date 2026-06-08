# Tablet UX Research From the Pioneer Days - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">Tablet UX Research From the Pioneer Days</h1>

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

January 25, 2015

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2015-01-25</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Tablet UX Research From the Pioneer Days&amp;body=https://www.nngroup.com/articles/legacy-tablet-ux/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/legacy-tablet-ux/&amp;title=Tablet UX Research From the Pioneer Days&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/legacy-tablet-ux/&amp;text=Tablet UX Research From the Pioneer Days&amp;via=nngroup" data-share-type="Twitter">

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

</span>The PenPoint tablet was ahead of its time and too expensive and heavy, but had gestural syntax and personal-productivity benefits that we can still learn from.

</div>

<div class="article-body">

<p>I was recently looking through a stack of old photos and came across one from my days as a scientist at Bell Communications Research (Bellcore, the arm of Bell Labs owned by the regional Bell operating companies, which was one of the last Grand Labs). In <strong>1992</strong> we conducted research on the usability of tablet computers, and the photo shows me using a tablet with the<strong> PenPoint system from GO Corp</strong>:</p>

<figure class="caption" style="text-align: center;"><img alt="1992 photo of Jakob Nielsen using a tablet running the PenPoint operating system" height="440" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/10/29/tablet-research-1992.jpg" width="450"/>

<figcaption><em>PenPoint tablet computer in 1992</em></figcaption>

</figure>

<p>GO was a stylus-operated device, complete with handwriting recognition. As you can tell from the photo, it was definitely a clunkier device than current tablets, weighing 4.5 pounds (5 times as much as a current iPad). My research with the GO didn’t discover most of our current <a href="/reports/tablets/">tablet-design guidelines</a> — mainly because this early device had virtually no applications. Instead, we studied the implications of handwritten data entry and stylus-controlled graphical user interfaces (GUI).</p>

<p>In one of our research studies with PenPoint tablets, Susan T. Dumais (now a Microsoft Distinguished Scientist) and I found that we could compensate for the inaccuracies of handwriting recognition by using a meaning-dependent form of search (LSI). This allowed us to retrieve handwritten notes about as well as typed documents, despite the higher frequency of misspellings in the former.</p>

<p>(As an aside, it’s sad to note the abysmal <strong>lack of progress in personal-information retrieval</strong> and personal-information management since Bellcore’s research in the early 1990s. Virtually all efforts and all the ensuing progress have been directed toward searching huge information spaces such as the entire web. Our own personal information has been left behind, and the productivity of knowledge workers has suffered accordingly.)</p>

<p>Using a <strong>stylus instead of one’s finger</strong> to control the tablet allowed for a wider range of interactions, in particular in the form of more precise gestures. With a pen, the user can precisely touch a very small point on the screen, thus avoiding the <a href="http://www.nngroup.com/articles/ipad-usability-first-findings/">read–tap asymmetry</a> that’s one of the main usability concerns with modern touchscreen user interfaces. (RTA = you can <em>see </em>small things, but only <em>touch </em>big things.)</p>

<p><strong>Pen precision</strong> allowed for a rich set of editing gestures: for example, one could boldface a word by drawing a small “<strong>B</strong>” gesture on top of that word. Yet other gestures would result in other actions: for example drawing an “<strong>X</strong>” on top of a character would delete that character whereas drawing a proofreading “pigtail” gesture would delete a full word. As the deletion example shows, the concept of <a href="http://www.nngroup.com/articles/generic-commands/">generic commands</a> wasn’t fully realized, partly because of the difficulty of defining the scope of a command when it was drawn on top of the content. This definitely increased the learning time needed to use the system.</p>

<p>An interesting interaction design innovation followed from drawing the operations (commands) on top of the operands (the objects on which the commands operated): PenPoint was one of the few computer systems to <strong>unify the command syntax</strong> by avoiding the distinction between operator and operand. Usually, interactions have one of two possible syntax formats:</p>

<ul>

<li><strong>Verb-noun</strong> syntax: first the user specifies what should be done (the verb) and subsequently follows this by specifying the item that should be acted upon (the noun). For example, classic command-line-based operating systems would use a command format like <em>DEL foo</em> to delete a file named “foo.”</li>

<li><strong>Noun-verb</strong> syntax: first the user specifies what item should be acted upon (the noun) and subsequently the user tells the computer what it should do to that item (the verb). For example, most graphical user interfaces use the following sequence of actions to delete a file: first select the icon representing the file. Second, drag this icon into the trash (or touch a trash icon).</li>

</ul>

<p>Both formats have their own problems, including the basic point that they require the user to specify <em>tw</em>o things in order to have <em>one</em> action performed. In contrast, writing a squiggle on top of the thing to be deleted means that there is no ordering requirement for the operation and operand: both are specified in that single gesture. (Remember, the operand depended on the gesture: for example, if the gesture was an “<strong>X</strong>” a character would be deleted; a “pigtail” would erase the whole word.)</p>

<p>In retrospect, while GO Corp. pioneered many innovative interaction techniques and allowed us to do interesting early research on tablet user experience, it went nowhere commercially. The machine cost $3,920 in 1992 which is equivalent to <strong>$6,660</strong> in 2015 dollars or 11 times the cost of an iPad Air 2. (The iPad has 64 GB of storage, whereas the most popular PenPoint model — the NCR 3125 — had 20 MB.) While price didn’t matter to the lavishly funded elite research lab where I worked, there was no way an average company could afford tablet computers in 1992.</p>

<p>Reflecting back on my experience with GO in 1992 does show some areas where current tablet UX could be improved:</p>

<ul>

<li>A <strong>pen or stylus</strong> (as included with a few Android devices) allows for many richer interactions than are supported by current touchscreens due to the fat-finger problem. (Update September 2016: Apple introduced the Apple Pencil as a stylus for its high-end tablets in September 2015 — 8 months after this article was published — we've now bought a few and as I predicted we do find it useful for many applications.)</li>

<li>An emphasis on <strong>personal productivity</strong> instead of consumption of  entertainment and social media would lead to more useful UX designs.</li>

</ul>

<p>Tony Hoeber, Robert Carr, Jerry Kaplan, and the remaining team responsible for GO Corp’s pioneering work should not be forgotten. Neither should the many other early tablet computers that had the misfortune to be ahead of their time. The <a href="/articles/tablet-usability/">tablets we’re currently enjoying</a> didn’t come out of nowhere.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=legacy-tablet-ux&amp;pt=article">

<h4 class="title heading-small">Emerging Patterns in Interface Design</h4>

<p id="emerging-patterns-in-interface-design" class="description body-small">

Trending UX patterns and their impact on the total user experience

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet,new technologies</span>

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