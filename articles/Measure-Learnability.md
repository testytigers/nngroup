# How to Measure Learnability of a User Interface - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">8</span>

<div class="article-header">

<h1 class="article-h1">How to Measure Learnability of a User Interface</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Alita Kendrick</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/alita-kendrick.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/alita-kendrick/">

Alita Kendrick</a></span>

<p class="publication-date">

October 20, 2019

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2019-10-20</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: How to Measure Learnability of a User Interface&amp;body=https://www.nngroup.com/articles/measure-learnability/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/measure-learnability/&amp;title=How to Measure Learnability of a User Interface&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/measure-learnability/&amp;text=How to Measure Learnability of a User Interface&amp;via=nngroup" data-share-type="Twitter">

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

</span>To measure learnability, determine your metric, gather your data, and plot the averages on a line curve. Analyze the learning curve by looking at its slope and its plateau.

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

<a class="ga-article-toc-item" href="#toc-what-is-learnability-1">What Is Learnability?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-learnability-vs-efficiency-2">Learnability vs Efficiency</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-why-measure-learnability-3">Why Measure Learnability?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-running-a-learnability-study-4">Running a Learnability Study</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-5">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-what-is-learnability-1">What Is Learnability?</h2>

<p>Learnability is one of the <a href="https://www.nngroup.com/articles/usability-101-introduction-to-usability/">five quality components of usability</a> (the others being efficiency, memorability, errors, and satisfaction). Testing learnability is especially valuable for complex applications and systems that users access frequently, though knowing how quickly users can acclimate to your interface is valuable for even objectively simple systems.</p>

<p><strong>Learnability considers how easy it is for users to accomplish a task the first time they encounter the interface and how many repetitions it takes for them to become efficient at that task.</strong></p>

<p>In a learnability study, we want to produce a <a href="https://www.nngroup.com/articles/power-law-learning/">learning curve</a>, which reveals longitudinal changes of a quantified aspect of human behavior. With the data from the learning curve, we can identify how long it takes users to reach saturation — a plateau in our charted data which tells us that users have learned the interface as much as possible.</p>

<p>For example, let’s say we are redesigning an enterprise file-backup application intended to be run by IT administrators on a regular basis. We assume users will use the application frequently enough that they will progress up that learning curve. For such an application, it is crucial that users be able to complete their work as fast as possible. In this scenario, a learnability study will determine how fast administrators learn to run a backup efficiently. We recruit several representative users and invite them to the lab. Then we ask them to perform the backup and measure how long they take to do so for the first time. Next, we ask them to come back into the lab and do the task for a second time — again, measuring their task-completion time. This process repeats for several more times. The result of our study will be a learning curve which plots the task time over a set number of trials. </p>

<div style="text-align:center">

<figure class="caption" style="display:inline-block"><img alt="Learning curve with average time on task decreasing across six trials and a saturation point reached at the fourth trial." loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/18/filebackup.png" width="693"/>

<figcaption><em>This learning curve shows the hypothetical completion time for a backup as a function of the number of task repetitions (or trials). Notice that the time for the first repetition is longest, and then the completion time decreases — by trial 4, it levels off, reaching the saturation plateau. Although details such as how many repetitions are needed to reach saturation will vary from case to case, this learning curve is representative of all human learning.</em></figcaption>

</figure>

</div>

<h2 id="toc-learnability-vs-efficiency-2">Learnability vs Efficiency</h2>

<p>There are 3 different aspects of learnability, each of which is important to different kinds of users:</p>

<ul>

<li><strong>First-use learnability</strong>: How easy is it to use the design the first time you try? This aspect of learnability is of interest to those users who will only perform the task once. These users won’t progress up the learning curve, so they don’t care how it looks.</li>

<li><strong>Steepness of the learning curve:</strong> How quickly do people get better with repeated use of the design? This facet of learnability is particularly important for users who will use the design multiple times, even though they won’t use it excessively. If people feel that they are progressing and getting better and better at using your system, they’ll be motivated to stick with it. (And conversely, if people feel that it’s hardly getting better, no matter how hard they try, they’ll start looking for a better solution.)</li>

<li><strong>Efficiency of the ultimate plateau:</strong> How high is the productivity that users can reach with this interface, once they have fully learned how to use it? This aspect is particularly important for people with a frequent and long-lasting need to use the system — for example, when it’s the main tool for important everyday tasks.</li>

</ul>

<p>Ideally, of course, your system should fare well on all 3 aspects. But, in the real world, design tradeoffs are often necessary, and you should shape the learning curve to cater mostly to those users who have the highest business value.</p>

<p>The relative importance of these dimensions also depends on the stages in the users’ lives. New users want to be able to learn the system quickly and get to the point of optimal (plateau) performance as soon as possible, but expert users want the plateau to be as low (i.e., the optimal task time as short) as possible.</p>

