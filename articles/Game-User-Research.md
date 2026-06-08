# Games User Research: What’s Different? - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">9</span>

<div class="article-header">

<h1 class="article-h1">Games User Research: What’s Different?</h1>

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

March 20, 2016

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2016-03-20</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Games User Research: What’s Different?&amp;body=https://www.nngroup.com/articles/game-user-research/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/game-user-research/&amp;title=Games User Research: What’s Different?&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/game-user-research/&amp;text=Games User Research: What’s Different?&amp;via=nngroup" data-share-type="Twitter">

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

</span>Game testing researches the notion of fun. Compared with mainstream UX studies, it involves many more users and relies more on biometrics and custom software. The most striking findings from the Games User Research Summit were the drastic age and gender differences in motivation research.

</div>

<div class="article-body">

<p>Last week, I attended the <a href="http://gamesurconf.com/">Games User Research Summit</a> (GamesUR or GUR), which happened in connection with the Game Developer Conference (GDC), but was hosted separately at Electronic Arts (EA) in Silicon Valley — as you can tell, these guys love their acronyms.</p>

<p>With EA being the gracious hosts, the conference happened under the watchful eyes of an enormous dragon and the break room was festooned with large posters of the classic <em>Star Wars</em> characters. It was clear just from the surroundings that we were not in Kansas anymore. (Or, rather, not in the realm of mainstream UX. Here <em>really </em>be dragons.)</p>

<p>It was clear from the terminology bantered around in the talks that games are different from other design projects. Take, for example, the game Rainbow Six Siege (inevitably abbreviated as R6S, because they do like acronyms). One of the UX metrics tracked during the testing of this game was the <strong>kill/death ratio</strong>, which, admittedly, is not one of the things we teach in our otherwise comprehensive <a href="https://www.nngroup.com/courses/measuring-ux/">Measuring User Experience seminar</a>. (This ratio is the number of opponents you kill divided by the number of your team members who die during a death match. Another term we don’t use much in mainstream design projects.)</p>

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

<a class="ga-article-toc-item" href="#toc-much-remains-the-same-1">Much Remains the Same</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-multiuser-testing-2">Multiuser Testing</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-professional-users-3">Professional Users</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-designing-fun-4">Designing Fun</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-more-tech-5">More Tech</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-age-and-gender-differences-6">Age and Gender Differences</a>

</li>

</ul>

</div>

</div><h2 id="toc-much-remains-the-same-1">Much Remains the Same</h2>

<p>Despite the dragon and the death matches, I actually saw many similarities between the games user-experience (GUX) world and the mainstream UX world.</p>

<p>In a brilliant opening talk, Brandon Hsiung (Director of Insights at Riot Games) explained how he has organized his department of 70 people. A main takeaway was the benefit of embedding UX researchers within product teams, both at the feature-design level, but ideally at the higher level of the complete game. Twenty years ago, at Sun Microsystems, we made the same key point of using a matrix organization where researchers report to a central, specialized group but sit with a product team in a dotted-line relationship.</p>

<p>Since Riot Games has close to 2,000 employees, a department of 70 insight professionals might seem too low for the recommended share of <a href="https://www.nngroup.com/articles/return-on-investment-for-usability/">10% of project teams being allocated to user research</a>. However, because Riot is both a studio (designing and implementing games) and a publisher (distributing and selling games), much of the total staff must be allocated to the publishing side. So an insights team of 70 may actually be close to the recommended 10% of the people actually building the new products.</p>

<p>The main innovation I got from Hsiung’s talk lies in the very name of his department: the Insights Team. The wording may seem like superficial propaganda, but in reality it makes a profound point: the goal of research is to increase company profitability by improving products and raising <a href="https://www.nngroup.com/articles/conversion-rates/">conversion rates</a>. We can achieve these profitability goals only if the UX teams deliver <strong>actionable insights and drive the company’s development activities</strong> at both the tactical level (better design) and the strategic level (discovering customer needs and building products to meet and exceed these needs). Most companies’ <a href="https://www.nngroup.com/articles/usability-maturity-stages-1-4/">UX maturity</a> is not even at the tactical level yet, but to reach the strategic level, we do have to don that “insight team” hat.</p>

