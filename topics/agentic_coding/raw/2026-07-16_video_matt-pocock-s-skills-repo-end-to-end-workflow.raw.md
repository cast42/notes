---
type: source
date: 2026-07-16
timestamp: 2026-07-16
source_url: "https://youtu.be/M6mYodf0dJM"
canonical_url: "https://youtube.com/watch?v=M6mYodf0dJM"
resource: "https://youtube.com/watch?v=M6mYodf0dJM"
title: Matt Pocock’s skills repo — end-to-end workflow
author: Matt Pocock
handle: mattpocockuk
created_at: 2026-07-16
topics: [agentic_coding]
tags:
  - agent-skills
  - context-engineering
  - specification-driven-development
  - code-review
description: "Timestamped automatic-caption transcript for Matt Pocock's end-to-end skills repository tutorial."
content_hash: 550eeee6bd1fdfae3c70d0da1eaf70d44c33a507fd4353a90944b3dcff0e07f3
extracted_at: "2026-07-16T20:22:35"
extractor: youtube-auto-captions
---

# Raw content

Source: https://youtube.com/watch?v=M6mYodf0dJM


1
00:00:00,000 --> 00:00:04,360
Hello friends, it occurs to me that I've

2
00:00:01,640 --> 00:00:06,360
never actually put together a proper

3
00:00:04,360 --> 00:00:09,040
tutorial for my skills repo. At the time

4
00:00:06,360 --> 00:00:12,760
of recording this repo is up to 162,000

5
00:00:09,040 --> 00:00:14,120
stars. We have 7.5 million downloads and

6
00:00:12,760 --> 00:00:15,600
I've never made a tutorial for it. I get

7
00:00:14,120 --> 00:00:17,520
questions all the time like what is the

8
00:00:15,600 --> 00:00:18,960
sequence I should use these skills in,

9
00:00:17,520 --> 00:00:20,360
how should I install them, how should I

10
00:00:18,960 --> 00:00:22,840
set them up? So this video is going to

11
00:00:20,360 --> 00:00:25,000
be a walk through of the main flow you

12
00:00:22,840 --> 00:00:26,120
use when you're using these skills.

13
00:00:25,000 --> 00:00:27,360
We're not going to look at the advanced

14
00:00:26,120 --> 00:00:29,320
stuff, we're not going to look at the

15
00:00:27,360 --> 00:00:31,280
new stuff really, we're just going to

16
00:00:29,320 --> 00:00:33,080
focus on the main flow. The stuff you

17
00:00:31,280 --> 00:00:34,600
need to get started. To walk you through

18
00:00:33,080 --> 00:00:37,160
this, I'm going to be using one of my

19
00:00:34,600 --> 00:00:38,760
work repos which is the AI Hero CLI.

20
00:00:37,160 --> 00:00:41,440
This is the command line interface that

21
00:00:38,760 --> 00:00:43,040
drives a lot of my exercises that I use

22
00:00:41,440 --> 00:00:44,720
on my courses. I've never actually set

23
00:00:43,040 --> 00:00:46,320
up my skills to work with this repo so

24
00:00:44,720 --> 00:00:48,040
now is a great chance. If you want to

25
00:00:46,320 --> 00:00:49,520
set up my skills on a brand new project,

26
00:00:48,040 --> 00:00:51,240
you just do this except you do it in an

27
00:00:49,520 --> 00:00:52,680
empty directory. So it works the same

28
00:00:51,240 --> 00:00:54,440
whether you're using a brownfield code

29
00:00:52,680 --> 00:00:55,960
base or a greenfield code base. I'm

30
00:00:54,440 --> 00:00:58,760
going to open up the command line

31
00:00:55,960 --> 00:01:03,760
interface here and I'm going to type NPX

32
00:00:58,760 --> 00:01:05,000
skills at latest add mattpocock/skills.

33
00:01:03,760 --> 00:01:06,960
This assumes a couple of things. It

34
00:01:05,000 --> 00:01:10,880
assumes that you've got Node.js

35
00:01:06,960 --> 00:01:13,760
installed. This NPX comes from Node.js

36
00:01:10,880 --> 00:01:15,360
and it runs the skills.sh command line

37
00:01:13,760 --> 00:01:17,880
installer from Vercel. What this

38
00:01:15,360 --> 00:01:20,200
basically does is it installs a GitHub

39
00:01:17,880 --> 00:01:22,760
repo of skills called mattpocockskills

40
00:01:20,200 --> 00:01:24,200
and it can walk through a few setup

41
00:01:22,760 --> 00:01:25,800
questions here. It first says it needs

42
00:01:24,200 --> 00:01:28,320
to install the following packages. Yes,

43
00:01:25,800 --> 00:01:30,040
that seems fine to me and then it did a

44
00:01:28,320 --> 00:01:31,800
couple of things and we now have a long

45
00:01:30,040 --> 00:01:34,520
long list of all the skills that we

46
00:01:31,800 --> 00:01:36,080
could install. It found 38 skills here

47
00:01:34,520 --> 00:01:37,480
which is a lot and you can see if I

48
00:01:36,080 --> 00:01:39,760
scroll up and down that they're in two

49
00:01:37,480 --> 00:01:42,280
groups. We've got the mattpocockskills

50
00:01:39,760 --> 00:01:43,920
and then we've got other skills. So the

51
00:01:42,280 --> 00:01:46,280
mattpocockskills are the ones that I

