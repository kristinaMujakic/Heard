# Submissions grouped by teams

team_alpha_submissions = [
    {
        "id": 1,
        "message": "I often face communication issues with my team, which affects my work. It would be better if my manager helps improve team collaboration."
    },
    {
        "id": 2,
        "message": "I need more training in our new software tools to become more efficient at work."
    },
    {
        "id": 3,
        "message": "I find it challenging to meet tight deadlines. It would help if we have better time management strategies within the team."
    },
    {
        "id": 4,
        "message": "I would be more productive if I had a quieter workspace."
    },
    {
        "id": 5,
        "message": "Improved feedback from my manager would help me grow in my role."
    }
]

team_bravo_submissions = [
    {
        "id": 6,
        "message": "I often face communication issues with my team, which affects my work. It would be better if my manager helps improve team collaboration."
    },
    {
        "id": 7,
        "message": "I need more training in our new software tools to become more efficient at work."
    },
    {
        "id": 8,
        "message": "I find it challenging to meet tight deadlines. It would help if we have better time management strategies within the team."
    },
    {
        "id": 9,
        "message": "I would be more productive if I had a quieter workspace."
    },
    {
        "id": 10,
        "message": "Improved feedback from my manager would help me grow in my role."
    }
]

team_charlie_submissions = [
    {
        "id": 11,
        "message": "Our team lacks clear project objectives, making it hard to focus our efforts effectively."
    },
    {
        "id": 12,
        "message": "I struggle with maintaining work-life balance and need support in this area to avoid burnout."
    },
    {
        "id": 13,
        "message": "The constant flow of meetings disrupts my workflow and makes it challenging to concentrate on tasks."
    },
    {
        "id": 14,
        "message": "Our communication channels are scattered, causing information to get lost and affecting our team's efficiency."
    },
    {
        "id": 15,
        "message": "I'd appreciate more training opportunities to enhance my skills and contribute effectively to the team."
    }
]

team_delta_submissions = [
    {
        "id": 16,
        "message": "Our team struggles to adapt to new technology tools, which hinders our productivity."
    },
    {
        "id": 17,
        "message": "I face difficulties understanding the company's long-term goals and how my work contributes to them."
    },
    {
        "id": 18,
        "message": "I feel isolated working remotely and miss the social interactions we had in the office."
    },
    {
        "id": 19,
        "message": "The lack of a dedicated feedback system makes it hard for employees to provide input on the company's direction."
    },
    {
        "id": 20,
        "message": "Our team needs a more organized task management system to keep everyone on the same page and meet deadlines consistently."
    }
]


# Team data with summarized blockers
teams = [
    {
        "id": 1,
        "name": "Team Alpha",
        "summarized_blockers": "Faces communication challenges affecting their collaborative efforts. Employees report that without designated time to meet, they don't have context of when their managers may be busy or available for inquiries. This leads to them feeling like they are bothering their managers and not being sure when a good time is. They also mention that they might miss out on communication from teams working on adjacent projects, causing them to feel siloed and uncertain about where their work fits into the larger picture at the company.",
        "submissions": team_alpha_submissions
    },
    {
        "id": 2,
        "name": "Team Bravo",
        "summarized_blockers": "Encounters communication issues that impact their work. They express concerns about not having designated time to meet, making it challenging to understand when their managers are available. This can lead to employees feeling like they are bothering their managers and not being sure when it's a good time. Additionally, they mention that they might miss out on communication from teams working on adjacent projects, causing them to feel isolated and unsure about their work's place within the larger company context.",
        "submissions": team_bravo_submissions
    },
    {
        "id": 3,
        "name": "Team Charlie",
        "summarized_blockers": "Deals with communication challenges that hinder their work. They report that without designated time to meet, employees lack context about their managers' availability, making them unsure about when it's appropriate to inquire. This can lead to employees feeling like they are bothering their managers. They also express concerns about potentially missing communication from teams working on adjacent projects, leading to a sense of isolation and uncertainty about their work's alignment with the larger company goals.",
        "submissions": team_charlie_submissions
    },
    {
        "id": 4,
        "name": "Team Delta",
        "summarized_blockers": "Experiences communication obstacles that hinder their collaborative efforts. Team members mention that they lack designated meeting times, leading to uncertainty about when their managers are available. This sometimes makes them hesitant to seek assistance from their managers. They are also concerned about missing out on communication from adjacent project teams, resulting in a sense of isolation and uncertainty about their roles in the company.",
        "submissions": team_delta_submissions
    }
]


# Communication tools data
communication_tools = ["Regular check-in meetings (daily, weekly)", "Work chat (Slack)",
                       "Email", "Microsoft Teams", "Task forces", "Group presentations to leadership"]

# Possible solutions/features data
possible_solutions = [
    "Use of reminders",
    "Notifications via email and/or team chat (e.g., Slack)",
    "Screenshotting the issue",
    "Ability to validate issues (voting)",
    "Ability to share solutions (comments)",
    "Creating a task force",
    "Action plan with a time frame",
    "An indicator of the level of urgency to prioritize",
    "Asynchronous feedback",

]

# Additional comments data
additional_comments = [
    "IDEA: Software like ChatGPT for internal work documents, procedures, protocols, inquiries, 'how-to's' to speed up the process of searching for work-related information buried in different files/folders/intranet pages.",
    "Both users mentioned social disconnect as a major challenge in remote work, difficulty building rapport with new employees, missing micro-interactions as most communication is strictly business. Virtual happy hours aren't successful due to different time zones.",
    "Biggest strategy is to get people to write stuff down and use asynchronous communication instead of meetings. Eventually, you get into a cycle where most of your work is async, and you have better control of your time.",
]