<p>I was pleased to hear that Riot’s Insights Team encompasses the company’s user research, as well as their market research and analytics. <a href="https://www.nngroup.com/articles/analytics-user-experience/">Analytics and UX should be joined</a> at the hip, but are too often separated in different departments. And market research is usually kept even further from UX. This despite the many benefits of integrated customer insights that triangulate findings from multiple methods.</p>

<p>Another presentation that elicited some déjà-vu moments came from Laura Hammond from UEgroup, who talked about testing gesture-based games. She recommended avoiding swivel chairs when testing young children, because kids get too easily distracted by moving around on the chair. True, but an observation we made in 2001 in the first edition of our report from <a href="https://www.nngroup.com/articles/childrens-websites-usability-issues/">usability testing of children using websites</a>. The kids who were 6 years old in 2001 are now 21 and thus qualified to participate in our current <a href="https://www.nngroup.com/articles/millennials-digital-natives/">user research with young adults/Millennials</a>. It’s nice to know that the next generation of children is the same, at least when it comes to swivel chairs in the usability lab.</p>

<p>To record the test sessions and get the gestures on video, the researchers recommended using 3 video cameras: from above, from the side, and facing the user. Exactly what we did 20 years ago in the hardware human-factors lab to record system administrators installing hard drives in servers. Testing 3D user interfaces requires more equipment than studying 2D websites.</p>

<p>Of course, Hammond’s talk had also new observations, specific to games for the Intel RealSense camera (which requires users to control the game by moving their hands in front of the camera). For example, the researchers needed to include the users’ hand size as one of the <a href="https://www.nngroup.com/articles/recruiting-test-participants-for-usability-studies/">screening criteria when recruiting test participants</a>. We certainly don’t ask about hand size in our screeners, and apparently, it’s a challenge to get it right.</p>

<p>Another insight from Hammond’s talk was that testing 3D gestures introduces yet another opportunity for the study facilitator to bias the user: the very way you sit or move may <a href="https://www.nngroup.com/articles/priming/">prime</a> the user to copy aspects of your body language in their gestures.</p>

<h2 id="toc-multiuser-testing-2">Multiuser Testing</h2>

<p>Unlike <a href="https://www.nngroup.com/courses/usability-testing/">mainstream user testing</a>, game research often involves <a href="https://www.nngroup.com/articles/multiple-user-simultaneous-testing/">testing with many users in parallel</a> — either because the game takes a long time to play or because it involves multiple players.</p>

<p>(On occasion we do test with multiple users at the same time even in traditional UX projects — for example when running usability studies with young children, but mostly we run one user at a time, because we want to pay close attention to every detail of the user’s behavior. Also, a <a href="https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/">website visit usually only lasts 2–3 minutes, with a typical page view lasting maybe 30 seconds</a>, so we <em>should</em> aim to study everything in detail.)</p>

<p>Hardcore gamers will often play for hours at a stretch, with much of their time spent repeatedly shooting at something. As a result, playtesting labs around the world seem to be uniformly designed to accommodate 12–20 game testers (or more, for big companies) who play the same game, each at their own console.</p>

<p>Sebastian Long from Player Research in the UK described his company’s playtesting lab: The observation room included a big projection display with reduced versions of 12 users’ screens, as well as a pushbutton switch for observers to select one of the 12 screens to be magnified on a separate monitor for high-resolution observation when one of the testers did something interesting in the game. This need to alternate between surveying many peoples’ broad behavior and detailed attention to a single person’s specific interactions is rare outside games research.</p>

<p>The multiplayer component of many modern games is the second reason for multiuser sessions in game research. Whether several players play together in the same room or across the network in real time, researchers must understand their processes of communication and collaboration. In contrast, in mainstream UX, even when taking into account social media and <a href="https://www.nngroup.com/courses/cross-channel-user-experience/">omnichannel experiences</a>, people rarely work together at the same time with the same interface to solve the same task.</p>

<p>Games researchers often have access to <strong>data at true scale</strong>: in the case of the R6S kill/death ratio I mentioned above, Olivier Guedon from Ubisoft measured the ratio across 440,000 games during alpha testing and 182M games in two beta-testing rounds. In the alpha, the defending team won 61% of the time, resulting to tweaks making it easier to attack. As a result, the attackers won 58% of the time in the first beta test. Further redesigns finally made the game balanced in the second beta. A great example of <a href="https://www.nngroup.com/articles/parallel-and-iterative-design/">iterative design</a> and the common observation that fixing one UX problem (too hard to attack) sometimes introduces a new problem (too easy to attack), which is why I recommend as many rounds of iteration as possible.</p>

