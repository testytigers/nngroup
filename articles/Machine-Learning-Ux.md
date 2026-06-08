# Can Users Control and Understand a UI Driven by Machine Learning? - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">14</span>

<div class="article-header">

<h1 class="article-h1">Can Users Understand Recommendations and Personalization Driven by Machine Learning?</h1>

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

December 16, 2018 &centerdot; Updated Sep. 17, 2024

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2024-09-17</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Can Users Understand Recommendations and Personalization Driven by Machine Learning?&amp;body=https://www.nngroup.com/articles/machine-learning-ux/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/machine-learning-ux/&amp;title=Can Users Understand Recommendations and Personalization Driven by Machine Learning?&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/machine-learning-ux/&amp;text=Can Users Understand Recommendations and Personalization Driven by Machine Learning?&amp;via=nngroup" data-share-type="Twitter">

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

</span>In a study of people interacting with systems using machine-learning algorithms for recommendations and personalization, users had weak mental models and difficulties making the UI do what they want.

</div>

<div class="article-body">

<p>In this article, we examine some of the challenges that users encounter when interacting with machine-learning algorithms on Facebook, Instagram, Google News, Netflix, and Uber Driver. Our discussion is based on a week-long <a href="https://www.nngroup.com/articles/diary-studies/">diary study</a> in which 14 existing users of these systems video-logged their interactions with them.</p>

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

<a class="ga-article-toc-item" href="#toc-machine-learning-for-recommendations-and-personalization-1">Machine Learning for Recommendations and Personalization</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-the-black-box-model-2">The Black-Box Model</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-unclear-inputs-3">Unclear Inputs</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-lack-of-control-of-the-output-4">Lack of Control of the Output</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-recommendations-5">Recommendations</a>

</li>

</ul>

</div>

</div><h2 id="toc-machine-learning-for-recommendations-and-personalization-1">Machine Learning for Recommendations and Personalization</h2>

<p>We live in a world flooded by information. It’s harder and harder for us to keep track of it or to manually curate it for others; luckily, modern data science can sort through the vast amounts of information and surface those items that are relevant to us.</p>

<p><strong>Machine-learning algorithms</strong> rely on user knowledge and patterns observed in the data to make inferences and suggestions about what we may like or be interested in.  With machine-learning technologies becoming more and more accessible to developers, there’s a push for companies to take advantage of these algorithms to improve their products and their users’ experience.</p>

<p>Typical uses of such artificial-intelligence (AI) technologies for UX purposes include:</p>

<ul>

<li>Recommendations (e.g., a list of movies to watch or products to purchase)</li>

<li>Choice of what advertisements or content (e.g., news headlines) to display</li>

<li>Deals and special offers, <a href="https://www.nngroup.com/articles/recommendation-expectations/">personalized</a> to appeal to the current user</li>

<li>Personalized shortcuts with one-click access to whatever a user will likely want to do next</li>

</ul>

<p>Unfortunately, these algorithms are usually not transparent to the end users. People are not sure which of their actions are taken into account by these algorithms, and their outputs are not always easy to make sense of.  Suggestions and recommendations may be right on spot or apparently random and nonsensical. Often, these algorithms sort their output according to invisible criteria or group it into ad-hoc categories that are not mutually exclusive. While these decisions make sense from an algorithmic viewpoint, they are often too obscure for the lay user and go against traditional ways of structuring content.</p>

<h2 id="toc-the-black-box-model-2">The Black-Box Model</h2>

<p>To interact successfully with any system, users must create a <a href="https://www.nngroup.com/articles/mental-models/">mental model</a> of the system. Most people are not computer scientists and have no idea of how software is implemented, but they can form decent mental models based on prior knowledge about software artifacts, interfaces, or even the world at large. In many situations, they treat the system as a black box and determine how they can change the output of the system by playing with the possible inputs.</p>