52
00:01:43,920 --> 00:01:48,440
have blessed as the skills that I think

53
00:01:46,280 --> 00:01:49,520
are good enough to be public facing. The

54
00:01:48,440 --> 00:01:51,800
other ones are ones that I'm

55
00:01:49,520 --> 00:01:53,680
experimenting with right now and may

56
00:01:51,800 --> 00:01:55,680
delete in future. What I recommend you

57
00:01:53,680 --> 00:01:58,000
do is you go to the top here and you can

58
00:01:55,680 --> 00:02:00,840
kind of go up and down. It's kind of

59
00:01:58,000 --> 00:02:02,680
broken, I have to say. And if you press

60
00:02:00,840 --> 00:02:04,320
space here, and you should see that if

61
00:02:02,680 --> 00:02:06,520
you scroll up, okay, they're now all

62
00:02:04,320 --> 00:02:09,880
selected. You press space, and then you

63
00:02:06,520 --> 00:02:11,760
press return, and now uh you've selected

64
00:02:09,880 --> 00:02:13,600
all of the official skills. I'm not

65
00:02:11,760 --> 00:02:15,440
terribly happy with Versel's CLI here,

66
00:02:13,600 --> 00:02:18,000
so I may change it in future, or maybe

67
00:02:15,440 --> 00:02:19,280
even just ship my own. But uh for now,

68
00:02:18,000 --> 00:02:21,160
that's as good as it gets. One thing

69
00:02:19,280 --> 00:02:24,200
that is good is that it will set up your

70
00:02:21,160 --> 00:02:26,200
skills to work with any agent. So, I use

71
00:02:24,200 --> 00:02:27,560
Claude Code, but you can go down here

72
00:02:26,200 --> 00:02:30,800
and sort of just select the ones that

73
00:02:27,560 --> 00:02:33,520
you want. I'm using space to select. I

74
00:02:30,800 --> 00:02:36,040
think by default, if I zoom out a touch,

75
00:02:33,520 --> 00:02:38,600
then it supports all of these universal

76
00:02:36,040 --> 00:02:41,120
ones up here. So, cursor, Codex, Claude,

77
00:02:38,600 --> 00:02:42,800
etc. But anything that uses like Claude

78
00:02:41,120 --> 00:02:44,480
skills, such as Claude Code, then you

79
00:02:42,800 --> 00:02:47,040
need to set up yourself. So, I'm going

80
00:02:44,480 --> 00:02:48,920
to press return here, and it should now

81
00:02:47,040 --> 00:02:50,400
be configured to set up my skills for

82
00:02:48,920 --> 00:02:52,200
Claude Code. The installation scope

83
00:02:50,400 --> 00:02:53,680
defines where your skills are installed,

84
00:02:52,200 --> 00:02:55,080
whether they're installed just in the

85
00:02:53,680 --> 00:02:56,560
current directory, or whether they're

86
00:02:55,080 --> 00:02:58,080
global. This will depend on what your

87
00:02:56,560 --> 00:02:59,440
team's conventions are. If you're

88
00:02:58,080 --> 00:03:01,400
working in a team, I would say that

89
00:02:59,440 --> 00:03:03,160
project skills are the right way to go.

90
00:03:01,400 --> 00:03:05,840
That way, everyone is using the same

91
00:03:03,160 --> 00:03:07,400
skill set on every project, and it means

92
00:03:05,840 --> 00:03:08,760
that you can contribute to the skills

93
00:03:07,400 --> 00:03:11,000
together and make those decisions

94
00:03:08,760 --> 00:03:12,480
together. But global is fine if you're

95
00:03:11,000 --> 00:03:14,160
just a solo developer working on your

96
00:03:12,480 --> 00:03:16,239
own stuff, like I am. So, I'm going to

97
00:03:14,160 --> 00:03:17,880
press return here, install it in my home

98
00:03:16,239 --> 00:03:20,200
directory, and I'm going to choose

99
00:03:17,880 --> 00:03:22,200
symlink as the recommended way. The

100
00:03:20,200 --> 00:03:25,120
choice here is whether you copy it to

101
00:03:22,200 --> 00:03:27,080
the agents folder as well as the dot uh

102
00:03:25,120 --> 00:03:28,760
Claude folder. And

103
00:03:27,080 --> 00:03:30,560
it's kind of not a nice way to do it.

104
00:03:28,760 --> 00:03:31,920
Symlink is just the nice, easy way to do

105
00:03:30,560 --> 00:03:33,320
it. So, I wouldn't even make a decision

106
00:03:31,920 --> 00:03:34,800
here, just choose symlink. So, it now

107
00:03:33,320 --> 00:03:36,560
gives you a summary of all the things

108
00:03:34,800 --> 00:03:38,720
that you're installing here. There seems

109
00:03:36,560 --> 00:03:40,519
to be an alert on Socket about to spec.

110
00:03:38,720 --> 00:03:42,239
I'll take a look at that later. But yes,

111
00:03:40,519 --> 00:03:44,160
we can proceed with installation, and

112
00:03:42,239 --> 00:03:46,320
it's now installed all of the skills.

113
00:03:44,160 --> 00:03:48,720
This means then that I can run Claude

114
00:03:46,320 --> 00:03:51,040
inside here, or whatever your agent is,

115
00:03:48,720 --> 00:03:52,920
and I'm going to create a new So, I'm

116
00:03:51,040 --> 00:03:54,480
just going to say hello to get out of

