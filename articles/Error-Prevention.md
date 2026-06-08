# What the Erroneous Hawaiian Missile Alert Can Teach Us About Error Prevention - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">What the Erroneous Hawaiian Missile Alert Can Teach Us About Error Prevention</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Kim Flaherty</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Kim-Headshot-2022.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Kim Flaherty

</span>

<p class="publication-date">

January 16, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-01-16</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: What the Erroneous Hawaiian Missile Alert Can Teach Us About Error Prevention&amp;body=https://www.nngroup.com/articles/error-prevention/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/error-prevention/&amp;title=What the Erroneous Hawaiian Missile Alert Can Teach Us About Error Prevention&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/error-prevention/&amp;text=What the Erroneous Hawaiian Missile Alert Can Teach Us About Error Prevention&amp;via=nngroup" data-share-type="Twitter">

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

</span>People should not be blamed for errors caused by poorly designed systems.

</div>

<div class="article-body">

<p>On Saturday, January 13th 2018, residents and tourists in the Hawaiian islands received a very frightening emergency alert on their mobile devices. The alert from Hawaii’s emergency alert command center read “BALLISTIC MISSILE THREAT INBOUND TO HAWAII. SEEK IMMEDIATE SHELTER. THIS IS NOT A DRILL.”</p>

<figure class="caption"><img alt="Hawaiian Missile Alert" height="279" loading="lazy" src="https://media.nngroup.com/media/editor/2018/01/16/hawaiianmissilealert.png" width="350"/>

<figcaption><em>The missile emergency alert was sent to residents and tourists in Hawaii. Note the all-capitals font: while capital letters can be appropriate for <a href="https://www.nngroup.com/articles/glanceable-fonts/">glanceable text</a>, a 3-line paragraph is difficult to read when formatted like this.</em></figcaption>

</figure>

<p>Thankfully, this was in fact a drill: there was no inbound missile headed toward the islands. However, the message had been inadvertently sent live to cell phones across the islands rather than to the test network it had been meant for. Since this incident occurred, there has been extensive news coverage about the operator who was responsible for this false alarm. Many headlines focused on the human error, and some even called for the job of the person responsible:</p>

<ul>

<li><em>Hawaii missile alert: How one employee ‘pushed the wrong button’ and caused a wave of panic</em> – Washington Post</li>

<li><em>‘Wrong button’ sent false missile alert to Hawaii </em>– Daily Beast</li>

<li><em>‘Inexcusable’ false ballistic missile alert in Hawaii was caused by human error </em>– TechCrunch</li>

</ul>

<p>Apparently, the person erred twice:</p>

<ol>

<li>by selecting the wrong choice (real alert instead of test)</li>

<li>by confirming the previous selection</li>

</ol>

<p>This angle to the story did not sit well with me. When I heard about this mishap, my immediate question was, “What is wrong with the interface that caused the operator to inadvertently make the incorrect selection?”</p>

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

<a class="ga-article-toc-item" href="#toc-slips-and-error-prevention-1">Slips and Error Prevention</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-interface-design-problems-2">Interface Design Problems</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-lack-of-undo-capability-3">Lack of Undo Capability</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-4">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-slips-and-error-prevention-1">Slips and Error Prevention</h2>

<p>I think we can all relate to pushing the wrong button by accident. I’ve cancelled transactions at store checkouts and gas pumps after pushing<em> No</em> instead of <em>Yes</em>. I’ve opted into add-on offers on websites by inadvertently selecting <em>Accept</em> rather than <em>Decline</em>. Luckily none of these mistakes sent an entire state into panic, but they are all examples of <a href="https://www.nngroup.com/articles/slips/">slips</a>.</p>

<p><strong>Slips</strong> occur when a user wants to do one action but unintentionally takes another (usually similar) action. They often happen in situations where users are on autopilot and do not fully devote their attentional resources to the task at hand. Accidentally putting liquid hand soap on one’s toothbrush instead of toothpaste is an unconscious slip. But slips can also happen when the two choices look too similar or are placed too closely to each other.</p>

<p>Often times, when you stop to assess the design of an interface where a slip has occurred, there is an underlying UI issue at play that sets people up for these errors.</p>

<p>There are a few common system-design problems that cause unconscious slips:</p>

<ul>

<li><strong>Miscues</strong>: When the design gives the wrong cue to users — for example, by violating design conventions</li>

<li><strong>Poorly differentiated options: </strong>When an interface provides multiple choices, but it uses similar names or similar visual styling for them</li>

<li><strong>Problematic presentation or interaction design: </strong>When the layout, presentation, or workflow does not include appropriate safeguards — for example, by placing two buttons very close to each other</li>

<li><strong>Lack of confirmation for destructive actions:</strong> When the design does not ask users to <a href="https://www.nngroup.com/articles/confirmation-dialog/">confirm an action with major consequences</a></li>

</ul>

<p>All these issues illustrate poor error prevention. Error prevention is one of Jakob Nielsen’s <a href="https://www.nngroup.com/articles/ten-usability-heuristics/">10 heuristics for user interface design;</a> it becomes especially important for critical systems like the Hawaii emergency-alert system or hospital systems where pushing the wrong button could be the difference between life and death.</p>

<p>In the case of the mistaken missile alert, some news outlets have provided examples of the interface involved. The same system screen is used to deliver several different types of emergency alerts to the public including amber alerts, road closures, and high-surf warnings. There are 9 unique options which include both real-time alerts that go to the general public and drill versions of these alerts meant to test and troubleshoot them. (A 10th option was added later, to send a “it was a false alarm” retraction message in case of future errors.)</p>