<p>Machine-learning algorithms are one such type of black-box systems for users. They know that the algorithm uses as input some of their actions and can see what the output is. To successfully interact with the algorithm, users must form a mental model of how it works and figure out how the output can be changed to match their need. There are two big hurdles in creating this model:</p>

<ol>

<li><strong>Unclear inputs</strong>: It’s not clear which of the users’ actions are taken into account to produce the output.</li>

<li><strong>Lack of control on the output</strong>: Even when people know which of their actions are considered as inputs by the algorithm, it is not clear whether those inputs were effective in producing a desired output.</li>

</ol>

<figure class="caption"><img alt='The black box is the machine-learning algorithm with several potential inputs and an output.; inputs include tap, like,watch, save. User wonders "Which of my actions counts" and "How do I change the output"?' height="468" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/13/visual5.png" width="700"/>

<figcaption><em>The black-box model</em></figcaption>

</figure>

<p>We discuss each of these reasons separately.</p>

<h2 id="toc-unclear-inputs-3">Unclear Inputs</h2>

<p>The lack of clarity in the input makes the problem of creating an accurate mental model of the black box quite difficult. There are several reasons for which the input status can be unclear:</p>

<ul>

<li><strong>The algorithm is not transparent</strong> — it does not explicitly tell people which of their actions matter.</li>

<li><strong>The user is not aware of the universe of possible inputs</strong>, for example, because they are not limited to actions inside a system or a platform, but come from other behavior data (e.g., visiting third-party sites).</li>

<li><strong>There is a delay between input and output</strong>: a certain action may not immediately influence the output that the user sees within the same session.</li>

</ul>

<p>Among the machine-learning systems we looked at, Netflix did the best job in helping users understand which of their actions were taken into account by the recommender system. Netflix’s homepage (as well as the main-category landing pages) are usually one long set of lists; many of these lists have labels that explain how they were created — <em>Because you watched The Curious Creations of Christine McConnell, Because you added 22 July to your list, </em>and so on.</p>

<figure class="caption"><img alt='Two Netflix lists: "Because you watched The Curious Creations of Christine McConnell" and "Because you added 22 July to your list"' height="371" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/13/netflix-because.png" width="700"/>

<figcaption><em>Netflix explains some of the inputs used by its recommender system.</em></figcaption>

</figure>

<p>People were very appreciative of these types of suggestions, not only because they could feel in control but also because they gave them valuable information about the content being displayed.</p>

<p>Yet, even Netflix wasn’t totally successful in creating a good understanding of how the user’s actions are taken into account to create recommendations — also because these actions were not immediately reflected in the output of the algorithm. For example, one participant was puzzled that her <em>Top</em> <em>picks</em> seemed unaffected by the stand-up comedy shows that she had watched the last time she used Netflix. She said:</p>

<blockquote>

<p>“Top picks<em> changed — I guess based on what I watched, but this has nothing to do with what I watched, there's not a lot of comedy.”</em></p>

</blockquote>

<p>Another person wondered why <em>Top picks </em>overlapped so much with her Netflix watchlist:</p>

<blockquote>

<p>“Top picks — I don't know how they get them, I'm sure there's some algorithm or something, but I wish it was a little bit better because a lot of it is stuff that I watched years ago, or stuff that I have had on my list or stuff that I am just absolutely not interested in, so I'm like, hmm I wonder why they're recommending these things.”</p>

</blockquote>

<p>A Facebook user took the time to hide an ad on her newsfeed only to see the same ad repeated down the page.  </p>

<p>Facebook and Instagram users had a harder time understanding which of their actions really mattered for the content that was displayed on their newsfeed. They assumed that the posts in their newsfeed that they engaged with (through the <em>Like </em>button and its relatives) are taken into account by the algorithm in order to decide what content is displayed to them. But some of the theories regarding possible inputs were clearly farfetched (sometimes <a href="https://www.nngroup.com/articles/technology-myths/">technology myths</a>) and reflected the lack of transparency in the algorithm. For example, one user noted:</p>