117
00:03:52,920 --> 00:03:55,920
this agent's view here. Now, depending

118
00:03:54,480 --> 00:03:57,400
on the harness you're using, this will

119
00:03:55,920 --> 00:03:59,760
show up in different ways, but on Cloud

120
00:03:57,400 --> 00:04:01,640
Code, I can press forward slash and I

121
00:03:59,760 --> 00:04:03,360
now see that I have a few skills

122
00:04:01,640 --> 00:04:05,720
available to me. I have grill me,

123
00:04:03,360 --> 00:04:07,440
grilling, way finder, grill with docs,

124
00:04:05,720 --> 00:04:09,400
etc. Loads of stuff. Now, the difference

125
00:04:07,440 --> 00:04:11,520
between my skills and lots of other

126
00:04:09,400 --> 00:04:14,320
skills repos that are out there is my

127
00:04:11,520 --> 00:04:17,840
skills are mostly user invoked. That

128
00:04:14,320 --> 00:04:19,959
means that if I run context here, not

129
00:04:17,840 --> 00:04:22,440
many of my skills actually leech their

130
00:04:19,959 --> 00:04:24,600
way into the description. And the

131
00:04:22,440 --> 00:04:26,520
descriptions I have are quite short and

132
00:04:24,600 --> 00:04:28,640
precise. So, that means that even though

133
00:04:26,520 --> 00:04:32,080
we've downloaded all of my skills, the

134
00:04:28,640 --> 00:04:33,880
skills only take up 660 tokens here. So,

135
00:04:32,080 --> 00:04:35,400
it's very, very light in terms of

136
00:04:33,880 --> 00:04:37,440
context load. So, okay, we got the

137
00:04:35,400 --> 00:04:40,200
skills. Now, what we have to do is we

138
00:04:37,440 --> 00:04:42,680
have to run set up Mac Pocock skills.

139
00:04:40,200 --> 00:04:46,120
And this will do a few things. My skills

140
00:04:42,680 --> 00:04:49,240
rely on some uh configuration inside the

141
00:04:46,120 --> 00:04:51,600
repository, and this does a few things

142
00:04:49,240 --> 00:04:53,360
for you. The first thing is it means you

143
00:04:51,600 --> 00:04:56,040
need to use an issue tracker. We're

144
00:04:53,360 --> 00:04:57,680
going to be saving um specs, we're going

145
00:04:56,040 --> 00:05:00,000
to be saving tickets, and we need to

146
00:04:57,680 --> 00:05:01,880
save them somewhere. You've got kind of

147
00:05:00,000 --> 00:05:04,400
an infinity of choices here. You can use

148
00:05:01,880 --> 00:05:06,760
GitHub, you can use local markdown, or

149
00:05:04,400 --> 00:05:09,200
you can literally use anything. The way

150
00:05:06,760 --> 00:05:11,040
that the skill works is that it looks at

151
00:05:09,200 --> 00:05:13,000
your local configuration. And so, you

152
00:05:11,040 --> 00:05:14,680
can set it up for Jira, you can set it

153
00:05:13,000 --> 00:05:16,400
up for Linear. And the way you do that

154
00:05:14,680 --> 00:05:18,000
is you just tell the agent what you want

155
00:05:16,400 --> 00:05:19,240
to set it up for, and it will go and set

156
00:05:18,000 --> 00:05:20,600
it up for it. I just want to emphasize

157
00:05:19,240 --> 00:05:22,840
that. People are asking me all the time,

158
00:05:20,600 --> 00:05:25,160
"How do I make my skills work with Jira,

159
00:05:22,840 --> 00:05:27,200
work with Beads, work with Linear?" It

160
00:05:25,160 --> 00:05:29,560
already does. All you need to do is just

161
00:05:27,200 --> 00:05:31,800
run set up Mac Pocock and just say, "Set

162
00:05:29,560 --> 00:05:33,240
it up with Jira." Except, I don't want

163
00:05:31,800 --> 00:05:35,640
to set it up with Jira. I'm just going

164
00:05:33,240 --> 00:05:37,160
to set it up with local markdown,

165
00:05:35,640 --> 00:05:39,200
please. So, that's fine by me. The next

166
00:05:37,160 --> 00:05:41,120
question to answer here is about triage

167
00:05:39,200 --> 00:05:42,919
labels. So, there are a set of labels

168
00:05:41,120 --> 00:05:44,440
that the skill relies on to communicate

169
00:05:42,919 --> 00:05:46,760
information about the tickets that it

170
00:05:44,440 --> 00:05:48,280
produces. It's not really that important

171
00:05:46,760 --> 00:05:50,000
here, so I'm just going to accept the

172
00:05:48,280 --> 00:05:51,800
defaults. You can look at the docs on

173
00:05:50,000 --> 00:05:54,920
the triage skill if you want to learn

174
00:05:51,800 --> 00:05:57,320
more. So, defaults is fine. The next one

175
00:05:54,920 --> 00:05:59,720
is about the domain documentation. So,

176
00:05:57,320 --> 00:06:03,880
my skills like to have a little bit of

177
00:05:59,720 --> 00:06:05,920
docs, a context .md file, and an ADR

178
00:06:03,880 --> 00:06:07,680
inside the repo. And it's basically

179
00:06:05,920 --> 00:06:09,840
asking if it's going to be a single

180
00:06:07,680 --> 00:06:12,760
context or a multi-context. I think