<p>Sometimes these different attributes of learnability may pull the design in different directions. For instance,<strong> a learnable system is not always efficient</strong>. Coming back to our  example, let’s assume that the backup was performed through a step-by-step <a href="https://www.nngroup.com/articles/wizards/">wizard</a> workflow with a lot of instructions and explanations. This system may be highly learnable: users may be able to perform the task as fast as possible even as they complete it for the first time. But the curve would be pretty much flat: they would not be able to perform it much faster the second time, as they would need to go through the same screens and answer the same questions.   As users become well-versed in the interface, this design will feel like hand-holding and will be inefficient for repeated use. (It is for this reason that we recommend implementing <a href="https://www.nngroup.com/videos/flexibility-efficiency-use/">accelerators</a>, or process shortcuts, for expert users.) Designers must carefully balance learnability and efficiency.</p>

<div style="text-align:center">

<figure class="caption" style="display:inline-block"><img alt="Learning curve with average time on task consistent across all six trials." loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/18/backupwizard.png" width="692"/>

<figcaption><em>This learning curve shows the hypothetical completion time for a backup application with a wizard flow as a function of the number of task repetitions (or trials). Notice that, despite the increase in trials, the task time stays steady around 16 minutes. This system is learnable but not efficient.</em></figcaption>

</figure>

</div>

<h2 id="toc-why-measure-learnability-3">Why Measure Learnability?</h2>

<p>High learnability contributes to usability. It results in quick system onboarding which translates to low training costs. Additionally, good learnability can result in high satisfaction because users will feel confident in their abilities.</p>

<p><strong>If your system and corresponding tasks are complex and ones that users access frequently, your product may be a good case for a learnability study</strong>. Learnability studies are time and budget consuming, so don’t pitch them haphazardly to stakeholders. It wouldn’t make sense to measure learnability for tasks which users complete infrequently or one time (for example, signing up for a service or filing annual taxes) because users will most likely behave like new users each time they encounter the task. In these cases, a standard <a href="https://www.nngroup.com/articles/quant-vs-qual/">usability test</a> would be better suited and more cost-effective than a learnability study.</p>

<h2 id="toc-running-a-learnability-study-4">Running a Learnability Study</h2>

<p>In learnability studies, we’re focused on gathering metrics, which is why we turn to <a href="https://www.nngroup.com/articles/quant-vs-qual/">quantitative research</a> methods. This sort of study requires focused tasks and controlled experiments, and therefore <strong>quantitative usability testing is best suited for studying system learnability</strong>.</p>

<h3>Participants</h3>

<p>In running this type of study, we’re trying to determine how easily people learn our interfaces. Therefore, it is important to <strong>gather participants with little to no experience</strong> using the system that they’ll be testing.</p>

<p>One consideration when it comes to testing learnability is prior experience with similar systems. Prior experience may help users (for example, because they may be already familiar with domain conventions) or may slow them down (for example, because they may suffer from <a href="https://www.nngroup.com/videos/users-hate-change/">change aversion</a>).  However, this data is still valuable, especially when launching a new product with the goal to steal customers away from existing products. When applicable, recruit participants with no similar system experience <em>and</em> participants with some similar-system experience, and plan to compare corresponding data from both groups.</p>

<p>As for any <a href="https://www.nngroup.com/articles/quantitative-user-research-methods/">quantitative study</a>, we recommend that you <a href="https://www.nngroup.com/articles/quantitative-studies-how-many-users/">recruit a fairly large number of participants</a> (usually at least 30–40). The exact number will depend on the complexity of your task, with highly complex tasks requiring more participants to account for the inherently higher data variability, and simpler tasks requiring fewer participants.</p>

<h3>Step 1: Determine the Metric</h3>

<p><strong>Time on task is the most commonly collected metric for learnability studies</strong>. The reason is the <a href="https://www.nngroup.com/articles/power-law-learning/">power law of learning</a>, which says that the time it takes to complete a task decreases with the number of repetitions of that task. The rest of this article will assume you’re collecting time on task as the primary metric.</p>

<p>Depending on your system, time on task might not be relevant and therefore you need a different metric. In these situations, consider collecting the <strong>number of errors </strong>users make for a given task.</p>

<h3>Step 2: Determine the Number of Trials</h3>

<p>The next step consists of deciding how often to collect these metrics — each instance of data collection is known as a trial.</p>

<p>Remember, we’re trying to plot this metric over time, so we need to have the <strong>same participants complete the same task multiple times</strong>. We recommend you <strong>repeat the trials until a plateau is</strong> <strong>reached.</strong> A flattened curve indicates our participants have learned the system (specific to this task) as much as possible.</p>

<p>When considering trials, there are two questions you may be asking: how many trials should I run? And how far apart should the trials be? The answer to both of these questions depend on your circumstances.</p>

