# You Are Not the User: The False-Consensus Effect - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">You Are Not the User: The False-Consensus Effect</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Raluca Budiu</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2023-04-portraits-raluca.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/raluca-budiu/">

Raluca Budiu</a></span>

<p class="publication-date">

October 22, 2017

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2017-10-22</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: You Are Not the User: The False-Consensus Effect&amp;body=https://www.nngroup.com/articles/false-consensus/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/false-consensus/&amp;title=You Are Not the User: The False-Consensus Effect&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/false-consensus/&amp;text=You Are Not the User: The False-Consensus Effect&amp;via=nngroup" data-share-type="Twitter">

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

</span>Designers, developers, and even UX researchers fall prey to the false-consensus effect, projecting their behaviors and reactions onto users.

</div>

<div class="article-body">

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

<a class="ga-article-toc-item" href="#toc-introduction-1">Introduction</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-the-false-consensus-effect-2">The False-Consensus Effect</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-why-you-must-test-3">Why You MUST Test</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-reference-4">Reference</a>

</li>

</ul>

</div>

</div><h2 id="toc-introduction-1">Introduction</h2>

<p>As a graduate student, I used to write quite a few programs. Besides the occasional homework, I would also write little scripts in Unix to speed up my work, as well as Lisp code intended to run the cognitive models I was devising at the time.</p>

<p>I was the only user of these pieces of code: their only purpose was to help me do my research. As such, I could afford to write them as (un)intelligibly as I wanted, have weird parameter names that made sense only to me, and dispense of pretty much all user interface except for the command line.</p>

<p>While many people who earn a living from developing software will write tons of programs to make their own life easier, much, if not most, of their output will in fact be intended for other people ­ ­— people who are not working in a cubicle nearby, or not even in the same building. These “users” are usually very different than those who write the code, even in the rare case where they are developers: they have different backgrounds, different experiences with user interfaces, different mindsets, different <a href="https://www.nngroup.com/articles/mental-models/">mental models</a>, and different goals. They are not us.</p>

<p>By now you probably have heard the phrase “you are not the user”  — it’s become one of the mantras of user experience, and rightly so. All our work as UX professionals stems from the assumption that we are different from our users. Artifacts that are right for us are not necessarily right for our users: we can’t judge user-interface quality based on whether we like a design ourselves. We need to learn how to create systems that are right for those who will actually use them.</p>

<p>Assuming that you are your user is a fallacy that is ingrained in the human mind. It even has a name in social psychology — it’s called the false-consensus effect.</p>

<h2 id="toc-the-false-consensus-effect-2">The False-Consensus Effect</h2>

<p><strong>Definition</strong>: The false-consensus effect refers to people’s tendency to assume that others share their beliefs and will behave similarly in a given context. Only people who are very different from them would make different choices.</p>

<p>The false-consensus effect was first defined in 1977 by Ross, Greene, and House. They showed that unlike scientists, “layperson psychologists” (that is, all of us who are put into the position to guess how others would behave) tend to overestimate how many people share their choices, values, and judgments, and perceive alternate responses as rare, deviant, and more revealing of the responders.</p>

<p>Ross and his colleagues ran a series of experiments in which participants had to estimate what percentage of people would make one of two choices: for example, what percentage of people would choose to contest a speeding ticket in court versus just pay the fine. After they made their estimate, participants disclosed what they would do in that situation, and also filled in two questionnaires about the personality traits of those who would make each of the two choices. The researchers discovered that participants expected (1) that the majority of people would make the same choice that they made (e.g., pay the ticket), and (2) that those opting for the alternative would have different, more extreme personality traits than those opting for their choice.</p>

<p>We tend to assume that our next-door neighbor has voted for the same candidate that we did in the last presidential election. Only someone who is very different from us — living in a completely different part of the country, from a different socioeconomic class, with a different education — could have voted for the other candidate. Or so we think.</p>

<p>These assumptions are natural. The human mind makes inferences based on one or few examples: if our ancestors were attacked by a wild beast, it would make sense to assume that the beast was dangerous and stay away from it even in the absence of other examples.</p>