<blockquote>

<p><em>“This is interesting and creepy — yesterday I was talking about craving pho, which I normally don't eat, and now I see this [ad for a] pho burrito; I wonder if they just record your conversations." </em></p>

</blockquote>

<p>Upon seeing an ad for Hawaiian Airlines, a participant said, half joking and half serious, <em>“Maybe they know I need a vacation."</em>  And yet another one: “<em>Ever since I got pregnant, I get ads about pregnancy, baby stuff, and life insurance.”</em></p>

<p>Thus, lack of transparency in the input makes users suspicious — they assume that almost every one of their actions (whether online or in the real world) is taken into account by the algorithm and they end up believing that the systems are more “creepy” and intrusive than they are in reality. Such a perception is facilitated by the rising concerns about privacy and an awareness of the vast amounts of data that companies like Google and Facebook are in control of.</p>

<p>Google News users were generally pleased with the successful personalization that the app did for them, but they were also not sure what types of data it was based on.  A participant said:</p>

<blockquote>

<p><em>“This [the Google News app] seems to be catered to me and my interests […] — the fact that there’s three articles related to cars, which […] is the kind of topic I am interested in. It would be interesting to know how the</em> For you<em> page is generated. […] It’s got my local stories, so it obviously knows my location, that’s pretty handy.”</em></p>

</blockquote>

<p>While Uber does not make recommendations per se, it reputedly uses machine learning to predict demand and create incentives for drivers in the form of price surges, promotions, and gamification (for example, Uber drivers can take advantage of ‘quests’ that give them an extra gain when they drive a certain number of rides within a designated timeframe). The Uber algorithm is not based on driver actions per se; instead, its inputs are likely mostly external data such as historical traffic patterns. Yet, even in this case, a clear understanding of the input had some say in whether drivers were persuaded by some of the promotions or not. For example, one driver was notified that he needed to drive 15 minutes to pick up a passenger located at 2.3 miles away and that a premium was possible. He said:</p>

<blockquote>

<p><em>“This is an irritating new feature. I think that in the past you used to get only 5 minutes rides [to pick up passengers], but this one says 15 minutes distance and premium is possible. I had that before and it didn’t happen. I am guessing it’s just a way to entice drivers to go a long distance without getting a fare.[…] I don’t like that possible premium.”</em></p>

</blockquote>

<p>Not understanding why the premium was offered and what it was based on made the driver suspicious about Uber’s intentions.</p>

<h2 id="toc-lack-of-control-of-the-output-4">Lack of Control of the Output</h2>

<p>In all the systems we looked at, the output depended not only on the users’ actions but also on external events such as other people’s postings, news stories, new movie releases, or traffic. This wide variety of data made it even more difficult to understand how the algorithm could be controlled and to isolate the effects of the user’s own actions from those of third-party actions.</p>

<p>When a set of relevant items has been determined based on some automated prediction, often the order in which those items is displayed and whether they are displayed at all are dictated by a <strong>relevancy metric</strong>: items with a high relevancy are displayed first, followed by less relevant items. If relevancy is below a certain threshold, the item may not be shown at all.  (Netflix displayed this relevancy metric explicitly in the form of a match score. The metric itself was of no direct interest to users — people in our study completely ignored this score).</p>

<p>While one could argue that a good relevancy metric should not place important items low on the list, the truth is that these systems gather only fragmentary information about the users, who are complex individuals whose needs depend not only on past habits but also on context and even mood. (For example, one participant said <em>“I wish there’s a way to hide all the sad posts on Facebook.”</em> And some posters may be of high interest, but very infrequent, so the system may not be able to accumulate enough data about their relevancy.) So it is very possible that even good relevancy metrics would fail to predict relevancy correctly — at least occasionally.  </p>

<h3>Issues Due to Imperfect Relevancy Metrics</h3>

<p>There are a few issues that arise due to imperfect relevancy metrics:</p>