<h2 id="toc-professional-users-3">Professional Users</h2>

<p>In the gaming domain, some companies have to accommodate two classes of users: normal users (who buy the game and play for fun) and professional users who are paid to play the game as an “eSport.” eSports are a big business with huge audiences watching the championship games. (In 2014, Amazon.com paid almost a billion dollars for one eSports site.)</p>

<p>Of course, one of the oldest lessons in traditional user experience is that we need to design for <a href="https://www.nngroup.com/articles/novice-vs-expert-users/">both novice and expert users</a>. Each have different skill levels and need different features. (More on this in our <a href="https://www.nngroup.com/courses/ux-basic-training/">UX Basic Training course</a> — it’s that fundamental a concept.) But professional users take this distinction to an entirely different level and require separate research of what happens when operating a user interface becomes its own goal and the focus of somebody's career.</p>

<h2 id="toc-designing-fun-4">Designing Fun</h2>

<p>User satisfaction has always been one of the <a href="https://www.nngroup.com/articles/usability-101-introduction-to-usability/">5 main usability criteria</a>: people will most definitely leave a website that’s too unpleasant. Even in enterprise software, you want users to like your design to reduce employee turnover. That said, mainstream UX research spends much time on other criteria, such as learnability and efficiency, because users are so goal oriented: they go to a website to get something done (say, buy something or read the news), not to have fun with the user interface per se.</p>

<p>In strong contrast, a game has no purpose other than fun. The stated goal may be to kill the boss. (No, not your manager, but a nasty gremlin or alien invader — these game enemies are referred to as bosses.) But the real goal is to have fun while doing so. That’s why it’s important to study the kill/death ratio: if designers made the game interface too good at killing bosses, that would be <em>efficient</em>, but not <em>fun</em>. (Good traditional UX; bad GUX.) Gamers need just the right level of challenge, because it’s also no fun if you die immediately and don’t get to off some bosses.</p>

<p>In an attempt to pinpoint exactly when users are excited or bored, some GUR researchers employ esoteric biometrics sensors. For example, they measure skin-conductance levels (sweat activity), which is related to physiological arousal. Pierre Chalfoun gave a good overview of biometrics at Ubisoft, and he emphasized that these physiological sensors are not always directly connected to user emotions, which is what we really want to design for. (The goal is engaged users, not sweaty users, even if there is a correlation.)</p>

<p>Chalfoun presented an interesting study of game tutorials, which showed that users’ levels of frustration, as indirectly measured by biometrics, mounted every time they failed to understand a game tutorial. First failure: somewhat frustrated. Third failure in a row: very frustrated. While this finding makes intuitive sense and may not be worth the cost of a biometrics lab, Chalfoun stressed that good visualizations of such data convince management and developers to take research seriously and invest in fixing the bad designs that caused such growing user frustration. (Without quantifiable data, it’s easier to dismiss user frustration as a minor matter that can’t hold up the release schedule.)</p>

<h2 id="toc-more-tech-5">More Tech</h2>

<p>Across the conference presentations, it was striking how many GUX teams make use of custom-written software. Anything from running the playtest lab to game telemetry (“calling home” with data about live play in a beta test) requires the company to allocate software developers to build special features just for the researchers.</p>

<p>I think there are two reasons that GUX teams seem to be more tech heavy than mainstream UX teams:</p>

<ul>

<li>The game researchers are embedded in highly geeky companies with legions of programmers, and it’s their company culture that if you need something, you go build it.</li>

<li>The many game genres are widely diverging in needs, and thus require custom software to study seriously. In contrast, all websites are built on top of the browser and require the same types of interactions. This means that it’s actually possible for third-party solutions to offer, say, cloud-based analytics tools that collect most data needed to study a website, thus eliminating the need for custom software.</li>

</ul>

<h2 id="toc-age-and-gender-differences-6">Age and Gender Differences</h2>

