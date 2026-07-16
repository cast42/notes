---
title: "Agent Skills with Anthropic — video transcript"
date: 2026-07-15
timestamp: 2026-07-15
type: source
topics:
  - agentic_coding
tags:
  - agent-skills
  - progressive-disclosure
  - claude-code
  - model-context-protocol
  - subagents
resource: "https://x.com/0xwhrrari/status/2077498534128218116"
description: "Timestamped machine transcript of the 1h50m Agent Skills with Anthropic course video."
source_url: "https://x.com/0xwhrrari/status/2077498534128218116"
extractor: "whisper.cpp base.en"
transcript_quality: "machine-generated; names and product terms may contain errors"
---

# Agent Skills with Anthropic — video transcript

Machine-generated transcript. Obvious recurring errors include “Cloud” for “Claude”; consult the video where exact wording matters.

1
00:00:00,000 --> 00:00:03,760
 and taught by returning instructor, Ellie Schorvik.

2
00:00:03,760 --> 00:00:08,120
 Skills give Cloud Code and other agents new abilities to carry out tasks

3
00:00:08,120 --> 00:00:10,320
 are thrilled to have Ellie return to teach this.

4
00:00:10,320 --> 00:00:13,320
 Thank you Andrew, I'm happy to be back and work with you all on this one.

5
00:00:13,320 --> 00:00:18,640
 Skills are folders of instructions that extend your agents' capabilities with specialized knowledge.

6
00:00:18,640 --> 00:00:23,720
 In the scores, you learn how skills work, learn best practices for creating them,

7
00:00:23,720 --> 00:00:29,400
 and build skills for different use cases, including coding and research and data analysis and more.

8
00:00:29,400 --> 00:00:32,280
 What's exciting about skills is they're now an open standard,

9
00:00:32,280 --> 00:00:36,800
 which means they have a standardized format that work with any skills compatible agent.

10
00:00:36,800 --> 00:00:40,880
 So you can build your skills once and deploy them across multiple agent products.

11
00:00:40,880 --> 00:00:46,200
 Any skill should include a skill.md markdown file, which contains a school's name,

12
00:00:46,200 --> 00:00:48,640
 description, and main instructions.

13
00:00:48,640 --> 00:00:53,440
 The main instructions can also refer to other files such as scripts, additional markdown files,

14
00:00:53,440 --> 00:00:56,560
 and accents such as templates and images.

15
00:00:56,560 --> 00:00:59,720
 Skills are progressively disclosed to the agents,

16
00:00:59,720 --> 00:01:04,000
 which means that the skills name and description always live in your agent's context window,

17
00:01:04,000 --> 00:01:07,760
 but the agent does not load the rest of the instructions into its context

18
00:01:07,760 --> 00:01:11,440
 until a user's request matches the skills' description.

19
00:01:11,440 --> 00:01:16,720
 At that point, the agent might then additionally load the reference and asset files if needed as well.

20
00:01:16,720 --> 00:01:19,600
 To use the skill, your agent needs a basic set of tools,

21
00:01:19,600 --> 00:01:23,680
 files is an access to reading right files and a badge to the execute code.

22
00:01:23,680 --> 00:01:28,120
 And these tools enable your agent to execute what the commands a skill requires.

23
00:01:28,120 --> 00:01:33,440
 Your agent can combine skills with MCP and subagents to create powerful agentic workflows.

24
00:01:33,440 --> 00:01:37,360
 For example, it can use MCP to get data from external sources,

25
00:01:37,360 --> 00:01:42,320
 then rely on a skill to know what to do with that data, or how to retrieve it efficiently.

26
00:01:42,320 --> 00:01:46,040
 It can also delegate tasks to a subagent with isolated context,

27
00:01:46,040 --> 00:01:48,840
 which can itself use skills for specialized knowledge.

28
00:01:48,840 --> 00:01:50,840
 In this course, we'll start with Cloud AI,

29
00:01:50,840 --> 00:01:56,800
 where we'll create a skill for a marketing campaign and combine it with the pre-built skills for Excel and PowerPoint.

30
00:01:56,800 --> 00:02:01,240
 Then we'll create two skills for content creation and data analysis workflows,

31
00:02:01,240 --> 00:02:03,400
 and try them with the Cloud API.

32
00:02:03,400 --> 00:02:07,360
 After that, we'll use skills with Cloud Code for reviewing and testing code.

33
00:02:07,360 --> 00:02:14,040
 And finally, we'll build a research agent with a Cloud Agent SDK that uses a skill to combine research results.

34
00:02:14,040 --> 00:02:19,400
 I'd like to thank Hara Salami from DBLAND.AI, who contributed to this course.

35
00:02:19,400 --> 00:02:22,200
 So how do you know when to use a skill?

36
00:02:22,200 --> 00:02:26,360
 Let's say you have a workflow that you repeatedly ask your agent to implement.

37
00:02:26,360 --> 00:02:29,160
 Instead of explaining the same workflow every time,

38
00:02:29,160 --> 00:02:34,160
 you can package it as a skill so your agent automatically knows what to do.

39
00:02:34,160 --> 00:02:37,960
 That's exactly what you learned with Eli in the first lesson.

40
00:02:37,960 --> 00:02:41,200
 So please go on to the next video to learn more.

41
00:02:41,200 --> 00:02:45,280
 Skills are folders of instructions that package repeated workflows,

42
00:02:45,280 --> 00:02:48,480
 specialized knowledge, or new capabilities for your agent.

43
00:02:48,480 --> 00:02:52,000
 If you find yourself typing the same prompt across conversations,

44
00:02:52,000 --> 00:02:54,680
 you should consider transforming that into a skill.

45
00:02:54,680 --> 00:02:57,200
 Let's explore how to do that using Cloud AI.

46
00:02:57,200 --> 00:03:03,120
 So before we talk a little bit more about skills and dive into what a skill looks like and how it works,

47
00:03:03,120 --> 00:03:07,320
 let's walk through a scenario to showcase why skills are so useful.

48
00:03:07,320 --> 00:03:12,840
 Right here, I've got some campaign data in a CSV that I'd like to analyze the performance of.

49
00:03:12,840 --> 00:03:14,760
 So just to show you what this looks like,

50
00:03:14,760 --> 00:03:18,720
 I've got a date, a campaign name, impressions, clicks, conversions,

51
00:03:18,720 --> 00:03:21,800
 you can imagine here that we're going to take in some marketing data

52
00:03:21,800 --> 00:03:24,600
 and use Cloud to analyze this information.

53
00:03:24,600 --> 00:03:27,000
 So my first prompt, I'm attaching this data,

54
00:03:27,000 --> 00:03:29,440
 explaining what the input data looks like,

55
00:03:29,440 --> 00:03:32,360
 asking to check for quality, funnel analysis,

56
00:03:32,360 --> 00:03:37,000
 and some useful metrics around what I expect for click-through rates and conversion rates.

57
00:03:37,000 --> 00:03:42,200
 At the bottom, I've got an output format that I'm requesting for this particular piece of data.

58
00:03:42,200 --> 00:03:46,920
 Now you can imagine it would be valuable to not have to include this prompt every time

59
00:03:46,920 --> 00:03:48,840
 and to have that packaged up.

60
00:03:48,840 --> 00:03:51,560
 As we take a look at what we're seeing in our campaign data,

61
00:03:51,560 --> 00:03:54,040
 Cloud is going to read this CSV.

62
00:03:54,040 --> 00:03:58,200
 It's then going to perform the data quality check and funnel analysis

63
00:03:58,200 --> 00:04:01,240
 and give us back our campaign performance analysis.

64
00:04:01,240 --> 00:04:04,840
 Here is going to show the total records, any missing data,

65
00:04:04,840 --> 00:04:07,640
 and any anomalies in the data that exist.

66
00:04:07,640 --> 00:04:09,480
 If we take a look a little bit further,

67
00:04:09,480 --> 00:04:14,760
 we'll see our funnel analysis versus the benchmark data that we were looking for before.

68
00:04:14,760 --> 00:04:17,000
 We can see here some things that are working better,

69
00:04:17,000 --> 00:04:18,920
 some things that are not working as well.

70
00:04:18,920 --> 00:04:22,360
 We're getting a lot of useful data back that we can take action around,

71
00:04:22,360 --> 00:04:25,160
 change our marketing campaigns, and move forward.

72
00:04:25,160 --> 00:04:29,880
 We've got a nice interpretation of what Cloud is telling us, what's working, what's not working.

73
00:04:29,880 --> 00:04:33,240
 And now we're going to go ahead and ask for additional computations

74
00:04:33,240 --> 00:04:36,280
 of certain efficiency metrics for marketing.

75
00:04:36,280 --> 00:04:41,640
 These include return on our ad spend, cost per acquisition, and net profit, and so on.

76
00:04:41,640 --> 00:04:45,080
 We're also going to ask for an output format in a certain fashion.

77
00:04:45,880 --> 00:04:48,200
 We'll see the results from this efficiency analysis.

78
00:04:48,200 --> 00:04:51,480
 We'll see what's working again, what's not working, and some interpretations.

79
00:04:52,040 --> 00:04:55,400
 We'll see our portfolio performance and our total net profit.

80
00:04:55,400 --> 00:04:59,080
 Looks like we're making money here, but there's still much more that I'm sure we can do.

81
00:04:59,080 --> 00:05:03,000
 The next step that we're going to do here is to take in an additional piece of data,

82
00:05:03,000 --> 00:05:05,080
 our budget reallocation rules.

83
00:05:05,080 --> 00:05:08,200
 The idea here is that we have extra money to play around with

84
00:05:08,200 --> 00:05:11,560
 and think about allocating towards other marketing channels.

85
00:05:11,560 --> 00:05:16,920
 You can imagine this file has quite a bit of data around the rules for allocating,

86
00:05:16,920 --> 00:05:21,960
 what we're trying to figure out, and how best to decide where to increase our budget.

87
00:05:21,960 --> 00:05:25,240
 This could also lead to maintaining a budget or decreasing a budget

88
00:05:25,240 --> 00:05:27,160
 based on this framework that we have here.

89
00:05:27,160 --> 00:05:31,320
 Again, this is a lot of data that is specific to our particular use case.

90
00:05:31,320 --> 00:05:35,960
 Claude knows how to handle particular decisions and analyze marketing metrics,

91
00:05:35,960 --> 00:05:39,960
 but here we're specifying exactly the way that we want to do things.

92
00:05:39,960 --> 00:05:44,360
 This requires me bringing in external documentation, finding the right people,

93
00:05:44,360 --> 00:05:48,360
 and even if I'm not the most knowledgeable about this, hoping that I get it right.

94
00:05:48,360 --> 00:05:52,040
 We're going to go ahead and see these allocation rules, our recommendations.

95
00:05:52,040 --> 00:05:56,360
 We can see what's passing, what's not passing, and a proposed reallocation here.

96
00:05:56,360 --> 00:06:01,880
 Freeing up some budget, analyzing what's working, and where to allocate additional budget towards.

97
00:06:01,880 --> 00:06:06,360
 What we've seen here is a step-by-step process that requires us as the user

98
00:06:06,360 --> 00:06:11,480
 to put in the necessary documentation and have the necessary pre-existing knowledge.

99
00:06:11,480 --> 00:06:14,440
 Not only that, but everything that I'm putting in here

100
00:06:14,440 --> 00:06:17,320
 is immediately getting added to the context window.

101
00:06:17,320 --> 00:06:19,320
 What happens if I want to ask something different?

102
00:06:19,320 --> 00:06:22,200
 What happens if I want to have a different kind of conversation?

103
00:06:22,200 --> 00:06:26,840
 This information here is not always necessary for everything I'm going to do.

104
00:06:26,840 --> 00:06:30,200
 What we're going to take a look at here is how we can take this information

105
00:06:30,200 --> 00:06:34,920
 and package it into a skill, a standalone asset, a folder really,

106
00:06:34,920 --> 00:06:39,640
 that contains instructions for how to go about performing the campaign analysis,

107
00:06:39,640 --> 00:06:44,200
 while also being intentional about what information goes into the context window,

108
00:06:44,200 --> 00:06:46,040
 and what information does it.

109
00:06:46,040 --> 00:06:50,200
 As we've seen, this is a weekly campaign performance analysis.

110
00:06:50,200 --> 00:06:54,840
 So this isn't something that I want to have to repeat on my own every single week

111
00:06:54,840 --> 00:06:58,040
 with this particular prompt by copying and pasting.

112
00:06:58,040 --> 00:07:01,960
 This is going to be much nicer to have pre-packaged that I can use myself,

113
00:07:01,960 --> 00:07:05,000
 share with members of the team, and edit as necessary.

114
00:07:05,000 --> 00:07:09,320
 So with that, let's take a look at what a skill.md file is.

115
00:07:09,320 --> 00:07:13,240
 This file needs to be named skill.md in markdown format,

116
00:07:13,240 --> 00:07:17,800
 and this is going to be the underlying set of instructions to perform the task that we saw.

117
00:07:18,360 --> 00:07:21,640
 In this markdown file, I have very similar information

118
00:07:21,640 --> 00:07:24,200
 to what I included in the previous prompt.

119
00:07:24,200 --> 00:07:27,240
 I have my input requirements, a data quality check,

120
00:07:27,240 --> 00:07:30,600
 funnel analysis with the metrics that we were working at before,

121
00:07:30,600 --> 00:07:31,880
 and historical benchmarks.

122
00:07:32,600 --> 00:07:37,080
 I have that same efficiency analysis as well as the output format that I expect.

123
00:07:37,640 --> 00:07:40,920
 Finally, I have a note here on budget reallocation

124
00:07:40,920 --> 00:07:46,520
 that references a different file only when the user asks about budget reallocation.

125
00:07:46,520 --> 00:07:50,520
 So we talked a little bit about how this can be much more efficient with context.

126
00:07:50,520 --> 00:07:54,600
 This is one example where I'm only going to be reading and using this file

127
00:07:54,600 --> 00:07:57,720
 if a user asks about that particular piece of information.

128
00:07:59,240 --> 00:08:01,960
 In order to get this skill to work as expected,

129
00:08:01,960 --> 00:08:05,560
 there's one more piece of data that I need to add to the beginning here.

130
00:08:05,560 --> 00:08:09,560
 This data is in a data format called YAML, and here's what it looks like.

131
00:08:10,520 --> 00:08:14,040
 Every skill that you make across the entire standard

132
00:08:14,040 --> 00:08:16,520
 requires a name as well as a description.

133
00:08:16,520 --> 00:08:20,520
 The name of the skill is going to be important for referencing when to use it,

134
00:08:20,520 --> 00:08:23,720
 and in the view I that we're working with if it's being used,

135
00:08:23,720 --> 00:08:27,320
 and the description is important so that the model that we're working with

136
00:08:27,320 --> 00:08:30,680
 can understand when to use this particular skill.

137
00:08:31,240 --> 00:08:34,600
 When you make a skill, the name and description are required.

138
00:08:34,600 --> 00:08:38,360
 So we've got our skill MD file, and the second file I want to show you

139
00:08:38,360 --> 00:08:41,240
 is just this budget reallocation rules file,

140
00:08:41,240 --> 00:08:44,520
 which is very similar to the other prompt that we saw.

141
00:08:44,520 --> 00:08:48,360
 When you make a skill, your skill can reference other files

142
00:08:48,360 --> 00:08:51,160
 as long as they're all in the same parent folder.

143
00:08:51,160 --> 00:08:55,000
 These budget reallocation rules are exactly what I put

144
00:08:55,000 --> 00:08:57,320
 in that previous conversation with Cloud AI.

145
00:08:57,880 --> 00:09:00,280
 So what we're doing here is we're moving away

146
00:09:00,280 --> 00:09:03,960
 from putting in instructions directly in our conversation,

147
00:09:03,960 --> 00:09:06,120
 and instead putting it into a folder.

148
00:09:06,760 --> 00:09:10,600
 Now that I've got this skill file as well as any external files,

149
00:09:11,240 --> 00:09:13,240
 what I'm going to do here is make a new folder.

150
00:09:13,880 --> 00:09:16,920
 And I'll name that folder the name of the skill,

151
00:09:16,920 --> 00:09:18,520
 analyzing marketing campaign.

152
00:09:19,240 --> 00:09:22,200
 There are some high level rules around naming skills,

153
00:09:22,200 --> 00:09:25,960
 stick with lowercase letters, use dashes between words,

154
00:09:25,960 --> 00:09:29,000
 and don't use reserved keywords like Claude or Anthropic.

155
00:09:29,800 --> 00:09:33,800
 Now that I've created this folder for the skill that I'm making,

156
00:09:33,800 --> 00:09:37,240
 I'm going to go ahead and make another folder called references.

157
00:09:38,040 --> 00:09:40,440
 When we look at the open standard for skills,

158
00:09:40,440 --> 00:09:43,640
 we're going to see that this actually is a specific name

159
00:09:43,640 --> 00:09:48,120
 that we use when there are external references that the skill uses.

160
00:09:48,120 --> 00:09:49,960
 And inside of our skill MD,

161
00:09:49,960 --> 00:09:54,200
 we linked to references slash budget reallocation rules.

162
00:09:54,200 --> 00:09:57,000
 So I'll go ahead and put that file in this folder.

163
00:09:57,560 --> 00:10:00,600
 I'll put the folder inside of our marketing campaign,

164
00:10:00,600 --> 00:10:04,520
 and then I'll put the skill MD at the top level of this folder.

165
00:10:05,160 --> 00:10:07,320
 If we take a quick look at what's inside,

166
00:10:07,320 --> 00:10:11,160
 we should see our skill MD as well as our references folder

167
00:10:11,160 --> 00:10:14,200
 that contains that additional budget allocation file.

168
00:10:14,840 --> 00:10:18,440
 Now I'm going to go ahead and create a zip file from this folder,

169
00:10:19,080 --> 00:10:21,720
 and I'm going to go ahead and upload that to Claude AI.

170
00:10:22,280 --> 00:10:24,120
 Once I upload that skill,

171
00:10:24,120 --> 00:10:27,160
 I should be able to start using it in future conversations.

172
00:10:28,120 --> 00:10:31,000
 I'm going to head over to my settings right over here,

173
00:10:31,000 --> 00:10:32,760
 and I'm going to go to capabilities.

174
00:10:33,720 --> 00:10:36,680
 As I navigate to the bottom of capabilities,

175
00:10:36,680 --> 00:10:38,360
 we're going to see this section on skills.

176
00:10:38,920 --> 00:10:41,800
 There are some example ones that we'll talk a little bit about later,

177
00:10:41,800 --> 00:10:43,480
 but right now I want to add my own.

178
00:10:44,040 --> 00:10:45,480
 So I'm going to go ahead and add,

179
00:10:45,480 --> 00:10:49,640
 and I'm going to upload the skill in a zip file that I created.

180
00:10:49,640 --> 00:10:52,200
 I'm going to go ahead and drag and drop that zip file,

181
00:10:52,200 --> 00:10:54,040
 and give that a second to upload.

182
00:10:54,040 --> 00:10:56,760
 Once that's done, we can see the name of our skill

183
00:10:56,760 --> 00:10:58,760
 as well as that description.

184
00:10:58,760 --> 00:11:00,600
 Now that we've uploaded our skill,

185
00:11:00,600 --> 00:11:01,880
 let's go see this in action.

186
00:11:02,520 --> 00:11:03,800
 I'm going to start with a new chat.

187
00:11:04,440 --> 00:11:08,520
 I'm going to go ahead and ask Claude a similar prompt to what I had before,

188
00:11:08,520 --> 00:11:11,640
 and I'm going to go ahead now and attach the same CSV

189
00:11:11,640 --> 00:11:12,920
 that I was working with before.

190
00:11:13,480 --> 00:11:14,920
 If this works as expected,

191
00:11:14,920 --> 00:11:17,960
 we should start to see Claude pick up the skill

192
00:11:17,960 --> 00:11:19,480
 for our weekly marketing campaign.

193
00:11:20,040 --> 00:11:23,320
 Claude should then perform the tasks required in that skill,

194
00:11:23,320 --> 00:11:27,320
 and the need for us to have all that prompt back and forth is no longer there.

195
00:11:27,880 --> 00:11:29,800
 So let's go ahead and see what Claude can do here.

196
00:11:30,440 --> 00:11:32,760
 We'll see here it's going to read the skill file

197
00:11:32,760 --> 00:11:35,640
 to ensure it's following the right instructions.

198
00:11:35,640 --> 00:11:38,360
 The name of our skill as well as the description

199
00:11:38,360 --> 00:11:40,760
 is what is allowing Claude to pick this up.

200
00:11:40,760 --> 00:11:43,560
 Since we're asking about reallocating the budget,

201
00:11:43,560 --> 00:11:46,360
 it's going to go ahead and read that additional file

202
00:11:46,360 --> 00:11:48,760
 that we uploaded to our skill.

203
00:11:48,760 --> 00:11:51,080
 We'll then go ahead and analyze the data.

204
00:11:51,080 --> 00:11:54,600
 If you want to see the code that Claude is running and executing here,

205
00:11:54,600 --> 00:11:58,760
 you can always open this up and take a look at what's happening behind the scenes.

206
00:12:02,760 --> 00:12:06,360
 What we're going to see here is something very similar to what we saw before.

207
00:12:06,360 --> 00:12:09,400
 We're going to analyze channels that may have additional challenges.

208
00:12:09,400 --> 00:12:10,760
 In this case, TikTok,

209
00:12:10,760 --> 00:12:14,360
 we may see things that are working as well as recommended reallocations.

210
00:12:14,920 --> 00:12:18,200
 But in this case, we didn't have to add all the prompting ourselves.

211
00:12:18,200 --> 00:12:21,480
 This skill can be shared across many different platforms,

212
00:12:21,480 --> 00:12:23,400
 and since skills are an open standard,

213
00:12:23,400 --> 00:12:26,200
 this is supported in other coding environments

214
00:12:26,200 --> 00:12:28,760
 like codecs, Gemini, CLI, and much more.

215
00:12:29,320 --> 00:12:34,520
 So not only have we created a way to take this data and package it up into a centralized place,

216
00:12:34,520 --> 00:12:36,760
 we're being more efficient with the context window,

217
00:12:36,760 --> 00:12:39,160
 and the portability here is extremely valuable.

218
00:12:39,720 --> 00:12:44,360
 Now, let's go ahead and create a report with the data that we found.

219
00:12:44,360 --> 00:12:46,920
 We're going to go ahead and create an Excel report

220
00:12:46,920 --> 00:12:49,000
 with the following pieces of information,

221
00:12:49,000 --> 00:12:51,240
 as well as a color coding that we're recommending.

222
00:12:51,800 --> 00:12:54,600
 Under the hood, the ability to create spreadsheets

223
00:12:54,600 --> 00:12:57,080
 and execute necessary code to do so

224
00:12:57,080 --> 00:13:00,840
 actually lives in a skill that comes built in to cloud.

225
00:13:00,840 --> 00:13:04,040
 So we're actually going to see the underlying skill being used,

226
00:13:04,040 --> 00:13:06,840
 code being run to create this Excel file,

227
00:13:06,840 --> 00:13:10,280
 and then finally the output based on the requirements that we specified.

228
00:13:13,480 --> 00:13:15,000
 We've got our spreadsheet now.

229
00:13:15,000 --> 00:13:19,480
 Here we can see you've got an executive summary, funnel analysis, efficiency analysis,

230
00:13:20,040 --> 00:13:23,640
 and we can go and open this in Google Drive or download the spreadsheet.

231
00:13:24,200 --> 00:13:28,760
 Through the use of our skill to analyze data and give us what we need,

232
00:13:28,760 --> 00:13:31,560
 as well as built-in skills to create spreadsheets,

233
00:13:31,560 --> 00:13:36,520
 we can transform data from CSVs into meaningful, actionable insights

234
00:13:36,520 --> 00:13:38,440
 in many different kinds of file formats.

235
00:13:39,000 --> 00:13:41,960
 Next, we'll explore in a little bit more depth

236
00:13:41,960 --> 00:13:44,200
 what a skill looks like, how it works,

237
00:13:44,200 --> 00:13:46,920
 and where it fits into the entire AI ecosystem.

238
00:13:47,560 --> 00:13:51,480
 In the previous lesson, we saw how to create skills in cloud

