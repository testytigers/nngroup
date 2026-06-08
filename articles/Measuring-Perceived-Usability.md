# Beyond the NPS: Measuring Perceived Usability with the SUS, NASA-TLX, and the Single Ease Question After Tasks and Usability Tests - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">9</span>

<div class="article-header">

<h1 class="article-h1">Beyond the NPS: Measuring Perceived Usability with the SUS, NASA-TLX, and the Single Ease Question After Tasks and Usability Tests</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Page Laubheimer</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2022-portrait-page-3.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Page Laubheimer

</span>

<p class="publication-date">

February 11, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-02-11</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Beyond the NPS: Measuring Perceived Usability with the SUS, NASA-TLX, and the Single Ease Question After Tasks and Usability Tests&amp;body=https://www.nngroup.com/articles/measuring-perceived-usability/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/measuring-perceived-usability/&amp;title=Beyond the NPS: Measuring Perceived Usability with the SUS, NASA-TLX, and the Single Ease Question After Tasks and Usability Tests&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/measuring-perceived-usability/&amp;text=Beyond the NPS: Measuring Perceived Usability with the SUS, NASA-TLX, and the Single Ease Question After Tasks and Usability Tests&amp;via=nngroup" data-share-type="Twitter">

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

</span>Post-test questionnaires like the SUS measure perceived usability of an entire system; post-task scales suggest problematic parts of a design.

</div>

<div class="article-body">

<p>During usability testing, UX researchers often ask participants to provide a subjective assessment (usually in the form of a rating) of their experience using a product or a site. Instruments such as the SUS, NPS, or the task-difficulty question are among the most popular choices. However, for many new UX practitioners, the precise purpose of these tools (and the correct way to administer and analyze them) is often mysterious. What do they truly assess, and what’s the proper methodology for using them? When should they be administered — in-between tasks or at the end of the session, and why does that matter? Why would you use one of the standard questionnaires rather than create your own?</p>

<p>All these questionnaires represent self-reported <a href="https://www.nngroup.com/articles/quant-vs-qual/">quantitative data</a>; they are rarely meaningful by themselves, with no performance data (such as success rates or task times) to complement them. The format for all these questionnaires is usually a <strong>rating</strong> <strong>scale</strong>: the participant is given a question, and asked to select an answer, typically on 5- or 7-point scales (<a href="https://www.nngroup.com/courses/measuring-ux/">we don’t recommend using a scale with more than 7 options).</a> The actual method of collecting the data is straightforward: the questions can be administered on paper by the test facilitator, or using a digital survey tool (which is the typical method used in remote unmoderated testing). However, knowing when and why to use which questionnaire is much more elusive for many budding test facilitators.</p>

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

<a class="ga-article-toc-item" href="#toc-post-task-vs-post-test-questionnaires-1">Post-Task vs Post-Test Questionnaires</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-the-system-usability-scale-sus-post-test-assessment-of-usability-2">The System Usability Scale (SUS): Post-Test Assessment of Usability</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-single-ease-question-seq-post-task-satisfaction-3">Single Ease Question (SEQ): Post-Task Satisfaction</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-nasa-tlx-post-task-workload-4">NASA-TLX: Post-Task Workload</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-limitations-of-these-metrics-5">Limitations of These Metrics</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-summary-6">Summary</a>

</li>

</ul>

</div>

</div><h2 id="toc-post-task-vs-post-test-questionnaires-1">Post-Task vs Post-Test Questionnaires</h2>

<p>There are two categories of questionnaires used during usability testing:</p>

<ol>

<li><strong>Post-task questionnaires</strong> are completed immediately after finishing a task and <strong>capture participants’ impressions of that task</strong>. When each task is followed by one such questionnaires, there will usually be many subjective answers collected from each user, since there are usually <a href="https://www.nngroup.com/articles/task-scenarios-usability-testing/">many individual tasks</a> in a usability-study session.</li>

<li><strong>Post-test questionnaires </strong>are administered at the end of a session (or after the participant has finished all the tasks pertaining to a site). They <strong>reflect how your users perceive the usability of your website or app as a whole</strong> (i.e. what their lasting, overall impressions are). User impressions of the experience as a whole are subject to the <strong>peak-end effect</strong> (that is, the most intense and last parts of the experience, either positive or negative, impact participants’ recollections and evaluations the most).</li>

</ol>

<p>Post-task and post-test questionnaires aren’t incompatible; in fact, in most quantitative studies, it’s useful to collect both. (But be careful about tiring out your participants!) While these metrics do correlate fairly strongly, it’s not a perfect relationship; one type of quantitative data gives us a rather limited picture of the overall usability of the system, and the more metrics, the clearer the picture we can develop.</p>