<h4>Items of Interest Are Left Out</h4>

<p>In information-retrieval terms, this amounts to <strong>low recall.</strong></p>

<p>Leaving out a high-relevancy item can be costly for users. On sites like Facebook and Instagram, missing a post by one of your closest friends can cause annoyance and deteriorate the experience. The fact that newsfeeds on these sites contained only a subset of the new posts was a major nuisance for our participants. One participant said, “<em>I need to fight with the algorithm to get the accounts that I want to see to show up.</em>” People attempted to steer the algorithm according to their (often incorrect or fragmented) mental model of how the system worked. Some engaged (through the <em>Like </em>button) with all the posts from those pages they were interested in, with the hope to convince the algorithm to not miss those posts again. The meaning of <em>Like</em> thus went beyond its original literal and social connotations (liking something used to indicate appreciation of the content or of the poster) and started to become construed as a way to assert some control over the algorithm.</p>

<p>Even those who thought they could manipulate the algorithm often were suspicious of their effectiveness. They kept visiting directly the newsfeeds of those people or organizations they were interested in to make sure they did not miss content.</p>

<p>Leaving out a high-relevancy item is not always as costly. For example, on Netflix or Spotify, there are thousands of items that are potentially of high interest to users; leaving one out is unlikely to cause people to complain</p>

<h4>Unpredictable Ordering of Items</h4>

<p>Missing an item that is important to a user can happen not only because the algorithm did not include it in the list of results, but also because it did not include it high enough on the list. Ultimately, this concern is related to the <strong>attention economy</strong>: if people have a finite quantity of attention that they can deploy to news or social media, then items that are important to them may be missed simply because they were placed too low on the output list.</p>

<p>With some of the recommender systems that we saw, <strong>the ordering of the recommendations had no meaning</strong> for the user: people did not understand why a certain post on their Facebook feed was shown before another one, nor did they know why a movie was shown before another one in a Netflix carousel.</p>

<p>A common complaint on Facebook, Instagram, and Google News was that <strong>the order of stories was not chronological</strong>. Because of that, it was not easy to predict whether you’ve seen everything from a person or you may have missed some posts. Similarly, with news, participants were worried that interesting-to-them stories of less importance (such as a car-related article) may come first in a long list and may make them miss recent general-interest news items.</p>

<p>In the case of Netflix, the ad-hoc categories in which the recommendations were structured (e.g., <em>Because you watched…, Top </em>picks) obscured natural categories that people have already formed of the domain. For example, with video content, a common concern is time (e.g., users may know they only have 1 hour to watch) or the type of show. Yet, in the Netflix-created categories, TV shows are mixed with full-length movies and presented in no recognizable order without <a href="https://www.nngroup.com/articles/visual-indicators-differentiators/">differentiating markers</a>, and people have no easy way of filtering them out.</p>

<h4>Low-Interest Recommendations</h4>

<p>In information-retrieval terms, this amounts to<strong> low precision.</strong></p>

<p><strong>Bad suggestions are costly for the users’ attention </strong>— they must <em>inspect</em> them, <em>identify</em> them as irrelevant, and <em>skip</em> past them. However, the cost of a bad suggestion is not always the same across different types of systems. With Netflix’s list-of-carousels layout, a bad suggestion can be relatively easier to ignore — an uninteresting movie does not take up too much space on the page and people can move around it easily</p>

<figure class="caption"><img alt="Netflix homepage" height="464" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/13/netflix-2.png" width="624"/>

<figcaption><em>Netflix: A bad recommendation takes relatively little space in the list layout; people can easily ignore it.</em></figcaption>

</figure>

<p>On systems like Spotify or StichFix (a clothing-shipping service), users cannot ignore a bad suggestion — they cannot simply sit and listen to a song they don’t like or wear a pair of pants that is not their style. Facebook is somewhere in between: an irrelevant post or ad takes space on the page and requires people to scroll past it.</p>