239
00:13:51,480 --> 00:13:56,040
 and move from prompts with data to package skills that we can use

240
00:13:56,040 --> 00:13:57,880
 across many different conversations.

241
00:13:58,440 --> 00:14:01,320
 Now let's dive deeper and talk about what skills are

242
00:14:01,320 --> 00:14:03,320
 and the open standard that powers them.

243
00:14:03,880 --> 00:14:09,400
 Similar to the model context protocol, skills themselves are an open standard

244
00:14:09,400 --> 00:14:13,320
 that can be used across many different AI applications.

245
00:14:13,320 --> 00:14:16,920
 While skills were something originally created at anthropic,

246
00:14:16,920 --> 00:14:22,120
 skills themselves are now an open standard with a specific specification

247
00:14:22,120 --> 00:14:24,600
 that is used across many different platforms,

248
00:14:24,600 --> 00:14:29,960
 including codecs, Gemini CLI, Cloud Code, Open Code, and much more.

249
00:14:29,960 --> 00:14:32,760
 With that in mind, let's talk a little bit about how this works.

250
00:14:33,320 --> 00:14:38,360
 When we build AI applications, in order to use particular skills,

251
00:14:38,360 --> 00:14:41,160
 we need to make use of some kind of file system

252
00:14:41,160 --> 00:14:44,520
 when using tools like Cloud AI or Cloud Desktop.

253
00:14:44,520 --> 00:14:49,560
 In that file system, we load folders that contain a skill-empty file

254
00:14:49,560 --> 00:14:52,680
 and sub-folders or files that can be referenced.

255
00:14:52,680 --> 00:14:55,720
 Here we can see exactly what we did previously.

256
00:14:55,720 --> 00:15:00,440
 At the same time, skills themselves can not only include other

257
00:15:00,440 --> 00:15:03,960
 markdown documents, but scripts that can be executed.

258
00:15:03,960 --> 00:15:08,360
 For example, we have a skill for working with PDF documents.

259
00:15:08,360 --> 00:15:13,080
 We need to convert PDFs to images, extract info from form fields,

260
00:15:13,080 --> 00:15:16,120
 and even fill PDF forms with annotations.

261
00:15:16,120 --> 00:15:18,520
 This requires code to be executed,

262
00:15:18,520 --> 00:15:23,720
 but that code that needs to be executed can be referenced from the skill-empty file.

263
00:15:23,720 --> 00:15:27,880
 So as we start to explore our own custom skills and built-in skills,

264
00:15:27,880 --> 00:15:33,320
 it's important to note that skills are not just text files that reference other text files,

265
00:15:33,320 --> 00:15:38,760
 but text files that can reference scripts, what they do, and when they need to be executed.

266
00:15:38,760 --> 00:15:43,800
 Skills can also include icons, images, and other assets

267
00:15:43,800 --> 00:15:48,520
 as we start to think about ways of creating custom styles and brands.

268
00:15:48,520 --> 00:15:53,000
 Where skills really shine are places where Cloud might not know

269
00:15:53,000 --> 00:15:56,040
 exactly how you or your company operates.

270
00:15:56,040 --> 00:16:00,120
 You can imagine designing newsletters, creating brand guides,

271
00:16:00,120 --> 00:16:06,760
 things that Cloud has a general idea on, but not the exact way that your company or your team does it.

272
00:16:06,760 --> 00:16:13,320
 To give some more idea of why we bring agent skills into the mix when we're building our own agents,

273
00:16:13,320 --> 00:16:18,600
 the way that we used to think about building agents centered around agents with a single purpose,

274
00:16:18,600 --> 00:16:22,200
 coding, research, finance, marketing, and much more.

275
00:16:22,200 --> 00:16:25,960
 These domain-specific agents had a particular set of tools,

276
00:16:25,960 --> 00:16:29,240
 the context it needed to perform the task necessary.

277
00:16:29,240 --> 00:16:32,520
 But as we started to build more of these single-purpose agents,

278
00:16:32,520 --> 00:16:37,720
 we started to realize that under the hood, all that they really need is a simple scaffolding,

279
00:16:37,720 --> 00:16:43,720
 underlying tools like bash and a file system to find, edit, modify, execute,

280
00:16:43,720 --> 00:16:46,600
 and perform whatever tasks are necessary.

281
00:16:46,600 --> 00:16:51,480
 These simpler agents are easier to evaluate, understand, and scale.

282
00:16:51,480 --> 00:16:56,280
 But what these agents lacked was the underlying context and domain expertise

283
00:16:56,280 --> 00:16:57,960
 to do the job reliably.

284
00:16:57,960 --> 00:17:02,440
 That context can be provided through skills, through the model context protocol,

285
00:17:02,440 --> 00:17:06,440
 but that domain expertise is really where skills shine as well.

286
00:17:06,440 --> 00:17:10,840
 We want finance agents to perform financial analysis in a particular fashion.

287
00:17:10,840 --> 00:17:16,520
 We want research agents to have the domain expertise necessary to research the way that we want.

288
00:17:16,520 --> 00:17:20,680
 We want to be able to port that across many different ecosystems and agents,

289
00:17:20,680 --> 00:17:22,920
 and that's why we have agent skills.

290
00:17:22,920 --> 00:17:29,560
 These skills provide us the procedural knowledge and the user-specific context that they can load on demand.

291
00:17:29,560 --> 00:17:35,160
 In addition to domain expertise, skills can also provide a repeatable workflow.

292
00:17:35,160 --> 00:17:41,400
 In a non-deterministic system, where we don't always know exactly what the output of the model is going to be,

293
00:17:41,400 --> 00:17:45,800
 it can be difficult to find repeatable ways of producing the same output.

294
00:17:45,800 --> 00:17:49,560
 What skills allow us to do is provide a repeatable workflow

295
00:17:49,560 --> 00:17:54,440
 with very articulate steps or instructions that allow the agent to perform a task

296
00:17:54,440 --> 00:17:57,480
 that we can start to predict with more accuracy.

297
00:17:57,480 --> 00:18:01,160
 Skills also introduce the idea of new capabilities,

298
00:18:01,160 --> 00:18:04,040
 things that an agent does not know how to do out of the box,

299
00:18:04,040 --> 00:18:08,040
 or even data that Claude has no idea how to operate on.

300
00:18:08,040 --> 00:18:12,440
 When we bring in these new capabilities, we unleash an entire ecosystem

301
00:18:12,440 --> 00:18:17,000
 and new functionality for our agents with minimal additional context.

302
00:18:17,000 --> 00:18:23,000
 As we think about domain expertise, we want to lean on things that Claude might not know how to do,

303
00:18:23,000 --> 00:18:27,480
 or knows how to do, but not for your particular domain.

304
00:18:27,480 --> 00:18:31,640
 Claude can perform data analysis. Claude can perform legal review,

305
00:18:31,640 --> 00:18:36,200
 but how does it do it the way that you or your team or company want it to be done?

306
00:18:36,200 --> 00:18:40,440
 We previously saw the ability to perform weekly marketing campaign reviews,

307
00:18:40,440 --> 00:18:44,760
 and we want that to be predictable across many different individuals and teams.

308
00:18:44,760 --> 00:18:47,800
 As we start to think about some of these new capabilities,

309
00:18:47,800 --> 00:18:51,960
 things like generating presentations, Excel spreadsheets, PDF reports,

310
00:18:51,960 --> 00:18:55,240
 executing scripts when necessary to perform those actions,

311
00:18:55,240 --> 00:18:57,880
 that here is where agent skills can shine.

312
00:18:57,880 --> 00:19:02,600
 What we saw previously without skills was the idea of describing our instructions,

313
00:19:02,600 --> 00:19:07,240
 trying to predict workflows, and bundling all of the necessary files

314
00:19:07,240 --> 00:19:09,480
 in context at one time.

315
00:19:09,480 --> 00:19:12,360
 We talked a little bit about the portability of skills,

316
00:19:12,360 --> 00:19:15,960
 and while we've seen skills so far in Claude AI,

317
00:19:15,960 --> 00:19:18,840
 skills can be used in the exact same format,

318
00:19:18,840 --> 00:19:22,760
 not only across Claude code, the agent SDK, and the API,

319
00:19:22,760 --> 00:19:25,480
 but since agent skills are an open standard,

320
00:19:25,480 --> 00:19:28,760
 you can use this across a growing number of agent products.

321
00:19:28,760 --> 00:19:31,080
 You can create skills in one environment,

322
00:19:31,080 --> 00:19:35,720
 and use them and share them and scale them across many different environments.

323
00:19:35,720 --> 00:19:39,880
 When we say that skills are composable, this is something that we've seen already.

324
00:19:39,880 --> 00:19:43,800
 We can take custom skills like analyzing our marketing campaign,

325
00:19:43,800 --> 00:19:47,240
 and we can combine that with built-in skills like creating

326
00:19:47,240 --> 00:19:50,840
 PowerPoint presentations, PDFs, or Excel spreadsheets.

327
00:19:50,840 --> 00:19:53,880
 Not only can we use multiple skills together,

328
00:19:53,880 --> 00:19:58,680
 but we can combine them to build complex and predictable workflows.

329
00:19:58,680 --> 00:20:02,360
 We can reference the skills necessary, the steps necessary,

330
00:20:02,360 --> 00:20:07,160
 and start to create predictable outputs in a non-deterministic system.

331
00:20:07,160 --> 00:20:10,680
 Under the hood, skills can contain quite a bit of information.

332
00:20:10,680 --> 00:20:13,480
 We saw examples with additional markdown files

333
00:20:13,480 --> 00:20:16,600
 and even examples with scripts that can be executed.

334
00:20:16,600 --> 00:20:19,320
 You can have hundreds of skills across your system,

335
00:20:19,320 --> 00:20:21,320
 and what we're going to see quite a bit more

336
00:20:21,320 --> 00:20:23,480
 is that to protect the context window,

337
00:20:23,480 --> 00:20:26,280
 skills are progressively disclosed.

338
00:20:26,280 --> 00:20:28,680
 The idea of progressive disclosure

339
00:20:28,680 --> 00:20:34,440
 is to only load the data necessary and avoid polluting the context.

340
00:20:34,440 --> 00:20:37,480
 We like to think of the context window as a public good.

341
00:20:37,480 --> 00:20:40,200
 The more data that we add to the context window,

342
00:20:40,200 --> 00:20:41,960
 the more tokens we consume,

343
00:20:41,960 --> 00:20:43,960
 the faster our context window fills up,

344
00:20:43,960 --> 00:20:46,920
 and the likelihood of context degradation

345
00:20:46,920 --> 00:20:50,120
 or incorrect responses potentially increases.

346
00:20:50,120 --> 00:20:52,920
 In order to avoid polluting the context window

347
00:20:52,920 --> 00:20:55,000
 with data that we might not need,

348
00:20:55,000 --> 00:20:58,200
 skills introduce the idea of progressive disclosure.

349
00:20:58,200 --> 00:21:00,520
 When skills are loaded from the file system,

350
00:21:00,520 --> 00:21:03,720
 the only data that gets added to the context window

351
00:21:03,720 --> 00:21:06,040
 is the name and description of the skill.

352
00:21:06,040 --> 00:21:09,720
 This is essential so that Claude or any other system knows

353
00:21:09,720 --> 00:21:12,280
 what the skill is and how to trigger it.

354
00:21:12,280 --> 00:21:14,440
 Once that skill is triggered,

355
00:21:14,440 --> 00:21:17,080
 the underlying skill MD is loaded.

356
00:21:17,080 --> 00:21:20,520
 This is the next phase of loading data into context.

357
00:21:20,520 --> 00:21:23,160
 And depending on what is required,

358
00:21:23,160 --> 00:21:25,560
 if there are additional files or scripts

359
00:21:25,560 --> 00:21:27,880
 that need to be loaded and executed,

360
00:21:27,880 --> 00:21:30,120
 those will be loaded progressively.

361
00:21:30,120 --> 00:21:33,560
 These additional resources can be loaded as needed

362
00:21:33,560 --> 00:21:36,200
 and if there are scripts that need to be loaded,

363
00:21:36,200 --> 00:21:39,400
 those scripts are loaded and executed separately

364
00:21:39,400 --> 00:21:42,440
 from the context window to avoid polluting

365
00:21:42,440 --> 00:21:45,080
 with additional tokens that are not necessary.

366
00:21:45,080 --> 00:21:48,040
 By using tools like bash and a file system,

367
00:21:48,040 --> 00:21:51,480
 Claude can load only the information that's necessary,

368
00:21:51,480 --> 00:21:55,800
 execute only scripts and reading of files that is necessary,

369
00:21:55,800 --> 00:21:58,760
 and intentionally only add what is necessary

370
00:21:58,760 --> 00:22:00,360
 to the context window.

371
00:22:00,360 --> 00:22:03,560
 In the next lesson, we'll continue talking about skills

372
00:22:03,560 --> 00:22:07,560
 and particularly how they're used alongside other technologies

373
00:22:07,560 --> 00:22:10,360
 like the model context protocol, subagents,

374
00:22:10,360 --> 00:22:12,040
 underlying tools, and much more.

375
00:22:12,920 --> 00:22:16,120
 In the first lesson, Claude AI used the Excel skill

376
00:22:16,120 --> 00:22:18,920
 to create spreadsheets displaying the marketing results.

377
00:22:19,560 --> 00:22:22,680
 The Excel skill is one of anthropics pre-built skills,

378
00:22:22,680 --> 00:22:26,600
 which also include a PowerPoint, Word, and PDF skill,

379
00:22:26,600 --> 00:22:28,920
 as well as a skill creation skill.

380
00:22:28,920 --> 00:22:30,600
 Let's take a look at those.

381
00:22:30,600 --> 00:22:35,240
 Now that we've seen how skills fit in the entire AI ecosystem,

382
00:22:35,240 --> 00:22:37,960
 let's take a look at some of the pre-built skills

383
00:22:37,960 --> 00:22:42,120
 that you can use out of the box with Claude AI and Claude Desktop

384
00:22:42,120 --> 00:22:45,640
 and that you can install yourself with tools like Claude Code.

385
00:22:45,640 --> 00:22:50,920
 Inside of this repository that lives at github.com/anthropic/skills,

386
00:22:50,920 --> 00:22:52,680
 let's take a look at the skills folder

387
00:22:52,680 --> 00:22:55,160
 and see which built-in ones that we have.

388
00:22:55,160 --> 00:22:58,040
 All of these are ready for production usage

389
00:22:58,040 --> 00:23:00,760
 and we actually saw in a previous lesson

390
00:23:00,760 --> 00:23:03,240
 the use case of this Excel skill.

391
00:23:03,800 --> 00:23:06,200
 It's important to note that this list of skills

392
00:23:06,200 --> 00:23:08,680
 while created at anthropic is actually

393
00:23:08,680 --> 00:23:10,920
 bucketed into two different sections.

394
00:23:10,920 --> 00:23:16,280
 The skills from Microsoft Docs, PDFs, PowerPoints, and Excel

395
00:23:16,280 --> 00:23:18,440
 are known as document skills.

396
00:23:18,440 --> 00:23:22,440
 These are built-in and always used in tools like Claude AI.

397
00:23:22,440 --> 00:23:26,440
 The remainder of these skills are examples that we've created

398
00:23:26,440 --> 00:23:28,920
 that you can toggle on and off in Claude

399
00:23:28,920 --> 00:23:31,720
 but by default with the exception of skill creator

400
00:23:31,720 --> 00:23:32,920
 are toggled off.

401
00:23:32,920 --> 00:23:36,440
 Let's first start by analyzing the PowerPoint skill.

402
00:23:37,240 --> 00:23:39,720
 We can see just like other structures

403
00:23:39,720 --> 00:23:43,640
 that we have a skill MD file as well as other files

404
00:23:43,640 --> 00:23:45,000
 and folders to reference.

405
00:23:46,040 --> 00:23:48,120
 Inside of this skill MD,

406
00:23:48,120 --> 00:23:50,760
 we have that same YAML front matter

407
00:23:50,760 --> 00:23:53,160
 that includes the name and the description.

408
00:23:53,960 --> 00:23:57,000
 What you're seeing here is how GitHub is rendering

409
00:23:57,000 --> 00:23:59,880
 this markdown file but the underlying code

410
00:24:00,440 --> 00:24:03,320
 looks very similar to what we've made before.

411
00:24:03,320 --> 00:24:05,480
 You can view it this way if you're familiar

412
00:24:05,480 --> 00:24:06,840
 with markdown files.

413
00:24:06,840 --> 00:24:08,360
 I'll switch back to the preview

414
00:24:08,360 --> 00:24:09,800
 because it looks a little bit nicer.

415
00:24:10,360 --> 00:24:12,680
 When we take a look at how this skill works

416
00:24:12,680 --> 00:24:15,400
 and what it does, we've got an overview.

417
00:24:15,400 --> 00:24:18,040
 The users may ask to create, edit,

418
00:24:18,040 --> 00:24:20,680
 analyze contents of a PowerPoint file.

419
00:24:20,680 --> 00:24:21,880
 Here's what it looks like.

420
00:24:21,880 --> 00:24:23,320
 Here's how you read it.

421
00:24:23,320 --> 00:24:26,440
 And if there are particular tasks that need to be done,

422
00:24:26,440 --> 00:24:29,960
 there are underlying scripts to go ahead and execute.

423
00:24:29,960 --> 00:24:33,400
 Remember, these are not executed right out of the box.

424
00:24:33,400 --> 00:24:36,680
 These are only loaded and executed when necessary.

425
00:24:36,680 --> 00:24:40,360
 There's quite a bit that we can do with PowerPoint presentations,

426
00:24:40,360 --> 00:24:42,040
 colors, topography.

427
00:24:42,040 --> 00:24:44,440
 As you can imagine, this is how we can start to make things

428
00:24:44,440 --> 00:24:48,280
 that look nicer and look more like real world presentations

429
00:24:48,280 --> 00:24:48,920
 out of the box.

430
00:24:49,560 --> 00:24:51,640
 There are design principles that we have,

431
00:24:51,640 --> 00:24:53,480
 requirements that are necessary

432
00:24:53,480 --> 00:24:55,160
 and color palette selections

433
00:24:55,160 --> 00:24:56,920
 that we can have clawed pick from

434
00:24:56,920 --> 00:24:58,680
 when the user does not specify them.

435
00:24:59,400 --> 00:25:01,160
 This skill MD is quite long,

436
00:25:01,160 --> 00:25:03,080
 as there's quite a bit that we can do

437
00:25:03,080 --> 00:25:05,000
 with PowerPoint presentations.

438
00:25:05,000 --> 00:25:07,240
 But what we're going to see later in this lesson

439
00:25:07,240 --> 00:25:09,320
 is that I actually use this skill

440
00:25:09,320 --> 00:25:10,760
 to take existing data

441
00:25:10,760 --> 00:25:13,240
 and turn it into a beautiful looking presentation.

442
00:25:14,120 --> 00:25:15,640
 The next skill I want to show you

443
00:25:15,640 --> 00:25:18,360
 is a little bit of a meta idea here

444
00:25:18,360 --> 00:25:20,600
 and that's called the skill creator.

445
00:25:20,600 --> 00:25:23,000
 And the skill creator is a skill

446
00:25:23,000 --> 00:25:24,360
 that serves the purpose

447
00:25:24,360 --> 00:25:27,560
 of programmatically creating skills for you.

448
00:25:27,560 --> 00:25:30,120
 Instead of having to do things from scratch

449
00:25:30,120 --> 00:25:33,400
 and create the necessary files and folder structure,

450
00:25:33,400 --> 00:25:35,720
 the skill creator can do that for you.

451
00:25:35,720 --> 00:25:38,280
 Let's take a look at the skill MD file

452
00:25:38,280 --> 00:25:39,800
 and see what's happening here.

453
00:25:39,800 --> 00:25:41,400
 Similar to our other skills,

454
00:25:41,400 --> 00:25:43,400
 we have a name and a description.

455
00:25:43,400 --> 00:25:44,760
 And I'm actually going to take a look

456
00:25:44,760 --> 00:25:46,360
 at the underlying code here

457
00:25:46,360 --> 00:25:47,960
 since it's a little bit easier to follow.

458
00:25:48,760 --> 00:25:51,720
 We specify in this skill MD file

459
00:25:51,720 --> 00:25:54,120
 what a skill is, what it provides,

460
00:25:54,680 --> 00:25:57,160
 and then we include some of the best practices

461
00:25:57,160 --> 00:25:58,440
 associated with skills.

462
00:25:59,080 --> 00:26:01,160
 We're going to dive into those best practices

463
00:26:01,160 --> 00:26:02,040
 in the next lesson.

464
00:26:02,600 --> 00:26:04,440
 But you can imagine when Claude is

465
00:26:04,440 --> 00:26:06,760
 programmatically creating skills for you,

466
00:26:06,760 --> 00:26:08,920
 we want to leverage some of these best practices.

467
00:26:09,560 --> 00:26:11,880
 When we take a look at the skill creation process,

468
00:26:12,760 --> 00:26:14,280
 we're extremely explicit

469
00:26:14,280 --> 00:26:15,720
 with the steps that we have here.

470
00:26:16,280 --> 00:26:20,360
 Since we want to use this skill to create a predictable workflow,

471
00:26:20,360 --> 00:26:22,440
 we want to be extremely explicit

472
00:26:22,440 --> 00:26:24,040
 with what the steps are,

473
00:26:24,040 --> 00:26:25,320
 how to follow them,

474
00:26:25,320 --> 00:26:29,080
 and what to skip only if some reason exists.

475
00:26:29,080 --> 00:26:31,320
 We start with concrete examples,

476
00:26:31,320 --> 00:26:33,560
 we plan reusable skill contents,

477
00:26:34,120 --> 00:26:36,520
 and here you can start to see examples

478
00:26:36,520 --> 00:26:39,560
 that are very helpful for Claude to pattern match

479
00:26:39,560 --> 00:26:41,400
 when there's a skill you'd like to create.

480
00:26:41,960 --> 00:26:43,560
 When we start initializing the skill,

481
00:26:44,200 --> 00:26:47,320
 here we're running underlying Python scripts

482
00:26:47,320 --> 00:26:49,480
 to perform the task necessary.

483
00:26:49,480 --> 00:26:51,560
 Let's take a look at what those scripts do.

484
00:26:53,720 --> 00:26:55,480
 Inside of the scripts folder,

485
00:26:55,480 --> 00:26:57,240
 I have three Python files here,

486
00:26:57,880 --> 00:26:59,960
 a script to initialize the skill

487
00:26:59,960 --> 00:27:01,640
 and provide the underlying text,

488
00:27:02,360 --> 00:27:04,280
 a Python file to package that skill,

489
00:27:05,080 --> 00:27:07,480
 and then a script to validate that skill.

490
00:27:08,040 --> 00:27:10,920
 Let's take a look at what this underlying code does

491
00:27:10,920 --> 00:27:12,440
 to initialize a skill.

492
00:27:12,440 --> 00:27:14,760
 We take an existing template that we have,

493
00:27:14,760 --> 00:27:16,360
 with some yaml front matter,

494
00:27:16,360 --> 00:27:18,360
 and some placeholders and todos,

495
00:27:18,360 --> 00:27:21,800
 and we fill that in based on the data that is coming in.

496
00:27:22,360 --> 00:27:24,200
 This underlying script allows us

497
00:27:24,200 --> 00:27:28,040
 to create the necessary text files when making our skills.

498
00:27:29,240 --> 00:27:31,800
 Once we've generated the necessary files,

499
00:27:31,800 --> 00:27:33,160
 we can package that up.

500
00:27:33,160 --> 00:27:36,120
 Here you can see we're bringing in the necessary modules

501
00:27:36,120 --> 00:27:38,200
 to zip our skill necessary

502
00:27:38,200 --> 00:27:39,640
 and make sure that we're doing this

503
00:27:39,640 --> 00:27:41,800
 in the right folder and file structure.

504
00:27:42,520 --> 00:27:44,520
 Finally, we have one last script

505
00:27:44,520 --> 00:27:47,160
 to perform a validation of our skill.

506
00:27:47,160 --> 00:27:49,320
 Make sure that a skill MD exists,

507
00:27:50,040 --> 00:27:52,280
 validate some of the yaml front matter,