<p>Both these types of instruments are indicators for the current state of the subjective user experience; you can use them to compare your current design against future iterations (or known industry benchmarks). These <a href="https://www.nngroup.com/articles/quant-vs-qual/">metrics do <strong>not</strong> tell you why</a> users struggle with your design, <a href="https://www.nngroup.com/articles/risks-of-quantitative-studies/">nor do they provide direct insights as to how you can improve it</a>. They simply are a way of keeping track of how your users feel about the experience of using your product.</p>

<p>It is critical to note that these questionnaires are quantitative instruments, and therefore they require <a href="https://www.nngroup.com/articles/quantitative-studies-how-many-users/">larger sample sizes</a> (typically at least 20–30 users) to be confident that their results generalize. Collecting quantitative data with small sample sizes (such as the <a href="https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/">5 users we typically recommend</a> during formative, qualitative usability testing) will almost certainly not generate statistically significant findings. However, if you combine a subjective rating scale with the follow-up question, <em>Why did you give [site X] a score of [Y]?</em> you can derive useful qualitative insights into what people feel about the design, even if you only test a handful of users. (Just don’t make a big deal about the average score.)</p>

<p>In most cases, we recommend using standard questionnaire over homegrown ones, since the former are supported by a lot of research to <em>demonstrate</em> their <strong>validity</strong> (that they actually measure what they intend to measure), <strong>reliability</strong> (that users will consistently answer the questions in the same way), and <strong>sensitivity</strong> (that they can detect meaningful differences).</p>

<h2 id="toc-the-system-usability-scale-sus-post-test-assessment-of-usability-2">The System Usability Scale (SUS): Post-Test Assessment of Usability</h2>

<p>The most well-known questionnaire used in UX research is the System Usability Scale (SUS). The SUS has been around since the command-line interface days of the 1980s, and has been repeatedly demonstrated experimentally to be valid and reliable. It was invented by John Brooke at Digital Equipment Corporation. The SUS is a post-test instrument, given to a participant after an entire usability testing session is over (or, when testing multiple sites, like in <a href="https://www.nngroup.com/articles/competitive-usability-evaluations/">competitive evaluations</a>, after the participant has worked on all the tasks related to a site).</p>

<figure class="caption"><img alt="SUS questionnaire showing all 10 Likert-scale questions" height="902" loading="lazy" src="https://media.nngroup.com/media/editor/2017/12/18/sus.png" width="700"/>

<figcaption><em>The System Usability Scale is a post-test questionnaire containing 10 different questions that address the usability and learnability of a system. Do not alter the order or the wording of the SUS questions if you want to compare your score with the scores collected from other designs.</em></figcaption>

</figure>

<p>The SUS is a series of 10 Likert-scale questions and produces a score from 0–100. However, the 0–100 score is <strong>not equivalent</strong> to a percentage score, such as on an exam — Jeff Sauro has done extensive <a href="https://measuringu.com/sus/">benchmarking of SUS scores</a> on many different systems, and has found an average SUS score of 68 across 500 studies. For your site’s usability to be in the top 10% of all sites, you would need a score of 80 or higher, whereas a score of 73 would place you only in the top 30%.</p>

<p>One of the biggest advantages to using the SUS is that it’s such an old scale that there is a large amount of industry-wide data available to help benchmark your score and understand it in context of your peers and competitors — something that less widely used survey instruments can’t provide. Be aware that the <a href="https://measuringu.com/usability-loyalty/">SUS correlates strongly</a> with a much simpler metric, the single-question <a href="https://www.nngroup.com/articles/nps-ux/">Net Promoter Score</a>. They do provide different data, but for many organizations, the NPS may be more useful overall, as it’s a simpler metric to collect (one question versus SUS’s 10), and is a well-established general bellwether for the company (even if it’s not as sensitive to UX-focused concerns).</p>

<h2 id="toc-single-ease-question-seq-post-task-satisfaction-3">Single Ease Question (SEQ): Post-Task Satisfaction</h2>

<p>In contrast to the SUS, post-<em>task</em> questionnaires are administered at the end of every task in a test session. They are useful for two big reasons:</p>

<ol>

<li>They allow you to compare which parts of your interface (or workflows) are perceived as most problematic, since you collect this data after <em>every</em> task.</li>

<li>Since the task itself just concluded, it’s fresh in the participant’s mind, and therefore she is more able to provide a clear indication of her attitude toward the experience, without subsequent tasks coloring her memory.</li>

</ol>

<p>Post-task questionnaires need to be short (1–3 questions) to interfere as little as possible with the flow of using the site in a testing session.</p>