<p>The best (but <em>very</em> data-dense) presentation at GamesUR was by Nick Yee from Quantic Foundry. Yee has collected data from 220,000 gamers who completed a <a href="https://apps.quanticfoundry.com/lab/10">survey about what motivates them</a> to play computer games. <a href="http://quanticfoundry.com/2015/12/21/map-of-gaming-motivations/">Motivations clustered into 6 groups</a>: action, social, mastery, achievement, immersion, and creativity. Obviously, different games speak to different motivations: a death-march game will attract gamers motivated by action and social play, whereas a simulation game would be preferred by people interested in immersion and creativity.</p>

<p>One of the main components of the social cluster is <strong>competition</strong>. In this cluster gamers care about beating other players and being acknowledged as a high-ranking player (even if they don’t take it to the eSports extreme). The following chart shows the average score on the competition metric for men and women at different ages:</p>

<figure class="caption"><img alt="Strength of competition as motivation for gamers of across age and gender" border="0" height="303" loading="lazy" src="https://media.nngroup.com/media/editor/2016/03/17/games-competitiveness-by-age-and-gender.png" width="600"/>

<figcaption><em>Average gamer scores, expressed as standard deviations from the overall mean across all ages and genders. High scores indicate people who are more motivated by competition. Source: </em><a href="http://quanticfoundry.com/2016/02/10/gamer-generation/"><em>Quantic Foundry</em></a><em>, reprinted by permission.</em></figcaption>

</figure>

<p>Two observations from the chart:</p>

<ul>

<li>Men are more competitive than women. (Or, more precisely, men like competitive games more than women do.) Maybe not a big surprise.</li>

<li>Competitiveness decreases drastically by age. In fact, the difference between young and old gamers is more than twice the difference between men and women, and by age 50 there’s no real difference between men and women anymore. (Older women might even be more competitive than older men, but there’s too little data in this research to say for sure.)</li>

</ul>

<p>We sometimes find <a href="https://www.nngroup.com/articles/young-adults-flat-design/">differences between young and old users in mainstream UX research</a>, but our effect sizes are usually much more modest than those in the Gamer Motivation Study: as users age, task <a href="https://www.nngroup.com/articles/middle-aged-web-users/">performance using websites declines by 0.8% per year</a>. And it’s almost unheard of to see any reportable differences between male and female users. Say you want to study menu design: the difference between how men and women use any given menu is so negligible that is has zero practical meaning compared to the difference between a design that complies with <a href="https://www.nngroup.com/articles/menu-design/">menu UX guidelines</a> and a poorly designed menu.</p>

<p>In conclusion, the Games User Research Summit was a great conference with many insightful talks by top professionals. Both they and we probably think that mainstream UX and GUR are more different than they really are, but all of us should periodically reflect on the notable similarities between the two fields to make sure that we don’t unduly limit our methods to those traditionally employed in our UX niche. For sure, as <a href="https://www.nngroup.com/courses/credibility-and-persuasive-web-design/">persuasive web design</a> becomes increasingly important, mainstream user researchers will need to adopt (and adapt) methods from games user research.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="User Interviews" href="/courses/user-interviews/?lm=game-user-research&amp;pt=article">

<h4 class="title heading-small">User Interviews</h4>

<p id="user-interviews" class="description body-small">

Uncover in-depth, accurate insights about your users

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-research" />

</svg>

<p class="ux-specialty ux-research">Research</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="Lean UX and Agile" href="/courses/lean-ux-and-agile/?lm=game-user-research&amp;pt=article">

<h4 class="title heading-small">Lean UX and Agile</h4>

<p id="lean-ux-and-agile" class="description body-small">

Strategies to stay user-centered in fast-paced Agile environments

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-management" />

</svg>

<p class="ux-specialty ux-management">Management</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="Service Blueprinting" href="/courses/service-design/?lm=game-user-research&amp;pt=article">

<h4 class="title heading-small">Service Blueprinting</h4>

<p id="service-blueprinting" class="description body-small">

Orchestrate people, props, and processes that are core to your digital experience

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-management" />

</svg>

<p class="ux-specialty ux-management">Management</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">games,User Testing,emotional design,Managing UX Teams,Analytics &amp; Metrics</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">User Testing</span>

<a class="ga-article-related-topic" href="/topic/user-testing/">User Testing</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/ux-management/">Managing UX Teams</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/analytics-and-metrics/">Analytics &amp; Metrics</a>

</li>

</ul>

</div>

</div>

</div>

</div>