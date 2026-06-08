# Security &amp; Human Factors - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">Security &amp; Human Factors</h1>

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

November 25, 2000

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2000-11-25</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Security &amp; Human Factors&amp;body=https://www.nngroup.com/articles/security-and-human-factors/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/security-and-human-factors/&amp;title=Security &amp; Human Factors&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/security-and-human-factors/&amp;text=Security &amp; Human Factors&amp;via=nngroup" data-share-type="Twitter">

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

</span>A big lie of computer security is that security improves as password complexity increases. In reality, users simply write down difficult passwords, leaving the system vulnerable. Security is better increased by designing for how people actually behave.

</div>

<div class="article-body">

<p>Usability advocates and security people have opposite goals that create a fundamental conflict:</p>

<ul>

<li>Usability advocates <strong> favor making it <em> easy </em> to use a system</strong>, ideally requiring no special access procedures at all, whereas</li>

<li>security people <strong> favor making it <em> hard </em> to access a system</strong>, at least for unauthorized users.</li>

</ul>

<p>How do we resolve this conflict? By recognizing that the real goal of security is to minimize the <em> relative </em> amount of unauthorized use. Although a system with extremely poor usability would certainly discourage unauthorized users, it is likely to turn off the target users as well.</p>

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

<a class="ga-article-toc-item" href="#toc-secure-passwords-facilitate-break-ins-1">"Secure" Passwords Facilitate Break-Ins</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-higher-security-through-realistic-design-2">Higher Security Through Realistic Design</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-web-design-for-usable-security-3">Web Design for Usable Security</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-single-sign-on-4">Single Sign-On</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-logout-5">Logout</a>

</li>

</ul>

</div>

</div><h2 id="toc-secure-passwords-facilitate-break-ins-1">"Secure" Passwords Facilitate Break-Ins</h2>

<p>The <strong> big lies of computer security</strong>?</p>

<ul style="margin-top: 2pt">

<li>Random passwords are more secure.</li>

<li>A system-selected password is more secure than one the user chooses.</li>

<li>Long passwords are more secure than short ones.</li>

<li>Forcing the user to change passwords frequently increases security.</li>

<li>Requiring different passwords for different systems increases security.</li>

</ul>

<p>All of these statements would be true if we did not have to consider the human factor.</p>

<p>In reality, passwords that comply with the above list of "security-enhancing" principles lead to one outcome: <strong> Users write down their passwords</strong>. Take a walk around any office in the world and you can collect as many passwords as you like by</p>

<ul style="margin-top: 2pt">

<li>looking at the yellow stickies pasted onto terminals,</li>

<li>finding the cheat sheet in the user's top drawer, or</li>

<li>searching the user's hard drive for the file that inevitably contains all required passwords in one conveniently machine-readable spot.</li>

</ul>

<h2 id="toc-higher-security-through-realistic-design-2">Higher Security Through Realistic Design</h2>

<p>The only people who can remember many long strings of random elements are circus performance artists. Better to design for the rest of us (and our limited memories).</p>

<p>When you require simple passwords that users can remember, you increase the probability of passwords being kept secret. The same goes for passwords that users choose and that they don't have to change too frequently.</p>

<p>While it's true that such passwords are easier to crack, the vast majority of security breaks come from intruders (or insiders) who expose a human weakness, not those who run code-breaking algorithms.</p>

<p>In the future, security will improve through biological verification mechanisms, such as fingerprint recognition or retina scanning. However, it will take time for this infrastructure to be built (and fingerprint systems won't work for some people). In any case, for now, it is best to avoid imposing awkward log-in procedures and instead simply cookie users on systems with low security needs.</p>

<p>With ecommerce in particular, users should not have to create a userid and password before they can shop. How many sales are lost because shoppers either cannot think up a unique userid or don't understand how to deal with passwords?</p>

<h2 id="toc-web-design-for-usable-security-3">Web Design for Usable Security</h2>

<p>Even if you remove registration from the critical path, you might still need a way for users to become members of your site. This necessity can create a classic usability problem, especially if you require an email address as the userid. In many cases, users assume you are asking for their email address and their AOL password, which they then enter, creating a security problem (assuming users get to this stage; many are shut out at the gate because their password is hardwired in their software and they can't remember it).</p>

<p>Nonetheless, I do recommend letting users enter their email address instead of a userid: It's guaranteed to be unique and it is easy to remember. However, you should always recommend that they choose a new and different password. Also, in usability testing, I've found that some users expect the system to create the password and then e-mail it to them. You should thus make it explicit that they must create their own while registering or you risk having users either get stuck or close their browser before completing their account set up.</p>

<p>Many websites have harsh requirements for password format. I suggest that you relax the rules as much as possible. Obviously, a system for trading millions of dollars must be more secure than one that lets people read the daily news.</p>

<p>If your rules are too strict, many users will not be able to use names and passwords that make sense to them. This increases the likelihood of users forgetting their login information the next time they visit. Forgotten passwords are the cause of countless repeated registrations across the Web: People often have five to ten "accounts" on the same website.</p>

<p>You should place instructions for userids and passwords immediately next to the field label:</p>

<form> </form>

<table align="center">

<tbody>

<tr>

<td align="right" valign="middle">Password:<br/>

<span style="font-size: 75%">at least 6 characters</span></td>

<td valign="middle"><input name="dummypassword" size="12" type="password"/></td>

</tr>

</tbody>

</table>

<p> </p>

<p>Any other placement and many users will not read the instructions.</p>

<h2 id="toc-single-sign-on-4">Single Sign-On</h2>

<p>Every security study I have ever conducted has had a common major finding: Users want a single log-in that follows them as they use the system. Nobody wants to log in again and again.</p>

<p>A key issue here is the definition of "the system." Ideally, the system is the users' total experience and thus they should only have to identify themselves to the computer once. The fact that they are actually browsing multiple websites should not be the users' problem. Indeed, in the future, personal computers will probably become truly personal and serve as users' agents in cyberspace, including taking over responsibility for passwords and identification.</p>

<p>For now, at a minimum, "the system" should include everything under a user's control. This means, for example, that users should have a single log-in for viewing their account and trading, and a single log-in for entering an extranet and checking on the status of an order. Although the back-end might need to enforce certain privileges for certain users, it should do so transparently without the need for additional log-ins.</p>

<p>[Update added 2004: Our <a href="/reports/intranet-usability-guidelines/" title="Nielsen Norman Group report: Intranet Usability, Design Guidelines from Studies with Intranet Users"> research study on intranet usability</a>, testing the intranets across a large number of companies, found that the sign-on process had the second-largest impact on employee productivity of the factors we tested. (Search was #1.) The difference in sign-on usability between intranets in the top 25% and intranets in the bottom 25% amounted to $2.5 million per year for a company with 10,000 employees.]</p>

<h2 id="toc-logout-5">Logout</h2>

<p>For sensitive systems, many users feel more comfortable when they see an explicit logout button. For most systems, however, you can assume that users will not log out and instead will simply leave. That's the spirit of the Web and that's what the security system must support. However, do not set time-outs to trigger too soon or you will annoy people who are simply taking a break from using your site. For most non-sensitive applications, a time-out interval of an hour will accommodate lunch breaks and still provide decent security.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=security-and-human-factors&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">security,Human Computer Interaction,password,new technologies</span>

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