# It’s Time We Addressed Time-Zone Selectors

**Author:** Maria Rosala, Kelley GordonMaria RosalaandKelley GordonDecember 11, 20222022-12-11

**Topics:** Application Design

**Source:** https://www.nngroup.com/articles/time-zone-selectors/

---

December 11, 20222022-12-11

Share

Time-zone selectors allow users to change the local time on a UI. They are commonly found in scheduling features, in the user-settings section of an application or website, and on websites that support live, virtual events — like our own. This article discusses findings from our research about how best to design a time-zone selector.

Before jumping into the topic, it’s important to clarify some important terminology:

Usually, time zones are presented in a list such as adropdown menu. Such a list could technically be sorted in several different ways:

Designing time-zone selectors can be tricky because:

Understandably, this is not a fun task for users. Participants in our recent research openly shared:

“This is something that I hate doing in [sic] most websites.”

“​​I hate time zones. I hate having to select the time zone. I don't know why they always go wrong, especially when it comes to scheduling for me.”

“I'm terrible with time zones, like really bad.”

When reviewing some popular time-zone selectors, we found many different design approaches.

To understand the best method of ordering and presenting time-zone selectors, we conducted:

We wanted to learn:

We used UserInterviews.com to recruit participants for both studies. For our remote, unmoderated study, we recruited 83 people (42 men and 41 women, median age 37) from 4 countries: Australia (21 participants), the United States (22 participants), Germany (20 participants), and the United Kingdom (20 participants). We recruited from these 4 countries to control for and study any differences in behavior and familiarity with time zones across different geographical regions.

We ran 2 rounds of moderated tests using think-aloud protocol.

Participants were invited to complete a 10-minute remote, unmoderated study in one sitting and were askednotto reference their phone or another browser tab during the study. The study was hosted on UserZoom.com.

The study began with a short questionnaire that included some questions about the participant’s location and time zone. Participants were also asked to rate their familiarity with certain time zones. Following the questionnaire, participants were given two tasks. In each task they had to find their time zone. One task displayed a search field and the other a dropdown. The order of the tasks was randomized.

To understand the effect of grouping time zones by continent, we randomly assigned participants to one of two conditions: grouped (in which time zones in the dropdown were grouped by continent) and ungrouped (in which time zones were ordered by offset with no grouping). We recorded participants’ time on task as the dependent variable.

As participants completed the tasks, their screen and audio were recorded, allowing us to identify any participants who cheated (by referring to another browser tab), experienced technical issues or disruptions, didn’t attempt the task, or had issues with the remote-testing software. These data points were removed or corrected.

Participants were asked to write their current time zone in a text field. We analyzed and checked the responses and found thatmost participants (73%) knew their own time zone, sharing time zones such asPacific TimeorEuropean Central Time. A small proportion (18%) shared the offset (e.g.,UTC -3) rather than — or in addition to — a time zone. Interestingly, 3 of the 83 participants did not know their time zone or guessed their time zone incorrectly.

We wanted to know whether participants knew their offset. In our initial review of time-zone selectors, we found that some designers chose to useGreenwich Mean Time(GMT) over UTC, so we wanted to explore whether one was more recognizable than the other. (Although GMT is a time zone, it is often used as a time standard since GMT’s offset is equal to UTC+0.)

We asked all our participants to identify the offset for their location in UTC and in GMT. The order of each question was randomized. 1 participant cheated by looking up their offset and so was excluded. Only a third of our 82 participants (34%) knew their time-zone offset in UTC, whereas over half of our participants knew their time in GMT (55%). This difference was statistically significant (p<.001). Given that GMT originated in the UK and the UK’s time zoneisGMT for half of the year, we analyzed this difference by country. We found that the difference was statistically significant (p<.01) only for UK participants. In other words,displaying offsets in GMT, rather than UTC, helped only the UK-based participantsand did not benefit people from the other 3 countries.

