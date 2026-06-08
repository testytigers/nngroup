# Why Most Product Teams Aren't Really Empowered

**Author:** Laura KleinLaura KleinJanuary 9, 20262026-01-09

**Topics:** Managing UX Teams, Agile

**Source:** https://www.nngroup.com/articles/teams-arent-empowered/

---

January 9, 20262026-01-09

Share

We've all heard the promises. Empowered teams make better products. They're more engaged, more innovative, and they ship faster. According to Marty Cagan's definition in his bookEmpowered, truly empowered product teams are "given problems to solve rather than features to build" and have "the authority to decide the best way to solve those problems." They're accountable for outcomes, not outputs.

Sounds great, right? But the uncomfortable truth is that most teams aren't empowered, despite what the company handbook says. And it's not usually because leadership is lying or being intentionally manipulative. It's because empowerment is often incompatible with how most large organizations work.

Imagine a product manager at a mid-sized fintech company whose team is supposedly empowered to improve the onboarding experience. They've done their research, identified several significant problems, and have some great solutions. One of them involves changing the mainnavigationto make it easier for new users to find critical features.

Simple fix, right? Just change the nav.

Except it turns out that the navigation component is shared across several different product areas, each with its own team. Each team has its own roadmap, metrics, and stakeholders. The PM spends six weeks just trying to schedule meetings with all the relevant teams to discuss the change. Three of them have upcoming releases that would break if the nav changed. Five more have their own planned nav changes that conflict with the proposal. Two teams are convinced that any change to the nav will hurt theirconversionmetrics.

By month three, there's a 47-page document outlining the proposed changes, the business case, the technical approach, the rollout plan, and the mitigation strategies for every team's concerns. Fourteen separate meetings have happened. Compromises on top of compromises have been made. The elegant solution the team had designed is now a Frankenstein's monster that will sort of help new users but won't really solve the core problem.

This is the scale problem.When you have dozens of teams working on the same product, everybody genuinely can't just do their own thing. The promise of empowerment crashes into the reality of shared systems, shared components, and shared screens.

The scale problem gets worse when you look at how teams are structured within the organization. In theory, empowered teams should be organized around customer problems or user journeys. In practice, they're often organized around whatever makes sense from an engineering or org-chart perspective.

Consider a large ecommerce company where:

None of these teams can make a meaningful improvement to the product-detail page without coordinating with the others. The reviews team can't test moving reviews higher on the page because it doesn't control anything else on the page. It can't improve how reviews integrate with the purchase flow because that's owned by the cart team. It can't even change thevisual designof the reviews section without considering how it will look next to components owned by the other teams.

So, what problems can this team solve?It can optimize the sort order of reviews. It canA/B testdifferentfilteringoptions. It can micro-optimize one little rectangle of the screen within very narrow parameters.

The team is empowered to make decisions, technically, but their decisions that don't matter very much.

Even when teams are reasonably well-structured, dependencies between various product components destroy autonomy. Products are systems, and systems have interdependencies.

Consider a company that has built a marketplace connecting healthcare providers with patients. One team works on the provider-scheduling system. Another team works on the patient-booking experience. A third team handles notifications and reminders.

The provider team wants to launch a new feature that would let doctors block off time for administrative work. It designs the feature, builds it, and prepares to launch it.

Then someone asks, “What happens when a patient tries to book an appointment during a doctor's admin time?”

The patient-booking team needs to update the availability logic. But it’s in the middle of launching its own feature — aBook with next available provideroption that would automatically match patients with whoever has the earliest opening.

Now the features are in conflict.If a doctor blocks off admin time, will the autobooking- system accidentally schedule patients during that time? What will the notification team send in that case? An appointment confirmation? A booking error?

The provider team can't launch without the booking team updating its code. The booking team can't guarantee its feature will work correctly until the provider team's changes are live. The notification team is stuck waiting for both to figure it out.

Now we have three different empowered teams, all blocked by each other. No one has done anything wrong. The product just has inherent dependencies that no amount of team autonomy can eliminate.

One thing that makes all this even harder is that companies want certainty. Executives, boards, and investorsall want to know what's being built and when it will be done.They want to make strategic plans, allocate resources, and coordinate across the business.

Sales needs release dates for new features to retrain staff. Customer service requires advance notice of upcoming changes to prepare support scripts. Marketing needs time to plan campaigns.

Butempowered teams are often working iteratively based on feedback and experimentation. They change direction based on what they learn from users. They pivot when something isn't working. If they release something that doesn’t meet the metric they set for it, they can keep working on it until it improves. They're supposed to be flexible and responsive.

Certainty conflicts with iteration.You can't have teams that are empowered to build whatever they discover is most valuable and also have certainty about what will be built six months from now.

Most companies resolve this tension by choosing certainty. They createroadmaps, they set quarterly goals, and they make commitments. Then they call the teams "empowered" while simultaneously telling them exactly what features need to ship by when.

The certainty demand gets worse when leadership has specific strategic directions they want to pursue. Countless product managers have shared some version of this story in the last two years:

"My team did research and discovered our users' biggest problem. We designed a solution. We were ready to build. Then leadership announced that this year's strategic priority is AI. Every team needs to add AI features to their product area. Our users don't need AI for this problem. AI doesn't help solve this problem.But we're building an AI feature anywaybecause that's the company strategy."

This happens constantly, not just with AI. It could just as easily describe mobile-first mandates, platform initiatives, internationalization pushes, security improvements, or pivots to subscription-based services. These are often legitimate business needs, but they come from the top and override whatever the empowered team has discovered about users' actual problems.

The team is empowered to choose how to implement the AI feature, but it’s not empowered to decide whether an AI feature is what it should be building in the first place.

