# Response Time Limits: Article by Jakob Nielsen - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">Response Times: The 3 Important Limits</h1>

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

January 1, 1993

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1993-01-01</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Response Times: The 3 Important Limits&amp;body=https://www.nngroup.com/articles/response-times-3-important-limits/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/response-times-3-important-limits/&amp;title=Response Times: The 3 Important Limits&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/response-times-3-important-limits/&amp;text=Response Times: The 3 Important Limits&amp;via=nngroup" data-share-type="Twitter">

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

</span>There are 3 main time limits (which are determined by human perceptual abilities) to keep in mind when optimizing web and application performance.

</div>

<div class="article-body">

<p><em>Excerpt from Chapter 5 in my book <a href="/books/usability-engineering/"> Usability Engineering</a></em>, from 1993:</p>

<p>The basic advice regarding response times has been about the same for thirty years [Miller 1968; Card et al. 1991]:</p>

<ul>

<li><strong>0.1 second</strong> is about the limit for having the user feel that the system is <strong>reacting instantaneously</strong>, meaning that no special feedback is necessary except to display the result.</li>

<li><strong>1.0 second</strong> is about the limit for the <strong>user's flow of thought</strong> to stay uninterrupted, even though the user will notice the delay. Normally, no special feedback is necessary during delays of more than 0.1 but less than 1.0 second, but the user does lose the feeling of operating directly on the data.</li>

<li><strong>10 seconds</strong> is about the limit for <strong>keeping the user's attention</strong> focused on the dialogue. For longer delays, users will want to perform other tasks while waiting for the computer to finish, so they should be given feedback indicating when the computer expects to be done. Feedback during the delay is especially important if the response time is likely to be highly variable, since users will then not know what to expect.</li>

</ul>

<p>Normally, response times should be as fast as possible, but it is also possible for the computer to react so fast that the user cannot keep up with the feedback. For example, a scrolling list may move so fast that the user cannot stop it in time for the desired element to remain within the available window. The fact that <a href="http://www.nngroup.com/articles/too-fast-ux/" title="When the UI Is Too Fast, article">computers can be too fast</a> indicates the need for user-interface changes, like animations, to be timed according to a real-time clock rather than being timed as an indirect effect of the computer's execution speed: Even if a faster model computer is substituted, the user interface should stay usable.</p>

<p>In cases where the computer cannot provide fairly immediate response, continuous feedback should be provided to the user in form of a <strong>percent-done indicator</strong> [Myers 1985]. As a rule of thumb, percent-done progress indicators should be used for operations taking more than about 10 seconds. Progress indicators have three main advantages: They reassure the user that the system has not crashed but is working on his or her problem; they indicate approximately how long the user can be expected to wait, thus allowing the user to do other activities during long waits; and they finally provide something for the user to look at, thus making the wait less painful. This latter advantage should not be underestimated and is one reason for recommending a graphic progress bar instead of just stating the expected remaining time in numbers.</p>

<p>For operations where it is unknown in advance how much work has to be done, it may not be possible to use a percent-done indicator, but it is still possible to provide running progress feedback in terms of the absolute amount of work done. For example, a system searching an unknown number of remote databases could print the name of each database as it is processed. If this is not possible either, a last resort would be to use a less specific progress indicator in the form of a spinning ball, a busy bee flying over the screen, dots printed on a status line, or any such mechanism that at least indicates that the system is working, even if it does not indicate what it is doing. <span style="color:#666666"> Note added for the web version of this essay: Most web browsers fail in providing useful progress bars, since they don't communicate what percentage of the <em> entire download </em> for a page has been completed. </span></p>

<p>For reasonably fast operations, taking between 2 and 10 seconds, a true percent-done indicator may be overkill and, in fact, putting one up would violate the principle of display inertia (flashing changes on the screen so rapidly that the user cannot keep pace or feels stressed). One could still give less conspicuous progress feedback. A common solution is to combine a "busy" cursor with a rapidly changing number in small field in the bottom of the screen to indicate how much has been done.</p>