<figure class="caption"><img alt="A Patagonia ad on Facebook" height="758" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/13/facebook-patagonia.png" width="350"/>

<figcaption><em>An irrelevant ad on Facebook may take up the whole viewport and requires more effort to ignore than a bad movie suggestion on Netflix.</em></figcaption>

</figure>

<p><strong>The cost of ignoring a bad suggestion will dictate how likely people are to directly provide feedback on the item</strong>. For example, on Spotify, they will engage with the system and rate the bad item not only in order to tune the algorithm, but also to save themselves from sitting through a song they don’t like.On Facebook, we did notice users engaging occasionally with the <em>Hide ad </em>button, but because it was hidden under a menu, some perceived that it was not worth doing it. Instead of down-rating poor recommendations, people focused on <em>Like-</em>ing good suggestions.</p>

<figure class="caption"><img alt="Facebook more button associated to an ad" height="758" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/13/facebook-ghide-ad.png" width="350"/>

<figcaption><em>Facebook: Few users took advantage of the </em>Hide<em> ad option that was hidden under the </em>More<em> button.</em></figcaption>

</figure>

<p><strong>The more real estate (or time to process) taken by a piece of recommended content, the more prominent a feedback button should be.</strong> If recommended content can be easily ignored, the method for providing feedback can be secondary.</p>

<h3>Personalization Should Not Increase User Effort</h3>

<p>We saw above that, in the user experience, the most successful recommendation algorithms were those that were able to convey users a reasonable mental model of the inputs they used. In particular, our study participants loved Netflix’s <em>Because you (watched/added to list/ etc.)… </em>suggestion lists.</p>

<p>However, a problem with such approaches is that the same item may end up being recommended multiple times. For example, a movie that is included in a <em>Because you watched</em> …  list can also appear in <em>My List</em> or in <em>Top picks</em>. <strong>People have to spend extra effort when they encounter these duplicate items</strong> because, at a minimum, they have to recognize that they have seen them before and move over. One user commented:</p>

<blockquote>

<p>“<em>Why have various lists and keep duplicates? I hate these duplicate lists. I go over it and see the same things I have seen before and it annoys me, ‘cause I feel it’s such a waste of time…”</em></p>

</blockquote>

<figure class="caption"><img alt="" height="619" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/13/neflix-nina-simone.png" width="350"/>

<figcaption><em>Netflix: The same movie (“What happened Miss Simone?”) appeared both under </em>Suggestions For You<em> and under the </em>Jazz &amp; Easy Listening<em> lists.</em></figcaption>

</figure>

<p>But duplication of effort is not restricted to repeated items only. Netflix admits going beyond content personalization and creating an individualized (and even session-specific) <a href="https://medium.com/netflix-techblog/learning-a-personalized-homepage-aa8ec670359a">homepage layout</a> and <a href="https://medium.com/netflix-techblog/artwork-personalization-c589f074ad76">personalized cover art</a> for videos.</p>

<p>Both these types of personalization can increase <a href="https://www.nngroup.com/articles/interaction-cost-definition/">interaction cost</a>.</p>

<h3><strong>Session-Specific Thumbnails, Descriptions, and Headings</strong></h3>

<p>Personalizing how a piece of content is presented to a specific user can go a long way in capturing attention. Our study participants were presented with a plethora of content, and they scanned through it quickly, glancing at the thumbnails and reading 1–2 words of text here and there. A Facebook user said, ““<em>I don't normally even read what people wrote; I just skim through it,” </em>while a Netflix user commented that <em>“I look for stuff that is different and interesting, and the cover art calls my attention.” </em></p>

<p>On Netflix, not only will two different users see different thumbnails for the same movie (e.g., “Empire Games”), but the same user may see different thumbnails for the same movie in two different sessions.</p>

<figure class="caption"><img alt="" height="450" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/13/netflix-chappaquid.png" width="500"/>