This is where everything comes together into a user-experience nightmare. When you have dozens of empowered teams, each optimizing its own metrics and building its own features, you get a product that feels like it was designed by dozens of different companies.

One team's area uses amodal dialogfor confirmations. Another team uses an inline message. A third team navigates to a new page. The buttons saySubmitin one place,Savein another, andContinuein a third. Thetoneof themicrocopyvaries wildly from formal to casual. One feature uses a three-stepwizard, another uses a single long form, a third uses a conversational interface.

Users don't see teams. They don't see component boundaries. They just see a confusing, inconsistent product that seems to have been designed by people who never talked to each other, because, in a sense, it was.

Each team was empowered to make the best decisions for their area, and it did!But nobody was empowered to maintain coherence across the whole experience.

All this creates an impossible situation for product managers. In theory, PMs on empowered teams should spend their time understanding users, identifying opportunities, and making strategic decisions. In practice, theyspend most of their time serving as the connective tissue that holds the entire fractured system together.

Picture a PM who spends 70% of her time in meetings coordinating with other teams, getting buy-in for a small change, negotiating priorities, trying to align roadmaps, escalating conflicts, chasing down dependencies, and attending working groups created to solve coordination problems.

She spends a tiny fraction of her time with users. The rest is spent writing documents that explain her team's work to other teams, updating roadmaps, reporting status, and attending planning meetings.

She was hired to be a strategic product thinker, but she's become a project manager, focused entirely on logistics and coordination. This isn’t because she's bad at her job, but because that's what the organization requires to ship anything at all.

This is what happens when you try to layer empowered team structures on top of products that are inherently interconnected. The coordination cost gets pushed onto individuals who have to personally manage the complexity that the organization structure created.

This all sounds pretty grim. But understanding why teams aren't empowered is the first step to getting more autonomy, even in imperfect situations.

Luckily, there are things you can do to make this process work better. It’s never going to work exactly like a tiny “two-pizza team” at a startup building something from scratch, but you can still have strategic impact, even when your team isn’t fully autonomous and empowered.

As you’ve probably noticed, the problems with empowered teams scale with the size of the company. At a certain point, if all the teams are working on different parts of the same product, things simply get too complex for any team to get much done across the whole organization.

An alternative is to shift from product-centric design, in which companies divide work at the level of interface components, tojourney-centric design, where the focus is on the end-to-end user journey across different channels and touchpoints. Our reportArchitecting a Journey-Management Practicedocuments how businesses of different sizes are addressing the challenges of developing a journey-centric design practice across industries.

Of course, this approach does conflict somewhat with the concept of individually empowered teams where each group is given a problem to solve or a metric to hit and given freedom to do so. In the end, it is a tradeoff you may have to make between allowing teams to be fully autonomous and having a product with a more consistent and holistic user experience.

You probably can't eliminate all dependencies on other teams within your company, but you can choose to work on problems that have fewer of them. When evaluating opportunities, consider not just the impact and effort, but also how many other teams you'll need to coordinate with. Sometimes the slightly less impactful project that you can build independently is better than the high-impact project that requires two years of coordination and may never get shipped.

Don't wait until you need something from another team to start talking to them. Understand what they're working on, what their constraints and metrics are. When you eventually need help, you'll be asking a colleague instead of interrupting a stranger, and you’ll have a much better idea of the size of the request you are making.

If you're blocked because five teams need to align on something, be the person who gets them aligned. Create the shared document, facilitate the decision, and do the work to coordinate. Yes, this feels like it shouldn't be your job, but being the person who makes coordination happen gives you influence over what gets coordinated.

If your team's metrics are misaligned with broader company outcomes, you'll always be fighting an uphill battle. Work with leadership to add metrics that capture what actually matters, even if they're harder to move. If you're measured solely on your team's local metrics, you'll be incentivized to make locally optimal decisions that hurt the broader product.

When you make decisions, when you learn something about users, when you discover constraints, write it down in a place other teams can find it. This reduces the coordination tax over time. Teams won't need to ask you basic questions if the answers are already documented. You won't need to explain your rationale in meeting after meeting if it's written down somewhere.

You can't fight every top-down mandate. Sometimes "add AI to everything" is the hill the company is going to die on, and you're not going to change that. But you can influence how it's implemented. You can ensure that the AI feature you're forced to build helps users, even if it wasn't what they needed most. Save your political capital for the fights that you can win.

Don't just optimize your area in isolation. Understand how your work affects other teams' metrics and priorities. Proactively identify conflicts before they become problems. Propose solutions that work for multiple teams simultaneously. The more you think about the whole system, the more strategic influence you'll have.

The best way to get more autonomy is to consistently ship things that work and that drive business results. Teams that execute well get more trust and more freedom. If your team has a reputation for making good decisions and shipping quality work, you'll find that coordination gets easier and you get more latitude to pursue the opportunities you think matter most.

Maybe you can't choose what problem to solve, but can you choose how to solve it? Maybe you can't control the roadmap, but can you control the prioritization within a feature? Maybe you can't change what gets built, but can you influence the release strategy or the rollout plan? Look for the spaces where you do have agency and use them strategically.

True team empowerment is rare because it requires a level of organizational coherence and trust that most companies don't have. But that doesn't mean you're helpless. Understanding the real constraints you're operating under – the legitimate coordination challenges, the necessary dependencies, the business needs for certainty — lets you work more strategically within those constraints.

You might not be able to make your team fully empowered and autonomous, but you can probably become more empowered than you are today. And sometimes, in a large and complex organization, that's the best we can hope for.

M. Cagan, 2020.Empowered,Hoboken: Wiley.

Understand UX and product roles (PM and PO) to better collaborate in product development

Management

Define, share, and implement design operations

Management

Empower and guide UX and product teams to reach their full potential

Management