We also asked participants to rate the familiarity of GMT and UTC.Participants rated GMT as more familiar than UTC. The average familiarity rating for GMT was 3.6 (where 1 wasnot at all familiar, and 5 wasvery familiar), whereas the average familiarity rating for UTC was 2.3. This difference was statistically significant (p<.001). Even when removing UK participants, the average familiarity rating for GMT (3.2) was higher than UTC (2.3). This difference was statistically significant (p<.01). This means, while displaying offsets in GMT doesn’t necessarily help non-UK audiences locate their offset more accurately, seeing offsets expressed as GMT may seem more familiar to users.

Despite GMT being rated as more familiar, almost half of our participants did not know their offset, which meanscommunicating the offset alone is not enough. Many participants commented that they didn’t know much about offsets:

“I never pay attention to these.”

“I'm not sure, honestly never had to think of UCT (sic) or GMT as time zones or the meaning of the letter initials themselves”

“I know it’s Chicago/Central, but that’s all I know”

As participants interacted with the dropdown organized by offset, they struggled to find their time zone in the list and many participants from all countries in our studiesexpected the list to be ordered alphabetically.

“I found it strange that it was grouped by kind of like location rather than alphabetical order.” Australian participant in our unmoderated testing

“I would have thought it would have been in alphabetical order as opposed to it didn't seem to be in any order. Actually, it was in order of UTC (....) I would expect [London to be under] L (…) halfway through the lot.” UK participant in our unmoderated testing

“It was difficult because they are not how I expected it to be because it wasn't sorted alphabetically, which is normally the case, but it was sorted based on the time zone.” German participant in our unmoderated testing

“I've used a lot of these dropdowns before. Like I think it's on Google calendar and I have to scroll down the whole list to find a city because most of the time, I don't really know the GMT time for each city. I don't even know. I think for Paris it may be plus one, but I'm not, never even that sure.” French participant in our moderated testing

“I think I prefer that [being organized alphabetically] because that's a more familiar grouping to me than the time zones (....) ‘Cause I don't know the times on offhand and the other one assumes that I would know that. And it's just like more mental gymnastics to stop and pause looking for it when it's sorted by time zone versus by alphabet.” US participant in moderated testing

“So, it comes up with the time zone first and then the location. Okay, so this is where I have to do some more thinking in my head, in my opinion, just because I need to work out, which time zone I’m in, which usually isn't very hard because UK, London time is zero usually, but we've just put our clocks forward, which means we're plus one, but I have to go through this thinking process in my head.”  UK participant in moderated testing

Based on our findings, we recommend youavoid organizing time zones by offset. If you do organize by offset, list the offset first to help users quickly understand how the list is ordered. When we presented participants with time zones ordered by offset but had the offset trailing the time zone, participants did not understand how the list was ordered. One participant from the UK could not understand the ordering and felt she had to look through every entry.

“So, this one is it's not even alphabetical. What is it? Yes, it's alphabetical until you get to… No, it's just a mishmash; slightly alphabetical but not properly. You've got to look at every single entry, which is scattered all over the world…”

When we gave participants the task to use a dropdown to find their time zone, we deactivated the search field so that participants had to scroll. Nearly all our participants tried to search the dropdown and either expressed dissatisfaction when this was not possible or wished they could search.

“It would be really cool if I can just search for it, you know?” Participant from UAE in our moderated session

Since time-zone lists are long, users find it more efficient to perform a search for the time zone (if they know it).

“I think having the search bar at the top is very helpful. I think that’s just going to besomething I would use firstbefore scrolling through this window to find, you know, where I am in America.” US participant in one of our moderated sessions.

Several participants mentioned that they do a lot of tasks that require them to use time-zone selectors on their phones and search helps a lot with these tasks.

If possible,provide a search field within the dropdown. Most users will use this functionality to locate their time zone, rather than scrolling through the dropdown. Make sure that the search field is visible so that the functionality is discoverable — for example, by showing the search field as an "option” at the top of the dropdown field when that field is selected.

In addition to these specific recommendations for implementing search within the dropdown field, manysearch best practicesapply, such as displayingsearch suggestionsorfiltering the dropdown in real timeas the user types.

In the search task, we provided a search field with the dropdown deactivated (so participants couldn’t inspect the list or scroll through it) and asked participants to find their time zone. We analyzed the type of query that was first executed by participants.The most-common first query was a city.