508
00:27:52,280 --> 00:27:54,280
 and make sure that what we put

509
00:27:54,280 --> 00:27:57,080
 inside of our folder and files is correct.

510
00:27:57,880 --> 00:28:00,760
 We're going to be leveraging this skill creator skill

511
00:28:00,760 --> 00:28:02,840
 to take existing content that we have

512
00:28:02,840 --> 00:28:06,440
 and package it up into a reusable and modular script.

513
00:28:06,440 --> 00:28:09,320
 Now let's go ahead and shift gears back to cloud

514
00:28:09,320 --> 00:28:11,880
 and see how to put together built-in skills

515
00:28:12,440 --> 00:28:15,000
 our own skills and a predictable workflow

516
00:28:15,000 --> 00:28:16,200
 with an MCP server.

517
00:28:17,080 --> 00:28:19,640
 Back in cloud, let's go and take a look

518
00:28:19,640 --> 00:28:22,440
 and make sure that we have the correct skills enabled

519
00:28:22,440 --> 00:28:23,320
 and where those live.

520
00:28:24,280 --> 00:28:26,840
 Back in settings, inside of capabilities,

521
00:28:27,480 --> 00:28:30,840
 we saw previously we can create skills in this section.

522
00:28:31,400 --> 00:28:34,200
 What I want to show you are the example skills that we have

523
00:28:34,840 --> 00:28:36,520
 and this should look pretty familiar.

524
00:28:36,520 --> 00:28:38,040
 This is what we saw on GitHub.

525
00:28:38,760 --> 00:28:41,560
 By default, these skills are turned off

526
00:28:41,560 --> 00:28:44,280
 if we want to toggle them on, we can absolutely do so.

527
00:28:44,920 --> 00:28:47,640
 The skill that is toggled on by default

528
00:28:47,640 --> 00:28:50,280
 is the skill creator that we just saw.

529
00:28:50,280 --> 00:28:53,160
 It's important to note that while the skill creator

530
00:28:53,160 --> 00:28:56,440
 is extremely effective at creating underlying skills

531
00:28:56,440 --> 00:28:58,040
 and structure necessary,

532
00:28:58,040 --> 00:29:01,400
 we still have to be intentional about the prompt that we provide

533
00:29:01,400 --> 00:29:04,360
 and the data that goes in to the skill that we're going to make.

534
00:29:05,240 --> 00:29:08,280
 What we're going to do now is put all of these ideas

535
00:29:08,280 --> 00:29:12,040
 around skills, MCP, and prompting together.

536
00:29:12,760 --> 00:29:14,840
 First, we're going to modify

537
00:29:14,840 --> 00:29:18,120
 our previous skill that we created for analyzing campaigns

538
00:29:18,680 --> 00:29:23,480
 to not use a CSV for data, but instead, BigQuery.

539
00:29:23,480 --> 00:29:27,640
 If you're not familiar, BigQuery is a data store powered by Google

540
00:29:27,640 --> 00:29:30,120
 and in order to bring in the necessary tooling

541
00:29:30,120 --> 00:29:32,360
 and context to work with BigQuery,

542
00:29:32,360 --> 00:29:34,840
 we're going to connect an MCP server.

543
00:29:34,840 --> 00:29:38,520
 So we're going to use the skill creator skill to modify

544
00:29:38,520 --> 00:29:42,440
 our previous marketing analyzing skill to use BigQuery.

545
00:29:42,440 --> 00:29:46,680
 We're then going to use skill creator to create another skill.

546
00:29:46,680 --> 00:29:49,560
 This will be for the purpose of brand guidelines.

547
00:29:49,560 --> 00:29:54,440
 We'll include a file that specifies the guidelines as well as logos

548
00:29:54,440 --> 00:29:57,960
 and we'll build for ourselves another skill to perform that task.

549
00:29:58,600 --> 00:30:02,120
 Finally, we'll take our two skills that we used

550
00:30:02,120 --> 00:30:06,040
 to extract and analyze data and to leverage brand guidelines

551
00:30:06,040 --> 00:30:08,440
 and combine them with a built-in skill

552
00:30:08,440 --> 00:30:10,680
 for creating PowerPoint presentations

553
00:30:10,680 --> 00:30:13,800
 to create a workflow that makes use of prompting,

554
00:30:13,800 --> 00:30:16,440
 skills, and the model context protocol.

555
00:30:16,440 --> 00:30:18,920
 Before we jump in, you might be wondering

556
00:30:18,920 --> 00:30:21,240
 where the Excel and PowerPoint

557
00:30:21,240 --> 00:30:24,440
 and other document skills that we saw before live.

558
00:30:24,440 --> 00:30:26,920
 These are built in to Cloud AI

559
00:30:26,920 --> 00:30:29,080
 and are not things that can be toggled on and off.

560
00:30:29,720 --> 00:30:32,520
 So with that in mind, let's start this workflow.

561
00:30:32,520 --> 00:30:36,360
 Before we modify our analyzing marketing campaign skill

562
00:30:36,360 --> 00:30:38,840
 to use BigQuery, let's also make a note

563
00:30:38,840 --> 00:30:40,920
 that we're using Cloud Desktop here

564
00:30:40,920 --> 00:30:45,080
 to connect to a local MCP server to leverage BigQuery.

565
00:30:45,880 --> 00:30:49,240
 So let's take a look at how that BigQuery server is configured.

566
00:30:49,960 --> 00:30:52,360
 I'm going to head over to Settings, Developer,

567
00:30:53,080 --> 00:30:56,360
 and here we can take a look at the underlying command

568
00:30:56,360 --> 00:31:00,520
 and arguments and environment variables for the particular project

569
00:31:00,520 --> 00:31:02,040
 and where my credentials live.

570
00:31:02,600 --> 00:31:05,080
 For this example, we don't have to use BigQuery.

571
00:31:05,080 --> 00:31:07,800
 You can use a database, some external data store,

572
00:31:07,800 --> 00:31:10,200
 but we just want to showcase what it looks like

573
00:31:10,200 --> 00:31:13,000
 with skills and MCP servers working together.

574
00:31:13,720 --> 00:31:17,240
 And if you're interested in seeing that underlying config file,

575
00:31:17,240 --> 00:31:18,120
 here's what it looks like.

576
00:31:18,680 --> 00:31:22,920
 In this config file, we specify the servers we want to connect to

577
00:31:22,920 --> 00:31:26,680
 and the underlying commands to run when Cloud Desktop starts.

578
00:31:27,320 --> 00:31:29,880
 With that in mind, let's go ahead and modify

579
00:31:30,440 --> 00:31:36,280
 our previous skill to now use BigQuery instead of CSVs for data access.

580
00:31:37,080 --> 00:31:38,920
 To make sure this is working correctly,

581
00:31:38,920 --> 00:31:44,280
 let's first ask Cloud to list the tables in BigQuery that exists.

582
00:31:46,760 --> 00:31:49,800
 This is going to make use of the MCP server that we have.

583
00:31:50,360 --> 00:31:54,280
 We're going to allow this and we should get back the list of tables.

584
00:31:54,280 --> 00:31:55,800
 In this case, we only have one.

585
00:31:57,800 --> 00:32:00,440
 So here we can see there's a data set called Marketing

586
00:32:00,440 --> 00:32:01,960
 that contains a single table.

587
00:32:02,680 --> 00:32:07,080
 Now we're going to ask Cloud to show me the schema of the table.

588
00:32:09,400 --> 00:32:12,360
 Hopefully, Cloud can pick up that small spelling mistake

589
00:32:12,360 --> 00:32:13,320
 and we should be in business.

590
00:32:15,160 --> 00:32:17,320
 Here, we're specifying what the table looks like

591
00:32:17,880 --> 00:32:19,160
 and this looks great.

592
00:32:19,160 --> 00:32:21,080
 And we're going to make use of this schema

593
00:32:21,080 --> 00:32:25,240
 when we go ahead and update our analyzing marketing campaign skill.

594
00:32:25,960 --> 00:32:29,080
 What we're going to do now is ask Cloud to update

595
00:32:29,080 --> 00:32:31,640
 our analyzing marketing campaign skill

596
00:32:31,640 --> 00:32:34,760
 so that instead of a CSV upload, we pull from BigQuery.

597
00:32:34,760 --> 00:32:38,360
 We specify the data from the BigQuery table,

598
00:32:38,360 --> 00:32:41,080
 specifically the schema that we just saw above.

599
00:32:41,080 --> 00:32:43,640
 Since we're all in one single conversation,

600
00:32:43,640 --> 00:32:46,840
 Cloud should have no problem taking a look at what the schema is.

601
00:32:46,840 --> 00:32:49,240
 We're specifying some requirements for this.

602
00:32:49,240 --> 00:32:51,320
 And just like in our existing skill,

603
00:32:51,320 --> 00:32:52,760
 we want to make sure that the reference

604
00:32:52,760 --> 00:32:56,280
 to our budget reallocation rules does not get modified.

605
00:32:56,280 --> 00:32:57,800
 Like we spoke about earlier,

606
00:32:57,800 --> 00:33:01,080
 the skill creator skill is extremely helpful and efficient,

607
00:33:01,080 --> 00:33:03,400
 but we still need to give the context necessary.

608
00:33:05,560 --> 00:33:07,640
 Notice here, the first thing it's going to do

609
00:33:07,640 --> 00:33:10,760
 is analyze the necessary skill structure

610
00:33:10,760 --> 00:33:15,160
 and use our skill creator skill to modify the existing skill

611
00:33:15,160 --> 00:33:16,600
 and follow best practices.

612
00:33:18,040 --> 00:33:19,400
 We're going to go ahead now

613
00:33:19,400 --> 00:33:23,080
 and create the updated skill with a new skill MD file.

614
00:33:24,360 --> 00:33:25,960
 Here we can start to see something

615
00:33:25,960 --> 00:33:27,960
 that feels similar to our previous skill,

616
00:33:28,760 --> 00:33:32,120
 but instead adding BigQuery instead of CSV uploads.

617
00:33:33,320 --> 00:33:35,960
 Under the hood, we're using the file system

618
00:33:35,960 --> 00:33:39,240
 and bash tools to create the necessary file

619
00:33:39,240 --> 00:33:40,680
 and folder structure for us.

620
00:33:42,520 --> 00:33:45,320
 What we can see here is instead of using a CSV,

621
00:33:45,320 --> 00:33:46,840
 we're using BigQuery

622
00:33:46,840 --> 00:33:49,080
 and we're following the best practice

623
00:33:49,080 --> 00:33:51,400
 of using MCP servers with skills

624
00:33:51,400 --> 00:33:55,480
 or we specify the server and the name of the tool.

625
00:33:55,480 --> 00:33:58,040
 The skill creator is following best practices

626
00:33:58,040 --> 00:34:00,520
 to take our existing skill and modify it.

627
00:34:01,160 --> 00:34:03,480
 So as we instructed skill creator

628
00:34:03,480 --> 00:34:05,880
 when we specified our required input,

629
00:34:05,880 --> 00:34:08,520
 we're seeing this in practice right now.

630
00:34:08,520 --> 00:34:11,560
 It's best practice not to use an ambiguous date range

631
00:34:11,560 --> 00:34:12,760
 or the entire range.

632
00:34:12,760 --> 00:34:14,840
 So we asked the user to clarify

633
00:34:14,840 --> 00:34:17,160
 and when we show an example of querying,

634
00:34:17,160 --> 00:34:19,320
 we're specifying a date range.

635
00:34:19,320 --> 00:34:21,960
 So some of the tools and requirements that we put in

636
00:34:21,960 --> 00:34:24,920
 are being directly applied when we update this skill.

637
00:34:25,560 --> 00:34:27,880
 So our skill looks like it's in great shape.

638
00:34:27,880 --> 00:34:31,640
 In order to make sure this is saved to subsequent conversations,

639
00:34:31,640 --> 00:34:34,200
 let's go ahead and copy this skill.

640
00:34:38,200 --> 00:34:39,560
 Now we're going to shift gears

641
00:34:39,560 --> 00:34:42,680
 and create a new skill for brand guidelines

642
00:34:42,680 --> 00:34:45,560
 that will use alongside this skill

643
00:34:45,560 --> 00:34:49,240
 to create a compelling data-driven PowerPoint presentation.

644
00:34:49,880 --> 00:34:52,200
 So let's go ahead and start with a new chat

645
00:34:52,200 --> 00:34:54,200
 and we're going to ask Claude

646
00:34:54,200 --> 00:34:57,080
 to create a brand guidelines skill

647
00:34:57,080 --> 00:34:58,920
 from files that we upload.

648
00:34:58,920 --> 00:35:00,440
 The first thing I'm going to do

649
00:35:00,440 --> 00:35:03,560
 is upload a file with my brand guidelines

650
00:35:03,560 --> 00:35:06,440
 as well as some logos to be used in the presentation.

651
00:35:07,640 --> 00:35:09,800
 Before we go ahead and create this skill,

652
00:35:09,800 --> 00:35:12,280
 let me just show you what these brand guidelines look like.

653
00:35:12,840 --> 00:35:15,880
 I've got a color palette, supporting colors, topography.

654
00:35:16,440 --> 00:35:18,200
 Claude knows how to design things,

655
00:35:18,200 --> 00:35:19,880
 but where skills really shine

656
00:35:19,880 --> 00:35:22,040
 are where you can tell Claude exactly

657
00:35:22,040 --> 00:35:24,280
 how you want things done for your company.

658
00:35:24,840 --> 00:35:27,960
 Logos, colors, fonts, great example.

659
00:35:28,520 --> 00:35:32,040
 Now let's go ahead and create a skill from these files

660
00:35:32,040 --> 00:35:35,080
 that we can apply to future presentations and documents.

661
00:35:36,280 --> 00:35:37,960
 What we're going to see here

662
00:35:37,960 --> 00:35:41,160
 is the skill creator skill in action again.

663
00:35:41,160 --> 00:35:43,080
 We're leveraging the existing tooling

664
00:35:43,080 --> 00:35:46,120
 and skills that we have to use best practices

665
00:35:46,120 --> 00:35:48,520
 as well as the guideline and logos

666
00:35:48,520 --> 00:35:51,480
 to make a skill that is repeatable and portable.

667
00:35:52,040 --> 00:35:54,360
 We're going to analyze other existing skills

668
00:35:54,360 --> 00:35:56,120
 to see what patterns they use

669
00:35:56,120 --> 00:35:58,840
 and make sure that this new skill we're creating

670
00:35:58,840 --> 00:35:59,720
 can complement them.

671
00:36:00,360 --> 00:36:01,880
 And this is extremely valuable

672
00:36:01,880 --> 00:36:03,320
 since we're going to be using this

673
00:36:03,320 --> 00:36:04,920
 with PowerPoint presentations.

674
00:36:05,800 --> 00:36:07,960
 Now that we have a good idea of what needs to be done,

675
00:36:08,600 --> 00:36:11,880
 let's run that init skill Python script that we saw before.

676
00:36:12,680 --> 00:36:14,840
 This will create the underlying skill

677
00:36:14,840 --> 00:36:17,400
 and now we can start adding our assets

678
00:36:17,400 --> 00:36:18,920
 to the skills assets folder.

679
00:36:20,920 --> 00:36:23,240
 We're going to start to see colors populate,

680
00:36:23,240 --> 00:36:27,240
 accent colors, fonts, topography, and in a bit,

681
00:36:27,240 --> 00:36:29,320
 we'll have a skill that we can start adding

682
00:36:29,320 --> 00:36:31,720
 to all future conversations

683
00:36:31,720 --> 00:36:33,480
 when there's design that we need done.

684
00:36:34,120 --> 00:36:35,560
 Our logos are being pulled in,

685
00:36:36,280 --> 00:36:38,600
 Word documents and PDFs are specified,

686
00:36:38,600 --> 00:36:41,400
 and presentation layouts are the way that we want them to be.

687
00:36:42,920 --> 00:36:45,240
 The skill creator has finished running

688
00:36:45,240 --> 00:36:48,440
 and here we have a skill MD file that's been created,

689
00:36:49,000 --> 00:36:52,280
 following best practices with a name and a description,

690
00:36:52,280 --> 00:36:54,440
 as well as underlying folders

691
00:36:54,440 --> 00:36:57,400
 with the necessary data and logos that we need.

692
00:36:57,400 --> 00:36:59,320
 There's one more step we need to do

693
00:36:59,320 --> 00:37:02,840
 to make sure that this gets added to future conversations

694
00:37:02,840 --> 00:37:06,600
 in order to make sure this is saved to subsequent conversations,

695
00:37:06,600 --> 00:37:09,080
 let's go ahead and copy this skill.

696
00:37:10,760 --> 00:37:14,120
 Once this is done, we should see this skill

697
00:37:14,120 --> 00:37:16,040
 in the list of skills that we've created.

698
00:37:17,080 --> 00:37:21,960
 Now that we've updated our skill to move from CSVs to BigQuery

699
00:37:21,960 --> 00:37:25,080
 and created a new skill for our brand guidelines,

700
00:37:25,080 --> 00:37:27,240
 let's combine that to build a workflow

701
00:37:27,240 --> 00:37:31,000
 alongside the built-in PowerPoint presentation skill

702
00:37:31,000 --> 00:37:34,520
 to first analyze our data and then generate a presentation.

703
00:37:35,080 --> 00:37:37,720
 So we're going to first analyze our marketing data

704
00:37:37,720 --> 00:37:39,800
 for a different week in BigQuery

705
00:37:39,800 --> 00:37:41,320
 to see how each channel is doing,

706
00:37:41,880 --> 00:37:43,560
 and then based on that data,

707
00:37:43,560 --> 00:37:46,600
 generate a presentation with our brand guidelines.

708
00:37:47,080 --> 00:37:48,040
 Let's see what this looks like.

709
00:37:49,640 --> 00:37:52,680
 First, we're going to go ahead and read the relevant skill files.

710
00:37:52,680 --> 00:37:55,560
 This includes our marketing campaign analysis

711
00:37:55,560 --> 00:37:58,360
 and will include our BigQuery guidelines as well.

712
00:37:58,920 --> 00:38:02,440
 We're going to go ahead and make sure we have the correct PowerPoint presentation skill

713
00:38:02,440 --> 00:38:04,360
 as well as our brand skill for styling.

714
00:38:05,080 --> 00:38:08,120
 Inside of the underlying PowerPoint presentation skill,

715
00:38:08,120 --> 00:38:10,920
 there's additional documentation for presentation creation.

716
00:38:11,720 --> 00:38:14,120
 First, we're going to go ahead and start with BigQuery.

717
00:38:14,120 --> 00:38:15,880
 We're going to query what's necessary.

718
00:38:19,000 --> 00:38:22,120
 We can take a look and see the underlying SQL that's being written

719
00:38:22,680 --> 00:38:25,480
 and like we saw before, that date range that we're looking for.

720
00:38:26,840 --> 00:38:29,640
 Now that we have the data, we're going to use these metrics

721
00:38:29,640 --> 00:38:32,360
 to go ahead and generate a PowerPoint presentation.

722
00:38:32,840 --> 00:38:36,600
 We're going to do so with the styling that we've advised in our brand style

723
00:38:36,600 --> 00:38:38,760
 and turn this into a PowerPoint presentation.

724
00:38:38,760 --> 00:38:42,680
 You can see here the underlying CSS and HTML being written for our slides,

725
00:38:43,240 --> 00:38:45,640
 and then we're going to lean into the built-in skill

726
00:38:45,640 --> 00:38:47,640
 for creating the underlying presentation.

727
00:38:49,640 --> 00:38:51,960
 Now that we've got the right HTML files,

728
00:38:51,960 --> 00:38:54,200
 let's go ahead and create our presentation.

729
00:38:54,840 --> 00:38:57,880
 Here we're using the native PowerPoint skill

730
00:38:58,680 --> 00:39:01,400
 and writing the necessary code to create the presentation.

731
00:39:02,440 --> 00:39:05,480
 We can see here even when there are particular issues,

732
00:39:05,480 --> 00:39:09,000
 the model will go back, edit anything necessary,

733
00:39:09,000 --> 00:39:13,160
 and lean on the exact workflow not only for running code necessary

734
00:39:13,160 --> 00:39:14,920
 but validating what needs to be done.

735
00:39:16,280 --> 00:39:18,680
 This ability that the model has, the backtrack

736
00:39:18,680 --> 00:39:20,600
 and follow particular patterns,

737
00:39:20,600 --> 00:39:23,000
 allows for us to create presentations

738
00:39:23,000 --> 00:39:26,360
 that don't come with built-in issues that we need to immediately then correct.

739
00:39:27,560 --> 00:39:29,640
 So we're seeing that Claude's done is verification,

740
00:39:29,640 --> 00:39:31,000
 the slides look great.

741
00:39:31,000 --> 00:39:34,840
 Now it's going to go ahead and generate that underlying PowerPoint presentation,

742
00:39:35,400 --> 00:39:38,760
 which I can open up in Google Drive and use as Google Slides,

743
00:39:38,760 --> 00:39:40,280
 or I can download directly.

744
00:39:41,160 --> 00:39:43,880
 We can see here I've got some really nice-looking slides

745
00:39:43,880 --> 00:39:46,680
 with the colors, fonts, logos,

746
00:39:46,680 --> 00:39:49,240
 and everything that I want from my particular company.

747
00:39:49,800 --> 00:39:52,200
 We have our efficiency analysis, funnel analysis,

748
00:39:52,760 --> 00:39:55,800
 and the executive summary that highlights what needs review

749
00:39:55,800 --> 00:39:56,840
 and what's doing quite well.

750
00:39:57,560 --> 00:39:59,080
 I can download this presentation,

751
00:39:59,080 --> 00:40:00,920
 I can continue to build off of it,

752
00:40:00,920 --> 00:40:04,520
 and again open it up in Google Drive to share with teammates.

753
00:40:04,520 --> 00:40:07,160
 I can continue prompting and working with this presentation,

754
00:40:07,720 --> 00:40:11,160
 but what we're seeing here is an underlying PowerPoint presentation

755
00:40:11,160 --> 00:40:16,040
 created from a built-in skill combined with two skills that we've made,

756
00:40:16,040 --> 00:40:19,800
 alongside an MCP server pulling in data from BigQuery.

757
00:40:20,280 --> 00:40:23,400
 In the next lesson, we'll explore some of the best practices

758
00:40:23,400 --> 00:40:26,920
 around creating skills and take a look at two other custom skills

759
00:40:26,920 --> 00:40:29,640
 that we create and see if we're following the best practices.

760
00:40:30,440 --> 00:40:34,520
 You can combine skills with tools, MCP, and subagents

761
00:40:34,520 --> 00:40:36,600
 to create powerful, agentic workflows.

762
00:40:37,240 --> 00:40:40,280
 Let's go through each component, see how they work together,

763
00:40:40,280 --> 00:40:42,120
 and learn when to use what.

764
00:40:42,120 --> 00:40:42,760
 I'll see you there.

765
00:40:43,400 --> 00:40:49,160
 In this lesson, we're going to explore how skills fit in to the agent ecosystem,

766
00:40:49,160 --> 00:40:52,120
 with so many different technologies like MCP,

767
00:40:52,680 --> 00:40:55,080
 skills, tools, and subagents.

768
00:40:55,080 --> 00:40:57,880
 Let's make sure we understand how they all work together.

769
00:40:58,440 --> 00:41:00,120
 In your existing applications,

770
00:41:00,120 --> 00:41:03,640
 we can bring in MCP servers for the context that we need,

771
00:41:03,640 --> 00:41:09,000
 leverage subagents for their own main thread and parallelization,

772
00:41:09,000 --> 00:41:11,640
 and bring in skills for those repeatable workflows.

773
00:41:12,200 --> 00:41:13,640
 Let's see this in a little more depth.

774
00:41:14,200 --> 00:41:17,400
 When we compare skills with the model context protocol,

775
00:41:17,400 --> 00:41:21,400
 we want to think a lot about working with external data systems

776
00:41:21,400 --> 00:41:24,360
 and bringing in the tools and resources that we need.

777
00:41:24,920 --> 00:41:29,320
 The model context protocol connects our agent or AI applications

778
00:41:29,320 --> 00:41:31,320
 with external systems and data.

779
00:41:31,320 --> 00:41:34,360
 That could be an external database, data from Google Drive,