<p>To predict the number of trials needed for a user to reach a point of saturated learning, consider your system complexity. As a starting point, consider 5–10 trials but when in doubt, <strong>plan for more trials than you think you need</strong>, for two reasons: (1) you want to be sure that you’ve reached stable performance and (2)  once you’ve reached a point of stable performance, it’s generally easier to cancel usability sessions than to schedule more.</p>

<p>If you’re wondering how much time is necessary between trials, consider how often you anticipate your customers to use the product and match that interval as closely as possible. For a task that users perform daily or a few times a week, you can have trials on consecutive days. But for tasks done once a month you may want to leave 4 weeks between trials.  </p>

<h3>Step 3: Gather and Plot the Data</h3>

<p>Remember to <a href="https://www.nngroup.com/articles/recruiting-test-participants-for-usability-studies/">recruit</a> the same participants for each trial and have them complete the same task(s) in each trial. (This is different than the normal case, where you want <a href="https://www.nngroup.com/videos/using-usability-test-participants-multiple-times/">different test users to study different iterations</a> of a design.) You may want to run a learnability study and test with multiple tasks. If this is the case, be sure to randomize your tasks to avoid biasing your results. In research studies, users take what they know from one task and apply it to future tasks; task randomization helps to mitigate this effect.</p>

<p>For each task, <strong>calculate the metric averages for each trial</strong> and plot them on a line graph with labeled axes. By plotting the data for each trial, you will obtain the learning curve for that task.</p>

<h3>Step 4: Analyze the curve</h3>

<p>As with any quantitative study, you will want to analyze the data for statistical significance. In other words, you will have to investigate whether the trial effect was indeed significant — namely, whether the drop that you see in your learning curve is real or is just the result of noise in the data. Usually, the statistical method involved will be fairly simple — a <a href="https://en.wikipedia.org/wiki/One-way_analysis_of_variance">one-way repeated-measures ANOVA</a> with trial as the factor.</p>

<p>Once you’ve done your analysis (and presumably found that the trial effect was significant), consider the big picture: What is the slope of your learning curve? Less-learnable interfaces have relatively small drops in the curve and take many trials to reach a point of saturation. Alternatively, highly learnable systems have curves that are steep and drop quickly and reach the saturation point after fewer repetitions.</p>

<p>For example, in our original file-backup example, it took users 4 trials to reach the saturation plateau and become efficient. That may seem acceptable. On the other hand, if it took them 30 trials to reach that same point, the learnability will likely be too low.</p>

<p>Also, consider the final efficiency: is it acceptable that, once users have learned how to perform the task, it will take them 10 minutes? The answer may depend on what that number is for competitor products. If a competitive analysis isn’t viable, you can also compare the findings to costs and <a href="https://www.nngroup.com/articles/usability-roi-declining-but-still-strong/">ROI</a>. If an administrator spends 10 minutes a day to complete a backup task in an optimal way and performs the task daily for a year, this amounts to 3650 minutes or approximately 60 hours. At a cost of $100 per hour, it means that the company will spend $6000 for completing the backups. Whether that amount is acceptable or may need to be lowered (by improving the design) will depend on the specifics of each product.</p>

<h2 id="toc-conclusion-5">Conclusion</h2>

<p>The learnability of a product tells us how fast users reach optimal behavior with that product. It is important to measure learnability for UIs that get used relatively frequently. A learnability study involves repeated measurements of the same participants completing the same task. The result of a learnability study is a learning curve that will uncover how many repetitions are needed in order for users to complete the task efficiently.</p>

<p>Even if you don’t conduct a complete learnability research project to plot the full learning curve, thinking about these concepts will help you make the trade-off decisions to design products that target your most important customers.</p>

<p>For more on design tradeoffs, like learnability versus efficiency, check out our course, <a href="https://www.nngroup.com/courses/design-tradeoffs/">Design Tradeoffs and UX Decision Frameworks</a>.</p>

<p> </p>

<h3>References</h3>

<p>Tom Tullis, Bill Albert (2013) <em>Measuring the User Experience: Collecting, Analyzing, and Presenting Usability Metrics</em>. Morgan Kaufmann.</p>

<p>Allen Newell, Paul Rosenbloom (1980). <a href="http://repository.cmu.edu/cgi/viewcontent.cgi?article=3420&amp;context=compsci"><em>Mechanisms of skill acquisition and the law of practice</em></a><em>. </em>Technical Report. School of Computer Science, Carnegie Mellon University.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Persuasive and Emotional Design" href="/courses/persuasive-emotional-design/?lm=measure-learnability&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=measure-learnability&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Measuring UX and ROI" href="/courses/measuring-ux/?lm=measure-learnability&amp;pt=article">

<h4 class="title heading-small">Measuring UX and ROI</h4>

<p id="measuring-ux-and-roi" class="description body-small">

Use metrics from quantitative research to demonstrate value

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

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Human Computer Interaction,Psychology and UX,quantitative studies</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/psychology-and-ux/">Psychology and UX</a>

</li>

</ul>

</div>

</div>

</div>

</div>