<figure class="caption"><img alt="AlertScreen" height="519" loading="lazy" src="https://media.nngroup.com/media/editor/2018/01/16/alertscreen.jpg" width="692"/>

<figcaption><em>Photo released by the Hawaii Governor's office of the system screen that was used to send out the erroneous missile alert. (Note that the first option in the list, </em>BMD False Alarm,<em> was added after the mishap, to allow for sending retraction messages in the case of future false alarms. Normal <a href="https://www.nngroup.com/articles/menu-design/">menu-design guidelines</a> would have recommended putting this option at the bottom of the list, since it’s presumably a rarely used choice.)</em> Source: <a href="https://twitter.com/CivilBeat/status/953127542050795520">Honolulu Civil Beat</a></figcaption>

</figure>

<figure class="caption"><img alt="AlertScreen" height="304" loading="lazy" src="https://media.nngroup.com/media/editor/2018/01/18/revised-hawaii-alert-ui.png" width="557"/>

<figcaption><em>Revised screenshot released by the Hawaii Emergency Management Agency after we wrote this article. Supposedly, the Governor's screenshot may not have been the one actually in use. This second design suffers from the same usability problems, but is marginally better in having a smaller number of  obscure and poorly formatted menu options.</em></figcaption>

</figure>

<p>The two options that were involved in this mishap were the following:</p>

<ul>

<li>PACOM (CDW) – STATE ONLY : the option the operator mistakenly selected</li>

<li>DRILL- PACOM (CDW) – STATE ONLY : the option the operator should have selected</li>

</ul>

<p>The operator was supposed to have selected the second option DRILL-PACOM (CDW) – STATE ONLY, but instead selected the other one.</p>

<h2 id="toc-interface-design-problems-2">Interface Design Problems</h2>

<p>This missile-alert UI includes several design problems:</p>

<ul>

<li><strong>Poorly differentiated options</strong>: The options listed on the page have cryptic labels that require too much mental effort to differentiate. Moreover, some of these labels (for example, the two relevant to this incident) are fairly similar. Couldn’t these options be replaced with simpler ones like those below?

<ul>

<li>Test Alert: PACOM</li>

<li>Live Alert: PACOM</li>

</ul>

<p>One may argue that these labels are not descriptive enough on a screen that contains many different types of alerts that are listed in no particular order. Why not group them in a meaningful way – for example, with all amber alerts placed together under a heading meant to distinguish them?</p>

</li>

<li><strong>Problematic presentation or interaction design</strong>: Maybe the root of the problem comes before this screen entirely. Should we really have the live vs. test options presented in the same environment and on the same screen for critical system like this? With this design, a slip of the finger could result in a major problem, as seen. Why not have two separate workflows or modes? One <a href="https://www.fastcodesign.com/90157153/don-norman-what-went-wrong-in-hawaii-human-error-nope-bad-design">mode reserved for test work</a>, which should be the default, and another for live system commands, where an explicit action must be taken to enter and submit commands. In my days as a developer, we had such structural safeguards in place, with live environments completely separated and visually distinct from the test environments.</li>

<li><strong>Possibly poor confirmation screen</strong>: News reports point out that, after the operator selected the wrong network, she was presented with a confirmation screen — indicating that the system’s designers may have tried to create some safeguards against accidental actions. But what did that screen look like? Often, when people go to similar confirmation screens ten times a day or when every action has a confirmation screen, they no longer pay attention to them — these dialogue boxes feel like roadblocks in their flow.

<p>Could a more intrusive type of confirmation for a live alert have helped? Perhaps it could have required users to reenter their passwords — not for added security against intruders, but to make it clear to users that they were about to do something unusual with serious consequences. Many banks use such an intrusive confirmation step before initiating irreversible actions such as a wire transfer.</p>

</li>

</ul>

<h2 id="toc-lack-of-undo-capability-3">Lack of Undo Capability</h2>

<p>Another application-design heuristic violated by the Hawaiian warning system is the ability to undo an erroneous command. The sending of messages cannot literally be undone, which is why a confirmation step is appropriate before the system starts sending. But one can at least send out a second message saying that the first one was a false alarm. This was indeed done, but only after a 38-minute delay.</p>

<p>According to news outlets, the delay was caused by bureaucratic disagreements between different levels of government, because the Hawaiian state agency that issued the (false) alert was not authorized to send anything except alerts. The agency had to secure additional levels of approval in order to send out a second, different type of message. However, whoever is authorized to take a certain action ought also to be authorized to undo that action if it turned out to be a mistake. In addition to this bureaucratic problem, sending a message to rescind the prior alert was not supported by the system, and this capability had to be created in the system on-the-fly by off-site developers.</p>

<p>Mistakes will be made, so plan for them. (Of course, the exact same mistake will likely not happen, but other mistakes will. This is why systems need to be designed to alleviate mistakes.)</p>

<h2 id="toc-conclusion-4">Conclusion</h2>

<p>The takeaway that human error was to blame and the user was at fault for having selected the incorrect option is wrong. Altogether <strong>a poorly designed system is to blame</strong>. A good UI makes it hard for people to err, and easier to recover from any remaining errors.</p>

<p>The solution is not to scold users, ask them to try harder, or to give them more extensive training. The answer is to redesign the system to be less error-prone.</p>

<p>Let’s just be happy we discovered this design problem now. Imagine if there was a real threat and the user accidentally sent the message to the test network rather than the live network.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=error-prevention&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">errors,Application Design,menus</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>