Despite cities being the most popular search term, they may not always be the most successful search strategy. The 33 participants who used a city as a search strategy made on average 2.5 search attempts. This was because sometimes a city was not in the list of time zones, and so users had to execute a different, often broader, search query to find their time zone.

Not all your users will live in a central city or know the right city for their time zone, so it’s a good idea toallow users to also search by country (and state if possible).

“So, I knew that by typing in ‘Brisbane’, I’d probably find it given I live in the capital city. I think if I didn’t live in Brisbane, I’d just go ‘Australia’ and then navigate through that way.” Australian participant in moderated testing

Showing the country and offset (alongside the city)can provide extra confirmationthat the selected time zone is the correct one.

“Maybe there would be a need for the country because I know Adelaide because I’ve lived in Australia for 10 years, but I think most people wouldn’t really know. So maybe [...] it would be nice to have the confirmation: ‘[Adelaide], Australia’; ‘Lisbon, Portugal’.” French participant in moderated testing

Given that many people know their time zone (like Pacific Time) and some use it as a search strategy,you can also provide common time zonesas discrete options or alongside cities, such asNew York (Eastern Time).However,don’t use the time zone and offset alone(e.g., Pacific Time,GMT-8). While most participants in our study knew their own time zone, users might not know the time zone (or offset) of another location.

In our remote unmoderated test, we compared two offset orders: onegrouped by continent and one with no grouping. In the grouped condition, the time zones were ordered by continent first (with continents listed in alphabetical order), then, within each continent, they were ordered by offset. In the ungrouped condition, the time zones were ordered by offset. The search functionality was removed so that participants had to scroll to find their time zone. An equal number of participants from each country were randomized to either the grouped or ungrouped condition.

We asked participants to find their time zone from the dropdown and we recorded how long it took them. The median completion time for the 37 participants successful in the grouped condition was 39 seconds, and the median completion time for the 40 participants successful in the ungrouped condition was 47 seconds. This difference was not statistically significant. Since each participant’s time zone would appear in a different place in the list, we compared the relative speed to select a correct time zone by dividing the time on task by the participant’s time zone’s position in the dropdown. The relative median time for the grouped condition was 0.29 seconds and the relative median time for the ungrouped condition was 0.52 seconds. This difference was statistically significant (p<.001). This means thatwhen time zones were ordered by offset,grouping helped participants to find their time zone more quickly. Since participants struggled to locate their time zone when time zones were ordered by offset, the presence of grouping may have helped participants locate the right area of the dropdown quicker.

Many participants commented that theyliked seeing the time zones grouped by continent. For example, an Australian participant commented:

“I do like how it’s sorted by region. That makes it a lot easier than if it was just all the cities in the world put on the list. So, it is good that it’s broken down by region…”

A participant from the UK who had dyslexia mentioned that she found the grouped dropdown easier to scan because of the added spacing.

Some participants from Europe and the US expressed dissatisfaction with the grouping; this was because our grouped dropdown had continents and regions ordered alphabetically, which resulted in participants from Europe and the US needing to scroll past continents like Africa, Asia, and Australasia first. Some participants commented that they would like to see their continent first or higher up the list. We did not test placing the most popular continents first. Had we done so, it’s possible that these participants may have found their time zone earlier in the dropdown.

If you do pursue grouping time zones, consider who your main audience is.Place continents or regions that most of your customers are in at the top of the list, like in Google’s or Calendly’s time-zone selectors.

One limitation of our analysis is that we did not test grouping in alphabetically ordered time-zone selectors, and so we don’t know whether grouping helps participants locate their time zone faster in such cases.

Many participants wished they could see their time zone highlighted in the dropdown as they first interacted with it. “I wish this was smart enough to find my geolocation or at least guess,”a Danish participant in our moderated testing said.

To do this, either present the location as a default in the dropdown field and allow users to change it or have the dropdown automatically scrolled to the point of the user’s location and show the location shaded in the list.

There are many ways to design a time-zone selector. Here’s a summary of our research findings:

Given our research, we recommend the following when designing time-zone selectors:

Components, design patterns, workflows, and ways of interacting with complex data

Interaction

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

Interaction

Essential UX design principles for small-screen websites and apps

Interaction