<figcaption><em>Netflix: The same user saw different thumbnails for the movie Chappaquiddick in different sessions.</em></figcaption>

</figure>

<p>In theory, this practice may increase the chance of the person liking the movie and watching it — since different aspects of the movie will be emphasized in different sessions, one of them may capture the user’s attention. Unfortunately, this inconsistency also makes the movie less memorable and wastes user time: people may end up visiting the movie-detail page and checking the description multiple times, only to discover that they are still not interested or that they have already added that movie to their watch list.</p>

<h3><strong>Session-Specific Layouts</strong></h3>

<p>Netflix also personalizes the layout of the homepage according to user, session, and device. Thus, <em>Continue watching</em> may appear very close to the top of the page for one user in one session, or could be lower on the page in the next session. This practice is an example of an adaptive interface and limits <a href="https://www.nngroup.com/articles/power-law-learning/">learning</a> of the page layout. Thus, users who prefer to start their browsing with checking the new additions may need to actively look for the <em>Recently added </em>list and will not benefit from having located that list in previous sessions. Because Netflix is such a browse-heavy interface, changing the order of the different lists of suggestions did not have a significant impact on our user pool; however, in general, this practice has been shown to significantly downgrade the user experience.</p>

<h2 id="toc-recommendations-5">Recommendations</h2>

<p>We looked at a fairly limited number of systems that are heavily dependent on machine-learning algorithms to present content to users. Here are some of the lessons learned:</p>

<ul>

<li><strong>Strive to create an accurate mental model of the algorithm</strong>. Be transparent about which of people’s actions can contribute to the output of the algorithm.</li>

<li>Give people <strong>easy controls over the output</strong> of the machine-learning algorithm. Allow them to sort or reorganize the output in ways familiar or natural to them. The higher the cost of a bad recommendation, the easier it should be to give feedback to the system.</li>

<li>Don’t <strong>duplicate content</strong> if it fits into multiple categories.</li>

<li><strong>Personalize to individual users</strong> and then stick with that personalized design; be cautious about personalizing at the session level and changing the UI under the user from one visit to the next.</li>

<li>Pick <strong>visual attributes</strong> that are likely to engage users, since they are very important when people have to consume large amounts of content.</li>

<li><strong>Frontload descriptions</strong> and headlines to support the scan of large amounts of data.</li>

</ul>

<p>Following these 6 UX guidelines will increase the likelihood that AI moves beyond a fancy technology to actively supporting users and increasing their satisfaction with the quality of their experience</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Designing AI Experiences" href="/courses/designing-ai-experiences/?lm=machine-learning-ux&amp;pt=article">

<h4 class="title heading-small">Designing AI Experiences</h4>

<p id="designing-ai-experiences" class="description body-small">

Design innovative, trusted, and useful AI products and features

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-ai" />

</svg>

<p class="ux-specialty artificial-intelligence">Artificial Intelligence</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="Accelerating Research with AI" href="/courses/research-with-ai/?lm=machine-learning-ux&amp;pt=article">

<h4 class="title heading-small">Accelerating Research with AI</h4>

<p id="accelerating-research-with-ai" class="description body-small">

The AI-assisted user research workflow

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-ai" />

</svg>

<p class="ux-specialty artificial-intelligence">Artificial Intelligence</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="AI for Design Workflows" href="/courses/ai-for-design/?lm=machine-learning-ux&amp;pt=article">

<h4 class="title heading-small">AI for Design Workflows</h4>

<p id="ai-for-design-workflows" class="description body-small">

Leverage AI to enhance creativity, efficiency, and impact in everyday design work

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-ai" />

</svg>

<p class="ux-specialty artificial-intelligence">Artificial Intelligence</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">machine learning,Artificial Intelligence,Human Computer Interaction,mental models,personalization</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Artificial Intelligence</span>

<a class="ga-article-related-topic" href="/topic/ai/">Artificial Intelligence</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

</ul>

</div>

</div>

</div>

</div>