181
00:06:09,840 --> 00:06:14,960
single context is the way to go here.

182
00:06:12,760 --> 00:06:17,640
Multi-context is if you have a big mono

183
00:06:14,960 --> 00:06:21,160
repo and you need lots of different

184
00:06:17,640 --> 00:06:22,680
bounded contexts within it. But for 99%

185
00:06:21,160 --> 00:06:24,040
of people, a single context is going to

186
00:06:22,680 --> 00:06:26,560
be fine. All right, so it's gone ahead

187
00:06:24,040 --> 00:06:28,760
and written a few things here. The first

188
00:06:26,560 --> 00:06:31,080
thing it's written is inside claw.md,

189
00:06:28,760 --> 00:06:33,200
it's added a few little links here. So,

190
00:06:31,080 --> 00:06:35,360
this is the new stuff. It's just linking

191
00:06:33,200 --> 00:06:37,160
to the issue tracker docs, linking to

192
00:06:35,360 --> 00:06:40,280
the triage labels, and linking to the

193
00:06:37,160 --> 00:06:43,240
domain docs. And each of these are at

194
00:06:40,280 --> 00:06:45,720
docs, agents, domain issue tracker. So,

195
00:06:43,240 --> 00:06:49,160
we can see here that it's going to save

196
00:06:45,720 --> 00:06:50,960
all of the issues and specs inside a

197
00:06:49,160 --> 00:06:52,960
scratch file. So, with that, our setup

198
00:06:50,960 --> 00:06:54,840
for this repo is complete. And so, you

199
00:06:52,960 --> 00:06:56,480
might be thinking, how do I get started?

200
00:06:54,840 --> 00:06:58,919
Well, before we get started, I'm going

201
00:06:56,480 --> 00:07:00,320
to show you one more really cool thing.

202
00:06:58,919 --> 00:07:02,720
You can, if you're following along, just

203
00:07:00,320 --> 00:07:05,040
stop the video now and use one skill.

204
00:07:02,720 --> 00:07:08,360
You can use the ask Matt skill. This ask

205
00:07:05,040 --> 00:07:10,600
Matt skill is essentially me as a skill.

206
00:07:08,360 --> 00:07:12,360
It knows everything that is needed about

207
00:07:10,600 --> 00:07:15,120
the skills repo and what you should do

208
00:07:12,360 --> 00:07:16,800
first. So, we can say, ask Matt, how do

209
00:07:15,120 --> 00:07:18,640
I get started? I want to make some code

210
00:07:16,800 --> 00:07:20,800
changes here. What is the main flow I

211
00:07:18,640 --> 00:07:22,120
should use? I can now submit that and

212
00:07:20,800 --> 00:07:23,760
see what it says. By the way, I'm using

213
00:07:22,120 --> 00:07:25,600
Whisper flow as my transcription. So,

214
00:07:23,760 --> 00:07:27,520
here we go. It's saying the main flow,

215
00:07:25,600 --> 00:07:29,240
idea to ship. Since you have a code

216
00:07:27,520 --> 00:07:32,120
base, start at the top of the main flow

217
00:07:29,240 --> 00:07:34,720
and walk down in it in one unbroken

218
00:07:32,120 --> 00:07:38,000
context window. So, it's very um

219
00:07:34,720 --> 00:07:40,640
kind of really telling you how to use

220
00:07:38,000 --> 00:07:43,160
your sessions as well. I I believe that

221
00:07:40,640 --> 00:07:44,920
being conscious about the context window

222
00:07:43,160 --> 00:07:46,800
that you're using, the tokens that

223
00:07:44,920 --> 00:07:48,840
you're using is essential to using AI

224
00:07:46,800 --> 00:07:50,720
well. It says you should start with

225
00:07:48,840 --> 00:07:52,120
grill with docs. It interviews you to

226
00:07:50,720 --> 00:07:54,440
sharpen the idea and because you're in a

227
00:07:52,120 --> 00:07:57,200
repo it's stateful. It records what it

228
00:07:54,440 --> 00:07:59,240
learns in context.md and ADRs. This is

229
00:07:57,200 --> 00:08:01,160
where you turn I want to change X into a

230
00:07:59,240 --> 00:08:03,200
crisp defensible plan. Defensible is

231
00:08:01,160 --> 00:08:04,640
such an LLM phrase, honestly. Can you

232
00:08:03,200 --> 00:08:06,440
settle every open question just by

233
00:08:04,640 --> 00:08:08,560
talking? If a question needs a runnable

234
00:08:06,440 --> 00:08:10,400
answer, then you can use prototype,

235
00:08:08,560 --> 00:08:12,800
which I've done a video about on it.

236
00:08:10,400 --> 00:08:14,240
Bridged in and out of by handoff, if not

237
00:08:12,800 --> 00:08:15,720
skip this. Once you've done the

238
00:08:14,240 --> 00:08:17,440
interview and grill with docs, you can

239
00:08:15,720 --> 00:08:20,160
either go straight to the implement

240
00:08:17,440 --> 00:08:22,000
skill, or if it needs multiple sessions

241
00:08:20,160 --> 00:08:24,040
to go through, then you can go to to

242
00:08:22,000 --> 00:08:26,080
spec and to tickets. Let me make this a

243
00:08:24,040 --> 00:08:27,960
little bit clearer for you. The default

244
00:08:26,080 --> 00:08:30,240
flow looks like this. You start with

245
00:08:27,960 --> 00:08:31,560
grill with docs, and this interviews you