<p>There are several widely used questionnaires in use; in most cases a <a href="https://www.nngroup.com/articles/keep-online-surveys-short/">single question instrument</a> is the right fit for quantitative usability testing, because it takes little time and effort for participants to answer it after a task and is minimally disruptive. Since <a href="https://www.nngroup.com/articles/time-budgets-for-usability-sessions/">time with users is precious</a>, it’s best to use an efficient survey instrument. More rating questions only give you marginally more insights than what you derive from a single question, so it’s better to invest your time budget in other activities, such as additional test tasks, than to ask more subjective-rating questions.</p>

<p>The “Single Ease Question” (<a href="https://measuringu.com/papers/Sauro_Dumas_CHI2009.pdf">SEQ</a>) is a useful and simple version of this idea that has been experimentally validated and demonstrated as reliable, valid, and sensitive. The SEQ asks the user to rate the difficulty of the activity they just completed, from <em>Very Easy</em> to <em>Very Difficult</em> on a 7-point rating scale.</p>

<figure class="caption"><img alt="Single ease question rating scale" border="0" height="101" loading="lazy" src="https://media.nngroup.com/media/editor/2017/12/18/seq.png" width="700"/>

<figcaption><em>The Single Ease Question, (SEQ) a single-question post-task questionnaire measures users’ perception of usability based on the last attempted task. Since the task is still fresh in the participants’ minds, their answer provides a useful assessment of the experience for that particular task.</em></figcaption>

</figure>

<p>The finer granularity of post-task questionnaires may suggest that they could generate more actionable findings for design teams than the coarser finding of the user’s overall impressions through a post-test instrument. However, there is less data available for comparing your SEQ results with those from other companies (and the tasks being compared would need to be comparable anyway), so you’re mainly restricted to finding out what tasks are relatively easier or harder within your own system.</p>

<h2 id="toc-nasa-tlx-post-task-workload-4">NASA-TLX: Post-Task Workload</h2>

<p>The <a href="https://humansystems.arc.nasa.gov/groups/TLX/index.php">NASA-TLX</a> (Task Load Index) is another type of post-<em>task</em> questionnaire that is useful for studying complex products and tasks in healthcare, aerospace, military, and other high-consequence environments. It tends to be used less frequently in UX work, but it is the standard questionnaire used by many studies in Human Factors and Ergonomics. The NASA-TLX emerged in the 1980s, as a result of NASA’s efforts to develop an instrument for measuring the perceived workload required by the complex, highly technical tasks of aerospace crew members.</p>

<p>The NASA-TLX contains 6 questions that users must answer on an unlabeled 21-point scale, ranging from <em>Very Low</em> to <em>Very High. </em>Each question addresses one dimension of the perceived workload: mental demand, physical demand, time pressure, perceived success with the task, overall effort level, and frustration level. After this initial assessment, users weigh each one of the six categories they just completed, to indicate which category mattered most to what they were doing. It’s a complex instrument to score, but thankfully NASA has released the TLX as a <a href="https://itunes.apple.com/us/app/nasa-tlx/id1168110608">free iOS app</a>.</p>

<figure class="caption"><img alt="NASA TLX Instrument, showing each of the 6 unnumbered rating scales" border="0" height="789" loading="lazy" src="https://media.nngroup.com/media/editor/2017/12/18/tlx.png" width="600"/>

<figcaption><em>The NASA-TLX instrument asks participants to rate each task they have performed on these 6 scales, each in 21-point increments. It provides rich data about what sorts of demands the task had on the user in multiple different areas, but requires time and expertise to collect during a study. Image from the official NASA-TLX <a href="http://humansystems.arc.nasa.gov/groups/tlx/tlxpaperpencil.php">paper and pencil worksheet</a>.</em></figcaption>

</figure>

<p>While the NASA-TLX is often used as a key metric in human factors studies about complex, mission-critical systems, it can also be used in other types UX research, with a few caveats:</p>

<ol>

<li>It’s a relatively complex questionnaire that needs to be answered after every key task, and so will add a lot of time (and potential participant fatigue) to the overall test process.</li>

<li>It can disrupt the study flow and make the experience quite a bit less natural for participants than if they progress smoothly through a test scenario.</li>

<li>It will often require that the facilitator explain the instrument multiple times (particularly with things like the difference between <em>effort</em> and <em>mental demand</em>, for example).</li>

<li>It is mostly helpful when studying situations where human errors are highly undesirable (healthcare, transportation, complex financial domains, and so forth).</li>

</ol>

