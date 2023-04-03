participant_text = "Hello! I am a fledging data scientist who is pursuing B.Sc. Major in Statistics at the University of British Columbia. "\
                    "I worked as a data science intern in multiple corporations in the past year. "\
                    "Through my research and internship experiences, I have gained exposure to data preprocessing, "\
                    "machine learning modelling, artificial neural networks and data visualizations. I am currently "\
                    "on a track to pave my career as a data scientist who specializes in working with biomedical health data."

investigation_text = "As evident from the case of COVID-19 where a large amount of misleading false information drove the general population into dramatic confusion, " \
                     "fake news plays a critical role in manipulating people into misguided thoughts and drive the society into disorganization."

introductory_text = "This interactive dashboard is created as a part of the submission process to the 2023 CANIS Data Visualization Hackathon. " \
                    "In this hackathon, we aim to answer three fundamental questions regarding analyzing and classifying ⌜Fake News⌟ against ⌜True News⌟. " \
                    "The ultimate goal of this hackathon is to come up with innovative ideas in characterizing ⌜Fake News⌟ to better distinguish propaganda, bias, and subjective opinions from facts."

first_question = "Q1. What are the differences between characteristics of ⌜True News⌟ and ⌜Fake News⌟?"
second_question = "Q2. Will there be any differences in the results of sentiment analysis between ⌜True News⌟ and ⌜Fake News⌟ articles?"
third_question = "Q3. What proportion of the Russian Propaganda articles will be classified as ⌜Fake News⌟ based on our model?"

conclusion_text = "In this section, we refer back to the questions that we asked in the Introduction section and answer them " \
                  "through the analysis we have done. "

first_list_text = "Comparing the number of total characters between Fake News and True News articles, we notice that the articles " \
                  "labelled as Fake News are shorter in length on average compared to True News, while there are prominent outliers that are very " \
                  "long in length. Interestingly, we observe that 'Trump' is the most frequently mentioned vocabulary for both Fake News and True News articles. " \
                  "Trump is mentioned slightly more frequently in the articles labelled as True News. Comparing between countries, " \
                  "the word 'America' is more frequently mentioned in the Fake News articles, whereas it is the opposite for 'China' and 'Russia'."

second_list_text = "The most prominent differences in the sentiment analysis results between Fake News and True News " \
                   "are noticed in the 'Compound' and 'Subjectivity' scores. 'Compound' score is calculated from the sum of positive, " \
                   "negative and neutral scores and is normalized between -1 to +1. 'Subjectivity' score is calculated using the TextBlob library; " \
                   "the higher the score is, the more subjective the article is."

third_list_text = "We created a classification model using logistic regression (LS) and linear support vector machine (SVC), " \
                  "which are popular and widely known classification algorithms. Among the two models, SVC performed better when testing " \
                  "its accuracy. SVC model classified 6007 articles as Fake News in the Russian Propaganda " \
                  "dataset, which is approximately 99.4% of articles in the Russian Propadanda dataset. Thus it is safe to assume that " \
                  "the majority of Russian Propaganda articles are classified as Fake News and the general population should refrain from trusing such articles."

suggestion_text = "Reflecting on the analysis we performed so far, a more accurate Fake News detection model can be created by " \
                  "filtering articles based on the sentiment analysis scores prior to creating the model. For example, as 'Compound' score " \
                  "showed distinguishable differences between Fake News and True News articles, filtering the articles " \
                  "within the lower 0.005 quantile of the 'Compound' score may create more accurate model and result in a higher accuracy value."

reference_text = "References"