246
00:08:30,240 --> 00:08:33,320
based on the idea that you want to

247
00:08:31,560 --> 00:08:35,560
produce. For instance, if I clear out of

248
00:08:33,320 --> 00:08:37,120
ask math, of course I could go and ask

249
00:08:35,560 --> 00:08:39,039
follow-ups here, use it as a tutorial

250
00:08:37,120 --> 00:08:40,840
itself, but let me just show you. I'm

251
00:08:39,039 --> 00:08:42,200
going to say grill with docs, and I'm

252
00:08:40,840 --> 00:08:44,440
going to kick it off with an idea. I'm

253
00:08:42,200 --> 00:08:47,640
going to say, I would like to remove

254
00:08:44,440 --> 00:08:49,560
most of the internal tooling on this CLI

255
00:08:47,640 --> 00:08:51,280
to make it just only public-facing.

256
00:08:49,560 --> 00:08:53,720
There's a lot of craft here. I want to

257
00:08:51,280 --> 00:08:55,160
just take this repo down a notch. It

258
00:08:53,720 --> 00:08:56,920
really can be as vague as this. You

259
00:08:55,160 --> 00:08:58,200
don't need to do too much here. Grill

260
00:08:56,920 --> 00:08:59,960
with docs is going to do the heavy

261
00:08:58,200 --> 00:09:01,360
lifting by asking you a bunch of

262
00:08:59,960 --> 00:09:03,320
follow-up questions. It's going and

263
00:09:01,360 --> 00:09:03,960
exploring a bunch of code here. And by

264
00:09:03,320 --> 00:09:06,560
the way, I'm [clears throat] using

265
00:09:03,960 --> 00:09:09,000
Claude Code, I'm using Opus 4.8 on

266
00:09:06,560 --> 00:09:10,440
medium effort, but you really don't have

267
00:09:09,000 --> 00:09:12,520
to use the same setup as me. These

268
00:09:10,440 --> 00:09:13,480
skills are being used by a bunch of

269
00:09:12,520 --> 00:09:14,920
different people, bunch of different

270
00:09:13,480 --> 00:09:16,200
harnesses, different models, different

271
00:09:14,920 --> 00:09:18,280
effort levels. And we can see it's

272
00:09:16,200 --> 00:09:19,920
already asked the first question here.

273
00:09:18,280 --> 00:09:21,520
So, it's gotten a clear map of the

274
00:09:19,920 --> 00:09:23,720
entire repo. It's looking at the

275
00:09:21,520 --> 00:09:25,560
internal namespace with 11 subcommands.

276
00:09:23,720 --> 00:09:27,320
So, this is what a grilling session

277
00:09:25,560 --> 00:09:30,240
looks like. You go through all of the

278
00:09:27,320 --> 00:09:32,080
questions until you feel or you and the

279
00:09:30,240 --> 00:09:33,480
agent feel that you've reached a shared

280
00:09:32,080 --> 00:09:35,320
understanding. I'm going to do that now,

281
00:09:33,480 --> 00:09:36,400
and then I'll check in with you once I'm

282
00:09:35,320 --> 00:09:38,520
done.

283
00:09:36,400 --> 00:09:41,640
Okay, it didn't end up taking too long.

284
00:09:38,520 --> 00:09:42,880
We ended up with what, six questions?

285
00:09:41,640 --> 00:09:44,640
That's not very much for grilling

286
00:09:42,880 --> 00:09:46,200
session. Usually mine end up being about

287
00:09:44,640 --> 00:09:48,200
sort of 20 questions depending on the

288
00:09:46,200 --> 00:09:50,600
size of it, but we've ended up with a

289
00:09:48,200 --> 00:09:52,960
decent plan. We're going to delete uh 10

290
00:09:50,600 --> 00:09:55,160
command files, delete three tests,

291
00:09:52,960 --> 00:09:57,600
rewire shared modules. And all I did

292
00:09:55,160 --> 00:09:59,560
here was I just answered questions until

293
00:09:57,600 --> 00:10:01,240
it said, "Okay, we've walked the whole

294
00:09:59,560 --> 00:10:03,240
tree. We've reached a shared

295
00:10:01,240 --> 00:10:05,200
understanding. Let me lay out the plan."

296
00:10:03,240 --> 00:10:06,960
Notice here, I wasn't using plan mode

297
00:10:05,200 --> 00:10:08,360
for this. I was actually in auto mode in

298
00:10:06,960 --> 00:10:11,160
claw code, which is kind of like the

299
00:10:08,360 --> 00:10:13,120
default mode. And you now have a fork in

300
00:10:11,160 --> 00:10:15,360
the road. If you think that this work is

301
00:10:13,120 --> 00:10:17,680
going to be big enough that it will need

302
00:10:15,360 --> 00:10:20,360
multiple agent sessions, then you can

303
00:10:17,680 --> 00:10:22,400
skip numbers two and three here and go

304
00:10:20,360 --> 00:10:24,280
straight into implement. The way you

305
00:10:22,400 --> 00:10:26,680
would do that is you would just say, uh

306
00:10:24,280 --> 00:10:28,880
forward slash implement this. And in

307
00:10:26,680 --> 00:10:31,600
this case, I do think that is what we

308
00:10:28,880 --> 00:10:33,760
should do. I've still got about, uh I

309
00:10:31,600 --> 00:10:35,640
think of my context window is kind of

