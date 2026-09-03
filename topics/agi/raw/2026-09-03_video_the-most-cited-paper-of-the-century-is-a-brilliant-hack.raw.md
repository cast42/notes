---
type: video
source_url: "https://youtu.be/QgH9sr7G13Q?is=HRwIgmb_8kYsW704"
canonical_url: "https://youtube.com/watch?v=QgH9sr7G13Q"
title: The most cited paper of the century is a brilliant hack
author: Welch Labs
created_at: 2026-09-03
topics: [agi]
tags: [resnet, residual-stream, neural-network-architecture, deep-learning]
timestamp: 2026-09-03
resource: "https://youtube.com/watch?v=QgH9sr7G13Q"
description: "Timestamped transcript captured from Welch Labs’ explanation of ResNet, residual streams, and register tokens."
content_hash: 3ea8c339942facaf6075aabee828805ad4bc321047ad68c51786e6486410123a
extracted_at: "2026-09-03T06:47:47"
extractor: youtube-transcript-api+oembed
---

# Raw content

Source: https://youtube.com/watch?v=QgH9sr7G13Q


[0.1] In early 2015, the relatively new field
[3.0] of deep learning got stuck. The field's
[5.9] namesake and main driver of progress,
[8.6] making models deeper, stopped working.
[11.6] Once researchers reached models between
[13.8] 20 and 30 layers deep, performance gains
[16.8] stalled out [music] and then actually
[19.0] reversed. Here's a 74 layer model being
[22.3] outperformed by an eight layer model.
[25.1] The solution to this problem turned out
[27.1] to be a shockingly simple idea.
[29.4] Originally published in this 12-page
[31.7] paper in December 2015 that has gone on
[34.6] to become the most cited paper of the
[36.6] 21st century.
[38.7] The impact of this simple idea is
[40.7] difficult to overstate.
[43.0] The discovery forced the field to
[44.8] completely reconceptualize how these
[47.0] models work. coming to the realization
[49.5] that this simple idea actually formed a
[51.8] new critical backbone for neural
[53.8] networks, a kind of working memory that
[57.1] ultimately enabled these models to reach
[59.0] unprecedented levels of performance.
[64.2] Giansoon's research team at Microsoft
[66.4] Research Asia was stuck. A few years
[69.1] earlier in 2012, the AlexNet paper
[71.4] kicked off the deep learning revolution,
[73.8] demonstrating an eight- layer
[75.0] convolutional neural network that
[76.7] significantly outperformed all previous
[78.8] methods on the imageet image
[80.4] classification challenge. In 2014, teams
[84.2] at Oxford and Google successfully
[86.0] trained deeper models with 19 and 22
[89.2] layers respectively, significantly
[91.4] improving on the original Alexet
[93.4] results. And in early 2015, Sunn's
[96.4] research group had made a real
[97.8] breakthrough careful parameter
[100.0] initialization. They reached an
[102.0] unprecedented depth of 30 layers. Here's
[105.4] a training plot from their paper,
[107.5] showing that using a then standard
[109.2] Xavier initialization approach. Their 30
[112.2] layer model completely failed to learn.
[114.8] The model's error rate just stays fixed
[116.6] at 100%. But when the team switched to
[119.6] their newly proposed initialization
[121.4] approach, now known as HU
[123.3] initialization,
[124.8] the model was actually able to learn,
[127.1] bringing down its error rate. However,
[130.0] while the team's new deeper models were
[131.9] able to learn, the final performance of
[134.6] these models was surprisingly poor.
[137.8] This 30 layer model only reached a
[139.8] 16.59%
[141.7] error rate while the team's 14 layer
[144.3] model using a similar architecture
[146.3] achieved a superior error rate of
[148.1] 13.34%.
[151.0] This result is especially confounding
[153.5] because as the team would later note
[155.6] there's an essentially trivial solution
[157.4] that we can obtain by construction where
[160.0] the 30 layer model would achieve at
[161.6] least the same performance as the 14
[163.8] layer model. If we take the first 14
[166.9] layers of our smaller trained model and
[169.4] add 16 pass through layers where each
[172.4] layer simply passes its input to its
[174.3] output unchanged, the 30 layer model
[177.3] would produce exactly the same final
[179.0] outputs as our 14 layer model. The
[182.4] layers in the team's models were
[183.8] perfectly capable of performing this
[185.4] identity mapping. So if the 30 layer
[188.1] model was capable of achieving at least
[189.8] the same performance as the 14 layer
[192.0] model, then why couldn't the team's
[194.1] optimizers find these solutions?
[197.8] Let's trace the flow of information
[199.4] through one of these shallower networks
[201.8] and see if we can figure out exactly
[203.4] what breaks down as we add more layers.
[206.3] In mid 2015, as the team puzzled over
[209.3] these results, the state-of-the-art deep
[211.7] learning architecture was the
[212.9] convolutional neural network. In
[215.8] convolutional networks, images are
[218.1] processed by sliding a window of
[219.8] learnable weights across the image and
[222.1] at each position computing the
[223.5] dotproduct between the image pixel
[225.8] intensity values and the learned weight
[227.7] kernel. This dotproduct operation will
[230.6] return large values when our kernels and
[233.1] image patches are similar. Here's a
[235.7] learned vertical edge detector kernel
[238.1] returning large activation values when
[241.0] passing over vertical edges in the
[242.6] image. The first layer of our network
[245.3] uses 64 different learned kernels,
[248.2] resulting in 64 new activation maps,
[251.8] each responding to various features in
[253.8] our image, such as different edge
[255.8] orientations or colors.
[258.3] From here, these 64 activation maps are
[260.6] stacked into a 64x 112x 112 tensor of
[264.5] activations.
[266.2] These activations form a new sort of
[268.2] image. But where our input image has
[270.9] red, green, and blue color channels, our
[273.4] activation tensor has 64 channels, each
[276.6] corresponding to a different type of
[278.3] image feature.
[280.3] Our activations are scaled and passed
[282.2] into a RLU activation function, which
[284.9] sets all values less than zero to zero.
[288.2] Note that here we're not showing values
[290.1] below a certain threshold to make our
[292.6] activations easier to see. These three
[295.8] steps, the sliding kernel convolution,
[298.5] scaling, and the RLU activation function
[300.6] form a single layer of our model.
[304.0] Our activations are then passed into a
[305.9] second convolutional layer where we
[308.3] slide a new set of learned kernels over
[310.4] our activation tensor, producing a new
[313.0] activation tensor of dimension 64x 56 x
[316.4] 56. Just as in our first layer, this
[319.7] tensor is again passed through a scaling
[321.6] step and a RLU activation function.
[325.2] These sliding kernel scaling and
[327.0] activation steps are repeated again and
[329.0] again with a down sampling step every
[331.6] few layers until we're left with an
[333.8] activation tensor of dimension 256x
[336.7] 14x4.
[338.8] This tensor is downsampled one final
[341.0] time to a 256x1
[343.4] vector of activations.
[346.0] These 256 numbers are then multiplied by
[348.9] a final matrix of learned weights of
[351.4] dimension 256 by a th00and resulting in
[354.9] a thousand numbers where each number
[357.4] corresponds to the model's confidence in
[359.3] each of the a thousand classes in the
[361.0] imageet data set. If we plot these final
[364.4] a thousand numbers, we see that index
[367.0] 951 has the largest value. This index
[371.0] corresponds to lemon in the imageet
[373.0] labeling scheme, meaning that our model
[375.4] has correctly classified this image.
[379.1] Our model currently has eight total
[381.2] layers and achieves an accuracy of 44.1%
[384.7] on the imageet validation data set. As
[388.0] we've seen, it correctly classifies this
[389.8] lemon, but it mclassifies this rocking
[392.5] chair, safe, and screwdrivers.
[395.5] Now, just as the Oxford and Google teams
[397.7] did in 2014,
[399.5] let's add more layers to our model and
[401.9] see if we can improve performance.
[404.3] Adding layers to our convolutional
[405.9] architecture is a surprisingly simple
[407.9] affair. We just need to choose where to
[410.2] place them within our model. Let's add
[412.6] six new layers. Two in this first block
[415.4] of layers and four after our final
[417.8] convolutional block.
[420.5] These new layers perform the same exact
[422.5] sliding dot product, scaling, and RLU
[424.9] operations as their neighbors, just with
[427.4] different learned weights.
[429.8] Now, let's visualize the accuracy of our
[432.2] new deeper 14 layer model as it learns
[435.4] and compare these results to our
[436.9] shallower eight layer model. After
[439.4] 40,000 steps, our deeper model performs
[442.2] significantly better, reaching an
[444.6] accuracy of 56.7% on the imageet
[447.6] validation set.
[449.7] Now, as Giann's team did in early 2015,
[453.1] let's add even more layers and see if we
[455.9] can continue improving performance.
[459.0] At 20 layers, we get this training
[461.1] curve, only reaching an accuracy of
[463.5] 53.1% after the same 40,000 training
[466.8] steps.
[468.3] Now, note that our accuracy curve hasn't
[470.4] really leveled off yet, and deeper
[472.6] models with more parameters may require
[474.8] more training steps.
[477.3] Training our 20 layer model for 20,000
[479.7] more steps, we're able to reach a higher
[482.3] image net accuracy of 62.5%.
[486.2] Pushing to 26 layers and training a bit
[488.6] longer, we see a modest improvement to
[491.0] 63.6%.
[493.4] At 34 layers, though, our luck starts to
[495.9] run out. Even after 80,000 training
[499.0] steps, we only reach an accuracy
[501.3] slightly below our 26 layer model at
[504.2] 62.8%.
[506.8] If we add even more layers, the trend
[509.4] amplifies with this 56 layer model only
[512.9] reaching an accuracy of 56.6%.
[516.7] And this 74 layer model getting stuck at
[519.4] an accuracy of just 38.9%.
[522.9] This is worse performance than our
[524.3] dramatically smaller eight layer model.
[527.6] This is the same performance degradation
[529.4] problem that Soon's team found.
[532.7] Why does adding more layers no longer
[534.9] help? and actually start making things
[537.0] worse.
[538.6] Soon's team speculated in early 2015
[541.5] that this could just be a fundamental
[543.2] limitation of neural networks, writing,
[546.3] this is perhaps because the method of
[548.0] increasing depth is not appropriate.
[551.5] Let's take a closer look at our
[553.0] shallower eight layer model and see if
[555.5] we can figure out exactly where things
[557.4] go wrong. This model has 1.45 million
[560.9] learnable parameters spread across its
[563.4] eight layers. Let's consider one of the
[565.8] images our model got wrong earlier. When
[568.6] we pass this image of these long
[570.6] screwdrivers into our shallow eight
[572.5] layer model, our model only returns a
[575.0] probability of 0.056
[577.2] for the correct label of screwdriver.
[580.0] The model's maximum output probability
[581.9] is 0.09
[583.7] at index 623
[586.0] corresponding to the class for letter
[587.8] opener.
[589.4] Note that here we're plotting our
[590.7] model's outputs after a final softmax
[593.0] operation. which scales our final
[595.4] activations into nice probabilities that
[597.4] all add up to one. Now, the whole point
[600.8] of training is to adjust our model's
[603.2] millions of parameters to increase the
[605.2] model's predicted probability of the
[606.9] correct answer. Let's focus for a moment
[609.8] on just one parameter in our model's
[612.1] final layer. Our parameter's current
[614.7] value is 0.215.
[618.2] Let's explore a range of values for this
[620.2] single parameter. Starting by setting
[622.5] our parameter to a large negative value
[625.0] of minus2.5.
[627.5] This change pushes down the model's
[629.5] probability of the correct answer to
[631.4] essentially zero. Increasing our
[633.7] parameter's value, our model slowly
[635.9] becomes more confident in the correct
[637.6] answer of screwdriver.
[639.7] And by the time our parameter reaches
[641.4] positive 2.5, our model's probability of
[644.5] the correct label is almost 100%. We can
[647.6] plot our model's confidence in the
[649.1] correct label as a function of the value
[651.1] of the single parameter and see that
[653.6] large values of our parameter cleanly
[655.7] lead to higher probabilities of the
[657.5] correct answer in this case. Now, we of
[660.5] course can't train our model just by
[662.2] tuning one parameter. And this parameter
[665.0] happens to be connected directly to the
[666.7] model's output for the screwdriver
[668.6] class. How does this picture change as
[671.2] we move to earlier layers in our model?
[673.7] Here are the curves for a few parameters
[675.5] in the middle of our model. Here, the
[678.2] relationship between our parameters and
[679.8] the model's outputs becomes more
[681.7] complex. We can see that as we sweep
[684.3] through these parameters, the model's
[685.8] output probabilities change in less
[687.8] predictable ways.
[690.2] Now, note that these curves are
[691.9] intimately connected to how our model
[694.0] actually learns. While it's
[696.2] computationally infeasible to compute
[698.1] curves like this for all 1.45 45 million
[700.6] parameters. Remarkably, we can
[703.0] efficiently compute the slopes of all
[705.1] 1.45 million curves using back
[707.6] propagation. This collection of slopes
[709.8] is known as the gradient and it guides
[711.9] the entire learning process.
[715.0] Let's look at the curve for one more
[716.6] parameter. This time in the very first
[719.1] layer of our model. Here, the mapping
[721.6] between our parameter and the model's
[723.2] probability of the correct label becomes
[725.1] even more complex. The output of this
[727.9] first layer is modified by the millions
[730.2] of parameters in our later layers before
[732.8] becoming the final output, resulting in
[735.2] increasingly complex mappings. And we're
[738.2] still only looking at our eight layer
[740.0] model. How might this complexity build
[742.8] as we move to deeper models?
[746.0] Let's make an improvement to our
[747.4] visualization process and then explore
[749.8] how things change as we move to these
[751.6] deeper models.
[753.4] Thus far, we focused on maximizing the
[755.4] model's probability of the correct
[757.0] answer. But in practice, we typically
[759.4] use a slightly different objective. For
[761.8] classification problems like this, we
[763.5] would typically use the cross entropy
[765.5] loss. To compute the cross entropy loss,
[769.0] we take the negative natural logarithm
[771.3] of the model's probability of the
[772.9] correct answer.
[775.2] So if our model's probability of the
[776.8] correct answer is one, our loss is zero.
[780.8] Plotting our cross entropy loss on top
[782.8] of our probability curves, we see that
[785.4] our loss is essentially a flipped and
[787.4] stretched version of the model's
[788.8] probability of the correct answer.
[792.1] The critical conceptual change here is
[794.6] that we're now trying to minimize our
[796.5] loss instead of trying to maximize our
[798.8] probability.
[801.3] Now, when we train our model, we of
[803.4] course aren't updating single parameters
[805.2] at a time. Instead, all 1.45 four or
[808.4] five million parameters are updated
[810.0] simultaneously at each learning step.
[813.0] Visualizing this full process is
[815.0] perilous because our model is
[817.1] effectively stepping through 1.45
[819.4] million dimensional parameter space as
[821.3] it learns and we're limited to
[823.5] visualizing just a few dimensions at
[825.4] once.
[827.5] One approach we can take here is to
[829.9] choose a direction randomly in this
[831.7] parameter space. iteratively taking
[834.3] steps in this direction [music] and
[836.2] recomputing our loss at each step along
[838.2] the way.
[840.0] Functionally, this means sampling a
[841.6] vector with the same number of entries
[843.4] as the number of parameters we're
[844.9] exploring and adding scaled versions of
[847.1] this vector to our initial parameters.
[850.0] This gives us a new 1D curve for each
[852.2] randomly chosen direction.
[855.5] Things get more interesting when we pair
[857.4] two randomly chosen directions together,
[860.2] computing the loss for each combination
[862.0] of random directions in a grid and
[864.4] visualizing the results as a landscape.
[867.5] For more on this process, see chapter 2
[869.9] of the Welch Labs illustrated guide to
[871.9] AI. Here's what the lost landscape looks
[874.6] like for a modern LLM. Let's apply this
[877.8] lost landscape approach to our shallower
[879.9] eight layer model. When we vary the
[882.6] parameters in just the last few layers
[884.4] of this model, we see a very smooth and
[887.0] convex landscape, suggesting that the
[889.5] gradient descent learning process should
[891.4] proceed smoothly for these layers.
[894.4] Switching to the first few layers of the
[896.3] model, our surface becomes more complex,
[899.4] just as we saw with our single weight
[901.4] probes. Now that we've developed a more
[903.9] robust visualization approach, let's use
[906.6] our approach to explore our deeper
[908.5] models.
[910.6] As we added layers to our model earlier,
[913.2] we saw accuracy saturate around 26
[916.0] layers. The loss landscape of the first
[918.9] few layers of this model is
[920.3] significantly more complex than our
[922.0] eight layer model. This makes sense
[925.0] given that we've added 18 additional
[927.1] layers between our initial layers and
[929.3] our final output, increasing the
[931.6] complexity of this mapping. Here's the
[934.3] loss landscape for the first few layers
[936.1] of our deep 74 layer model. This
[939.5] landscape is especially chaotic with
[942.1] many local minima, especially compared
[944.6] to the smooth landscape we see for the
[946.7] last few layers of this model.
[949.4] One way to think about the bearing of
[951.2] this landscape on the learning process
[953.5] is to consider the downhill direction,
[956.0] the gradient at each point on our
[958.3] surface.
[959.9] This is the signal that actually drives
[961.7] the learning process. Visualizing our
[964.6] gradient as a vector field, we see that
[966.9] our gradient direction varies wildly
[969.0] across our landscape.
[971.4] This general problem was given the
[973.0] memorable name the shattered gradient
[975.4] problem in this 2017 paper where the
[978.6] authors observed that as depth
[980.6] increases, gradients in standard feed
[983.5] forward networks increasingly resemble
[985.8] white noise.
[987.8] So the critical signal that guides our
[989.8] entire learning process, the gradient,
[993.0] appears to become less and less reliable
[995.4] as the depth of our model increases.
[998.6] This brings us back to Giansoon's
[1000.4] research team at Microsoft Research Asia
[1002.6] in 2015.
[1004.9] Remarkably, by the end of that year, the
[1007.8] team was able to find an incredibly
[1009.4] effective solution that [music] would
[1011.1] completely address the shattered
[1012.6] gradients problem, allow them to train
[1015.1] models up to,2 layers deep, and
[1018.2] completely crush every relevant computer
[1020.5] vision benchmark.
[1022.6] Earlier we saw that the output of each
[1024.4] layer in our model is a tensor of
[1026.1] activation values and that the
[1028.2] compounding complexity of each
[1029.7] additional layer as our activations pass
[1031.9] through our model makes our gradients a
[1034.4] potentially unreliable guide for the
[1036.2] learning process.
[1038.2] The solution GNS's team found is almost
[1041.3] comically simple. Between each pair of
[1044.5] layers in the model, simply take the
[1046.6] input activation tensor and add it to
[1049.4] the output of the layers.
[1052.4] This operation is now often referred to
[1054.5] as a skip connection. We're effectively
[1057.2] adding a direct path around each pair of
[1059.4] compute layers for activations to flow
[1061.8] forward through and gradients to flow
[1064.2] backwards through. Note that since we're
[1066.8] adding full tensors together, when our
[1069.2] skip connection goes around a down
[1071.1] sampling step in our network, we need to
[1073.4] change the dimension of the tensor
[1075.1] moving through our skip connection. And
[1077.4] soon's team found a few simple and
[1079.0] effective ways to handle this.
[1081.3] Let's temporarily switch to showing our
[1083.1] network layers as discrete blocks
[1085.1] instead of just kernels connecting our
[1087.0] intermediate activations.
[1089.3] Another way to think about the skip
[1090.9] connection is that we're adding an
[1092.6] identity pass through for our data
[1094.9] around our compute layers and now
[1097.4] relying on our compute layers to learn
[1099.3] additional or residual behavior on top
[1101.5] of this pass through.
[1104.2] The team called their modified network a
[1106.2] residual neural network or ResNet for
[1108.9] short. ResNets work shockingly well,
[1112.2] sweeping the 2015 imageet
[1114.2] classification, detection, and
[1115.9] localization competitions [music] and
[1117.9] the KCO detection and segmentation
[1120.2] competitions. Here's the ResNet papers
[1122.6] lead author, Kaiming Hu, presenting the
[1125.0] team's results at the CVPR conference.
[1127.8] So, here is how deep learning looked
[1129.4] like uh three or four years ago. And
[1131.5] this is the Alex net that has eight a
[1134.1] layers. So, here is how deep learning
[1136.4] looked like uh two years ago. And these
[1138.6] are the V net and Google net that has
[1140.2] about 20 layer. And here is the deep
[1142.9] residual network that have over 150
[1145.4] layer. And here is another view of this
[1147.4] zero network. And it is not too special.
[1150.4] It is just a lot of layers. Let's add
[1153.6] skip connections to our 74 layer
[1155.8] network. As we saw earlier, this network
[1159.6] struggled to learn, only achieving an
[1162.2] accuracy of 38.9%.
[1165.2] significantly lower than our much
[1166.8] shallower eight layer network.
[1169.6] We also observed the shattered gradient
[1171.7] problem and a chaotic loss landscape
[1174.2] when probing early layers of the model.
[1177.9] Converting our network into a residual
[1179.8] network by adding skip connections and
[1181.9] retraining. Our model learned
[1184.2] significantly more quickly, achieving a
[1186.8] very strong accuracy of 72.6%.
[1190.9] Outperforming all of the other models
[1192.5] that we tested. And when we recomputee
[1195.0] the loss landscape for our early layers,
[1197.6] we see a dramatically smoother and more
[1199.8] convex surface
[1202.0] with similar geometry to the loss
[1203.8] landscape from our later layers.
[1206.8] Our skip connections provide a more
[1208.6] direct path from our early layers to our
[1211.4] model's output, effectively eliminating
[1214.0] the shattered gradients problem. Few
[1217.4] ideas in the history of machine learning
[1219.0] have had such a profound and rapid
[1220.9] impact on the field, ultimately earning
[1223.5] the ResNet paper more citations than any
[1226.0] other paper in the 21st century.
[1229.1] But as the dust settled, some profound
[1231.4] new questions came into focus. It's
[1234.2] interesting to consider why such a
[1235.7] simple idea had not caught on before.
[1238.8] One likely reason is that skip
[1240.5] connections violated the mainline
[1242.4] understanding of how deep neural
[1244.0] networks operated at the time.
[1246.4] Within a few months of the ResNet
[1248.0] publication, a team at Cornell would
[1250.2] demonstrate some shocking [music] facts
[1251.7] about ResNets. It turns out that we can
[1254.4] just delete or even shuffle the layers
[1256.4] and residual networks with only small
[1258.9] impacts on performance.
[1261.2] These realizations and subsequent
[1262.9] developments would force the field to
[1265.0] completely reconceptualize how deep
[1267.2] neural networks operate. As we'll see,
[1269.7] the ResNet team had inadvertently
[1271.5] invented a new critical backbone for
[1273.6] neural networks. a kind of working
[1276.2] memory that would allow these models to
[1278.6] reach unprecedented levels of
[1280.3] performance.
[1282.8] One of the things that I love about
[1284.4] ResNet is that we have this relatively
[1287.0] simple but incredibly powerful
[1289.0] architecture change just waiting for
[1291.0] [music] someone to discover. I recently
[1293.0] had a chance to chat with Aloque
[1294.5] Perinic. Alok works as a researcher at
[1297.2] this video sponsor Jane Street. As Alok
[1300.0] told me, he recently found himself
[1301.8] digging into some fundamental
[1302.9] architecture questions himself. And
[1305.4] remarkably, it all started with Alok's
[1307.6] own personal exploration into quantum
[1309.5] mechanics. So, actually, the first
[1312.6] reason I started thinking about this is
[1314.0] because like I was studying kind of
[1317.0] quantum mechanics for like totally
[1318.9] irrelevant reasons. Um, and a thing that
[1321.5] happens or that comes up a lot in
[1323.2] quantum mechanics is like representation
[1325.4] theory where you have certain groups.
[1327.9] This got a look thinking about the
[1329.5] connection to positional encodings in
[1331.3] modern transformers.
[1333.4] Unlike the convolutional neural networks
[1335.2] that we've been considering, the
[1336.8] attention mechanism in transformers does
[1338.9] not naturally have a sense of where
[1340.8] input tokens are relative to each other.
[1344.0] So this capability is generally added to
[1346.3] the architecture using a technique known
[1348.6] as a positional encoding. Aloque has a
[1351.3] great write up on his approach on the
[1352.8] Jane Street blog. I won't spoil the
[1355.4] whole thing here, but Aloque found that
[1357.4] the space of possible positional
[1358.9] encodings is actually surprisingly
[1360.9] constrained and that the most sensible
[1363.2] strategies are already being used in
[1365.0] practice. But he also found that there's
[1367.3] a completely unexplored set of
[1369.0] approaches. Alok started his career at
[1371.5] Jane Street as an intern. Here's one of
[1373.7] the many great things he had to say
[1375.1] about his experience. the fact that all
[1378.2] the all my co-workers and like kind of
[1380.6] collaborators were really like
[1383.2] intellectually invested in the decisions
[1386.1] like I I could just like walk up to
[1387.9] anyone with an interesting topic for
[1390.4] discussion and they like listen and have
[1393.3] something insightful to say um was
[1395.6] really really incredible. I feel like I
[1396.8] was learning so much and I still feel
[1398.2] like I'm learning a lot. If this sounds
[1399.8] interesting to you, now is the perfect
[1401.7] time to apply for the Jane Street
[1403.3] internship program or for a full-time
[1405.5] role. Jane Street offers internships in
[1407.9] machine learning, [music] quantitative
[1409.3] trading, and many other areas. Interns
[1412.2] have the opportunity to work on real
[1414.0] problems alongside some incredibly
[1416.2] bright collaborators like ALOK. You
[1418.6] don't need a finance background, and you
[1420.6] can apply today at the link in the
[1422.2] description below.
[1425.4] A few months after the ResNet
[1427.0] publication, a team at Cornell showed
[1429.3] that these new models demonstrated some
[1431.0] highly counterintuitive behavior. In
[1434.0] 2015, the predominant understanding of
[1436.5] how deep neural networks operated was
[1439.0] through learning hierarchical
[1440.2] representations.
[1442.3] This viewpoint was supported by strong
[1444.2] empirical evidence.
[1446.7] Here's the activation patterns from the
[1448.6] first layer of AlexNet responding to
[1450.7] simple features like edges and color
[1452.6] blobs.
[1454.4] Here's the second layer of the model,
[1456.0] bringing these simple edges together
[1457.5] into features like corner detectors.
[1460.5] And here's the fifth layer of the model
[1462.2] responding to fully formed abstract
[1464.4] concepts like faces. So, as the field
[1467.4] understood it at the time, each layer of
[1469.8] the model builds on top of the learned
[1471.8] representation of the layer before. In
[1474.9] this mental model of neural networks,
[1477.2] each layer plays a critical role in the
[1479.2] chain.
[1480.7] Deleting or transposing layers would be
[1482.8] catastrophic.
[1484.6] However, in 2016, the Cornell team
[1487.3] showed that this was not true for
[1488.6] ResNets.
[1490.4] While removing or transposing layers
[1492.3] would destroy the performance in
[1493.8] non-residual networks like Alexnet,
[1496.6] completely removing a layer from a 56
[1499.0] layer ResNet barely impacted performance
[1502.5] and performance degraded smoothly as the
[1504.6] team removed more layers. Clearly, deep
[1507.8] residual networks were not just building
[1509.8] deeper versions of the hierarchical
[1512.2] representations learned by models like
[1514.1] AlexNet.
[1516.6] Let's have a closer look at the skip
[1518.2] connections introduced by the ResNet
[1519.8] authors.
[1521.4] Every two model layers, we take the full
[1524.1] input tensor, move it around the layers,
[1527.0] and add it to the layers output. Let's
[1529.7] redraw our network in a slightly
[1531.3] different way. We'll straighten out all
[1533.6] of our skip connections into a single
[1535.4] line from the input to the output of our
[1538.0] network and draw the inputs and outputs
[1540.8] to our layers as branching off of our
[1542.9] continuous skip connection.
[1545.8] Now, these drawings represent the same
[1547.8] exact network. Just as before, every two
[1551.3] layers, we take the full input tensor,
[1553.7] move it around the layers, and add it to
[1556.0] the layers output. However, this way of
[1558.7] drawing our network shows that there's
[1560.6] an unbroken flow of data from the input
[1563.4] to the output of our network that our
[1565.8] layers add to as we move through our
[1568.2] model. In a residual network with six
[1571.5] layers, if we label the outputs of each
[1573.9] pair of layers F, G, and H, then our
[1577.2] model's final output is equal to our
[1579.0] input X plus F + G plus H.
[1583.9] This flow of information from the input
[1586.0] to the output of our residual network
[1588.3] iteratively refined by each layer was
[1591.0] later given the name the residual stream
[1593.8] and has become one of the defining
[1595.6] features of modern AI. This shift in
[1598.8] understanding from the network's layers
[1600.8] forming hierarchical representations to
[1603.2] iteratively refining the residual stream
[1605.9] can help us make sense of the Cornell
[1607.8] team's results. If each layer in a 56
[1611.0] layer ResNet is just incrementally
[1612.7] refining the residual stream, then
[1615.3] removing or transposing layers should
[1617.3] only have an incremental effect.
[1620.7] Now, we should note here that both of
[1622.4] these things can be true. A separate
[1624.9] research team would later show strong
[1626.8] evidence that residual networks were
[1628.9] both learning hierarchal representations
[1631.0] in subsets of layers while iteratively
[1633.8] refining the residual stream.
[1636.7] In 2017, a team at Google published what
[1639.4] would become the breakthrough
[1641.0] transformer architecture, which is, by
[1643.3] the way, now the seventh most cited
[1645.0] paper of the 21st century. In their
[1647.0] architecture, the team included skip
[1649.1] connections between each of their
[1650.9] alternating attention and multi-layer
[1652.6] perceptron layers, placing the residual
[1655.5] stream at the heart of their design.
[1658.2] The transformer proved remarkably
[1660.2] effective at language modeling, becoming
[1663.0] the workhorse of large language models
[1665.6] and ultimately working its way into
[1667.2] vision applications, setting new
[1669.6] state-of-the-art results on the imageet
[1671.4] data set. But in 2023, a research team
[1674.9] at Meta noticed something strange about
[1677.6] the residual stream in vision
[1679.5] transformers.
[1681.7] Here's a look at the residual stream
[1683.2] from one of the models the team
[1684.5] investigated, Dino V2. This version of
[1687.9] the model has 40 layers and the residual
[1690.8] stream is of dimension 37x 37 x 1536 for
[1694.5] the full depth of the network. Let's
[1697.4] simplify our visualization. After each
[1700.2] layer, we'll collapse our residual
[1701.7] stream into a single 37x 37 2D array by
[1706.2] taking the maximum of our 1536
[1708.8] activation values at each position. This
[1711.8] gives us 40 2D arrays, each showing the
[1715.0] maximum activation values in the
[1716.7] residual stream after each of our models
[1719.3] 40 layers.
[1721.4] In the earlier stages of the model, we
[1723.6] can see high activations around visually
[1725.7] important regions of the image such as
[1727.6] the face, the hands, and the lights on
[1729.4] the bookshelf. But as we move deeper
[1731.7] into the model, these activations become
[1734.1] completely dominated by some very large
[1736.8] values at a small number of positions.
[1740.0] If we overlay these high activation
[1742.1] positions on our original image, we see
[1744.6] that they generally appear in
[1746.0] unimportant regions of the image, the
[1748.4] wall, the door, and the drawers. Are
[1751.0] these high activating positions just a
[1752.9] random artifact of the architecture, or
[1755.7] could they be serving some purpose?
[1758.4] The meta team developed an interesting
[1760.1] hypothesis.
[1761.6] We proposed the following interpretation
[1763.4] of these elements. The model learns to
[1766.2] recognize patches containing little
[1768.0] useful information and recycles the
[1770.6] corresponding tokens to aggregate global
[1773.3] image information while discarding
[1775.4] spatial information. So under this
[1777.7] hypothesis, the residual stream acts as
[1780.1] a working memory where the model can
[1782.4] store, edit, and retrieve information.
[1785.4] The meta team tested their hypothesis in
[1787.4] a few ways. First, they probed the
[1790.1] residual stream at these high activating
[1792.2] positions. training image classifiers
[1795.0] using the embedding vectors from these
[1797.1] positions as inputs.
[1799.4] Remarkably, the high activating
[1801.3] embeddings prove dramatically better at
[1803.4] image classification relative to
[1805.7] normally activating embeddings,
[1807.8] especially on fine grain data sets. Non-
[1811.2] highly activating embedding vectors
[1812.9] reached only a 10.8% accuracy on the
[1815.5] challenging cars data set, while the
[1818.2] highly activating embedding vectors
[1819.7] achieved an 85.2% accuracy. So these
[1823.5] highly activating positions appear to be
[1826.1] storing information about the image as a
[1828.1] whole rather than being limited to
[1830.2] information about the specific patch of
[1832.0] image that they fall on.
[1834.5] The meta team's next experiment was
[1836.3] brilliant. They simply gave the model
[1838.8] another place to put this information.
[1841.3] The team added new positions in the
[1843.2] residual stream alongside the 37 by 37
[1846.6] grid of patch embeddings from our input
[1849.0] images.
[1850.6] These are embedding vectors of length
[1852.3] 1536
[1853.8] just like the embedding vector for each
[1855.5] image patch. However, unlike the image
[1858.3] patch embedding vectors, these new
[1860.6] vectors are randomly initialized before
[1862.8] training and their values at the
[1865.0] beginning of the residual stream are
[1866.8] learned like any other parameter.
[1869.7] At the end of the model, these vectors
[1871.7] are simply discarded. Their final values
[1874.3] are not connected to any learning
[1876.1] objective. The team called these new
[1878.6] positions register tokens, borrowing the
[1881.4] term from the registers that perform
[1883.2] short-term data storage and computer
[1885.3] CPUs.
[1887.9] Let's visualize our maximum activation
[1889.9] values as 2D grids as we did earlier,
[1893.0] but now for a version of the model
[1894.8] trained with register tokens in place.
[1898.3] Remarkably, the strange high activation
[1901.0] values that the team saw in DOV2 and
[1903.5] other models completely disappear.
[1906.1] Here's a view of the residual stream
[1908.2] with and without the added register
[1910.1] tokens. The model has shifted from
[1912.9] storing global information in
[1914.4] unimportant patch positions to actually
[1917.0] using the register positions.
[1920.6] These results strongly support the view
[1922.7] of the residual stream as a working
[1924.7] memory for the model. And it's so
[1927.1] remarkable to me that in the absence of
[1929.4] registered tokens, these models
[1931.7] effectively learn to make their own by
[1934.1] repurposing unimportant parts of the
[1936.1] image.
[1938.4] A century before Alex Kreseky, Ilascover
[1941.3] and Jeff Hinton published the AlexNet
[1943.2] paper, Max Plac published on the law of
[1946.2] the distribution of energy in the normal
[1948.2] spectrum.
[1949.9] Plac showed that if he assumed that
[1951.6] energy was emitted and absorbed in
[1953.3] discrete quanta, he could solve one of
[1955.8] the most pressing physics problems of
[1957.5] the day known as the ultraviolet
[1959.8] catastrophe.
[1961.8] Plunk considered his work more of a
[1963.4] mathematical trick than a true
[1965.0] discovery. But the effectiveness of his
[1967.4] approach could not be ignored. A few
[1970.2] years later, Einstein applied Plonc's
[1972.3] idea successfully to the study of the
[1974.2] photoelectric effect. And a few years
[1977.0] after that, Neil's Boore extended
[1978.8] Plonc's idea further into a quantized
[1981.8] model of electron energy states within
[1983.8] the atom. From here, the dominoes
[1986.5] continued to fall in rapid succession,
[1989.2] culminating in the late 1920s with the
[1991.2] work of Schroinger, Heisenberg, and
[1992.8] Durac, resulting in a complete
[1995.4] reconceptualization of matter and
[1997.4] energy.
[1999.1] The physicist George Gamoff would later
[2001.6] call this buildup to quantum mechanics
[2003.8] 30 years that shook physics.
[2007.2] Today, the hype, noise, and
[2009.0] commercialization around modern
[2010.6] artificial intelligence can make it easy
[2013.1] to forget that real science, real
[2015.6] discoveries are happening and that we
[2017.8] have a front row seat.
[2020.7] Alexet definitively showed that given
[2023.0] sufficient training data, deep neural
[2025.2] networks could perform remarkably well.
[2028.2] The discovery of residual networks a few
[2030.2] years later was one of these critical
[2031.9] early dominoes to fall, enabling deeper
[2035.2] networks with unprecedented levels of
[2037.3] performance and ultimately forcing the
[2039.6] field to completely reconceptualize how
[2042.0] these models work. Residual networks
[2045.0] were critical in the subsequent
[2046.4] development of the transformer, large
[2048.4] language models, diffusion models, and
[2050.2] virtually all modern AI systems we use
[2052.7] today. We'll have to wait and see if
[2055.6] most of the dominoes in this wave of AI
[2057.8] have already fallen or if we're just
[2060.6] getting started.
[2067.7] Now is the perfect time to join the
[2069.4] Welch Labs Patreon. If you join at the
[2072.2] $5 per month or higher level, we'll send
[2074.5] you a real paper cutout from a video.
[2077.6] Making and shooting all these loss
[2079.1] curves was a ton of fun. This is the
[2081.4] next batch of cutouts that will ship. We
[2083.9] also do a book raffle every quarter for
[2086.0] patrons. This quarter, we'll have two
[2088.4] winners who will each receive a copy of
[2090.6] the Welch Labs Illustrated Guide to AI
[2093.0] and a book that I'm currently reading.
[2095.6] I've just decided on the book for this
[2097.4] raffle, and I really think you'll like
[2099.5] it. Finally, the first batch of Welch
[2102.6] [music] Labs t-shirts ever is coming out
[2104.6] this fall, and patrons will get early
[2106.7] and discounted access. Thank you so much
[2109.8] for your continued support and stay
[2112.0] tuned for some exciting new things
[2113.5] coming out this fall.