780
00:41:35,000 --> 00:41:37,960
 using a various array of systems,

781
00:41:37,960 --> 00:41:40,600
 but any time that you need external data

782
00:41:40,600 --> 00:41:42,760
 and context that the model doesn't know about,

783
00:41:42,760 --> 00:41:45,640
 the model context protocol is extremely helpful.

784
00:41:45,640 --> 00:41:50,440
 The skills that you have can leverage those underlying tools

785
00:41:50,440 --> 00:41:53,160
 and data from the model context protocol

786
00:41:53,160 --> 00:41:56,200
 to teach your agent what to do with that data.

787
00:41:56,200 --> 00:41:58,200
 Think of the model context protocol

788
00:41:58,200 --> 00:42:01,720
 as bringing in all of the underlying tooling that we need

789
00:42:01,720 --> 00:42:06,040
 and the skill as the set of instructions to put those tools together

790
00:42:06,040 --> 00:42:09,240
 to build particular workflows that are repeatable

791
00:42:09,240 --> 00:42:11,720
 and produce the kind of data that you want.

792
00:42:11,720 --> 00:42:14,440
 As we think about leveraging external data

793
00:42:14,440 --> 00:42:17,960
 to compute metrics and research and calculate data,

794
00:42:17,960 --> 00:42:21,320
 all of those underlying tools can be provided externally

795
00:42:21,320 --> 00:42:22,760
 through the model context protocol.

796
00:42:23,320 --> 00:42:26,280
 When we think a little bit about skills versus tools,

797
00:42:26,280 --> 00:42:30,760
 I like to draw the analogy of tools as a little bit more lower level.

798
00:42:30,760 --> 00:42:33,000
 You can imagine that you have tools,

799
00:42:33,000 --> 00:42:35,960
 like a hammer and a saw and some nails,

800
00:42:35,960 --> 00:42:38,920
 and you have a skill like how to build a bookshelf.

801
00:42:38,920 --> 00:42:42,120
 The tools themselves are underlying ways

802
00:42:42,120 --> 00:42:45,880
 of accessing systems and providing agents

803
00:42:45,880 --> 00:42:49,000
 with the capabilities they need to accomplish a task.

804
00:42:49,000 --> 00:42:53,160
 In fact, tools are used under the hood to power the ability

805
00:42:53,160 --> 00:42:55,640
 to generate skills, to read skills,

806
00:42:55,640 --> 00:42:59,640
 and even to produce a file system for executing code

807
00:42:59,640 --> 00:43:01,480
 and loading these skills.

808
00:43:01,480 --> 00:43:04,920
 Skills extend the capabilities with specialized knowledge,

809
00:43:04,920 --> 00:43:08,680
 bringing in additional files and scripts that need to be executed,

810
00:43:08,680 --> 00:43:11,960
 but the ability to execute those underlying scripts

811
00:43:11,960 --> 00:43:16,120
 and load those files and folders is provided by tools.

812
00:43:16,120 --> 00:43:19,720
 There are tools that are built in to certain agent ecosystems,

813
00:43:19,720 --> 00:43:21,960
 there are tools that we can write on our own,

814
00:43:21,960 --> 00:43:25,640
 and tools that we can load through the model context protocol.

815
00:43:25,640 --> 00:43:28,920
 Tool definitions always live in the context window

816
00:43:28,920 --> 00:43:32,520
 whereas skills are progressively loaded when necessary.

817
00:43:32,520 --> 00:43:35,160
 When we think about how these work together,

818
00:43:35,160 --> 00:43:38,760
 skills allow us to create predictable workflows,

819
00:43:38,760 --> 00:43:42,520
 and those skills can bring in scripts that can be executed

820
00:43:42,520 --> 00:43:44,520
 kind of like a tool on demand.

821
00:43:44,520 --> 00:43:48,840
 If there is a tool that we do not need in every single conversation,

822
00:43:48,840 --> 00:43:53,800
 we can use that only when needed through skills and progressive disclosure.

823
00:43:53,800 --> 00:43:56,520
 When we think about how subagents fit into the mix,

824
00:43:56,520 --> 00:43:59,560
 let's first define what we think of as a subagent.

825
00:43:59,560 --> 00:44:03,640
 We have a main agent that can spawn or create subagents

826
00:44:03,640 --> 00:44:06,120
 that can report back to the parent agent.

827
00:44:06,120 --> 00:44:11,640
 These subagents can be created through ecosystems like Cloud Code or the agent SDK,

828
00:44:11,640 --> 00:44:13,640
 or we can also make our own.

829
00:44:13,640 --> 00:44:16,520
 When we think of the value that subagents provide,

830
00:44:16,520 --> 00:44:21,240
 we think a lot about having an isolated context with fine-grained permissions

831
00:44:21,240 --> 00:44:24,520
 as well as executing tasks in parallel.

832
00:44:24,520 --> 00:44:27,320
 When we think about what these subagents can access,

833
00:44:27,320 --> 00:44:31,160
 we have limited tool permissions and we also can specify

834
00:44:31,160 --> 00:44:34,040
 what skills each subagent can access.

835
00:44:34,040 --> 00:44:36,920
 So while the main agent can serve as an orchestrator

836
00:44:36,920 --> 00:44:39,400
 and can leverage whatever skills necessary,

837
00:44:39,400 --> 00:44:44,760
 subagents can do the same type of idea with making use of particular skills.

838
00:44:44,760 --> 00:44:47,000
 Subagents work quite nicely with skills,

839
00:44:47,000 --> 00:44:50,200
 where we can have a particular subagent like a code reviewer,

840
00:44:50,200 --> 00:44:53,400
 whose sole task is to analyze and review a code base,

841
00:44:53,400 --> 00:44:59,000
 and leverage skills which specify exactly how you, your team, or your company

842
00:44:59,000 --> 00:45:01,240
 might perform a code review.

843
00:45:01,240 --> 00:45:02,680
 When we put this all together,

844
00:45:02,680 --> 00:45:06,280
 we can provide an analogy of a customer insight analyzer.

845
00:45:06,280 --> 00:45:08,200
 Let's think about how this all works together.

846
00:45:08,200 --> 00:45:11,240
 We have a main agent that is given a set of tools.

847
00:45:11,240 --> 00:45:14,760
 Those tools could be provided from MCP servers.

848
00:45:14,760 --> 00:45:18,280
 We can bring in the data, the resources, the tools necessary

849
00:45:18,280 --> 00:45:20,360
 to perform the tasks needed.

850
00:45:20,360 --> 00:45:23,560
 For dispatching subagents to analyze customers,

851
00:45:23,560 --> 00:45:27,320
 we might analyze interviews from customers or surveys from customers

852
00:45:27,320 --> 00:45:32,520
 and do those in isolation and parallelize them to get data back even faster.

853
00:45:32,520 --> 00:45:36,920
 When we think about how to actually analyze insights from customers,

854
00:45:36,920 --> 00:45:39,880
 how to categorize feedback, summarize findings,

855
00:45:39,880 --> 00:45:42,280
 how to analyze interviews and surveys,

856
00:45:42,280 --> 00:45:45,000
 and how to make sure we do those in a predictable fashion

857
00:45:45,000 --> 00:45:48,040
 with the right tools loaded at the right time,

858
00:45:48,040 --> 00:45:50,200
 that's where skills come into play.

859
00:45:50,200 --> 00:45:55,000
 We bring in data externally, we leverage subagents if we need to parallelize

860
00:45:55,000 --> 00:45:57,880
 an execute in a separate thread and context window,

861
00:45:57,880 --> 00:46:01,480
 and we bring in skills to consume all of this information

862
00:46:01,480 --> 00:46:04,920
 in a predictable, repeatable, and portable fashion.

863
00:46:04,920 --> 00:46:08,920
 To summarize this, there are many different pieces in the AI ecosystem

864
00:46:08,920 --> 00:46:11,480
 when we think about building AI applications.

865
00:46:11,480 --> 00:46:17,000
 Fundamentally, we have prompts the underlying most atomic unit in a conversation.

866
00:46:17,000 --> 00:46:20,600
 Prompts are the underlying tool for us to communicate with models,

867
00:46:20,600 --> 00:46:25,560
 but prompts themselves don't scale very well across teams and companies.

868
00:46:25,560 --> 00:46:30,840
 To bundle these underlying prompts and conversations and code and assets,

869
00:46:30,840 --> 00:46:32,440
 we can leverage skills.

870
00:46:32,440 --> 00:46:36,520
 Subagents that we have tasks delegated to can make use of skills,

871
00:46:36,520 --> 00:46:41,160
 those subagents can then consume tools necessary from a main agent

872
00:46:41,160 --> 00:46:44,040
 that are defined through the model context protocol.

873
00:46:44,040 --> 00:46:47,320
 As we think about what these particular features aim to solve,

874
00:46:47,320 --> 00:46:51,400
 we want to be really intentional about how we're loading this information

875
00:46:51,400 --> 00:46:53,400
 and what this is best used for.

876
00:46:53,400 --> 00:46:56,280
 When we think about the context window as a public good,

877
00:46:56,280 --> 00:46:59,800
 we want to be intentional about when subagents can help us minimize

878
00:46:59,800 --> 00:47:01,880
 what goes in the main context window

879
00:47:01,880 --> 00:47:07,080
 and how MCP can load the data necessary and skills can load it progressively.

880
00:47:07,080 --> 00:47:09,720
 When we talk a little bit about the persistence

881
00:47:09,720 --> 00:47:13,240
 and how we can think about drawing things into a longer-term memory,

882
00:47:13,240 --> 00:47:17,000
 with subagents, we can persist across many different sessions

883
00:47:17,000 --> 00:47:19,160
 from the subagent and the parent agent.

884
00:47:19,160 --> 00:47:23,080
 With skills, we can persist across conversations that we have

885
00:47:23,080 --> 00:47:25,640
 with the user and the AI application.

886
00:47:25,640 --> 00:47:29,240
 So as we think about where each of these steps are used,

887
00:47:29,240 --> 00:47:33,080
 we want to use skills for procedural, predictable workflows

888
00:47:33,080 --> 00:47:38,440
 and subagents for full agent logic only when necessary for specialized tasks.

889
00:47:39,000 --> 00:47:42,600
 In the next lesson, we'll take a look at some of the pre-built skills

890
00:47:42,600 --> 00:47:44,520
 that come with Cloud.

891
00:47:44,520 --> 00:47:47,240
 We'll take a look at the repository for these skills,

892
00:47:47,240 --> 00:47:50,280
 dive deep into some of the skill MD files,

893
00:47:50,280 --> 00:47:53,960
 and talk about a very useful skill called the skill creator

894
00:47:53,960 --> 00:47:57,480
 so that we don't have to manually create all of our skills from scratch.

895
00:47:58,280 --> 00:48:01,320
 In the first lesson, you saw how skills work with Cloud AI.

896
00:48:02,040 --> 00:48:05,800
 Now, we'll work with the Cloud API to test the two skills we made

897
00:48:05,800 --> 00:48:06,840
 from the previous lesson.

898
00:48:07,640 --> 00:48:09,800
 To use skills with the Cloud API,

899
00:48:09,800 --> 00:48:13,560
 we'll need to use the code execution tool and the files API.

900
00:48:14,200 --> 00:48:16,920
 This will equip Cloud with file system access

901
00:48:16,920 --> 00:48:20,600
 for reading and writing files and with bash for executing code.

902
00:48:20,600 --> 00:48:21,320
 Let's get to it.

903
00:48:22,200 --> 00:48:25,880
 We've talked quite a bit about how skills work and how to create them,

904
00:48:25,880 --> 00:48:29,720
 and we talked a little bit as well about the portability of skills

905
00:48:29,720 --> 00:48:32,920
 across different environments in the Cloud ecosystem,

906
00:48:32,920 --> 00:48:35,400
 as well as many other agentic applications.

907
00:48:35,960 --> 00:48:39,400
 We started by looking at skills in Cloud AI and Cloud Desktop,

908
00:48:39,400 --> 00:48:41,960
 and now we're going to move to talk about how to use skills

909
00:48:41,960 --> 00:48:44,360
 using the Cloud Messages API.

910
00:48:44,360 --> 00:48:46,360
 There are two things that are important to note.

911
00:48:46,360 --> 00:48:50,680
 First, skills that you create in Cloud AI and Cloud Desktop

912
00:48:50,680 --> 00:48:53,880
 are not shared in the Cloud API or Cloud code.

913
00:48:54,520 --> 00:48:58,600
 The second important piece is that in order for skills to work,

914
00:48:58,600 --> 00:49:01,800
 we need the ability for Cloud to execute code,

915
00:49:01,800 --> 00:49:06,200
 create and edit documents, presentations, PDFs, and data reports,

916
00:49:06,200 --> 00:49:08,280
 and work with a file system.

917
00:49:08,280 --> 00:49:10,600
 This is something that we're going to have to manually do

918
00:49:10,600 --> 00:49:12,200
 when we work with the Cloud API,

919
00:49:12,200 --> 00:49:14,840
 and this is something that is actually configured for you

920
00:49:14,840 --> 00:49:17,560
 right away when using Cloud AI and Cloud Desktop.

921
00:49:18,120 --> 00:49:21,640
 In Cloud Desktop or Cloud AI, if I go to Settings

922
00:49:22,600 --> 00:49:24,200
 and I take a look at the capabilities,

923
00:49:24,840 --> 00:49:27,960
 you can see here that there's a section for code execution

924
00:49:27,960 --> 00:49:29,320
 and file creation.

925
00:49:29,320 --> 00:49:31,320
 This is what we're going to talk about in more depth

926
00:49:31,320 --> 00:49:33,320
 when we work with the API directly,

927
00:49:33,320 --> 00:49:35,960
 but this is a setting that is enabled by default

928
00:49:35,960 --> 00:49:38,520
 that allows Cloud to execute code,

929
00:49:38,520 --> 00:49:41,400
 create docs, spreadsheets, presentations, and more.

930
00:49:41,400 --> 00:49:44,440
 This essentially gives a Cloud AI and Cloud Desktop

931
00:49:44,440 --> 00:49:48,120
 a computer or a virtual machine to execute code

932
00:49:48,120 --> 00:49:51,320
 and perform all those tasks that make skills happen.

933
00:49:51,320 --> 00:49:53,000
 If this is disabled,

934
00:49:53,000 --> 00:49:55,480
 we will actually see that we need to turn this on

935
00:49:55,480 --> 00:49:57,320
 to even be able to use skills.

936
00:49:58,040 --> 00:49:59,880
 Now let's shift back and talk a little bit

937
00:49:59,880 --> 00:50:03,560
 about how this code execution tool and file creation

938
00:50:03,560 --> 00:50:06,520
 works because we're going to need to enable this manually

939
00:50:06,520 --> 00:50:07,880
 when we work with the API.

940
00:50:08,680 --> 00:50:12,120
 When working with tools like Cloud Code and the Cloud Agent,

941
00:50:12,120 --> 00:50:14,600
 you have direct access to a file system,

942
00:50:14,600 --> 00:50:16,440
 whereas using the Cloud API,

943
00:50:16,440 --> 00:50:19,400
 we do not and need a container to execute code

944
00:50:19,400 --> 00:50:21,400
 in a file system to work with.

945
00:50:21,400 --> 00:50:23,480
 With Cloud AI and Cloud Desktop,

946
00:50:23,480 --> 00:50:26,120
 that containerized environment and file system

947
00:50:26,120 --> 00:50:29,000
 is given to you and not something you have to implement.

948
00:50:29,000 --> 00:50:32,040
 At the end of the day, the functionality is all the same,

949
00:50:32,040 --> 00:50:35,800
 but the way in which we utilize skills is slightly different.

950
00:50:35,800 --> 00:50:38,040
 The skills themselves do not change,

951
00:50:38,040 --> 00:50:40,120
 the format of those skills do not change,

952
00:50:40,120 --> 00:50:42,360
 but depending on the environment that you're in,

953
00:50:42,360 --> 00:50:45,400
 you may utilize the way in which skills work slightly differently.

954
00:50:45,960 --> 00:50:48,200
 As we start to explore the messages API,

955
00:50:48,200 --> 00:50:50,200
 we're going to use the code execution tool.

956
00:50:50,680 --> 00:50:55,880
 The code execution tool allows Cloud to run bash or shell commands

957
00:50:55,880 --> 00:50:59,560
 to perform all these actions that we saw when working with skills,

958
00:50:59,560 --> 00:51:02,920
 creating, viewing, editing files, and writing code

959
00:51:02,920 --> 00:51:05,080
 all in a sandbox environment.

960
00:51:05,080 --> 00:51:09,160
 The code execution tool gives our application the ability

961
00:51:09,160 --> 00:51:11,400
 to have a separate dedicated container,

962
00:51:11,400 --> 00:51:14,440
 to execute code, and work with a file system.

963
00:51:15,000 --> 00:51:17,480
 As you've seen with all the things that skills can do,

964
00:51:17,480 --> 00:51:20,200
 that is mission critical for reading our skills,

965
00:51:20,200 --> 00:51:22,120
 executing code within those skills,

966
00:51:22,120 --> 00:51:27,000
 and working with other files that we might want to edit and view and create.

967
00:51:27,000 --> 00:51:29,720
 To give you a visualization of what this looks like,

968
00:51:29,720 --> 00:51:32,120
 when we include the code execution tool,

969
00:51:32,680 --> 00:51:35,800
 we give Cloud an execution sandbox or a container.

970
00:51:36,520 --> 00:51:39,480
 When we ask Cloud to create and execute files,

971
00:51:39,480 --> 00:51:43,080
 these are executed in a safe and isolated environment.

972
00:51:43,080 --> 00:51:46,840
 There are limitations for the RAM, the disk, the CPU,

973
00:51:46,840 --> 00:51:50,200
 and more importantly, there is no internet connection provided,

974
00:51:50,200 --> 00:51:53,720
 and there are pre-installed libraries that you get out of the box.

975
00:51:53,720 --> 00:51:57,080
 So this does not work with every single kind of coding environment.

976
00:51:57,080 --> 00:51:59,800
 There are some limitations here to be mindful of.

977
00:51:59,800 --> 00:52:02,760
 At the same time, we also get access to a file system

978
00:52:02,760 --> 00:52:05,000
 that we can start adding directories to.

979
00:52:05,000 --> 00:52:06,680
 You might have even seen hints of that

980
00:52:06,680 --> 00:52:09,000
 when we worked with Cloud Desktop and Cloud AI.

981
00:52:09,560 --> 00:52:12,040
 This limitation of no internet connection

982
00:52:12,040 --> 00:52:14,920
 is something that is specific to the messages API.

983
00:52:14,920 --> 00:52:18,760
 When we're using the code execution tool in Cloud AI or Cloud Desktop,

984
00:52:18,760 --> 00:52:21,240
 we do have access to an internet connection,

985
00:52:21,240 --> 00:52:23,640
 and we can download and install packages.

986
00:52:23,640 --> 00:52:26,280
 The code execution tool works quite nicely

987
00:52:26,280 --> 00:52:30,120
 with another set of APIs that Cloud API allows us to work with.

988
00:52:30,680 --> 00:52:33,320
 As you can imagine, when we're working with files,

989
00:52:33,880 --> 00:52:37,240
 adding, creating, writing, modifying files,

990
00:52:37,240 --> 00:52:41,080
 we need some mechanism for actually storing those underlying files.

991
00:52:41,080 --> 00:52:45,560
 The Cloud API includes a set of APIs called the files API

992
00:52:45,560 --> 00:52:49,800
 to upload and download files that can be run and worked on

993
00:52:49,800 --> 00:52:51,560
 inside of the container.

994
00:52:51,560 --> 00:52:54,120
 You can imagine a scenario where the user asks

995
00:52:54,120 --> 00:52:58,040
 to summarize some input and save the summary to a text file.

996
00:52:58,040 --> 00:53:01,480
 We upload that input file, send it to the container,

997
00:53:01,480 --> 00:53:04,760
 download generated files with this files API.

998
00:53:04,760 --> 00:53:06,920
 We're going to be seeing this shortly in code

999
00:53:06,920 --> 00:53:10,600
 when we see the IDs that we get back from uploading and downloading files

1000
00:53:10,600 --> 00:53:14,600
 and how this works nicely with skills and our code execution tool.

1001
00:53:15,240 --> 00:53:17,480
 And this is exactly where skills come into play.

1002
00:53:18,120 --> 00:53:23,000
 The library of skills that we get out of the box in tools like Cloud AI,

1003
00:53:23,000 --> 00:53:26,120
 or that we can include if we want using the API,

1004
00:53:26,120 --> 00:53:29,640
 those live in a directory that are powered in the container,

1005
00:53:29,640 --> 00:53:32,520
 as we start to read from the skills directory.

1006
00:53:32,520 --> 00:53:35,160
 As we start to add information to our skills

1007
00:53:35,160 --> 00:53:38,760
 or use those underlying skills to create new files

1008
00:53:38,760 --> 00:53:42,440
 that we can download or upload, this is where skills come into play.

1009
00:53:42,440 --> 00:53:45,720
 And we're going to see a requirement when working with the API,

1010
00:53:45,720 --> 00:53:50,680
 when we want to use skills, we need to use the code execution tool as well.

1011
00:53:50,680 --> 00:53:54,200
 Now that we have a good sense of what the code execution tool and files

1012
00:53:54,200 --> 00:53:57,400
 API allow us to do, let's see how to use this in action.

1013
00:53:57,400 --> 00:54:00,520
 We're going to go and revisit the two previous custom skills

1014
00:54:00,520 --> 00:54:02,920
 that we built for generating practice questions,

1015
00:54:02,920 --> 00:54:04,840
 as well as time series analysis.

1016
00:54:04,840 --> 00:54:07,960
 So let's head over to a Jupyter notebook and explore this.

1017
00:54:07,960 --> 00:54:11,800
 Right here, I have my two custom skills that we've worked with before.

1018
00:54:11,800 --> 00:54:17,320
 I also have a folder for data that I'm going to be using to analyze time series data.

1019
00:54:17,320 --> 00:54:20,440
 I also have a folder for lecture notes that I'll be using

1020
00:54:20,440 --> 00:54:23,480
 when I use my generating practice questions skill.

1021
00:54:23,480 --> 00:54:24,920
 To get started in this notebook,

1022
00:54:24,920 --> 00:54:27,320
 I'm going to load the environment variables that I need,

1023
00:54:27,320 --> 00:54:31,480
 as well as a helper to help me find particular files from a directory.

1024
00:54:31,480 --> 00:54:34,280
 We're going to see this in action when we start using our skills.

1025
00:54:34,280 --> 00:54:38,360
 To start, I'm going to begin using my generating practice questions skill.

1026
00:54:38,360 --> 00:54:42,440
 So let's go ahead and take a look at the first part that I need to do.

1027
00:54:42,440 --> 00:54:45,160
 To begin, I need to upload the skill directory.

1028
00:54:45,160 --> 00:54:48,840
 Here you can see we're using that files from der helper function,

1029
00:54:48,840 --> 00:54:51,880
 as well as the necessary beta headers for skills.

1030
00:54:51,880 --> 00:54:56,920
 Once this is done, I should be able to see the skill ID that I've created.

1031
00:54:56,920 --> 00:55:00,600
 This beta's list are particular headers that I add

1032
00:55:00,600 --> 00:55:03,800
 when I make a request to the messages API.

1033
00:55:03,800 --> 00:55:06,600
 Under the hood, these are turning into request headers

1034
00:55:06,600 --> 00:55:08,680
 to make sure that I'm getting the right data back

1035
00:55:08,680 --> 00:55:11,720
 and communicating appropriately with the API.

1036
00:55:11,720 --> 00:55:13,640
 To take a look at all the skills that I have,

1037
00:55:13,640 --> 00:55:15,720
 I can use this dot list method,

1038
00:55:15,720 --> 00:55:17,960
 and I'm going to pass in a source of custom

1039
00:55:17,960 --> 00:55:20,440
 so that we don't load all the built-in skills,

1040
00:55:20,440 --> 00:55:24,680
 and instead just confirm that I've created the ones as expected.

1041
00:55:24,680 --> 00:55:26,280
 And here I can see the title,

1042
00:55:26,280 --> 00:55:29,560
 as well as the unique skill ID that I'm going to be using shortly.