310
00:10:33,760 --> 00:10:38,520
like ending or getting significantly

311
00:10:35,640 --> 00:10:40,200
dumber around 140k

312
00:10:38,520 --> 00:10:42,360
mark. I think of that as kind of like

313
00:10:40,200 --> 00:10:44,800
the smart zone of the LLM. If you go

314
00:10:42,360 --> 00:10:46,800
above 140k, you end up sort of with, you

315
00:10:44,800 --> 00:10:48,160
know, attention degradation. It ends up

316
00:10:46,800 --> 00:10:50,360
getting stupider, does weird

317
00:10:48,160 --> 00:10:52,480
hallucinations. So, I think of having

318
00:10:50,360 --> 00:10:54,920
like, okay, we've got 100k of budget

319
00:10:52,480 --> 00:10:57,000
here to remove 10 commands. That seems

320
00:10:54,920 --> 00:10:58,120
super easy. Definitely something, you

321
00:10:57,000 --> 00:10:59,520
know, we can definitely do that. So,

322
00:10:58,120 --> 00:11:01,000
this is what I would usually do. I would

323
00:10:59,520 --> 00:11:03,040
just say implement and then I would

324
00:11:01,000 --> 00:11:04,200
leave it, let it run, and it would

325
00:11:03,040 --> 00:11:05,600
finish the work. However, in the

326
00:11:04,200 --> 00:11:07,240
interest of showing you everything, I'm

327
00:11:05,600 --> 00:11:09,520
going to pretend that this work is going

328
00:11:07,240 --> 00:11:11,520
to take more than one session, that I've

329
00:11:09,520 --> 00:11:13,120
maybe run out of context window in the

330
00:11:11,520 --> 00:11:15,160
current or run out of smart zone in the

331
00:11:13,120 --> 00:11:16,800
current window, and I'm going to need to

332
00:11:15,160 --> 00:11:19,839
spread this out over multiple context

333
00:11:16,800 --> 00:11:21,480
windows. So, I'm going to call to spec

334
00:11:19,839 --> 00:11:23,839
here instead. So, instead of writing

335
00:11:21,480 --> 00:11:25,680
implement this, I'm going to say to spec

336
00:11:23,839 --> 00:11:27,280
here. And that's it. What this is going

337
00:11:25,680 --> 00:11:29,000
to do is it's going to take all of the

338
00:11:27,280 --> 00:11:32,000
discussion that I've had, all of this

339
00:11:29,000 --> 00:11:34,720
46.1k tokens, and it's going to compress

340
00:11:32,000 --> 00:11:36,880
it into a document that we can use

341
00:11:34,720 --> 00:11:38,600
later. This is where our issue tracker

342
00:11:36,880 --> 00:11:40,280
comes in. So, this issue tracker we're

343
00:11:38,600 --> 00:11:41,720
just going to use local markdown files

344
00:11:40,280 --> 00:11:43,920
and so it's just going to spit out the

345
00:11:41,720 --> 00:11:45,680
spec into a local directory. This spec

346
00:11:43,920 --> 00:11:48,520
is going to be the destination that

347
00:11:45,680 --> 00:11:50,160
we're heading to over this multi-ticket

348
00:11:48,520 --> 00:11:51,440
sprint. In other words, this is what

349
00:11:50,160 --> 00:11:53,080
we're going to end up with. This is the

350
00:11:51,440 --> 00:11:54,880
description of everything of how it's

351
00:11:53,080 --> 00:11:56,800
going to look at the end. And then the

352
00:11:54,880 --> 00:11:58,280
tickets is the description of how we're

353
00:11:56,800 --> 00:12:00,680
going to get there. Okay, we can see

354
00:11:58,280 --> 00:12:02,880
it's been written and published to the

355
00:12:00,680 --> 00:12:05,040
issue tracker. If I open this up, we can

356
00:12:02,880 --> 00:12:06,160
see it is in here. So, it's very nice

357
00:12:05,040 --> 00:12:08,400
and detailed. It's got a problem

358
00:12:06,160 --> 00:12:10,440
statement, a solution, a bunch of user

359
00:12:08,400 --> 00:12:12,960
stories, implementation decisions,

360
00:12:10,440 --> 00:12:14,480
testing decisions, a lot of stuff here.

361
00:12:12,960 --> 00:12:16,560
And this is going to be really useful

362
00:12:14,480 --> 00:12:19,040
cuz we'll be able to compare this at the

363
00:12:16,560 --> 00:12:20,520
end to make sure that our implementation

364
00:12:19,040 --> 00:12:22,360
matched the spec. So, now that we've got

365
00:12:20,520 --> 00:12:23,880
the spec, I'm going to go into the same

366
00:12:22,360 --> 00:12:25,880
session, not going to change sessions

367
00:12:23,880 --> 00:12:28,360
here, and now I'm going to say to

368
00:12:25,880 --> 00:12:31,080
tickets. And this is where it will

369
00:12:28,360 --> 00:12:32,840
basically try to turn the spec into an

370
00:12:31,080 --> 00:12:35,640
implementation plan. Each one of these

371
00:12:32,840 --> 00:12:37,640
tickets is supposed to just be the size

372
00:12:35,640 --> 00:12:39,440
of a single context window or a single

373
00:12:37,640 --> 00:12:42,720
smart zone. And if we look here, we can

374
00:12:39,440 --> 00:12:45,440
see that it's kind of given us three

375
00:12:42,720 --> 00:12:47,520
tickets here. So, three slices. I think