<p>Because of the complexity of this instrument, it’s not typically a good match for UX studies of consumer products or simple workflows. For <a href="https://www.nngroup.com/courses/application-ux/">highly complex processes</a>, performed by trained workers, where users cannot choose which <a href="https://www.nngroup.com/courses/application-ux/">application</a> they use and errors have high consequences, the NASA-TLX is the questionnaire of choice. Like the SUS, the NASA-TLX has published many studies and industry benchmarks to help you understand the scores in context, and to be able to meaningfully compare them to those of competitors.</p>

<h2 id="toc-limitations-of-these-metrics-5">Limitations of These Metrics</h2>

<p>All the various satisfaction metrics discussed in this article suffer from the following limitations:</p>

<ol>

<li>They are self-reported data, which can be <a href="https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/">unreliable</a>.</li>

<li>They measure subjective user perception, not objective performance. While there is some <a href="https://www.nngroup.com/articles/satisfaction-vs-performance-metrics/">correlation between satisfaction and objective performance</a> metrics (like task completion rates, time on task, or errors), satisfaction metrics usually tell a clearer story when combined with performance metrics.</li>

<li>These metrics tell you what the user’s satisfaction level was, but do not pinpoint any weaknesses or strengths of the experience (or what you can change to improve it). Moreover, each participant may have a wildly different sense of what a 5 out of 7, for example, means.</li>

<li>Like all quantitative metrics, low sample sizes (like the 5 users we typically recommend for each round of qualitative usability testing) are unlikely to provide statistically significant or meaningful results. <a href="https://www.nngroup.com/articles/quantitative-studies-how-many-users/">Numeric data from 5 users</a> should not inform design decisions, and reporting numbers collected with such a small sample is highly misleading.</li>

</ol>

<h2 id="toc-summary-6">Summary</h2>

<p>Self-reported data that addresses users’ satisfaction and perception of usability is often collected in quantitative studies together with other types of performance measures. Three popular instruments are: the post-test System Usability Scale (SUS), which provides helpful information about a user’s takeaways and overall experience; the post-task Single Ease Question (SEQ), which offers information about the usability of different task flows; and the post-task NASA-TLX, which is appropriate for measuring workload in complex, mission-critical tasks. Since all of these are quantitative measures, they require a reasonably large sample size to provide valid measurements.</p>

<p>For <strong>most</strong> practical UX research, we recommend simple satisfaction questionnaires, with as few questions as possible. The question to ask depends on your research goals:</p>

<ol>

<li>In most <strong>formative, qualitative studies:</strong>

<ul>

<li>Ask <em>How satisfied were you with this website? </em>plus the follow-up question of <em>Why did you give a score of [X]?</em> This will give you <strong>insights</strong> into whatever aspects of the user experience matters most to your users’ satisfaction, which is the main thing to learn from subjective user feedback.</li>

<li>If you’re specifically interested in the <strong>usability of the individual components</strong> of the UI, use the Single Ease Question after each task and ask users to explain their score. (However, usually it’s more accurate to judge the usability of design elements through direct observation than from subjective scores.)</li>

</ul>

</li>

<li><strong>For summative quantitative studies </strong>meant to benchmark the usability of your site (either by comparing it with its other design iterations, or with competitors):

<ul>

<li>In most cases, use the SUS after the test and the SEQ after each task, as satisfaction metrics to complement other performance metrics such as success rates and time on task.</li>

<li>If you have the special case of complex, mission-critical workflows, replace the SEQ with NASA-TLX.</li>

</ul>

</li>

<li>If you want to assess the<strong> business </strong>impact of your user experience, ask the NPS question, <em>How likely are you to recommend this website to a friend?</em></li>

</ol>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Analytics and User Experience" href="/courses/analytics-and-user-experience/?lm=measuring-perceived-usability&amp;pt=article">

<h4 class="title heading-small">Analytics and User Experience</h4>

<p id="analytics-and-user-experience" class="description body-small">

Study your users’ real-life behaviors and make data-informed design decisions

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

<a class="tile ga-article-related-course" data-course-title="Measuring UX and ROI" href="/courses/measuring-ux/?lm=measuring-perceived-usability&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="Statistics for UX" href="/courses/ux-statistics/?lm=measuring-perceived-usability&amp;pt=article">

<h4 class="title heading-small">Statistics for UX</h4>

<p id="statistics-for-ux" class="description body-small">

Calculate, interpret, and report the numbers from your quantitative UX studies

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Analytics &amp; Metrics,quantitative studies,Research Methods,surveys,facilitating research</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Analytics &amp; Metrics</span>

<a class="ga-article-related-topic" href="/topic/analytics-and-metrics/">Analytics &amp; Metrics</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/research-methods/">Research Methods</a>

</li>

</ul>

</div>

</div>

</div>

</div>