1043
00:55:30,200 --> 00:55:32,280
 In order for this to work as expected,

1044
00:55:32,280 --> 00:55:34,920
 we're going to need to make use of the LaTeX file

1045
00:55:34,920 --> 00:55:37,080
 where we're going to generate practice questions from.

1046
00:55:37,960 --> 00:55:43,080
 Here I'll use the files API to upload this particular LaTeX file,

1047
00:55:43,080 --> 00:55:47,080
 make sure that it's set for reading, and then get back a file object.

1048
00:55:47,960 --> 00:55:53,240
 I'll be using this file object in conjunction with the skills necessary

1049
00:55:53,240 --> 00:55:55,720
 to make sure that it's all working as expected.

1050
00:55:56,280 --> 00:55:57,720
 I'm using sonnet here,

1051
00:55:57,720 --> 00:56:01,880
 and I'm passing in the necessary beta headers not only for skills,

1052
00:56:01,880 --> 00:56:05,720
 but in order for skills to work as expected when talking to the model,

1053
00:56:05,720 --> 00:56:08,600
 I need to make sure I have the code execution beta as well.

1054
00:56:09,160 --> 00:56:11,000
 And since I'm sending a file here,

1055
00:56:11,000 --> 00:56:13,640
 we have to make sure we have the files API header as well.

1056
00:56:14,280 --> 00:56:15,720
 When working with skills,

1057
00:56:15,720 --> 00:56:18,840
 these skills are set in a keyword argument called container,

1058
00:56:18,840 --> 00:56:21,880
 and here is where I pass in the list of skills.

1059
00:56:21,880 --> 00:56:24,040
 These could be custom ones or built-in ones.

1060
00:56:24,600 --> 00:56:27,640
 As I create many different versions of the skills,

1061
00:56:27,640 --> 00:56:29,960
 I can reference a particular timestamp

1062
00:56:29,960 --> 00:56:31,880
 or just use the latest one that I have.

1063
00:56:32,440 --> 00:56:34,440
 As I start to communicate with the model,

1064
00:56:34,440 --> 00:56:36,760
 I ask it to generate practice questions

1065
00:56:36,760 --> 00:56:39,800
 and then specify the file that I'm working with.

1066
00:56:39,800 --> 00:56:42,440
 This file object was previously created

1067
00:56:42,440 --> 00:56:44,520
 when I uploaded the LaTeX file.

1068
00:56:44,520 --> 00:56:47,880
 We finally make sure we're bringing in the correct tools for code execution

1069
00:56:48,440 --> 00:56:50,200
 and send a message to our API.

1070
00:56:50,760 --> 00:56:53,800
 Now let's go take a look at the response that we got back.

1071
00:56:53,800 --> 00:56:57,560
 We can see here that there are multiple different pieces being used.

1072
00:56:57,560 --> 00:57:00,040
 Tools on the server, code execution,

1073
00:57:00,040 --> 00:57:01,720
 additional tools being used,

1074
00:57:01,720 --> 00:57:04,280
 and then finally, a bash code execution result.

1075
00:57:04,920 --> 00:57:06,680
 To make this a little bit cleaner to look at,

1076
00:57:06,680 --> 00:57:08,440
 let's add some nice formatting

1077
00:57:08,440 --> 00:57:10,440
 so that we can go ahead and take a look

1078
00:57:10,440 --> 00:57:13,720
 and analyze different text responses and tool use.

1079
00:57:13,720 --> 00:57:16,680
 We're going to go ahead and see in this particular series

1080
00:57:16,680 --> 00:57:18,760
 what's happening one step at a time.

1081
00:57:18,760 --> 00:57:21,080
 When we take a look at what the response is,

1082
00:57:21,080 --> 00:57:24,120
 which includes our text and our tool use and tool results,

1083
00:57:24,120 --> 00:57:25,960
 the first thing the model is telling us

1084
00:57:25,960 --> 00:57:28,520
 is it can help generate questions from these notes

1085
00:57:28,520 --> 00:57:31,000
 and it's going to start by reading the skill file

1086
00:57:31,000 --> 00:57:32,440
 and examining the lecture notes.

1087
00:57:33,160 --> 00:57:36,680
 Notice here it's detected the skill that it needs to use,

1088
00:57:36,680 --> 00:57:39,080
 but it's only reading the skill MD.

1089
00:57:39,080 --> 00:57:40,280
 We're going to see later on

1090
00:57:40,280 --> 00:57:42,920
 if there are additional files that need to be read,

1091
00:57:42,920 --> 00:57:45,240
 we'll make use of that progressive disclosure.

1092
00:57:45,240 --> 00:57:49,960
 We're also going to review in our input that LaTeX file as well.

1093
00:57:49,960 --> 00:57:52,200
 We're going to go ahead and see the underlying data

1094
00:57:52,200 --> 00:57:53,640
 that comes from these files.

1095
00:57:53,640 --> 00:57:56,360
 This is the yaml front matter that we've seen before,

1096
00:57:56,360 --> 00:58:00,200
 as well as the LaTeX from our notes4.tech file.

1097
00:58:00,200 --> 00:58:01,320
 Next, we're going to go ahead

1098
00:58:01,320 --> 00:58:04,440
 and check the markdown template to use the proper structure

1099
00:58:04,440 --> 00:58:06,360
 because we want our output to be in markdown.

1100
00:58:07,080 --> 00:58:09,240
 Here is where we're going to leverage a bit more

1101
00:58:09,240 --> 00:58:10,520
 of that progressive disclosure.

1102
00:58:11,080 --> 00:58:12,680
 Here's where we're going to read

1103
00:58:12,680 --> 00:58:16,360
 inside of the assets folder that markdown template MD.

1104
00:58:16,360 --> 00:58:18,360
 We'll get back the response that we've read

1105
00:58:18,360 --> 00:58:20,200
 and now we'll generate the questions

1106
00:58:20,200 --> 00:58:22,120
 based on the lecture notes that we've passed.

1107
00:58:22,680 --> 00:58:25,640
 Here we're going to use our code execution tool

1108
00:58:25,640 --> 00:58:27,880
 to create a particular file.

1109
00:58:27,880 --> 00:58:30,200
 We'll give that file text in markdown

1110
00:58:30,200 --> 00:58:32,200
 and we'll get back the result of that file.

1111
00:58:32,760 --> 00:58:34,520
 We're going to go ahead and copy that

1112
00:58:34,520 --> 00:58:36,200
 to an output directory

1113
00:58:36,200 --> 00:58:39,640
 and use our files API to get back a file ID

1114
00:58:39,640 --> 00:58:41,240
 that we can download later on.

1115
00:58:42,200 --> 00:58:43,960
 Once we get back that result,

1116
00:58:43,960 --> 00:58:45,960
 we can take a look at the underlying file

1117
00:58:45,960 --> 00:58:47,320
 that's been generated

1118
00:58:47,320 --> 00:58:50,680
 and make use of that file ID to programmatically download.

1119
00:58:51,240 --> 00:58:53,880
 We can see here it's been saved and is ready for use.

1120
00:58:54,840 --> 00:58:56,920
 Using that file ID that we saw above,

1121
00:58:57,560 --> 00:58:59,560
 let's go ahead and download the file.

1122
00:59:00,360 --> 00:59:02,200
 We'll go ahead and check in this response

1123
00:59:02,200 --> 00:59:04,840
 and make sure that we have the file ID correctly extracted

1124
00:59:05,400 --> 00:59:07,560
 and if we have that which we expect to do,

1125
00:59:07,560 --> 00:59:10,280
 we should be able to download that particular file.

1126
00:59:10,280 --> 00:59:12,200
 We'll go ahead and write to a file

1127
00:59:12,200 --> 00:59:14,840
 called notes4md with that content.

1128
00:59:15,400 --> 00:59:17,560
 That content includes the file ID

1129
00:59:17,560 --> 00:59:19,400
 as well as the necessary beta headers

1130
00:59:19,400 --> 00:59:20,760
 to communicate with the API.

1131
00:59:21,640 --> 00:59:25,320
 We can see here we've downloaded that notes4md file

1132
00:59:25,320 --> 00:59:27,800
 and this is coming from the files API

1133
00:59:27,800 --> 00:59:29,160
 with a code execution tool

1134
00:59:29,720 --> 00:59:32,120
 all generated with the model and a skill.

1135
00:59:33,000 --> 00:59:35,000
 Inside of this file that we've downloaded,

1136
00:59:35,000 --> 00:59:36,760
 we can see that we're following

1137
00:59:36,760 --> 00:59:38,760
 those exact parts that we had in the skill,

1138
00:59:39,320 --> 00:59:41,320
 starting with true and false questions,

1139
00:59:41,320 --> 00:59:43,080
 moving on to explanatory questions,

1140
00:59:43,080 --> 00:59:44,520
 to coding questions,

1141
00:59:44,520 --> 00:59:46,920
 and finally to use case applications.

1142
00:59:47,480 --> 00:59:50,040
 We can preview this in Markdown to see what that would look like

1143
00:59:50,600 --> 00:59:52,680
 and here we can see our use case application,

1144
00:59:52,680 --> 00:59:54,040
 all the things necessary.

1145
00:59:54,600 --> 00:59:57,720
 Now's a good time to evaluate this particular output.

1146
00:59:57,720 --> 00:59:59,560
 Did we do exactly what the skill wanted?

1147
00:59:59,560 --> 01:00:00,840
 It looks good to start,

1148
01:00:00,840 --> 01:00:02,200
 but bringing in some unit tests

1149
01:00:02,200 --> 01:00:04,280
 can really take this to the next level.

1150
01:00:04,280 --> 01:00:06,920
 If we need, we can go back and modify the skill

1151
01:00:06,920 --> 01:00:09,560
 just like we saw before using the API,

1152
01:00:09,560 --> 01:00:11,000
 the code execution tool,

1153
01:00:11,000 --> 01:00:12,520
 and the files API as well.

1154
01:00:13,160 --> 01:00:16,120
 We also have the ability to delete skills programmatically.

1155
01:00:16,120 --> 01:00:17,640
 In order to delete a skill,

1156
01:00:17,640 --> 01:00:19,720
 we first have to find all of the versions

1157
01:00:19,720 --> 01:00:21,400
 associated with that skill

1158
01:00:21,400 --> 01:00:22,600
 and then delete them.

1159
01:00:22,600 --> 01:00:24,680
 Once those versions are deleted,

1160
01:00:24,680 --> 01:00:27,880
 we should be able to delete the underlying skill right here.

1161
01:00:28,920 --> 01:00:30,520
 Next, we're going to go ahead and use

1162
01:00:30,520 --> 01:00:34,680
 our analyzing time series skill alongside another skill.

1163
01:00:34,680 --> 01:00:36,120
 This is going to look pretty familiar

1164
01:00:36,120 --> 01:00:37,240
 to what we saw above,

1165
01:00:37,240 --> 01:00:38,440
 so let's go through these steps.

1166
01:00:39,000 --> 01:00:41,400
 First, we're going to upload our custom skill,

1167
01:00:41,400 --> 01:00:42,520
 get back a skill ID,

1168
01:00:43,240 --> 01:00:45,400
 and confirm that we've done that as expected.

1169
01:00:45,960 --> 01:00:48,200
 Here, we can also see that we're not loading

1170
01:00:48,200 --> 01:00:49,640
 only the custom skills,

1171
01:00:49,640 --> 01:00:51,960
 we can see the built-in skills as well.

1172
01:00:51,960 --> 01:00:53,480
 We should look pretty familiar

1173
01:00:53,480 --> 01:00:55,160
 as we saw them as well in Cloud AI.

1174
01:00:56,600 --> 01:00:59,080
 Next, we're going to go ahead and upload our input file.

1175
01:00:59,080 --> 01:01:01,640
 This is going to be our retail sales CSV file.

1176
01:01:02,440 --> 01:01:05,160
 We're going to build a message to send to the API,

1177
01:01:05,160 --> 01:01:06,440
 and just like before,

1178
01:01:06,440 --> 01:01:08,920
 we're going to go ahead and use our skill.

1179
01:01:08,920 --> 01:01:12,680
 But here, we're also going to include the doc skill as well.

1180
01:01:13,320 --> 01:01:14,200
 We're going to use this

1181
01:01:14,200 --> 01:01:16,200
 because we want to create a Word doc

1182
01:01:16,200 --> 01:01:18,520
 summarizing the results and the plots.

1183
01:01:18,520 --> 01:01:20,360
 So here, we're seeing a combination

1184
01:01:20,360 --> 01:01:22,440
 of custom skills with the skill ID

1185
01:01:22,440 --> 01:01:23,880
 that we have as well as the version,

1186
01:01:24,440 --> 01:01:27,240
 and using anthropic built-in skills,

1187
01:01:27,240 --> 01:01:28,760
 in this case, the docx skill.

1188
01:01:29,560 --> 01:01:31,000
 We're passing in the same headers

1189
01:01:31,000 --> 01:01:32,680
 that we had to pass in before,

1190
01:01:32,680 --> 01:01:35,400
 skills, code execution, and the files API.

1191
01:01:37,080 --> 01:01:38,600
 Now that this has finished running,

1192
01:01:38,600 --> 01:01:42,520
 we can examine the particular type of response that we get.

1193
01:01:42,520 --> 01:01:45,080
 We're going to see something similar to what we saw before,

1194
01:01:45,080 --> 01:01:47,320
 but this time, there's just a little bit more happening.

1195
01:01:48,040 --> 01:01:49,720
 Let's go and see what's happening under the hood

1196
01:01:49,720 --> 01:01:50,840
 with our nice formatting.

1197
01:01:51,480 --> 01:01:53,640
 So here, the model is going to respond

1198
01:01:53,640 --> 01:01:56,200
 by helping us analyze time series data,

1199
01:01:56,200 --> 01:01:57,240
 and just like before,

1200
01:01:57,240 --> 01:01:59,400
 we're going to start reading the entirety

1201
01:01:59,400 --> 01:02:01,160
 of these skill MD files.

1202
01:02:01,160 --> 01:02:02,840
 We're going to read our custom skill

1203
01:02:02,840 --> 01:02:05,240
 as well as the built-in docx skill,

1204
01:02:05,240 --> 01:02:06,280
 which we're going to need to use.

1205
01:02:06,920 --> 01:02:09,560
 We can see the result of those include the content

1206
01:02:09,560 --> 01:02:11,160
 starting from the beginning of the file,

1207
01:02:11,160 --> 01:02:13,240
 and including the entire skill MD.

1208
01:02:13,800 --> 01:02:16,200
 Next, we're going to go ahead and examine the data

1209
01:02:16,200 --> 01:02:18,280
 to run our time series analysis.

1210
01:02:18,280 --> 01:02:21,560
 We're going to look at just the first 20 lines of this CSV

1211
01:02:21,560 --> 01:02:23,960
 to examine the names of the columns

1212
01:02:23,960 --> 01:02:25,880
 and the type of data that we're working with.

1213
01:02:26,520 --> 01:02:28,440
 Since this is working as expected,

1214
01:02:28,440 --> 01:02:31,400
 we're going to go ahead and run the diagnostics

1215
01:02:31,400 --> 01:02:33,080
 and create the visualizations.

1216
01:02:33,640 --> 01:02:36,280
 These particular commands that we need to run

1217
01:02:36,280 --> 01:02:38,600
 are coming directly from our skill.

1218
01:02:38,600 --> 01:02:40,520
 Here is where we're going to go ahead,

1219
01:02:40,520 --> 01:02:42,520
 read those underlying files,

1220
01:02:42,520 --> 01:02:46,120
 execute that code, and hand that back to clod to work with.

1221
01:02:46,760 --> 01:02:49,560
 We're going to get back the result of these executions.

1222
01:02:49,560 --> 01:02:52,920
 We're going to get that back for diagnose as well as visualize.

1223
01:02:53,560 --> 01:02:56,840
 We're then going to read the summary and diagnostics,

1224
01:02:56,840 --> 01:02:58,840
 which is the result of our script

1225
01:02:58,840 --> 01:03:01,720
 that comes in a file called summary.txt.

1226
01:03:02,520 --> 01:03:05,240
 Once we have that particular file created,

1227
01:03:05,240 --> 01:03:07,640
 we can then go ahead and create a Word document.

1228
01:03:08,280 --> 01:03:12,040
 The built-in docx skill includes the correct content

1229
01:03:12,040 --> 01:03:13,640
 for how to work with Word docs.

1230
01:03:14,440 --> 01:03:16,200
 We're going to go ahead and take a look

1231
01:03:16,200 --> 01:03:18,520
 at how best to generate that document

1232
01:03:18,520 --> 01:03:20,680
 and leverage progressive disclosure here.

1233
01:03:20,680 --> 01:03:23,400
 We don't need everything from the docx skill

1234
01:03:23,400 --> 01:03:26,520
 just using a way to get to those markdown files.

1235
01:03:27,080 --> 01:03:28,040
 Once we have that,

1236
01:03:28,040 --> 01:03:30,600
 we'll create the comprehensive Word document

1237
01:03:30,600 --> 01:03:32,520
 using the skill necessary,

1238
01:03:32,520 --> 01:03:34,600
 execute the code to make it do that,

1239
01:03:34,600 --> 01:03:36,840
 and generate the underlying Word document.

1240
01:03:37,400 --> 01:03:39,000
 Once we have that Word document,

1241
01:03:39,000 --> 01:03:41,160
 we'll copy that to the output directory,

1242
01:03:41,160 --> 01:03:42,760
 and just like we saw before,

1243
01:03:42,760 --> 01:03:45,080
 get back a file ID that we can use

1244
01:03:45,080 --> 01:03:47,080
 if we want to download this Word document.

1245
01:03:47,800 --> 01:03:50,360
 We can see a summary of what this data looks like,

1246
01:03:50,360 --> 01:03:52,040
 and now we can download the file.

1247
01:03:52,680 --> 01:03:55,880
 Similarly, we'll go ahead and find that file ID if it exists.

1248
01:03:56,360 --> 01:03:59,240
 We're going to go ahead and download that particular file

1249
01:03:59,240 --> 01:04:02,360
 with the necessary contents as a docx file.

1250
01:04:03,160 --> 01:04:04,920
 If we take a look at what this looks like,

1251
01:04:04,920 --> 01:04:07,720
 we now have a Word document with our findings,

1252
01:04:07,720 --> 01:04:09,720
 our overview, our statistics.

1253
01:04:09,720 --> 01:04:12,920
 We can see that we brought in those plots and visualizations,

1254
01:04:12,920 --> 01:04:16,040
 as well as the statistical analysis that we've requested.

1255
01:04:16,040 --> 01:04:19,000
 This is also a great time to not only evaluate

1256
01:04:19,000 --> 01:04:21,080
 if what we're doing is expected in the skill,

1257
01:04:21,800 --> 01:04:24,280
 but that we're doing this in a predictable fashion.

1258
01:04:24,920 --> 01:04:26,360
 As we continue to evaluate,

1259
01:04:26,360 --> 01:04:29,240
 we can always modify this skill as much as we want,

1260
01:04:29,240 --> 01:04:31,320
 but all this data is coming in

1261
01:04:31,320 --> 01:04:33,880
 from the skill as well as the docx skill

1262
01:04:34,440 --> 01:04:35,880
 to create this individual file.

1263
01:04:37,080 --> 01:04:38,040
 Like we saw before,

1264
01:04:38,040 --> 01:04:39,560
 if we want to delete this skill,

1265
01:04:39,560 --> 01:04:42,120
 we can list all the versions and delete all those versions,

1266
01:04:42,680 --> 01:04:44,440
 and once those versions are deleted,

1267
01:04:44,440 --> 01:04:45,960
 delete the underlying skill.

1268
01:04:46,760 --> 01:04:47,960
 In this lesson,

1269
01:04:47,960 --> 01:04:50,840
 we've combined our knowledge of the messages API,

1270
01:04:50,840 --> 01:04:52,440
 the code execution tool,

1271
01:04:52,440 --> 01:04:53,800
 the files API,

1272
01:04:53,800 --> 01:04:56,280
 and skills to take our custom skills

1273
01:04:56,280 --> 01:04:58,280
 and work with them programmatically.

1274
01:04:58,280 --> 01:04:59,400
 In the next lesson,

1275
01:04:59,400 --> 01:05:00,920
 we're going to move to cloud code

1276
01:05:00,920 --> 01:05:03,480
 and see how to add our own custom skills

1277
01:05:03,480 --> 01:05:05,320
 inside of a dot cloud folder

1278
01:05:05,320 --> 01:05:07,880
 and build a more sophisticated command line application.

1279
01:05:08,760 --> 01:05:10,440
 We'll now switch to cloud code

1280
01:05:10,440 --> 01:05:12,520
 and use skills for code generation,

1281
01:05:12,520 --> 01:05:13,880
 reviewing, and testing.

1282
01:05:14,360 --> 01:05:17,320
 We'll also set up subagents and equip them with skills.

1283
01:05:17,880 --> 01:05:19,080
 Let's have some fun.

1284
01:05:19,080 --> 01:05:22,040
 So far, we've seen how to use skills in cloud AI

1285
01:05:22,040 --> 01:05:24,520
 and using the cloud messages API.

1286
01:05:24,520 --> 01:05:27,160
 Now, let's talk about how to use skills in cloud code

1287
01:05:27,160 --> 01:05:28,440
 in a bit more depth.

1288
01:05:28,440 --> 01:05:30,040
 The application that I'm using

1289
01:05:30,040 --> 01:05:33,640
 is a command line application for creating

1290
01:05:33,640 --> 01:05:35,640
 to do's that need to be completed

1291
01:05:35,640 --> 01:05:38,920
 and listing them and eventually editing and clearing.

1292
01:05:38,920 --> 01:05:40,760
 I'm going to show the cloud MD file

1293
01:05:40,760 --> 01:05:43,160
 to give you a sense of what this project does.

1294
01:05:43,160 --> 01:05:44,520
 I know we're going to do a little demo

1295
01:05:44,520 --> 01:05:47,000
 before we jump into each of the individual files.

1296
01:05:47,560 --> 01:05:48,520
 In cloud code,

1297
01:05:48,520 --> 01:05:51,880
 you have the ability to create a cloud MD file.

1298
01:05:51,880 --> 01:05:54,920
 This file is created using the slash init command

1299
01:05:54,920 --> 01:05:56,520
 or manually by the user.

1300
01:05:57,080 --> 01:05:59,240
 This file is always in your context

1301
01:05:59,240 --> 01:06:01,080
 and specific to your project.

1302
01:06:01,080 --> 01:06:04,040
 This is where you can specify general instructions

1303
01:06:04,040 --> 01:06:05,240
 about the code base,

1304
01:06:05,240 --> 01:06:06,680
 project you're working on,

1305
01:06:06,680 --> 01:06:07,880
 technology stack,

1306
01:06:07,880 --> 01:06:09,560
 and things that cloud needs to know

1307
01:06:09,560 --> 01:06:11,400
 in every single conversation.

1308
01:06:11,960 --> 01:06:13,720
 So again, we're building a command line

1309
01:06:13,720 --> 01:06:15,480
 task management application

1310
01:06:15,480 --> 01:06:16,760
 using Python,

1311
01:06:16,760 --> 01:06:18,840
 typer as our CLI framework,

1312
01:06:18,840 --> 01:06:20,680
 using data classes, rich,

1313
01:06:20,680 --> 01:06:23,880
 we're storing information in a JSON file for persistence

1314
01:06:23,880 --> 01:06:26,040
 and using UV for dependency management.

1315
01:06:26,600 --> 01:06:28,120
 Our architecture follows,

1316
01:06:28,120 --> 01:06:29,480
 according to this pattern,

1317
01:06:29,480 --> 01:06:31,000
 we've got our entry point

1318
01:06:31,000 --> 01:06:34,520
 and all of our commands get their own individual Python file.

1319
01:06:34,520 --> 01:06:37,320
 We set up our data class in our models.py,

1320
01:06:37,320 --> 01:06:38,920
 our logic for storing,

1321
01:06:38,920 --> 01:06:42,040
 serializing, deserializing in our storage.py,

1322
01:06:42,040 --> 01:06:44,200
 and then to display things nicely in the terminal,

1323
01:06:44,200 --> 01:06:45,560
 our display.py.