376
00:12:45,440 --> 00:12:49,160
that these three slices are a little bit

377
00:12:47,520 --> 00:12:53,600
much. I actually think it can be done in

378
00:12:49,160 --> 00:12:55,760
one slice. Do it in one slice instead.

379
00:12:53,600 --> 00:12:58,640
And so it's now put this in a file. So,

380
00:12:55,760 --> 00:13:00,080
it's put the ticket in tickets.md. Now,

381
00:12:58,640 --> 00:13:02,160
this is quite a bad example cuz it's

382
00:13:00,080 --> 00:13:03,720
kind of copying the stuff that's in our

383
00:13:02,160 --> 00:13:05,839
product requirements documents. So, let

384
00:13:03,720 --> 00:13:07,600
me show you an actual real example. Here

385
00:13:05,839 --> 00:13:10,680
is a spec that I implemented a couple of

386
00:13:07,600 --> 00:13:13,120
days ago to remove a bunch of stuff from

387
00:13:10,680 --> 00:13:15,240
a repo. So, I'm on a real removal spree

388
00:13:13,120 --> 00:13:18,520
recently. And you can see that this is

389
00:13:15,240 --> 00:13:21,360
the spec and underneath it has 11 sub

390
00:13:18,520 --> 00:13:22,839
issues. So, 11 tickets underneath it.

391
00:13:21,360 --> 00:13:25,280
And each of these tickets, so this is a

392
00:13:22,839 --> 00:13:27,520
very detailed spec, each of these

393
00:13:25,280 --> 00:13:29,640
tickets is a single context window

394
00:13:27,520 --> 00:13:32,680
session. So, if we click into here, we

395
00:13:29,640 --> 00:13:35,120
can see it's just pretty short. Most of

396
00:13:32,680 --> 00:13:37,960
the acceptance criteria is already in

397
00:13:35,120 --> 00:13:39,520
the main spec, and so this one is just

398
00:13:37,960 --> 00:13:41,640
literally what do you build in this

399
00:13:39,520 --> 00:13:44,320
session? So, that's number session one,

400
00:13:41,640 --> 00:13:46,760
then session two, then session three.

401
00:13:44,320 --> 00:13:49,680
You can see that how this breaks down a

402
00:13:46,760 --> 00:13:51,440
huge chunk of work into manageable

403
00:13:49,680 --> 00:13:53,440
pieces that the agent can then go and

404
00:13:51,440 --> 00:13:55,560
do. However, here we are left with a

405
00:13:53,440 --> 00:13:57,280
single manageable piece. So, what I'm

406
00:13:55,560 --> 00:14:00,000
going to do is I'm going to clear the

407
00:13:57,280 --> 00:14:02,200
context here. Now, we have everything we

408
00:14:00,000 --> 00:14:04,560
need so that we can just run a bunch of

409
00:14:02,200 --> 00:14:06,480
agents to tackle this problem. So, I can

410
00:14:04,560 --> 00:14:09,800
clear the context, and then I'm just

411
00:14:06,480 --> 00:14:11,800
going to say at tickets here, and I'm

412
00:14:09,800 --> 00:14:14,200
before that I'll say

413
00:14:11,800 --> 00:14:16,160
implement this. So, now because we have

414
00:14:14,200 --> 00:14:18,120
the spec that decides where we're going

415
00:14:16,160 --> 00:14:20,680
and the tickets that decide how we get

416
00:14:18,120 --> 00:14:22,120
there, the agent has everything it needs

417
00:14:20,680 --> 00:14:23,960
and we're ready to implement. Now, when

418
00:14:22,120 --> 00:14:26,520
you're doing this by hand, the idea is

419
00:14:23,960 --> 00:14:28,840
that you then implement each ticket one

420
00:14:26,520 --> 00:14:31,000
by one. So, you don't say do every

421
00:14:28,840 --> 00:14:32,560
single ticket, you say okay, we go and

422
00:14:31,000 --> 00:14:34,680
implement, then we see if we've hit the

423
00:14:32,560 --> 00:14:37,000
smart zone. If we haven't, maybe we can

424
00:14:34,680 --> 00:14:39,920
squeeze in one more ticket here, but

425
00:14:37,000 --> 00:14:41,880
usually I would say you clear in between

426
00:14:39,920 --> 00:14:43,360
every single ticket. Then, once you've

427
00:14:41,880 --> 00:14:46,040
done all of the implementation, you've

428
00:14:43,360 --> 00:14:48,240
got your full thing all implemented,

429
00:14:46,040 --> 00:14:50,880
then you can go and code review and do

430
00:14:48,240 --> 00:14:52,720
the final check against the spec. We can

431
00:14:50,880 --> 00:14:55,000
see here it really was a very small

432
00:14:52,720 --> 00:14:58,040
piece of work actually. It's only 42

433
00:14:55,000 --> 00:15:00,480
.7k, and it's now about to, as part of

434
00:14:58,040 --> 00:15:01,800
the implement, run the code review. As

435
00:15:00,480 --> 00:15:03,480
part of the implement script, it goes

436
00:15:01,800 --> 00:15:06,000
and runs all the type check, runs the

437
00:15:03,480 --> 00:15:08,400
build, run is doing even more

438
00:15:06,000 --> 00:15:10,200
verification, checking AI Hero internal

439
00:15:08,400 --> 00:15:12,600
help, shows only edit commits, and it's