<p><strong>See Also: </strong><br/>

Article about <a href="http://www.nngroup.com/articles/website-response-times/">website response times</a> and how to improve them.</p>

<h2>Web-Based Application Response Time</h2>

<p>Update added 2014: I keep getting questions like this, so I decided to answer it here.</p>

<blockquote><strong>Q: </strong> "You mention many times that response time is important, and there are tons of tools to measure response time, but what is an acceptable web based application's response time? What is a user's tolerance, not for a shopping experience, but for an interactive application?"</blockquote>

<p><strong>A: </strong> I wish we could eradicate the term "web-based application" because it distracts from the real issue, which is one of application UI design (we have several <a href="http://www.nngroup.com/courses/topic/applications/">full-day courses on this topic</a>). We don't have special guidelines for applications implemented in C++ relative to apps implemented in JavaScript. The fundamental usability recommendations are the same, no matter the implementation, since we are discussing user experience, not coding.</p>

<p>Therefore, the <strong>response time guidelines for web-based applications are the same as for all other applications</strong>. These guidelines have been the same for 46 years now, so they are also not likely to change with whatever implementation technology comes next.</p>

<p><strong>0.1 second: </strong> Limit for users feeling that they are <a href="https://www.nngroup.com/articles/direct-manipulation/"><strong>directly manipulating</strong></a> objects in the UI. For example, this is the limit from the time the user selects a column in a table until that column should highlight or otherwise give feedback that it's selected. Ideally, this would also be the response time for sorting the column — if so, users would feel that <em> they </em> are sorting the table. (As opposed to feeling that they are <em>ordering</em> the computer to do the sorting for them.)</p>

<p><strong>1 second: </strong> Limit for users feeling that they are <strong>freely navigating</strong> the command space without having to unduly wait for the computer. A delay of 0.2–1.0 seconds does mean that users notice the delay and thus feel the computer is "working" on the command, as opposed to having the command be a direct effect of the users' actions. Example: If sorting a table according to the selected column can't be done in 0.1 seconds, it certainly has to be done in 1 second, or users will feel that the UI is sluggish and will lose the sense of "flow" in performing their task. For delays of more than 1 second, indicate to the user that the computer is working on the problem, for example by changing the shape of the cursor.</p>

<p><strong>10 seconds:</strong> Limit for users <strong>keeping their attention</strong> on the task. Anything slower than 10 seconds needs a percent-done indicator as well as a clearly signposted way for the user to interrupt the operation. Assume that users will need to reorient themselves when they return to the UI after a delay of more than 10 seconds. Delays of longer than 10 seconds are only acceptable during natural breaks in the user's work, for example when switching tasks.</p>

<p><strong>See Also:</strong><br/>

Article on <a href="http://www.nngroup.com/articles/powers-of-10-time-scales-in-ux/" title="Powers of 10: Time Scales in User Experience, article">time scales in user experience</a>.</p>

<h3>References</h3>

<p>Card, S. K., Robertson, G. G., and Mackinlay, J. D. (1991). The information visualizer: An information workspace. <em>Proc. ACM CHI'91 Conf.</em> (New Orleans, LA, 28 April-2 May), 181-188.</p>

<p>Miller, R. B. (1968). Response time in man-computer conversational transactions. <em>Proc. AFIPS Fall Joint Computer Conference</em> <strong>Vol. 33</strong>, 267-277.</p>

<p>Myers, B. A. (1985). The importance of percent-done progress indicators for computer-human interfaces. <em>Proc. ACM CHI'85 Conf.</em> (San Francisco, CA, 14-18 April), 11-17.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=response-times-3-important-limits&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=response-times-3-important-limits&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=response-times-3-important-limits&amp;pt=article">

<h4 class="title heading-small">Application Design for Web and Desktop</h4>

<p id="application-design-for-web-and-desktop" class="description body-small">

Components, design patterns, workflows, and ways of interacting with complex data

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">response time,Human Computer Interaction,Web Usability,Application Design</span>

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

<li>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>