1324
01:06:45,560 --> 01:06:47,880
 We have a couple of constants and then our tests.

1325
01:06:48,760 --> 01:06:49,880
 We can see in this file,

1326
01:06:49,880 --> 01:06:51,000
 we have our priority,

1327
01:06:51,000 --> 01:06:52,520
 our task as data models,

1328
01:06:52,520 --> 01:06:54,040
 how data is persisted,

1329
01:06:54,040 --> 01:06:56,440
 and remember again for this cloud MD,

1330
01:06:56,440 --> 01:06:59,320
 this is data that is always available in context

1331
01:06:59,320 --> 01:07:01,560
 in every conversation that we have.

1332
01:07:01,560 --> 01:07:03,080
 This is useful information

1333
01:07:03,080 --> 01:07:04,600
 to help cloud figure out

1334
01:07:04,600 --> 01:07:05,560
 where to find things

1335
01:07:05,560 --> 01:07:07,880
 and how best to structure information.

1336
01:07:07,880 --> 01:07:08,760
 So with that in mind,

1337
01:07:08,760 --> 01:07:10,840
 let's hop in and play around with this application.

1338
01:07:11,480 --> 01:07:13,000
 First, I'm going to go ahead

1339
01:07:13,000 --> 01:07:15,240
 and activate the virtual environment.

1340
01:07:15,240 --> 01:07:16,040
 So I'll source,

1341
01:07:17,000 --> 01:07:19,400
 then then activate.

1342
01:07:20,120 --> 01:07:21,320
 Once I've got that set up,

1343
01:07:21,320 --> 01:07:24,040
 make sure my dependencies are in order with UV sync.

1344
01:07:30,200 --> 01:07:33,080
 And once I've done that,

1345
01:07:33,080 --> 01:07:34,360
 I can actually start using

1346
01:07:34,360 --> 01:07:37,480
 this task command directly in the command line.

1347
01:07:37,480 --> 01:07:38,760
 If I take a look at the command,

1348
01:07:38,760 --> 01:07:42,280
 I see I have commands like add and done and list,

1349
01:07:42,280 --> 01:07:43,960
 as well as some additional options.

1350
01:07:44,520 --> 01:07:45,880
 So let's go ahead and take a look

1351
01:07:45,880 --> 01:07:47,960
 at the tasks that I have right here.

1352
01:07:47,960 --> 01:07:48,600
 Right now,

1353
01:07:48,600 --> 01:07:50,360
 I have none of them that are found.

1354
01:07:50,360 --> 01:07:51,400
 I'll clear the terminal

1355
01:07:51,400 --> 01:07:52,680
 so I can start from the top,

1356
01:07:52,680 --> 01:07:54,600
 and let's go ahead and add a task.

1357
01:07:54,600 --> 01:07:55,480
 Right here,

1358
01:07:55,480 --> 01:07:57,160
 we'll call this right the final report,

1359
01:07:58,200 --> 01:08:00,520
 and we'll give this a priority of high,

1360
01:08:01,240 --> 01:08:02,600
 and we'll give this a date

1361
01:08:02,600 --> 01:08:04,520
 to be done with the following.

1362
01:08:05,320 --> 01:08:05,960
 We can see here,

1363
01:08:05,960 --> 01:08:07,080
 I've added that successfully.

1364
01:08:07,080 --> 01:08:08,040
 So let's go take a look.

1365
01:08:09,000 --> 01:08:10,600
 We've got our task right there,

1366
01:08:10,600 --> 01:08:11,720
 our display.py,

1367
01:08:11,720 --> 01:08:14,280
 doing some nice formatting of that information.

1368
01:08:14,280 --> 01:08:16,040
 Now let's go ahead and complete it.

1369
01:08:16,040 --> 01:08:18,520
 I'll go ahead and mark that as done with the correct ID.

1370
01:08:19,160 --> 01:08:21,240
 And then if I go ahead and take a look at my list,

1371
01:08:22,440 --> 01:08:26,440
 I can see with that flag that I have this task that is done.

1372
01:08:27,240 --> 01:08:29,080
 The plan for this lesson here

1373
01:08:29,080 --> 01:08:32,280
 is to add another command line command for edit.

1374
01:08:32,280 --> 01:08:35,240
 So we're going to have to go to SRC

1375
01:08:35,240 --> 01:08:38,280
 to task and add another command here for editing.

1376
01:08:38,280 --> 01:08:39,960
 But we also want to make sure

1377
01:08:39,960 --> 01:08:42,440
 that when we add these additional commands,

1378
01:08:42,440 --> 01:08:44,680
 we're following the correct workflow.

1379
01:08:44,680 --> 01:08:46,440
 We're following a proper way

1380
01:08:46,440 --> 01:08:48,440
 of adding commands the right way

1381
01:08:48,440 --> 01:08:51,800
 to pattern match a bit of what we've done in this codebase.

1382
01:08:51,800 --> 01:08:52,840
 In order to do so,

1383
01:08:52,840 --> 01:08:54,520
 we're going to be using a skill here

1384
01:08:54,520 --> 01:08:57,160
 that we've added called adding CLI command.

1385
01:08:57,720 --> 01:09:00,920
 Skills are defined inside of the dot quad folder,

1386
01:09:00,920 --> 01:09:03,320
 followed by a folder called skills.

1387
01:09:03,320 --> 01:09:05,080
 When we take a look at this skill,

1388
01:09:05,080 --> 01:09:08,200
 first, not only we can see that this is available

1389
01:09:08,200 --> 01:09:09,720
 at the project level,

1390
01:09:09,720 --> 01:09:12,280
 we can also create skills at the user level

1391
01:09:12,280 --> 01:09:14,440
 in our home directory if we'd like as well.

1392
01:09:14,440 --> 01:09:15,320
 For this example,

1393
01:09:15,320 --> 01:09:17,640
 we'll be focusing in project specific skills.

1394
01:09:18,600 --> 01:09:22,120
 So let's dive into what's happening for this particular skill.

1395
01:09:22,120 --> 01:09:23,320
 Just like we saw before,

1396
01:09:23,320 --> 01:09:25,320
 we have a name and a description.

1397
01:09:25,320 --> 01:09:27,000
 And here, we're going to really lean

1398
01:09:27,000 --> 01:09:29,320
 into the particular coding styles

1399
01:09:29,320 --> 01:09:31,160
 and functionality that we want

1400
01:09:31,160 --> 01:09:33,240
 when creating new commands.

1401
01:09:33,240 --> 01:09:36,280
 We're going to start by identifying the workflow necessary

1402
01:09:36,280 --> 01:09:39,560
 and creating files in the appropriate directories.

1403
01:09:39,560 --> 01:09:42,360
 Just like we have commands for add and done and list,

1404
01:09:42,360 --> 01:09:43,560
 we want to make sure

1405
01:09:43,560 --> 01:09:45,880
 that when we make new files for commands,

1406
01:09:45,880 --> 01:09:47,000
 it lives there.

1407
01:09:47,000 --> 01:09:47,960
 We also want to make sure

1408
01:09:47,960 --> 01:09:49,880
 that these commands are registered

1409
01:09:49,880 --> 01:09:52,040
 in our dunderinit.py file

1410
01:09:52,040 --> 01:09:53,960
 that lives in the command folder.

1411
01:09:53,960 --> 01:09:56,600
 When we think about how to create different commands,

1412
01:09:56,600 --> 01:09:58,600
 there may be lots of different kinds.

1413
01:09:58,600 --> 01:10:01,000
 There may be commands that involve subcommands

1414
01:10:01,000 --> 01:10:03,560
 or flags or additional arguments.

1415
01:10:03,560 --> 01:10:06,280
 You can provide plain text instructions to Claude,

1416
01:10:06,280 --> 01:10:08,120
 but especially for coding examples,

1417
01:10:08,120 --> 01:10:09,480
 Claude does really well

1418
01:10:09,480 --> 01:10:11,080
 when you tell it exactly

1419
01:10:11,080 --> 01:10:13,560
 what pattern and style you want to follow.

1420
01:10:13,560 --> 01:10:14,680
 In the type or library,

1421
01:10:14,680 --> 01:10:15,800
 there are many different ways

1422
01:10:15,800 --> 01:10:18,040
 of accomplishing particular tasks.

1423
01:10:18,040 --> 01:10:18,920
 For example,

1424
01:10:18,920 --> 01:10:20,040
 there are many different ways

1425
01:10:20,040 --> 01:10:22,600
 of adding type annotations to arguments

1426
01:10:22,600 --> 01:10:24,040
 that are being decorated.

1427
01:10:24,040 --> 01:10:25,560
 In this particular case,

1428
01:10:25,560 --> 01:10:27,560
 this is the convention we want to follow

1429
01:10:27,560 --> 01:10:29,160
 as it's a little bit more modern.

1430
01:10:29,160 --> 01:10:32,200
 You can imagine in libraries and code bases that you use,

1431
01:10:32,200 --> 01:10:34,600
 there are many different ways of doing things.

1432
01:10:34,600 --> 01:10:36,120
 But what's useful about skills

1433
01:10:36,120 --> 01:10:38,440
 is it gives us that predictable workflow

1434
01:10:38,440 --> 01:10:40,120
 for a set of tasks.

1435
01:10:40,120 --> 01:10:41,160
 We also want to make sure

1436
01:10:41,160 --> 01:10:43,960
 we're using this display object here

1437
01:10:43,960 --> 01:10:46,600
 and calling methods like success and info

1438
01:10:46,600 --> 01:10:48,200
 to make sure that when we add a command,

1439
01:10:48,200 --> 01:10:50,520
 we're not only executing the business logic,

1440
01:10:50,520 --> 01:10:52,200
 but displaying the correct information

1441
01:10:52,200 --> 01:10:53,880
 to the user at the end.

1442
01:10:53,880 --> 01:10:55,080
 When we work with flags,

1443
01:10:55,080 --> 01:10:56,840
 we want particular shorthand,

1444
01:10:56,840 --> 01:10:59,160
 we want particular longer ways of addressing it,

1445
01:10:59,160 --> 01:11:01,560
 we want to make sure that there's help text as well.

1446
01:11:01,560 --> 01:11:02,680
 All of these pieces,

1447
01:11:02,680 --> 01:11:05,000
 type annotations, default arguments,

1448
01:11:05,000 --> 01:11:06,440
 certain return values

1449
01:11:06,440 --> 01:11:08,360
 are valuable to add in your skill

1450
01:11:08,360 --> 01:11:10,440
 so that you know how best the pattern match

1451
01:11:10,440 --> 01:11:12,360
 and follow predictable workflows.

1452
01:11:12,360 --> 01:11:14,840
 As we think about commands with subcommands,

1453
01:11:14,840 --> 01:11:16,520
 not only can you see here

1454
01:11:16,520 --> 01:11:19,080
 how we want to structure individual commands,

1455
01:11:19,080 --> 01:11:21,160
 but also how we want to display

1456
01:11:21,160 --> 01:11:24,440
 when things like migrations or versions are changed.

1457
01:11:24,440 --> 01:11:26,840
 As we imagine commands that might be destructive,

1458
01:11:26,840 --> 01:11:29,320
 as we start adding functionality to clear,

1459
01:11:29,320 --> 01:11:32,360
 we might want to specify what kind of delete we're doing.

1460
01:11:32,360 --> 01:11:34,280
 If we choose to do a hard delete,

1461
01:11:34,280 --> 01:11:35,800
 we want to make sure that we confirm

1462
01:11:35,800 --> 01:11:39,080
 before we go ahead and delete that particular task.

1463
01:11:39,080 --> 01:11:40,680
 This pattern can be followed

1464
01:11:40,680 --> 01:11:43,240
 as Claude starts to see additional commands

1465
01:11:43,240 --> 01:11:45,640
 that might need to involve some kind of deletion.

1466
01:11:45,640 --> 01:11:47,240
 As we think about registering,

1467
01:11:47,240 --> 01:11:48,360
 we want to be intentional

1468
01:11:48,360 --> 01:11:51,080
 about how to add single commands and command groups.

1469
01:11:51,080 --> 01:11:53,880
 So not only are we giving Claude instructions

1470
01:11:53,880 --> 01:11:55,320
 for how to register commands,

1471
01:11:55,320 --> 01:11:58,040
 we're being very specific with what conventions to follow.

1472
01:11:58,760 --> 01:12:00,920
 And finally, as we talk about conventions,

1473
01:12:00,920 --> 01:12:02,280
 here's where we can lean into

1474
01:12:02,280 --> 01:12:04,200
 requirements on our doc strings,

1475
01:12:04,200 --> 01:12:05,640
 being mindful of exit codes

1476
01:12:05,640 --> 01:12:07,560
 and following constants that we have,

1477
01:12:07,560 --> 01:12:09,720
 being mindful of commands that are destructive.

1478
01:12:09,720 --> 01:12:11,320
 This is a really useful place

1479
01:12:11,320 --> 01:12:13,480
 so that when we build our predictable workflows,

1480
01:12:13,480 --> 01:12:16,040
 we know exactly what conventions we're following.

1481
01:12:16,040 --> 01:12:18,120
 These are not conventions that have to exist

1482
01:12:18,120 --> 01:12:19,320
 everywhere in the code base

1483
01:12:19,320 --> 01:12:21,640
 and have to be loaded everywhere in context.

1484
01:12:21,640 --> 01:12:23,800
 If so, we could put them in the Claude MD.

1485
01:12:23,800 --> 01:12:26,520
 But in this case, just for adding individual commands,

1486
01:12:26,520 --> 01:12:28,760
 there's a subset of conventions to follow.

1487
01:12:28,760 --> 01:12:31,000
 Let's only load those when necessary.

1488
01:12:31,000 --> 01:12:34,920
 And not only are we using generic naming like CLI app,

1489
01:12:34,920 --> 01:12:37,400
 we can use this skill across any platform

1490
01:12:37,400 --> 01:12:39,560
 that follows the agent skills convention.

1491
01:12:39,560 --> 01:12:41,880
 And depending on whatever CLI you're building,

1492
01:12:41,880 --> 01:12:44,440
 if you want Claude to follow these particular patterns,

1493
01:12:44,440 --> 01:12:46,520
 this skill can easily be adapted to do that.

1494
01:12:47,080 --> 01:12:50,120
 Now that we have a skill for adding CLI commands,

1495
01:12:50,120 --> 01:12:52,600
 let's also make sure that when we start to do

1496
01:12:52,600 --> 01:12:55,000
 this particular workflow of adding commands,

1497
01:12:55,000 --> 01:12:56,680
 we're being mindful of testing

1498
01:12:56,680 --> 01:12:59,240
 and also validating the commands that we write.

1499
01:12:59,240 --> 01:13:01,560
 This is another great use case for another skill.

1500
01:13:02,280 --> 01:13:05,560
 In our second skill, for generating CLI tests,

1501
01:13:05,560 --> 01:13:08,920
 we generate PyTest tests for type or commands.

1502
01:13:08,920 --> 01:13:12,360
 We include here what kinds of fixtures we want,

1503
01:13:12,360 --> 01:13:14,120
 how to handle edge cases.

1504
01:13:14,120 --> 01:13:16,280
 And this is really important that we add

1505
01:13:16,280 --> 01:13:19,240
 what to do and how to trigger this particular skill.

1506
01:13:19,240 --> 01:13:20,200
 You can see here,

1507
01:13:20,200 --> 01:13:22,280
 use when the user asks to write tests,

1508
01:13:22,280 --> 01:13:24,680
 test for my CLI, or add test coverage.

1509
01:13:25,240 --> 01:13:27,160
 It's always important to be very explicit,

1510
01:13:27,160 --> 01:13:29,720
 not only in what the description is,

1511
01:13:29,720 --> 01:13:31,560
 but how Claude can detect how to run it.

1512
01:13:32,120 --> 01:13:33,640
 Similar to other skills,

1513
01:13:33,640 --> 01:13:35,400
 we specify the workflow that we want.

1514
01:13:35,960 --> 01:13:36,920
 When writing tests,

1515
01:13:36,920 --> 01:13:39,880
 it's often best practice to leverage fixtures.

1516
01:13:39,880 --> 01:13:42,520
 You can think of fixtures as information

1517
01:13:42,520 --> 01:13:45,720
 that is run each time as you arrange your tests,

1518
01:13:45,720 --> 01:13:47,240
 to set up information,

1519
01:13:47,240 --> 01:13:48,760
 to set up dummy data,

1520
01:13:48,760 --> 01:13:51,560
 as well as any kind of mocking or test infrastructure

1521
01:13:51,560 --> 01:13:54,360
 that you need for each of the tests that you write.

1522
01:13:54,360 --> 01:13:55,560
 For example, here,

1523
01:13:55,560 --> 01:13:58,680
 we specify what our temporary storage might look like,

1524
01:13:58,680 --> 01:14:01,880
 and we specify what some sample data might look like.

1525
01:14:01,880 --> 01:14:03,960
 As we run each of these tests,

1526
01:14:03,960 --> 01:14:07,240
 this information will be exposed to allow us to arrange

1527
01:14:07,240 --> 01:14:09,400
 and set up the tests necessary

1528
01:14:09,400 --> 01:14:12,760
 when we test individual files, folders, and workflows.

1529
01:14:13,640 --> 01:14:15,080
 As we take a look at the test structure,

1530
01:14:15,080 --> 01:14:16,600
 we're following a pattern of arranging,

1531
01:14:16,600 --> 01:14:18,360
 like we mentioned with our fixtures,

1532
01:14:18,360 --> 01:14:20,200
 invoking some kind of action,

1533
01:14:20,200 --> 01:14:22,520
 and then asserting that the result is the case.

1534
01:14:22,520 --> 01:14:25,000
 Right here, we're simply trying to build patterns

1535
01:14:25,000 --> 01:14:26,200
 that Claude can use

1536
01:14:26,200 --> 01:14:28,440
 and follow when the skill is leveraged.

1537
01:14:28,440 --> 01:14:31,880
 We can continue on with how we want this test runner to be done,

1538
01:14:31,880 --> 01:14:34,360
 and how to test scenarios by a command type.

1539
01:14:34,360 --> 01:14:36,040
 As we read, as we add,

1540
01:14:36,040 --> 01:14:39,160
 here are examples for what we want our tests to look like.

1541
01:14:39,160 --> 01:14:41,000
 As with many testing libraries,

1542
01:14:41,000 --> 01:14:43,960
 there are lots of ways to accomplish a similar kind of task.

1543
01:14:43,960 --> 01:14:45,000
 For these examples,

1544
01:14:45,000 --> 01:14:46,520
 here's the pattern we want to follow.

1545
01:14:47,960 --> 01:14:49,960
 As we wrap towards the end of the skill,

1546
01:14:49,960 --> 01:14:52,520
 we want to think a little bit about edge cases to cover.

1547
01:14:52,520 --> 01:14:53,480
 When writing tests,

1548
01:14:53,480 --> 01:14:55,400
 we want to think about invalid input,

1549
01:14:55,400 --> 01:14:57,560
 any kind of state, confirmation,

1550
01:14:57,560 --> 01:15:00,920
 or what happens when things are not found or don't exist.

1551
01:15:00,920 --> 01:15:03,640
 We want to make sure that we're following a checklist as well

1552
01:15:03,640 --> 01:15:05,720
 when we go ahead and write our tests.

1553
01:15:05,720 --> 01:15:06,840
 And then finally,

1554
01:15:06,840 --> 01:15:08,840
 to make sure we're running tests correctly,

1555
01:15:08,840 --> 01:15:10,440
 providing the correct commands,

1556
01:15:10,440 --> 01:15:12,360
 as well as how to run in a verbose mode,

1557
01:15:12,360 --> 01:15:13,560
 and for specific files.

1558
01:15:14,200 --> 01:15:15,720
 The last skill that we have here

1559
01:15:15,720 --> 01:15:17,400
 is to wrap up and review

1560
01:15:17,400 --> 01:15:20,520
 and make sure that we're executing the commands as expected.

1561
01:15:20,520 --> 01:15:23,240
 Once we've generated the tests and the tests are running,

1562
01:15:23,240 --> 01:15:26,120
 let's make sure we're following the correct conventions.

1563
01:15:26,120 --> 01:15:28,200
 Just like we saw with other skills,

1564
01:15:28,200 --> 01:15:30,840
 there are ways in which we can execute the task necessary

1565
01:15:30,840 --> 01:15:32,360
 and then come back and validate

1566
01:15:32,360 --> 01:15:34,440
 that things are working as expected.

1567
01:15:34,440 --> 01:15:36,520
 As we think about reviewing these commands,

1568
01:15:36,520 --> 01:15:39,160
 not only do we think about the underlying structure,

1569
01:15:39,160 --> 01:15:40,760
 is this in the right location?

1570
01:15:40,760 --> 01:15:42,600
 Is this using the right decorator?

1571
01:15:42,600 --> 01:15:44,360
 Is this registered correctly?

1572
01:15:44,360 --> 01:15:45,480
 But we're also making sure

1573
01:15:45,480 --> 01:15:47,240
 that some of those practices we wanted

1574
01:15:47,240 --> 01:15:50,360
 around type annotations or options for parameters

1575
01:15:50,360 --> 01:15:52,120
 or flags when possible,

1576
01:15:52,120 --> 01:15:53,560
 always are included.

1577
01:15:53,560 --> 01:15:56,920
 It's often helpful to provide positive and negative examples.

1578
01:15:56,920 --> 01:15:59,480
 So as we mentioned, using this annotated type

1579
01:15:59,480 --> 01:16:02,760
 versus a different kind of way to type your arguments.

1580
01:16:04,120 --> 01:16:06,680
 As we think more about error handling and output,

1581
01:16:06,680 --> 01:16:09,080
 we make sure that this checklist exists

1582
01:16:09,080 --> 01:16:10,680
 so that the skill can go through

1583
01:16:10,680 --> 01:16:14,360
 and confirm that all of these pieces are as expected.

1584
01:16:14,360 --> 01:16:17,800
 We're not telling Claude how to perform these actions

1585
01:16:17,800 --> 01:16:19,880
 like adding commands and generating tests.

1586
01:16:19,880 --> 01:16:22,440
 We're making sure that it's working as expected.

1587
01:16:22,440 --> 01:16:25,240
 You can think of this like an evaluation almost

1588
01:16:25,240 --> 01:16:27,000
 for the other skills that we have

1589
01:16:27,000 --> 01:16:29,480
 and including this skill as part of our workflow.

1590
01:16:30,440 --> 01:16:31,960
 As we take a look at the bottom,

1591
01:16:31,960 --> 01:16:34,360
 making sure that our best practices are followed,

1592
01:16:34,360 --> 01:16:36,920
 as well as examples of mistakes we might see

1593
01:16:36,920 --> 01:16:38,520
 and fixes for those.

1594
01:16:38,520 --> 01:16:41,000
 As we take a look at the output format of this skill,

1595
01:16:41,000 --> 01:16:44,120
 we want to make sure that all of our checklist is addressed,

1596
01:16:44,120 --> 01:16:46,920
 including a summary and suggested fixes.

1597
01:16:46,920 --> 01:16:49,320
 It's very useful to have this underlying review

1598
01:16:49,320 --> 01:16:50,760
 so that when features are finished,

1599
01:16:50,760 --> 01:16:52,840
 we can start by taking a look at this review,

1600
01:16:52,840 --> 01:16:55,080
 include this even as part of our code review,

1601
01:16:55,080 --> 01:16:57,240
 make sure we're building production grade features

1602
01:16:57,240 --> 01:16:59,560
 backed by tests following best practices.

1603
01:17:00,120 --> 01:17:01,160
 With that in mind,

1604
01:17:01,160 --> 01:17:03,480
 let's start to put all of these skills together.

1605
01:17:03,480 --> 01:17:05,000
 The first thing we're going to do here

1606
01:17:05,000 --> 01:17:09,240
 is to add a new command that allows us to edit individual tasks.

1607
01:17:09,240 --> 01:17:10,920
 We're going to want to make sure we edit the title

1608
01:17:10,920 --> 01:17:13,800
 and priority and pass in an ID that is valid.

1609
01:17:14,360 --> 01:17:17,000
 Now let's hop into Claude code and use these skills.

1610
01:17:18,040 --> 01:17:20,920
 To make sure that I've registered these correctly,