440
00:15:10,200 --> 00:15:15,320
gone and loaded the code review skill.

441
00:15:12,600 --> 00:15:17,960
This review is based on two axes. First,

442
00:15:15,320 --> 00:15:20,080
it compares the work done against the

443
00:15:17,960 --> 00:15:22,680
original spec. This is really useful

444
00:15:20,080 --> 00:15:24,120
when you've done a huge chunk of work

445
00:15:22,680 --> 00:15:25,640
and the agent might have forgotten

446
00:15:24,120 --> 00:15:27,680
things in tickets or the tickets might

447
00:15:25,640 --> 00:15:30,360
have been unspecified. Doing a final

448
00:15:27,680 --> 00:15:32,080
pass means you actually nail everything.

449
00:15:30,360 --> 00:15:33,920
And then it also checks against the

450
00:15:32,080 --> 00:15:35,600
standards documentation that you've got

451
00:15:33,920 --> 00:15:37,080
in your own repo. In this repo we don't

452
00:15:35,600 --> 00:15:39,000
really have any coding standards

453
00:15:37,080 --> 00:15:40,960
documented anywhere, but if it doesn't

454
00:15:39,000 --> 00:15:43,000
detect any, then it uses some classic

455
00:15:40,960 --> 00:15:45,480
ones kind of from Martin Fowler. So it

456
00:15:43,000 --> 00:15:46,680
looks at code smells, tries to figure

457
00:15:45,480 --> 00:15:48,560
out if there's any bad stuff. Doing

458
00:15:46,680 --> 00:15:51,120
these in sub agents is really important

459
00:15:48,560 --> 00:15:53,360
because if you do it in the main agent,

460
00:15:51,120 --> 00:15:55,600
it means that the main agent already has

461
00:15:53,360 --> 00:15:58,800
written the code and agents are often

462
00:15:55,600 --> 00:16:00,560
really bad at editing code or improving

463
00:15:58,800 --> 00:16:02,280
code they've just written. Because

464
00:16:00,560 --> 00:16:04,280
they've wrote it, so they just think,

465
00:16:02,280 --> 00:16:06,120
"Okay, that's fantastic. That's fine."

466
00:16:04,280 --> 00:16:07,320
Whereas if you spawn some agents, then

467
00:16:06,120 --> 00:16:08,680
they're going to have a clear context

468
00:16:07,320 --> 00:16:10,400
window and they're going to do a much

469
00:16:08,680 --> 00:16:14,000
better job reviewing the code. Okay, we

470
00:16:10,400 --> 00:16:16,080
can see that both came back. So

471
00:16:14,000 --> 00:16:18,160
cross-checked every acceptance criteria

472
00:16:16,080 --> 00:16:20,160
against the spec, checked everything

473
00:16:18,160 --> 00:16:21,600
against the standards, and cool. We're

474
00:16:20,160 --> 00:16:23,280
good to go. And it's now committed

475
00:16:21,600 --> 00:16:25,960
against the current branch. Beautiful.

476
00:16:23,280 --> 00:16:28,040
So that is our flow complete. We aligned

477
00:16:25,960 --> 00:16:30,080
before we got started. We created some

478
00:16:28,040 --> 00:16:32,000
spec and tickets in order to make sure

479
00:16:30,080 --> 00:16:33,680
it worked over multiple sessions. We

480
00:16:32,000 --> 00:16:36,160
then implemented it and the implement

481
00:16:33,680 --> 00:16:38,120
skill itself used the code review. This

482
00:16:36,160 --> 00:16:39,440
is the main flow that all of my work

483
00:16:38,120 --> 00:16:41,080
runs through. And the stuff that isn't

484
00:16:39,440 --> 00:16:42,600
in the main flow is stuff that I'm

485
00:16:41,080 --> 00:16:44,880
experimenting with, stuff that I'm

486
00:16:42,600 --> 00:16:48,280
improving, always trying to get this

487
00:16:44,880 --> 00:16:50,080
loop faster, better, easier to run. And

488
00:16:48,280 --> 00:16:51,640
for that, if you're interested in that,

489
00:16:50,080 --> 00:16:52,960
then you should check out my newsletter

490
00:16:51,640 --> 00:16:54,839
for these skills. This YouTube channel

491
00:16:52,960 --> 00:16:56,720
is a great place to be for subscribing

492
00:16:54,839 --> 00:16:58,520
to understanding more about the skills,

493
00:16:56,720 --> 00:16:59,839
but really the good stuff is on the

494
00:16:58,520 --> 00:17:01,680
newsletter. If you want on the day

495
00:16:59,839 --> 00:17:03,280
updates when I ship new skills, when I

496
00:17:01,680 --> 00:17:05,240
add updates to

497
00:17:03,280 --> 00:17:06,839
kind of that you need to keep updated

498
00:17:05,240 --> 00:17:07,839
with, then this is the place to be. But

499
00:17:06,839 --> 00:17:09,439
thank you so much for watching.

500
00:17:07,839 --> 00:17:11,079
Hopefully this tutorial gives you an

501
00:17:09,439 --> 00:17:12,920
idea on how to get set up with the

502
00:17:11,079 --> 00:17:14,240
skills and what the main flow is

503
00:17:12,920 --> 00:17:16,000
supposed to be. Thanks for watching,

504
00:17:14,240 --> 00:17:18,400
happy skilling, and I will see you very

505
00:17:16,000 --> 00:17:18,400
soon.