<p>Generalizing based on the examples available is a called the <strong>availability bias</strong> and is a type  of cognitive bias. (Others include <a href="https://www.nngroup.com/articles/negativity-bias-ux/">negativity bias</a>, <a href="https://www.nngroup.com/articles/prospect-theory/">loss aversion</a>, <a href="https://www.nngroup.com/articles/narrative-biases/">narrative</a> bias, and <a href="https://www.nngroup.com/articles/decision-framing-cognitive-bias-ux-pros/">framing</a> — which is a type of <a href="https://www.nngroup.com/articles/priming/">priming</a>.)  It is often a source of stereotypes and overgeneralizations. As my yoga teacher put it, with those Eastern European roots, I should have no problem with back bends — as if all Romanians were <a href="https://en.wikipedia.org/wiki/Nadia_Com%C4%83neci">Nadia Comăneci</a>.</p>

<h2 id="toc-why-you-must-test-3">Why You MUST Test</h2>

<p>Much in the same way, we, designers, developers, and UX researchers assume that people who will use our interfaces are like us. We have one example of someone using the interface: it’s us. And maybe our colleagues. And we make generalizations based on that example. So only someone who’s stupid or very different than us could actually fail to figure it out.</p>

<p>Wrong. We are wrong believing that, but it’s important to understand that we are no worse human beings for doing so. It’s deeply weaved into our nature to believe that others are like us.</p>

<p>So what’s a fallible human being to do? And how about a fallible designer or software developer? The answer is simple. Learn about this bias. Acknowledge it. And then do something to overcome it. When it comes to user interfaces, the answer is simpler than in other avenues of life: Test. With real users (<a href="https://www.nngroup.com/articles/employees-user-test/">not your colleagues</a>).  Know who your users are and how they respond to your designs by watching them use these designs. Don’t make assumptions.</p>

<p>UX researchers are also subjected to the false-consensus effect and the availability bias (and <a href="https://www.nngroup.com/courses/design-tradeoffs/">to many others</a> ). Much of our <a href="https://www.nngroup.com/articles/quant-vs-qual/">qualitative work</a> involves looking at a few users and one design, and then making inferences to other similar, but not quite-the-same situations. Or applying <a href="https://www.nngroup.com/articles/ten-usability-heuristics/">heuristics</a> and the knowledge that we’ve acquired to new paradigms. It’s important to understand that these inferences can be biased — we may be wearing blinds. Often what works in one situation may not work in others, and vice versa.</p>

<p>Acknowledge your vulnerability and establish checks. <a href="https://www.nngroup.com/articles/no-validate-in-ux/">Don’t validate</a>; instead investigate. Study with your actual target users whenever the slightest doubt is involved.</p>

<p>Learn more about the false-consensus effect and other cognitive biases in our class <a href="https://www.nngroup.com/courses/human-mind/">The Human Mind and Usability</a> .</p>

<h2 id="toc-reference-4">Reference</h2>

<p>L. Ross, D. Greene, P. House. 1977. <a href="http://web.mit.edu/curhan/www/docs/Articles/biases/13_J_Experimental_Social_Psychology_279_(Ross).pdf">The “False Consensus Effect”: An Egocentric Bias in Social Perception and Attribution Processes</a>. <em> Journal Of Experimental Social Psychology.</em></p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Persuasive and Emotional Design" href="/courses/persuasive-emotional-design/?lm=false-consensus&amp;pt=article">

<h4 class="title heading-small">Persuasive and Emotional Design</h4>

<p id="persuasive-and-emotional-design" class="description body-small">

Create delightful experiences that touch, convince, or excite your audience

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

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=false-consensus&amp;pt=article">

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

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Psychology and UX,usability research</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Psychology and UX</span>

<a class="ga-article-related-topic" href="/topic/psychology-and-ux/">Psychology and UX</a>

</li>

</ul>

</div>

</div>

</div>

</div>