1611
01:17:20,920 --> 01:17:23,560
 I'm first going to just type in /skills.

1612
01:17:24,280 --> 01:17:27,240
 This is going to list the available skills that I have to me.

1613
01:17:27,240 --> 01:17:28,840
 These are project skills.

1614
01:17:28,840 --> 01:17:32,280
 We also mentioned we can add skills in our home directory,

1615
01:17:32,280 --> 01:17:34,600
 but right now we're just dealing with project skills.

1616
01:17:34,600 --> 01:17:37,560
 We can also see the amount of tokens that these skills are taking

1617
01:17:37,560 --> 01:17:40,440
 as we just think about the name and description necessary.

1618
01:17:41,080 --> 01:17:43,720
 When you create a new skill in Claude code,

1619
01:17:43,720 --> 01:17:46,280
 you want to make sure that you close Claude code

1620
01:17:46,280 --> 01:17:49,480
 and open it up again so that skill can be identified.

1621
01:17:49,480 --> 01:17:51,880
 So if you find yourself looking at your list of skills,

1622
01:17:51,880 --> 01:17:54,200
 but you're missing the one that you might have just created,

1623
01:17:54,200 --> 01:17:56,520
 make sure to close that instance of Claude code,

1624
01:17:56,520 --> 01:17:58,520
 open it up again, and you should be in good shape.

1625
01:17:59,240 --> 01:18:01,240
 Now that our skills are loaded correctly,

1626
01:18:01,240 --> 01:18:04,040
 let's go ahead and add a new edit command

1627
01:18:04,040 --> 01:18:07,160
 to allow users to edit the title and priority.

1628
01:18:07,160 --> 01:18:08,920
 We're adding a little example here

1629
01:18:08,920 --> 01:18:11,160
 and ensuring that we follow the conventions

1630
01:18:11,160 --> 01:18:12,920
 for creating a new CLI command.

1631
01:18:13,480 --> 01:18:14,440
 So let's give this a shot.

1632
01:18:15,080 --> 01:18:17,800
 We can see here that Claude code is prompting

1633
01:18:17,800 --> 01:18:21,160
 to use the adding CLI command skill, and that's great.

1634
01:18:21,160 --> 01:18:23,080
 We'll go ahead and make sure that in the future,

1635
01:18:23,080 --> 01:18:25,000
 it doesn't prompt us to do so.

1636
01:18:25,000 --> 01:18:27,560
 We can see here we're going to read the existing files

1637
01:18:27,560 --> 01:18:29,880
 and storage to understand the convention,

1638
01:18:29,880 --> 01:18:33,880
 as well as take a look at examples of other commands for reference.

1639
01:18:34,520 --> 01:18:35,960
 Now that we know the conventions,

1640
01:18:35,960 --> 01:18:38,520
 let's go ahead and create that particular file.

1641
01:18:38,520 --> 01:18:41,800
 We can see here there's a new file edit.py being created,

1642
01:18:41,800 --> 01:18:43,480
 and we're going to go ahead and make that change.

1643
01:18:44,040 --> 01:18:46,280
 We'll see here edit.py appears,

1644
01:18:46,280 --> 01:18:48,760
 and we're now going to register that command

1645
01:18:48,760 --> 01:18:51,320
 following the order that the skill has set out for us.

1646
01:18:51,880 --> 01:18:54,360
 We can see here that the command is being registered

1647
01:18:54,360 --> 01:18:56,760
 inside of our dunder init as expected.

1648
01:18:56,760 --> 01:18:58,520
 We're going to go ahead and make that change as well.

1649
01:18:59,320 --> 01:19:02,200
 So we'll go ahead and let it proceed and run this command

1650
01:19:02,200 --> 01:19:05,000
 to test out and make sure it's working as expected.

1651
01:19:05,000 --> 01:19:07,800
 Looks like we're seeing what we expect, and that's in good shape.

1652
01:19:08,440 --> 01:19:12,120
 So now going to run the add command and then go ahead

1653
01:19:12,120 --> 01:19:14,760
 and run the list to make sure we've added successfully.

1654
01:19:14,760 --> 01:19:16,840
 It's seating some data that we can then make sure

1655
01:19:16,840 --> 01:19:18,440
 the edit command works as expected.

1656
01:19:19,240 --> 01:19:21,240
 We'll go ahead and edit that particular task.

1657
01:19:21,880 --> 01:19:24,840
 And we'll see here that we didn't specify a title or priority.

1658
01:19:25,480 --> 01:19:27,560
 We'll then go ahead and put in that title,

1659
01:19:27,560 --> 01:19:30,120
 and here we'll see that edited as expected.

1660
01:19:32,040 --> 01:19:34,440
 It's going to ask me again to edit this task,

1661
01:19:34,440 --> 01:19:36,440
 and this is going to happen over and over

1662
01:19:36,440 --> 01:19:38,600
 as we start to test all kinds of examples.

1663
01:19:39,080 --> 01:19:41,400
 And while I could proceed over and over again,

1664
01:19:41,400 --> 01:19:43,240
 we can imagine that this might start to fill up

1665
01:19:43,240 --> 01:19:45,000
 the context window quite a bit.

1666
01:19:45,000 --> 01:19:46,840
 And if this were a larger scale system,

1667
01:19:46,840 --> 01:19:50,040
 it might be very time intensive and even compute intensive.

1668
01:19:50,040 --> 01:19:52,920
 So what we're going to do here is something slightly different.

1669
01:19:52,920 --> 01:19:56,280
 We're going to leverage the functionality that cloud code has

1670
01:19:56,280 --> 01:19:57,640
 for using subagents.

1671
01:19:58,120 --> 01:20:01,160
 We're going to have one subagent to review code

1672
01:20:01,160 --> 01:20:05,720
 and follow the criteria so that the main agent can focus on the development.

1673
01:20:05,720 --> 01:20:07,800
 We're then going to have another subagent

1674
01:20:07,800 --> 01:20:11,080
 to generate and run the tests using the skill that we have.

1675
01:20:11,720 --> 01:20:13,400
 What's going to be useful about this

1676
01:20:13,400 --> 01:20:16,040
 is that we can have the main agent focus on development

1677
01:20:16,040 --> 01:20:21,080
 while subagents in their own context window focus on generating the tests

1678
01:20:21,080 --> 01:20:22,520
 and reviewing the code.

1679
01:20:22,520 --> 01:20:25,160
 We can then take the feedback and tests generated,

1680
01:20:25,160 --> 01:20:28,840
 bring it back to the main agent with a much more context efficient approach.

1681
01:20:29,480 --> 01:20:33,720
 It's important to note that subagents do not inherit skills from a parent,

1682
01:20:33,720 --> 01:20:38,040
 so we need to be explicit with the skills that we give to each subagent that we make.

1683
01:20:38,840 --> 01:20:42,440
 There are multiple ways of passing skills to subagents.

1684
01:20:42,440 --> 01:20:47,560
 One way we're going to show you is being explicit with the name of the skill in the subagent.

1685
01:20:47,560 --> 01:20:51,240
 Another option that will link in the notes is where you can provide

1686
01:20:51,240 --> 01:20:55,560
 the exact agent name and how best to run it from the skill directly.

1687
01:20:55,560 --> 01:20:58,280
 With that in mind, let's go ahead and create our subagents.

1688
01:21:00,600 --> 01:21:03,560
 The first agent we're going to make is our code reviewer,

1689
01:21:03,560 --> 01:21:06,600
 and we're going to create these agents using the slash agents command.

1690
01:21:07,160 --> 01:21:08,680
 We're going to create a new agent.

1691
01:21:08,680 --> 01:21:10,920
 We're going to do that on a project basis,

1692
01:21:10,920 --> 01:21:14,920
 but instead of generating with Claude, we're going to follow a manual configuration

1693
01:21:14,920 --> 01:21:18,600
 so you can see what it looks like to add a name, description, tools,

1694
01:21:18,600 --> 01:21:21,720
 and most importantly, skills for each of our agents.

1695
01:21:21,720 --> 01:21:23,800
 The first one I'll make we'll call code reviewer.

1696
01:21:24,600 --> 01:21:28,920
 This will be the unique identifier for our agent and then we'll pass a prompt to it.

1697
01:21:28,920 --> 01:21:32,760
 We're going to paste in a prompt that we'll take a look at once we've created this

1698
01:21:32,760 --> 01:21:35,800
 but it's going to look very familiar to how we review

1699
01:21:35,800 --> 01:21:39,800
 and how we're specific and actionable in the insights we make when doing the code review.

1700
01:21:40,680 --> 01:21:43,560
 We're going to go ahead and give this agent a description

1701
01:21:43,560 --> 01:21:45,640
 for when it should go ahead and be used.

1702
01:21:45,640 --> 01:21:48,920
 We're going to review for code quality, security, and so on.

1703
01:21:48,920 --> 01:21:51,560
 We're going to try to make this agent as generic as possible

1704
01:21:52,200 --> 01:21:53,880
 for the set of tools that we want here.

1705
01:21:54,680 --> 01:21:58,760
 We want to be very specific with the tools that our subagent has access to,

1706
01:21:58,760 --> 01:22:01,240
 so we'll make sure that if there's code that needs to be executed,

1707
01:22:01,240 --> 01:22:04,600
 we give it bash, glob and grep for finding files,

1708
01:22:04,600 --> 01:22:09,080
 and read to read underlying files that we're going to be reviewing.

1709
01:22:09,080 --> 01:22:11,800
 Once we've selected these tools, we can go ahead and continue.

1710
01:22:12,600 --> 01:22:15,880
 We'll decide to inherit from the parent with the model that we use,

1711
01:22:16,520 --> 01:22:18,600
 and we'll go ahead and give this a color of purple.

1712
01:22:19,880 --> 01:22:22,600
 Once we've got this set up, we'll go ahead and save this agent.

1713
01:22:23,480 --> 01:22:28,280
 We can see here now in our agents folder that we have a code reviewer agent to work with.

1714
01:22:29,240 --> 01:22:31,960
 We've got the code reviewer, a description, tools,

1715
01:22:31,960 --> 01:22:34,360
 and all of the wonderful pieces that we added.

1716
01:22:34,360 --> 01:22:38,760
 It's now time to make sure we specify the skills that we want this subagent to use.

1717
01:22:39,320 --> 01:22:45,240
 We'll do that using the skills field and specify the name of the skill that we're working with.

1718
01:22:45,880 --> 01:22:48,520
 In our case, reviewing CLI command.

1719
01:22:49,880 --> 01:22:53,560
 Before we create our next agent, let's do a quick review of what we made here.

1720
01:22:53,560 --> 01:22:58,040
 Our agent has a name and description, tools available, a model that we inherit,

1721
01:22:58,040 --> 01:23:00,680
 a color, and skills that we brought in.

1722
01:23:00,680 --> 01:23:03,560
 We can add multiple skills, but right now we're going to stick with one.

1723
01:23:04,120 --> 01:23:07,560
 In our prompt, we mentioned it's a code reviewer ensuring high standards.

1724
01:23:08,200 --> 01:23:13,960
 As we specify what this agent is, we specify when it's invoked, general quality checks,

1725
01:23:13,960 --> 01:23:18,360
 if we're working with Python, how to be intentional, CLI commands the same way,

1726
01:23:18,360 --> 01:23:20,360
 and a particular output format.

1727
01:23:20,360 --> 01:23:23,080
 Like we mentioned, this agent is a bit more generic.

1728
01:23:23,080 --> 01:23:26,840
 And while we're using it in the context of our specific application,

1729
01:23:26,840 --> 01:23:29,000
 skills can help us be more particular.

1730
01:23:29,000 --> 01:23:32,840
 But this agent might need to be used across a different variety of applications,

1731
01:23:32,840 --> 01:23:35,720
 so we want to be a little bit more generic to what we're trying to do here.

1732
01:23:36,280 --> 01:23:41,560
 It's important to note that skills operate slightly differently as subagents in cloud code.

1733
01:23:42,120 --> 01:23:45,000
 When this subagent is dispatched and created,

1734
01:23:45,000 --> 01:23:50,440
 the skill is not only loading the name and description, but the entire skill MD.

1735
01:23:50,440 --> 01:23:53,800
 The skills are preloaded when the agent is dispatched.

1736
01:23:53,800 --> 01:23:59,240
 If there is additional progressive disclosure, reading of other files or other commands,

1737
01:23:59,240 --> 01:24:04,120
 that is not done, but the entire skill MD is read when the subagent is dispatched.

1738
01:24:04,920 --> 01:24:10,760
 Now that we've got our code reviewer agent, let's add another agent for generating and running our tests.

1739
01:24:11,640 --> 01:24:14,200
 Let's go ahead and make our second agent.

1740
01:24:14,200 --> 01:24:18,760
 We're going to go create a new agent in our project using the manual configuration,

1741
01:24:19,320 --> 01:24:21,320
 and we'll call that test generator runner.

1742
01:24:21,960 --> 01:24:25,480
 We're going to go ahead and add a prompt here that we'll review a little bit later,

1743
01:24:25,480 --> 01:24:30,120
 but it's going to follow similar patterns to what we saw with the other agent that we made.

1744
01:24:30,120 --> 01:24:33,240
 We'll go ahead and specify a description for this agent,

1745
01:24:33,240 --> 01:24:37,560
 where we'll specify that it should run tests and generate them if missing.

1746
01:24:37,560 --> 01:24:43,240
 When the user asks to test or run tests, let's go ahead and make sure that this agent is dispatched.

1747
01:24:43,880 --> 01:24:48,520
 Like we saw before, instead of giving access to all tools, let's go to our advanced options.

1748
01:24:49,400 --> 01:24:53,320
 In our advanced options, we're going to go ahead and disable all of our tools,

1749
01:24:53,320 --> 01:24:57,720
 and here we'll make sure we have a bash tool, glob and grep read as well,

1750
01:24:57,720 --> 01:25:03,240
 but we're also going to need to edit and write individual files and in our case, edit files that

1751
01:25:03,240 --> 01:25:08,840
 may already exist. Once we've got these tools set up, let's move on, talk a little bit about the

1752
01:25:08,840 --> 01:25:13,800
 model we're going to be using. Just like before, we'll inherit from the parent and we'll go ahead

1753
01:25:13,800 --> 01:25:18,200
 and use yellow for this sub-agent. This looks good to us, so we'll go ahead and save it.

1754
01:25:19,080 --> 01:25:23,000
 Once we've created this agent, we also want to make sure we specify

1755
01:25:23,000 --> 01:25:27,240
 what skills are being used. In this case, the skills that we're going to be using,

1756
01:25:27,880 --> 01:25:33,400
 is the generating CLI test skill. Again, we could add multiple skills, but in this case,

1757
01:25:33,400 --> 01:25:38,600
 we're just going to use that individual one. As we saw before, we specify when it's invoked,

1758
01:25:39,240 --> 01:25:42,360
 we show how to discover tests and the output format that we want,

1759
01:25:42,920 --> 01:25:47,080
 and then some underlying rules to make sure that things are working as expected,

1760
01:25:47,080 --> 01:25:51,400
 and just like our other agent to be a little bit more generic and lean on skills to provide

1761
01:25:51,400 --> 01:25:56,520
 consistent workflows. Now that we've created our sub-agents and our skills, let's put this

1762
01:25:56,520 --> 01:26:01,800
 all together to make sure that when we add new commands, we dispatch sub-agents when necessary,

1763
01:26:01,800 --> 01:26:07,480
 using the skills that we want. Let's go ahead and start by using our code reviewer sub-agent

1764
01:26:07,480 --> 01:26:12,520
 to review the edit pi command that we made. This should not only dispatch the sub-agent,

1765
01:26:12,520 --> 01:26:17,480
 but also make use of the skill that we provided to that sub-agent. We're going to see here that

1766
01:26:17,480 --> 01:26:22,600
 the code reviewer agent has been dispatched, and now we're going to go ahead and use the necessary

1767
01:26:22,600 --> 01:26:29,080
 skills and tools that we've defined. We can see here what's working and what's not working.

1768
01:26:29,080 --> 01:26:34,840
 No critical results, but we've got some warnings, issues to fix, and suggested fixes. We can go

1769
01:26:34,840 --> 01:26:39,480
 ahead and use the main agent to implement those if we'd like. We're then going to use our test

1770
01:26:39,480 --> 01:26:45,560
 runner sub-agent to generate the tests for our edit.py command. So we'll go ahead and make sure

1771
01:26:45,560 --> 01:26:53,320
 that we're referencing the edit.py file and go ahead and dispatch the second sub-agent. We can

1772
01:26:53,320 --> 01:26:58,360
 see here it's generated the necessary commands and it's prompting me to make sure that we want to

1773
01:26:58,360 --> 01:27:04,600
 make this edit. So we'll go ahead and do so as we add tests for editing. I can confirm that the

1774
01:27:04,600 --> 01:27:09,880
 tests are working using this command uv run, and then we'll go ahead and run all of our tests with

1775
01:27:09,880 --> 01:27:15,720
 verbose mode to make sure things are passing and there are no regressions. Once this is done, we can

1776
01:27:15,720 --> 01:27:21,480
 see that all of our tests are passing, none are failing, and here's a summary as well. We made use

1777
01:27:21,480 --> 01:27:26,200
 of two different sub-agents leveraging multiple skills, and as we start to add more features and

1778
01:27:26,200 --> 01:27:31,000
 functionality, we can put these all together. The next thing we're going to do is see our code

1779
01:27:31,000 --> 01:27:37,480
 reviewer sub-agent and our test runner sub-agent in action. Let's imagine there's a clear.py file,

1780
01:27:37,480 --> 01:27:42,200
 a new command that's been added by someone on the team who hasn't followed best practices and maybe

1781
01:27:42,200 --> 01:27:47,080
 didn't use all the skills and infrastructure that we set up. We're going to go ahead and use our

1782
01:27:47,080 --> 01:27:53,080
 code reviewer sub-agent as well as our test runner sub-agent to figure out how best to fix the clear.py

1783
01:27:53,080 --> 01:28:00,440
 file. We're going to dispatch our code reviewer to review the clear.py command, and then we're

1784
01:28:00,440 --> 01:28:05,720
 going to use our test generator runner to generate the test necessary for this command. We'll validate

1785
01:28:05,720 --> 01:28:10,040
 finally that things are working as expected and make sure all the tests are passing and following

1786
01:28:10,040 --> 01:28:14,440
 the best practices that we've standardized. We can see here there are quite a few issues and

1787
01:28:14,440 --> 01:28:18,520
 some warnings. Now that we've found these issues, let's make sure that the main agent is reading the

1788
01:28:18,520 --> 01:28:23,240
 files and fixing them. We're going to want to make sure that we allow for these edits to clear.py,

1789
01:28:23,880 --> 01:28:29,160
 and here we can see things like displaying things so the console are done using the correct methods

1790
01:28:29,160 --> 01:28:33,960
 like display as mentioned in our best practices. We also want to make sure that we're registering

1791
01:28:33,960 --> 01:28:39,640
 this command correctly inside of our dunder init. The main agent itself is not adding additional

1792
01:28:39,640 --> 01:28:44,680
 context for the reviewing and generating tests. It's simply taking the output of the sub-agent

1793
01:28:44,680 --> 01:28:49,640
 to better execute these tasks. Next up, it's time to generate tests for the clear command

1794
01:28:49,640 --> 01:28:55,480
 that is following our best practices. We can see here it's adding a file to test this clear command.

1795
01:28:55,480 --> 01:29:01,080
 Let's go ahead and approve that. Now that we created this file, let's go ahead and run the tests and

1796
01:29:01,080 --> 01:29:06,120
 make sure they're working as expected, and now we can get a summary of what's been completed.

1797
01:29:06,760 --> 01:29:12,840
 Six critical issues, four warnings, and all of them fixed. Instead of using incorrect methods,

1798
01:29:12,840 --> 01:29:16,200
 instead of using flags that are not the right format that we want,

1799
01:29:16,200 --> 01:29:21,080
 incorrect exit codes, we fixed quite a few different issues. We've then added tests on

1800
01:29:21,080 --> 01:29:26,120
 top of that to make sure that we're confirming that all these best practices are done as expected,

1801
01:29:26,120 --> 01:29:31,640
 and the functionality is working that we'd like. In the next lesson, we'll shift away from Cloud Code

1802
01:29:31,640 --> 01:29:37,000
 and move to the Cloud Agent SDK and showcase how to use skills when building your own agents

1803
01:29:37,000 --> 01:29:42,520
 using the same harness that Cloud Code uses. In this final lesson, we'll create a research

1804
01:29:42,520 --> 01:29:47,880
 agent using the Cloud Agent SDK. The agent will use the skill to create a learning guide

1805
01:29:47,880 --> 01:29:53,720
 for an open source tool based on its documentation, GitHub repo, and web search. Let's go.

1806
01:29:54,520 --> 01:29:59,480
 Now that we've seen how to use skills on the web with Cloud, using the messages API

1807
01:29:59,480 --> 01:30:05,480
 and Cloud Code, let's talk about how to use skills with the Cloud Agent SDK. As a refresher,

1808
01:30:05,480 --> 01:30:11,560
 the Cloud Agent SDK is a programmatic way of building your own agent applications that use

1809
01:30:11,560 --> 01:30:16,760
 the same internal harness that Cloud Code does. What we're going to be building here is a general

1810
01:30:16,760 --> 01:30:22,280
 purpose research agent. The main agent is going to be able to research information from multiple

1811
01:30:22,280 --> 01:30:29,080
 sources and synthesize a summary. It will dispatch three different subagents for analyzing documentation,

1812
01:30:29,080 --> 01:30:34,120
 analyzing and downloading repositories, and researching information by searching the web.

1813
01:30:34,680 --> 01:30:37,880
 Let's take a look at those prompts, and then we'll take a look at a skill

1814
01:30:37,880 --> 01:30:43,000
 that's used to guide the main agent with a research methodology and what needs to be extracted and

1815
01:30:43,000 --> 01:30:48,840
 synthesized. To start, we have our main agent prompt. This is the orchestrator that has access

1816
01:30:48,840 --> 01:30:54,520
 to three available subagents with the following capabilities, finding information from documentation,

1817
01:30:54,520 --> 01:30:59,640
 analyzing repository structures, finding articles, videos, and community content to bring it all

1818
01:30:59,640 --> 01:31:05,640
 together. In this particular application, we mention that if the skill is provided, we want it to

1819
01:31:05,640 --> 01:31:11,160
 follow a particular pattern. It's possible that skills may or may not be provided for the application

1820
01:31:11,160 --> 01:31:15,880
 we're building, but in our case, we're going to provide one. If the skill matches the user's

1821
01:31:15,880 --> 01:31:21,640
 request, we need to follow that skills instructions precisely. Since we're starting from scratch with

1822
01:31:21,640 --> 01:31:27,240
 this agent application, we want to be very intentional about what to do when skills are provided, or

1823
01:31:27,240 --> 01:31:32,200
 when they're not. As we continue, we have a couple of high-level delegation guidelines for how to

1824
01:31:32,200 --> 01:31:38,440
 spawn subagents, and after receiving results, how to synthesize all of those pieces of information.

1825
01:31:38,440 --> 01:31:43,480
 Let's briefly dive into some of the prompts for our subagents. For the documentation researcher,

1826
01:31:43,480 --> 01:31:48,760
 we'll have access to web search and web fetch. We provide a process to locate documentation,

1827
01:31:48,760 --> 01:31:54,440
 particular input formats, guidelines, and an output to return findings in a certain way. For

1828
01:31:54,440 --> 01:31:59,720
 the repository analyzer, we also provide web search to find repositories, bash commands to clone and

1829
01:31:59,720 --> 01:32:06,280
 run Git, and then the ability to read and find files and data within files. Similarly, we provide

1830
01:32:06,280 --> 01:32:12,600
 a process and input format, guidelines, and an output. Finally, our web researcher makes use of

1831
01:32:12,600 --> 01:32:17,960
 web search and web fetch as well. This allows us to search for content relevant to that topic,

1832
01:32:17,960 --> 01:32:23,720
 and to receive extraction instructions as well from the main agent. We also provide guidelines,

1833
01:32:23,720 --> 01:32:29,000
 as well as an output format that's necessary, and if no output format is specified, follow a

1834
01:32:29,000 --> 01:32:33,880
 default structure. All of these prompts will be used together when we set up the code necessary

1835
01:32:33,880 --> 01:32:39,000
 to make our agent work. Finally, let's talk about the skill we're going to be using here.

1836
01:32:39,000 --> 01:32:45,640
 We have a skill named Learning A Tool. The purpose of this skill here is to guide the main orchestrator.

1837
01:32:45,640 --> 01:32:51,320
 We will not be using this skill in our individual subagents, but we're using this skill as a way

1838
01:32:51,320 --> 01:32:56,920
 to create a predictable pattern so that the main agent knows the ideal workflow and what and how

1839
01:32:56,920 --> 01:33:02,040
 to dispatch subagents. We give the skill a name and a description, and in this case, we want to

1840
01:33:02,040 --> 01:33:06,680
 create learning paths for programming tools to find what information should be researched

1841
01:33:06,680 --> 01:33:12,120
 and specify how best to follow an approach to researching all the way towards creating a

1842
01:33:12,120 --> 01:33:17,720
 comprehensive learning path. To start, we have a very particular workflow that we have here.

1843
01:33:17,720 --> 01:33:21,720
 We start with a research phase, and we specify for official documentation

1844
01:33:21,720 --> 01:33:28,360
 for that subagent exactly what to look for. For the repository analyzer, a similar kind of approach,

1845
01:33:28,360 --> 01:33:34,360
 and for our web researcher, very similar as well. So we're using this skill to provide a constant

1846
01:33:34,360 --> 01:33:39,240
 and predictable workflow for how best to work alongside the subagents that the main agent has.

1847
01:33:39,960 --> 01:33:45,320
 Once that data is given to us, we then organize that content into progressive levels.

1848
01:33:45,320 --> 01:33:50,120
 Here, we're using progressive disclosure to lean into loading another markdown file

1849
01:33:50,120 --> 01:33:54,520
 as the source of truth. In our progressive learning file, we can see there's quite a bit

1850
01:33:54,520 --> 01:33:59,640
 around the individual levels that we want. Starting from an overview and motivation

1851
01:33:59,640 --> 01:34:04,040
 all the way towards installing core concepts, practical patterns, and then where to go next.

1852
01:34:04,680 --> 01:34:09,960
 This progressive learning allows us to build levels so that we know how to start from the beginning

1853
01:34:09,960 --> 01:34:15,400
 and know eventually where to go deeper. While this initial skill is useful for learning a tool,

1854
01:34:15,400 --> 01:34:20,440
 you can also imagine that we might have additional skills for maybe comparing one tool with another

1855
01:34:20,440 --> 01:34:25,640
 depending on the data that we're working with. As we move towards the additional phases of working

1856
01:34:25,640 --> 01:34:31,720
 with this skill, we take that data and specify a structure and then specify an output. We're

1857
01:34:31,720 --> 01:34:37,160
 very, very particular with the exact format that we're working with. The goal here is to get access

1858
01:34:37,160 --> 01:34:43,160
 to a learning environment that gives us an overview, resources, a path, and code examples.

1859
01:34:43,160 --> 01:34:47,640
 The goal here is to combine the research from all of our subagents into a particular output

1860
01:34:47,640 --> 01:34:53,480
 format that we want and do that with consistency and predictability. Now that we've seen at a high

1861
01:34:53,480 --> 01:34:57,720
 level of the application we're going to build, there's one last piece that we'll layer on.

1862
01:34:57,720 --> 01:35:02,520
 We can imagine that we want to take the output and write it to a centralized place that we can

1863
01:35:02,520 --> 01:35:06,360
 share with teammates that might have a nicer interface. And to do that, we're going to use

1864
01:35:06,360 --> 01:35:11,960
 Notion. To connect to Notion, we're going to use an MCP server and bring in the tools necessary

1865
01:35:11,960 --> 01:35:17,480
 to go ahead and execute that. Now that we've examined the underlying prompts for our main agent

1866
01:35:17,480 --> 01:35:22,040
 and subagents, as well as the skill we're going to be using, let's go ahead and begin

1867
01:35:22,600 --> 01:35:28,280
 by running UV in it and initialize a project and add the necessary dependencies like Cloud

1868
01:35:28,280 --> 01:35:36,200
 Agent SDK, Python.env, and async.io. Once we've installed these dependencies, let's go ahead and

1869
01:35:36,200 --> 01:35:41,800
 create a file called agent.py. So I'll go ahead and make a new file called that agent.py.

1870
01:35:42,920 --> 01:35:48,520
 Inside of our agent.py, I'm going to be adding the necessary code to just get started with a small

1871
01:35:48,520 --> 01:35:56,440
 example using the Cloud Agent SDK. The boilerplate here brings in async.io to run this environment,

1872
01:35:56,440 --> 01:36:02,360
 .env to load environment variables, and then from our utils, the display message function.

1873
01:36:03,080 --> 01:36:08,600
 Just to give some context, display message gives us a bunch of helpers for truncating and formatting

1874
01:36:08,600 --> 01:36:13,880
 input, and it gives us a nice way to visually display information from the main agent and the

1875
01:36:13,880 --> 01:36:19,400
 subagent. This is very similar code to what we saw when we worked with the API, and we got that

1876
01:36:19,400 --> 01:36:23,080
 nice output for what's happening in each tool action and iteration.

1877
01:36:25,640 --> 01:36:31,240
 To start, we set up our Cloud Agent. We pass in a system prompt here. This is going to change.

1878
01:36:31,800 --> 01:36:35,720
 We pass in allowed tools. This is also going to change, but we just want to start with the basics

1879
01:36:35,720 --> 01:36:42,040
 here. To get started with a simple conversation, we set up a loop, accept some user input,

1880
01:36:42,920 --> 01:36:47,480
 run that through our model, and take back the response, and send that back to the user.

1881
01:36:47,480 --> 01:36:50,520
 Let's go and see what that looks like. I'm going to open the terminal again,

1882
01:36:51,480 --> 01:36:57,320
 and we're going to go ahead and run uvrun agent.py. This is going to provide a terminal

1883
01:36:57,320 --> 01:37:02,440
 environment to us where we can start a conversation. I'll just start by asking, how are you?

1884
01:37:03,320 --> 01:37:06,280
 In this case, I'm not going to get a ton of valuable information here,

1885
01:37:06,280 --> 01:37:10,680
 because I just have a helpful assistant. So what we're going to start layering on now

1886
01:37:10,680 --> 01:37:17,000
 is the ability for our agent to get access to MCP servers and the correct tools as well.

1887
01:37:17,640 --> 01:37:22,120
 Let's go ahead and make some modifications to our main function. Like we mentioned,

1888
01:37:22,120 --> 01:37:27,480
 the allowed tools are going to change. So what we're going to start doing is adding the tools

1889
01:37:27,480 --> 01:37:33,960
 that our subagents need to use so that they can be working as expected. Read only tools like reading,

1890
01:37:33,960 --> 01:37:38,920
 grep, and glob are allowed by default, but when we want to start doing things like writing files,

1891
01:37:38,920 --> 01:37:43,400
 searching the web, and executing commands by bash, we need to pass that in explicitly.

1892
01:37:43,960 --> 01:37:50,120
 So we'll bring in the write tool, the bash tool, and our web search and web fetch tools.

1893
01:37:52,280 --> 01:37:56,760
 We saw previously that our subagents are going to be making use of these particular tools.

1894
01:37:56,760 --> 01:38:01,640
 Our agent that's analyzing repositories needs bash to run git commands and writing files,

1895
01:38:01,640 --> 01:38:05,400
 and our docs researcher and web researcher will make use of searching and fetching.

1896
01:38:05,960 --> 01:38:11,160
 Now that we brought in these tools, the next thing we're going to add are MCP servers to connect to.

1897
01:38:11,800 --> 01:38:17,800
 We'll use the MCP server's keyword argument and specify the name of the MCP server, which in our

1898
01:38:17,800 --> 01:38:23,960
 case is Notion. We're going to pass in some default configuration, and we're going to specify the

1899
01:38:23,960 --> 01:38:30,680
 command to run the Notion server alongside a Notion environment variable that we have.

1900
01:38:30,680 --> 01:38:37,240
 So we're going to make sure before we go ahead from our .env file, load in our Notion token,

1901
01:38:37,240 --> 01:38:41,560
 and import the OS module to make sure that we can read that file correctly.

1902
01:38:42,120 --> 01:38:46,680
 Now that we've loaded our MCP server correctly, we need to make use of the tools that Notion

1903
01:38:46,680 --> 01:38:52,280
 provides. If we would like, we can ask Claude right now what are all the tools that you get

1904
01:38:52,280 --> 01:38:59,720
 from this MCP server, or we can go ahead and add those explicitly by using MCP, the name of our

1905
01:38:59,720 --> 01:39:04,760
 server followed by the name of the tool. In this case, we're going to be using all of the tools

1906
01:39:04,760 --> 01:39:11,800
 that Notion provides to us. We need to make sure that this MCP Notion exists in allowed tools so that

1907
01:39:11,800 --> 01:39:17,160
 we can give the main agent permission to use this set of tools. We can explicitly add the name of

1908
01:39:17,160 --> 01:39:21,800
 the tool, or in our case, we're just going to include all the tools available that MCP Notion

1909
01:39:21,800 --> 01:39:27,320
 provides to us. Now that we've set up our MCP servers and our allowed tools, let's go ahead and

1910
01:39:27,320 --> 01:39:33,160
 bring in our subagents and definitions for them. We mentioned that our system prompt is going to

1911
01:39:33,160 --> 01:39:38,760
 change, and to start, we're going to go ahead and load all of the prompts that we have. We'll bring

1912
01:39:38,760 --> 01:39:45,720
 in a constant and a helper function that we have to load all of these prompts. We're going to go

1913
01:39:45,720 --> 01:39:51,640
 ahead and call that function to go ahead and bring in these prompts inside of our main function.

1914
01:39:51,640 --> 01:39:56,280
 We're going to make use of these markdown files to load in the text necessary

1915
01:39:56,280 --> 01:40:01,320
 and pass them to our agent options. Before we go ahead and update the main agent,

1916
01:40:01,320 --> 01:40:06,760
 we're going to add a dictionary that references all of our agents with a definition. We're bringing

1917
01:40:06,760 --> 01:40:12,120
 in the agent definition class, which we'll want to make sure we import correctly. We can see in

1918
01:40:12,120 --> 01:40:16,680
 the agent definition, we have a description for our subagent, a prompt that specifies the

1919
01:40:16,680 --> 01:40:22,600
 instructions for the agent, and then the tools that we want that agent to use. Similar configuration

1920
01:40:22,600 --> 01:40:28,120
 to what we did in Cloud Code. You can see here, we still need to use our main agent prompt as well

1921
01:40:28,120 --> 01:40:34,360
 as this dictionary of agents. So we'll update our system prompt with the main agent prompt,

1922
01:40:35,000 --> 01:40:39,880
 and then we'll make sure to pass in an additional keyword argument of agents that references our

1923
01:40:39,880 --> 01:40:46,120
 dictionary with our agent definitions. As you can see here, our researcher, our analyzer,

1924
01:40:46,120 --> 01:40:52,920
 and our web researcher are using tools that we've defined here as well. It's important to make sure

1925
01:40:52,920 --> 01:40:58,120
 that you list all of the tools that your main agent and your subagents will need to use inside

1926
01:40:58,120 --> 01:41:03,320
 of your allowed tools, or else your subagents will not allow them, even if you include the tools here.

1927
01:41:04,280 --> 01:41:09,720
 Now that we've set up our agents, we need to make sure we also include the all-important task tool

1928
01:41:09,720 --> 01:41:14,760
 to make sure that we can dispatch subagents and assign tasks to them. The last piece we need to

1929
01:41:14,760 --> 01:41:20,120
 add here are skills. And the good news is, in order to add skills, there's just one more tool

1930
01:41:20,120 --> 01:41:25,240
 that we need to add, and that is the skill tool. Since we have an environment here where there's a

1931
01:41:25,240 --> 01:41:31,240
 file system and the ability to execute code using the bash tool, all we need to add is this skill

1932
01:41:31,240 --> 01:41:36,760
 tool so that we can correctly read skills and understand how best to use them. Similar to Cloud

1933
01:41:36,760 --> 01:41:43,400
 Code, skills are defined inside of the dot-cloud folder followed by a folder called skills. Make

1934
01:41:43,400 --> 01:41:49,720
 sure your markdown files are skill.md and your folder is called skills in the plural. Now that

1935
01:41:49,720 --> 01:41:54,760
 we've added the tool for working with skills, there's one more keyword argument that we need

1936
01:41:54,760 --> 01:42:01,080
 to pass in here. We need to specify where we find this particular set of skills, and we do so with

1937
01:42:01,080 --> 01:42:06,920
 a keyword argument called setting sources. And here we're going to specify that we want to find skills

1938
01:42:06,920 --> 01:42:13,160
 inside of the user directory, if we have skills in our home directory, as well as project, which

1939
01:42:13,160 --> 01:42:18,520
 is where we've loaded the skills for this particular application. Now that we put this all together,

1940
01:42:18,520 --> 01:42:23,720
 let's go ahead and test out our agent. I'm going to open up the terminal again. I'm going to go ahead

1941
01:42:23,720 --> 01:42:28,840
 and exit, and let's run this application again with the changes that we've made. We're going to

1942
01:42:28,840 --> 01:42:35,000
 start by learning a little bit about minor U. For those of you not familiar, minor U is an open library

1943
01:42:35,000 --> 01:42:40,120
 for PDF extraction. And the reason we're using this example is because this is not something that

1944
01:42:40,120 --> 01:42:45,640
 Claude might know a ton of from its initial training data. This is going to require external research,

1945
01:42:45,640 --> 01:42:51,400
 analyzing code repositories, community documents, and other sources. We're going to ask to create a

1946
01:42:51,400 --> 01:42:56,440
 learning guide, and then show me the plan first. Here, we're going to start to see that the skill

1947
01:42:56,440 --> 01:43:01,320
 is invoked, and the input here is that skill called learning a tool with the arguments that

1948
01:43:01,320 --> 01:43:07,640
 we specified. So here, we can see that we first specified the plan. We still have to go ahead and

1949
01:43:07,640 --> 01:43:12,600
 run what the subagents are going to do. But just like with Claude code and plan mode, we might want

1950
01:43:12,600 --> 01:43:17,880
 to see what the plan is before we start acting and consuming tokens and taking time. We can see the

1951
01:43:17,880 --> 01:43:23,000
 research phase of parallel investigation with our different researchers. We can see the structure

1952
01:43:23,000 --> 01:43:29,000
 necessary according to the skill. And then finally, the output that we're expecting. This looks like

1953
01:43:29,000 --> 01:43:34,360
 a good plan. So we'll just go ahead and ask it to proceed. It's going to start by spawning the

1954
01:43:34,360 --> 01:43:40,440
 docs research subagent, spawning the repo analyzer and web researcher, and executing these in parallel,

1955
01:43:41,000 --> 01:43:46,120
 using the tools that we've added under the allowed tools that we've also passed in to our

1956
01:43:46,120 --> 01:43:51,320
 subagents. We can see in parallel, the docs researcher is heading to the documentation,

1957
01:43:51,320 --> 01:43:56,600
 the repo analyzer is looking on GitHub, and the web researcher is searching across tutorials

1958
01:43:56,600 --> 01:44:02,120
 and YouTube guides. We're extracting the information from GitHub repositories using the bash commands,

1959
01:44:02,120 --> 01:44:06,920
 while at the same time, searching a YouTube channel for video demonstrations. These agents

1960
01:44:06,920 --> 01:44:11,960
 are interacting in parallel, fetching from different data sources to bring this all together into a

1961
01:44:11,960 --> 01:44:17,480
 compelling tutorial. Now that the subagents have finished completing their work, we're going to

1962
01:44:17,480 --> 01:44:22,520
 create the comprehensive guide, pull together all the necessary files based on this research

1963
01:44:22,520 --> 01:44:28,840
 that we have here. As instructed in the repository analyzer, we've cloned the repository for minor

1964
01:44:28,840 --> 01:44:33,880
 u and keeping that here, and we've started to build the folder structure for learning this.

1965
01:44:33,880 --> 01:44:38,920
 We can see here, we have our readme and resources, as well as code examples that are being put together.

1966
01:44:39,640 --> 01:44:44,920
 We can see here in the readme file, it provides the learning path to us, what we're going to learn,

1967
01:44:44,920 --> 01:44:50,200
 how to use this guide, and importantly, time estimates that we might need. We can see here,

1968
01:44:50,200 --> 01:44:55,320
 it's created for us, the readme, the resources, and the learning path is still in progress.

1969
01:44:55,320 --> 01:45:00,120
 Inside of our resources, we have links and references for minor u, so let's take a look at that.

1970
01:45:01,000 --> 01:45:06,360
 Inside of our resources, we have documentation, the repository, the pie-pie package, and the paper

1971
01:45:06,360 --> 01:45:10,600
 underlying this library. We have quick start guides, documentation, and related projects.

1972
01:45:11,320 --> 01:45:16,360
 As we pull in additional information from the community, we have all kinds of deep dives across

1973
01:45:16,360 --> 01:45:21,640
 a variety of different articles and news coverage. Now we can see that the learning path has been

1974
01:45:21,640 --> 01:45:27,480
 created, and it's time to create the code examples. Let's take a look at this learning path.

1975
01:45:28,760 --> 01:45:33,800
 Starting with an overview and motivation, what problem does it solve? We describe the origin

1976
01:45:33,800 --> 01:45:38,840
 story of the library, what existed before, and some of the problems with those libraries.

1977
01:45:38,840 --> 01:45:42,920
 We can see here, this is quite an in-depth guide and learning path, and you can imagine,

1978
01:45:42,920 --> 01:45:47,480
 this is something that would last a long time as you start to get up to speed, knowing very little,

1979
01:45:47,480 --> 01:45:52,200
 to becoming an expert in working with this library. We move into some of the distinct

1980
01:45:52,200 --> 01:45:57,400
 features of the back end of this library, all the way to code examples, and many different

1981
01:45:57,400 --> 01:46:02,920
 characteristics for how to use this as efficiently as possible. We can start to see that our code

1982
01:46:02,920 --> 01:46:09,400
 files are being written for Hello World examples, concepts, and patterns. For our Hello World example,

1983
01:46:09,400 --> 01:46:14,520
 we've got a nice readme to get started with some first steps, simple extraction to see how to start

1984
01:46:14,520 --> 01:46:19,560
 using this library as well as installation steps. If there were particular libraries we wanted to

1985
01:46:19,560 --> 01:46:24,120
 use for installing or patterns here, we could always add that to our skill, but right now,

1986
01:46:24,120 --> 01:46:27,320
 this is going to give us a great start to get up and running with this library.

1987
01:46:28,520 --> 01:46:32,760
 As we look at some of the core concepts, those are being created currently. Now that those are

1988
01:46:32,760 --> 01:46:37,640
 done, we can see in the readme where we go next. Once we've gotten up and running with the library,

1989
01:46:37,640 --> 01:46:42,200
 we can start to look at some of the fundamental concepts that the library possesses, as well as

1990
01:46:42,200 --> 01:46:47,640
 comparing different speeds across back ends. Finally, we're going to create practical patterns and

1991
01:46:47,640 --> 01:46:53,480
 examples with this third folder. We can take a look at this folder, and we can see here that we

1992
01:46:53,480 --> 01:46:58,440
 have real-world processing pipelines and production use cases. This includes examples for certain

1993
01:46:58,440 --> 01:47:05,160
 patterns, as well as quite in-depth code examples using this library with dock strings, comments,

1994
01:47:05,160 --> 01:47:10,840
 and everything necessary to use this library to its fullest extent. We'll wrap up by validating

1995
01:47:10,840 --> 01:47:15,480
 and creating a summary document, making sure everything has been done correctly. We can take

1996
01:47:15,480 --> 01:47:20,120
 a look at the output, which gives us a complete learning guide, the directory structure as specified

1997
01:47:20,120 --> 01:47:25,720
 in our skill, the learning path with the levels that we requested, and then key features and a quick

1998
01:47:25,720 --> 01:47:31,720
 start to get up and running. The final thing we're going to do here is write this particular file,

1999
01:47:31,720 --> 01:47:37,960
 the resources MD, to a resources sub-page in Notion. This page already exists, so let's take a look

2000
01:47:37,960 --> 01:47:42,520
 at what that looks like, and then we'll prompt to go ahead and use our MCP server to do the writing

2001
01:47:42,520 --> 01:47:48,520
 necessary. We can see here in Notion, under this learning section, I have a sub-page called

2002
01:47:48,520 --> 01:47:54,680
 resources. The goal here is to use the MCP server to populate what we had in our resources MD to

2003
01:47:54,680 --> 01:48:01,480
 this right here. So let's go ahead and ask our agent to write that file to that sub-page in Notion.

2004
01:48:03,240 --> 01:48:07,240
 We're going to be explicit with the tools that we use in Notion and allow it to use what we have

2005
01:48:07,240 --> 01:48:12,920
 available. We found the resources page, we're going to read the resources MD, and convert it to the

2006
01:48:12,920 --> 01:48:18,680
 correct format in Notion using rich Notion blocks. You can see here we're using multiple tools from

2007
01:48:18,680 --> 01:48:23,880
 Notion, doing this in batches, adding the quick start guide's ebi documentation, and the rest

2008
01:48:23,880 --> 01:48:30,680
 of the information inside of our resources MD. We can see here in the resources file, it's dynamically

2009
01:48:30,680 --> 01:48:36,680
 updating based on the documentation in our resources MD. As this finishes up, we're going to see all

2010
01:48:36,680 --> 01:48:42,040
 the content from that file appear on our Notion page. Now that it's finished, let's go take a look

2011
01:48:42,040 --> 01:48:46,840
 at what our Notion page looks like. We can see here we've got our official documentation,

2012
01:48:46,840 --> 01:48:51,320
 our tutorials, video resources, community channels, all the data that came from that

2013
01:48:51,320 --> 01:48:58,360
 markdown file we've now written to Notion. We made use of skills, MCP servers, agents, and sub-agents

2014
01:48:58,360 --> 01:49:04,440
 all using the agent SDK. You can imagine layering on additional skills for more complex workflow

2015
01:49:04,440 --> 01:49:09,880
 or additional sub-agents to perform a variety of tasks. We've just started to scratch the surface

2016
01:49:09,880 --> 01:49:14,200
 with functionality, and there's still some security concerns that we should be mindful of.

2017
01:49:14,200 --> 01:49:20,040
 For starters, we're allowing commands like write and bash to be executed without requiring permission

2018
01:49:20,040 --> 01:49:25,480
 from the user. The next step here is to build an interface, just like Cloud Code, that ensures

2019
01:49:25,480 --> 01:49:31,320
 that we allow the user to confirm that they want to use those particular tools for a certain action.

2020
01:49:31,320 --> 01:49:35,640
 We've also just started to scratch the surface with the ability to even add things like interrupts

2021
01:49:35,640 --> 01:49:41,000
 for our agents and sub-agents similar to Cloud Code. So we've given you the foundation to continue

2022
01:49:41,000 --> 01:49:44,840
 to build powerful, agentic applications, and we can't wait to see what you build next.

2023
01:49:45,560 --> 01:49:49,800
 Congratulations on making it this far. You've learned how to create skills,

2024
01:49:49,800 --> 01:49:53,800
 explored their best practices, and seen them in action across different platforms.

2025
01:49:54,440 --> 01:49:59,240
 When creating a skill, start with basic markdown instructions, then expand later

2026
01:49:59,240 --> 01:50:04,760
 following progressive disclosure. Monitor how your agent uses your skill in real scenarios

2027
01:50:04,760 --> 01:50:10,120
 and iterate based on observations. Make sure the description contains enough detail for your agent

2028
01:50:10,120 --> 01:50:15,240
 to know when to use it. And don't forget, Cloud is very knowledgeable about what skills are,

2029
01:50:15,240 --> 01:50:19,320
 so you can always start with a simple conversation to begin creating skills,

2030
01:50:19,320 --> 01:50:23,000
 and then use the skill creator skill to follow best practices.

2031
01:50:23,000 --> 01:50:27,400
 Thank you for joining me in this journey, and I can't wait to see what you build with agent skills.
