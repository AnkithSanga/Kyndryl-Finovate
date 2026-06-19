"""
Mock responses for the Kyndryl Banking Assistant.
This file contains fallback responses for all supported languages.
Real responses should prioritize RAG, AI, and FAQ sources.
"""

MOCKED_RESPONSES = {
    'en': {
        'greeting': "Hello! I'm your virtual banking assistant. How can I help you today?",
        'balance': "To check your current account balance, please log into your account or use your banking app. I can help guide you through the process if needed. What would you like to do?",
        'transactions': "You can view your transaction history through your banking app or by logging into your account online. Would you like help with anything else?",
        'transfer': "I can help guide you with money transfers. To proceed, you'll need to use your banking app or online portal. Please provide details about what you'd like to transfer, and I can guide you through the steps.",
        'loans': "We offer various loan products including Personal Loans, Home Loans, and Car Loans. Would you like to know more about any specific loan product or the eligibility criteria?",
        'cards': "For information about your card services, credit limits, and available card products, please check your banking app or contact our customer support team. How can I assist you?",
        'default': "I understand you're asking about banking services. Could you please be more specific? I can help with:\n- Account information and balance inquiries\n- Transaction history\n- Money transfers\n- Loan information\n- Card services"
    },
    'hi': {
        'greeting': "नमस्ते! मैं आपका वर्चुअल बैंकिंग सहायक हूं। आज मैं आपकी कैसे मदद कर सकता हूं?",
        'balance': "अपना वर्तमान खाता शेष जांचने के लिए, कृपया अपने खाते में लॉगिन करें या अपने बैंकिंग ऐप का उपयोग करें। यदि आवश्यकता हो तो मैं आपको प्रक्रिया के माध्यम से गाइड कर सकता हूं। आप और क्या करना चाहेंगे?",
        'transactions': "आप अपने बैंकिंग ऐप के माध्यम से या अपने खाते में लॉगिन करके अपना लेनदेन इतिहास देख सकते हैं। क्या मैं आपकी और कुछ मदद कर सकता हूं?",
        'transfer': "मैं आपको धन हस्तांतरण में गाइड करने में मदद कर सकता हूं। आगे बढ़ने के लिए, आपको अपने बैंकिंग ऐप या ऑनलाइन पोर्टल का उपयोग करना होगा। कृपया बताएं कि आप क्या स्थानांतरित करना चाहते हैं।",
        'loans': "हम विभिन्न ऋण उत्पाद प्रदान करते हैं जैसे व्यक्तिगत ऋण, गृह ऋण, और कार ऋण। क्या आप किसी विशिष्ट ऋण उत्पाद या पात्रता मानदंड के बारे में अधिक जानना चाहेंगे?",
        'cards': "आपकी कार्ड सेवाओं, क्रेडिट सीमा, और उपलब्ध कार्ड उत्पादों की जानकारी के लिए, कृपया अपने बैंकिंग ऐप को देखें या हमारी ग्राहक सेवा टीम से संपर्क करें। मैं आपकी कैसे मदद कर सकता हूं?",
        'default': "मैं समझ गया कि आप बैंकिंग सेवाओं के बारे में पूछ रहे हैं। कृपया अधिक विशिष्ट हो सकते हैं? मैं मदद कर सकता हूं:\n- खाता जानकारी और शेष पूछताछ\n- लेनदेन इतिहास\n- धन हस्तांतरण\n- ऋण जानकारी\n- कार्ड सेवाएं"
    },
    'ta': {
        'greeting': "வணக்கம்! நான் உங்கள் மெய்நிகர் வங்கி உதவியாளர். இன்று நான் உங்களுக்கு எவ்வாறு உதவ முடியும்?",
        'balance': "உங்கள் தற்போதைய கணக்கு இருப்பை சரிபார்க்க, தயவுசெய்து உங்கள் கணக்கில் உள்நுழையவும் அல்லது உங்கள் வங்கிக் கையை பயன்படுத்தவும். தேவைப்பட்டால் நான் உங்களை செயல்முறையின் மூலம் வழிகாட்ட முடியும். இன்னும் என்ன செய்ய விரும்புகிறீர்கள்?",
        'transactions': "நீங்கள் உங்கள் வங்கிக் கையின் மூலம் அல்லது உங்கள் கணக்கில் உள்நுழையுவதன் மூலம் உங்கள் பரிவர்த்தனை வரலாற்றைக் காணலாம். இன்னும் நான் உங்களுக்கு உதவ முடியுமா?",
        'transfer': "பணத் தடங்களுடன் உங்களுக்கு வழிகாட்ட நான் உதவ முடியும். முன்னேற வேண்டுமெனில், நீங்கள் உங்கள் வங்கிக் கையை அல்லது ஆன்லைன் போர்டலைப் பயன்படுத்த வேண்டும். தயவுசெய்து நீங்கள் என்ன மாற்ற விரும்புகிறீர்கள் என்பதைக் குறிப்பிடவும்.",
        'loans': "நாங்கள் தனிப்பட்ட கடன், வீட்டு கடன், மற்றும் கார் கடன்கள் உட்பட பல்வேறு கடன் பொருட்களை வழங்குகிறோம். குறிப்பிட்ட கடன் பொருள் அல்லது தகுதி அளவுகோல் பற்றி மேலும் அறிய விரும்புகிறீர்களா?",
        'cards': "உங்கள் கார்டு சேவைகள், கடன் வரம்புகள் மற்றும் கிடைக்கும் கார்டு பொருட்கள் பற்றிய தகவலுக்கு, தயவுசெய்து உங்கள் வங்கிக் கையை சரிபார்க்கவும் அல்லது எங்கள் வாடிக்கையாளர் சேவை குழுவிடம் தொடர்புகொள்ளவும். நான் உங்களுக்கு எவ்வாறு உதவ முடியும்?",
        'default': "நீங்கள் வங்கி சேவைகள் பற்றி கேட்கிறீர்கள் என்பதை புரிந்துகொள்கிறேன். தயவுசெய்து மேலும் குறிப்பிட்டதாக இருக்க முடியுமா? நான் உதவ முடியும்:\n- கணக்கு தகவல் மற்றும் இருப்பு விசாரணைகள்\n- பரிவர்த்தனை வரலாறு\n- பணம் மாற்றங்கள்\n- கடன் தகவல்\n- கார்டு சேவைகள்"
    },
    'te': {
        'greeting': "హలో! నేను మీ వర్చువల్ బ్యాంకింగ్ సహాయక్ని. ఈ రోజు నేను మీకు ఎలా సహాయం చేయవచ్చు?",
        'balance': "మీ ప్రస్తుత ఖాతా నిల్వను తనిఖీ చేయడానికి, దయచేసి మీ ఖాతాలో లాగిన్ చేయండి లేదా మీ బ్యాంకింగ్ యాప్‌ను ఉపయోగించండి. అవసరమైతే నేను ప్రక్రియ ద్వారా మీకు గైడ్ చేయవచ్చు. మరేమి చేయాలనుకుంటున్నారు?",
        'transactions': "మీరు మీ బ్యాంకింగ్ యాప్ ద్వారా లేదా మీ ఖాతాలో లాగిన్ చేయడ ద్వారా మీ లెన్లేదెన్ కోర్చరిని చూడవచ్చు. నేను ఇంకా సహాయం చేయవచ్చా?",
        'transfer': "నేను డబ్బు బదిలీ సంబంధించి మీకు గైడ్ చేయడానికి సహాయం చేయవచ్చు. ముందుకు సాగడానికి, మీరు మీ బ్యాంకింగ్ యాప్ లేదా ఆన్‌లైన్ పోర్టల్‌ను ఉపయోగించాలి. దయచేసి మీరు ఏమి బదిలీ చేయాలనుకుంటున్నారో తెలియజేయండి.",
        'loans': "మేము ఖాతా ऋణ, గృహ రుణ మరియు కారు రుణలు సహా వివిధ రుణ ఉత్పత్తులను అందిస్తాము. నిర్దిష్ట రుణ ఉత్పత్తి లేదా అర్హత ప్రమాణాల గురించి మీరు మరింత తెలుసుకోవాలనుకుంటున్నారా?",
        'cards': "మీ కార్డ్ సేవలు, క్రెడిట్ పరిమితులు మరియు అందుబాటులో ఉన్న కార్డ్ ఉత్పత్తుల గురించిన సమాచారం కోసం, దయచేసి మీ బ్యాంకింగ్ యాప్‌ను చెక్ చేయండి లేదా మా కస్టమర్ సపోర్ట్ టీమ్‌ను సంప్రదించండి. నేను మీకు ఎలా సహాయం చేయవచ్చు?",
        'default': "మీరు బ్యాంకింగ్ సేవల గురించి అడుగుతున్నారని నేను అర్థం చేసుకున్నాను. దయచేసి మరింత నిర్దిష్టంగా చెప్పగలరా? నేను సహాయం చేయవచ్చు:\n- ఖాతా సమాచారం మరియు నిల్వ విచారణలు\n- లెన్లేదెన్ కోర్చరి\n- డబ్బు బదిలీలు\n- రుణ సమాచారం\n- కార్డ్ సేవలు"
    },
    'kn': {
        'greeting': "ಹಲೋ! ನಾನು ನಿಮ್ಮ ವರ್ಚುವಲ್ ಬ್ಯಾಂಕಿಂಗ್ ಸಹಾಯಕ. ಇಂದು ನಾನು ನಿಮಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು?",
        'balance': "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಖಾತೆ ಬ್ಯಾಲೆನ್ಸ್ ಪರಿಶೀಲಿಸಲು, ದಯವಿಟ್ಟು ನಿಮ್ಮ ಖಾತೆಗೆ ಲಾಗಿನ್ ಮಾಡಿ ಅಥವಾ ನಿಮ್ಮ ಬ್ಯಾಂಕಿಂಗ್ ಆ್ಯಪ್ ಬಳಸಿ. ಅಗತ್ಯವಿದ್ದರೆ ನಾನು ಪ್ರಕ್ರಿಯೆಯ ಮೂಲಕ ನಿಮಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡಬಹುದು. ನೀವು ಇನ್ನೇನು ಮಾಡಲು ಬಯಸುತ್ತೀರಿ?",
        'transactions': "ನಿಮ್ಮ ಬ್ಯಾಂಕಿಂಗ್ ಆ್ಯಪ್ ಮೂಲಕ ಅಥವಾ ನಿಮ್ಮ ಖಾತೆಗೆ ಲಾಗಿನ್ ಮಾಡುವ ಮೂಲಕ ನಿಮ್ಮ ವಹಿವಾಟು ಇತಿಹಾಸ ನೋಡಬಹುದು. ನಾನು ಇನ್ನೂ ಸಹಾಯ ಮಾಡಬಹುದೇ?",
        'transfer': "ನಾನು ಹಣ ವರ್ಗಾವಣೆಗೆ ಸಂಬಂಧಿಸಿದಂತೆ ನಿಮಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡಲು ಸಹಾಯ ಮಾಡಬಹುದು. ಮುಂದಕ್ಕೆ ಹೋಗಲು, ನೀವು ನಿಮ್ಮ ಬ್ಯಾಂಕಿಂಗ್ ಆ್ಯಪ್ ಅಥವಾ ಆನ್‌ಲೈನ್ ಪೋರ್ಟಲ್ ಬಳಸಬೇಕು. ದಯವಿಟ್ಟು ನೀವು ಏನು ವರ್ಗಾಯಿಸಲು ಬಯಸುತ್ತೀರಿ ಎಂಬುದನ್ನು ತಿಳಿಸಿ.",
        'loans': "ನಾವು ವ್ಯಕ್ತಿಗತ ಸಾಲ, ಮನೆ ಸಾಲ ಮತ್ತು ಕಾರು ಸಾಲ ಸೇರಿದಂತೆ ವಿವಿಧ ಸಾಲ ಉತ್ಪನ್ನಗಳನ್ನು ನೀಡುತ್ತೇವೆ. ನಿರ್ದಿಷ್ಟ ಸಾಲ ಉತ್ಪನ್ನ ಅಥವಾ ಅರ್ಹತೆ ಮಾನದಂಡ ಬಗ್ಗೆ ನೀವು ಇನ್ನೂ ತಿಳಿಯಲು ಬಯಸುತ್ತೀರೆ?",
        'cards': "ನಿಮ್ಮ ಕಾರ್ಡ್ ಸೇವೆಗಳು, ಕ್ರೆಡಿಟ್ ಮಿತಿಗಳು ಮತ್ತು ಲಭ್ಯವಿರುವ ಕಾರ್ಡ್ ಉತ್ಪನ್ನಗಳ ಬಗ್ಗೆ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಲು, ದಯವಿಟ್ಟು ನಿಮ್ಮ ಬ್ಯಾಂಕಿಂಗ್ ಆ್ಯಪ್ ಪರಿಶೀಲಿಸಿ ಅಥವಾ ನಮ್ಮ ಗ್ರಾಹಕ ಸೇವಾ ತಂಡವನ್ನು ಸಂಪರ್ಕಿಸಿ. ನಾನು ನಿಮಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು?",
        'default': "ನೀವು ಬ್ಯಾಂಕಿಂಗ್ ಸೇವೆಗಳ ಬಗ್ಗೆ ಕೇಳುತ್ತಿರುವಿರಿ ಎಂದು ನಾನು ಅರ್ಥಮಾಡಿಕೊಂಡಿದ್ದೇನೆ. ದಯವಿಟ್ಟು ಹೆಚ್ಚು ನಿರ್ದಿಷ್ಟವಾಗಿ ಹೇಳಬಹುದೆ? ನಾನು ಸಹಾಯ ಮಾಡಬಹುದು:\n- ಖಾತೆ ಮಾಹಿತಿ ಮತ್ತು ಬ್ಯಾಲೆನ್ಸ್ ವಿಚಾರಣೆಗಳು\n- ವಹಿವಾಟು ಇತಿಹಾಸ\n- ಹಣ ವರ್ಗಾವಣೆ\n- ಸಾಲ ಮಾಹಿತಿ\n- ಕಾರ್ಡ್ ಸೇವೆಗಳು"
    },
    'ml': {
        'greeting': "ഹലോ! ഞാൻ നിങ്ങളുടെ വെർച്വൽ ബാങ്കിംഗ് സഹായി. ഇന്ന് ഞാൻ നിങ്ങളെ എങ്ങനെ സഹായിക്കാം?",
        'balance': "നിങ്ങളുടെ നിലവിലെ അക്കൗണ്ട് ബാലൻസ് പരിശോധിക്കാൻ, ദയവായി നിങ്ങളുടെ അക്കൗണ്ടിൽ ലോഗിൻ ചെയ്യുക അല്ലെങ്കിൽ നിങ്ങളുടെ ബാങ്കിംഗ് അപ്ലിക്കേഷൻ ഉപയോഗിക്കുക. ആവശ്യമെങ്കിൽ ഞാൻ നിങ്ങളെ പ്രക്രിയയിലൂടെ ഗൈഡ് ചെയ്യാം. നിങ്ങൾ ഇനി എന്താണ് ചെയ്യാൻ ആഗ്രഹിക്കുന്നത്?",
        'transactions': "നിങ്ങളുടെ ബാങ്കിംഗ് അപ്ലിക്കേഷനിലൂടെ അല്ലെങ്കിൽ നിങ്ങളുടെ അക്കൗണ്ടിൽ ലോഗിൻ ചെയ്ത് നിങ്ങളുടെ ഇടപാട് ചരിത്രം കാണാൻ കഴിയും. ഞാൻ കൂടുതൽ സഹായിക്കാവുന്നതുണ്ട്?",
        'transfer': "ഞാൻ പണ ട്രാൻസ്ഫർ സംബന്ധിച്ച് നിങ്ങളെ ഗൈഡ് ചെയ്യാൻ സഹായിക്കാം. മുന്നോട്ട് പോകാൻ, നിങ്ങൾ നിങ്ങളുടെ ബാങ്കിംഗ് അപ്ലിക്കേഷൻ അല്ലെങ്കിൽ ഓൺലൈൻ പോർട്ടൽ ഉപയോഗിക്കണം. ദയവായി നിങ്ങൾ എന്താണ് ട്രാൻസ്ഫർ ചെയ്യാൻ ആഗ്രഹിക്കുന്നത് എന്ന് പറയുക.",
        'loans': "ഞങ്ങൾ വ്യക്തിഗത കടം, വീട് കടം, കാർ കടം എന്നിവ ഉൾപ്പെടെ വിവിധ കടം ഉൽപ്പന്നങ്ങൾ നൽകുന്നു. നിർദ്ദിഷ്ട കടം ഉൽപ്പന്നം അല്ലെങ്കിൽ കർത്തവ്യ മാനദണ്ഡ ബാബിലെ നിങ്ങൾ ഇനി അറിയാൻ ആഗ്രഹിക്കുന്നുണ്ടോ?",
        'cards': "നിങ്ങളുടെ കാർഡ് സേവനങ്ങൾ, ക്രെഡിറ്റ് പരിധി, ലഭ്യമായ കാർഡ് ഉൽപ്പന്നങ്ങൾ എന്നിവ സംബന്ധിച്ച വിവരങ്ങൾക്കായി, ദയവായി നിങ്ങളുടെ ബാങ്കിംഗ് അപ്ലിക്കേഷൻ പരിശോധിക്കുക അല്ലെങ്കിൽ ഞങ്ങളുടെ കাস്റ്റമർ സപ്പോർട്ട് ടീമിനെ ബന്ധപ്പെടുക. ഞാൻ നിങ്ങളെ എങ്ങനെ സഹായിക്കാം?",
        'default': "നിങ്ങൾ ബാങ്കിംഗ് സേവനങ്ങൾ ബാബിലെ ചോദിക്കുന്നതായി ഞാൻ മനസ്സിലാക്കി. ദയവായി കൂടുതൽ വിശദമായി പറയാനാകുമോ? ഞാൻ സഹായിക്കാവുന്നത്:\n- അക്കൗണ്ട് വിവരം ബാലൻസ് അന്വേഷണം\n- ഇടപാട് ചരിത്രം\n- പണ ട്രാൻസ്ഫർ\n- കടം വിവരം\n- കാർഡ് സേവനങ്ങൾ"
    },
    'mr': {
        'greeting': "नमस्कार! मी आपला व्हर्च्युअल बँकिंग सहाय्यक आहे. आज मी आपल्याला कसे मदत करू शकतो?",
        'balance': "आपल्या वर्तमान खाते शेष तपासण्यासाठी, कृपया आपल्या खाते मध्ये लॉगिन करा किंवा आपल्या बँकिंग अँप वापरा. आवश्यकतेनुसार मी आपल्याला प्रक्रियेद्वारे मार्गदर्शन करू शकतो. आप आणखी काय करू इच्छाल?",
        'transactions': "आप आपल्या बँकिंग अँप द्वारे किंवा आपल्या खाते मध्ये लॉगिन करून आपला व्यवहार इतिहास पाहू शकता. मी आपल्याला आणखी मदत करू शकतो?",
        'transfer': "मी आपल्याला पैसा हस्तांतरणाबद्दल मार्गदर्शन करण्यास मदत करू शकतो. पुढे जाण्यासाठी, आपल्याला आपल्या बँकिंग अँप किंवा ऑनलाइन पोर्टल वापरणे आवश्यक आहे. कृपया सांगा की आप काय हस्तांतरित करू इच्छाल.",
        'loans': "आम्ही व्यक्तिगत कर्ज, गृह कर्ज आणि कार कर्ज यासह विविध कर्ज उत्पादने प्रदान करतो. कोणतेही विशिष्ट कर्ज उत्पादन किंवा पात्रता निकष बद्दल आप आणखी जाणू इच्छाल?",
        'cards': "आपल्या कार्ड सेवा, क्रेडिट मर्यादा आणि उपलब्ध कार्ड उत्पादनांची माहिती मिळविण्यासाठी, कृपया आपल्या बँकिंग अँप तपासा किंवा आमच्या ग्राहक सेवा संघाशी संपर्क साधा. मी आपल्याला कसे मदत करू शकतो?",
        'default': "मी समजलो की आप बँकिंग सेवांबद्दल विचारत आहात. कृपया अधिक विशिष्ट व्हा? मी मदत करू शकतो:\n- खाते माहिती आणि शेष चौकशी\n- व्यवहार इतिहास\n- पैसा हस्तांतरण\n- कर्ज माहिती\n- कार्ड सेवा"
    },
    'gu': {
        'greeting': "નમસ્તે! હું તમારો વર્ચુઅલ બેંકિંગ સહાયક છું. આજ હું તમને કેવી રીતે મદદ કરી શકું?",
        'balance': "તમારા વર્તમાન ખાતા બેલેન્સ તપાસવા માટે, કૃપયા તમારા ખાતામાં લૉગઇન કરો અથવા તમારી બેંકિંગ એપ્લિકેશન વાપરો. જરૂર હોય તો હું તમને પ્રક્રિયા દ્વારા માર્ગદર્શન કરી શકું છું. તમે આગળ શું કરવા માંગો છો?",
        'transactions': "તમે તમારી બેંકિંગ એપ્લિકેશન દ્વારા અથવા તમારા ખાતામાં લૉગઇન કરીને તમારી વ્યવહાર ઇતિહાસ જોઈ શકો છો. શું હું તમને વધુ મદદ કરી શકું છું?",
        'transfer': "હું તમને પૈસા ટ્રાન્સફર સાથે માર્ગદર્શન આપવામાં મદદ કરી શકું છું. આગળ વધવા માટે, તમે તમારી બેંકિંગ એપ્લિકેશન અથવા ઑનલાઇન પોર્ટલ વાપરવું પડશે. કૃપયા કહો કે તમે શું ટ્રાન્સફર કરવા માંગો છો.",
        'loans': "અમે વ્યક્તિગત ऋણ, હોમ લોન અને કાર લોન સહિત વિવિધ લોન ઉત્પાદો પ્રદાન કરીએ છીએ. શું તમે કોઈ ચોક્કસ લોન ઉત્પાદન અથવા પાત્રતા માપદંડ વિશે વધુ જાણવા માંગો છો?",
        'cards': "તમારી કાર્ડ સેવાઓ, ક્રેડિટ સીમાઓ અને ઉપલબ્ધ કાર્ડ ઉત્પાદનો વિશે માહિતી માટે, કૃપયા તમારી બેંકિંગ એપ્લિકેશન તપાસો અથવા આমના ગ્રાહક સેવા ટીમને સંપર્ક કરો. હું તમને કેવી રીતે મદદ કરી શકું?",
        'default': "હું સમજી ગયો કે તમે બેંકિંગ સેવાઓ વિશે પૂછી રહ્યા છો. કૃપયા વધુ ચોક્કસ બનો? હું મદદ કરી શકું છું:\n- ખાતા માહિતી અને બેલેન્સ પૂછપરછ\n- વ્યવહાર ઇતિહાસ\n- પૈસા ટ્રાન્સફર\n- લોન માહિતી\n- કાર્ડ સેવાઓ"
    },
    'bn': {
        'greeting': "হ্যালো! আমি আপনার ভার্চুয়াল ব্যাংকিং সহায়ক। আজ আমি আপনাকে কীভাবে সাহায্য করতে পারি?",
        'balance': "আপনার বর্তমান অ্যাকাউন্ট ব্যালেন্স পরীক্ষা করতে, দয়া করে আপনার অ্যাকাউন্টে লগইন করুন বা আপনার ব্যাংকিং অ্যাপ ব্যবহার করুন। প্রয়োজনে আমি আপনাকে প্রক্রিয়াটির মধ্য দিয়ে গাইড করতে পারি। আপনি আর কী করতে চান?",
        'transactions': "আপনি আপনার ব্যাংকিং অ্যাপের মাধ্যমে বা আপনার অ্যাকাউন্টে লগইন করে আপনার লেনদেনের ইতিহাস দেখতে পারেন। আমি আপনাকে আরও সাহায্য করতে পারি?",
        'transfer': "আমি আপনাকে অর্থ স্থানান্তর সম্পর্কে গাইড করতে সাহায্য করতে পারি। এগিয়ে যাওয়ার জন্য, আপনাকে আপনার ব্যাংকিং অ্যাপ বা অনলাইন পোর্টাল ব্যবহার করতে হবে। দয়া করে বলুন আপনি কী স্থানান্তর করতে চান।",
        'loans': "আমরা ব্যক্তিগত ঋণ, গৃহ ঋণ এবং গাড়ির ঋণ সহ বিভিন্ন ঋণ পণ্য প্রদান করি। আপনি কি কোনো নির্দিষ্ট ঋণ পণ্য বা যোগ্যতার মানদণ্ড সম্পর্কে আরও জানতে চান?",
        'cards': "আপনার কার্ড সেবা, ক্রেডিট সীমা এবং উপলব্ধ কার্ড পণ্যগুলির তথ্যের জন্য, দয়া করে আপনার ব্যাংকিং অ্যাপ চেক করুন বা আমাদের গ্রাহক সেবা দলের সাথে যোগাযোগ করুন। আমি আপনাকে কীভাবে সাহায্য করতে পারি?",
        'default': "আমি বুঝেছি যে আপনি ব্যাংকিং সেবা সম্পর্কে জিজ্ঞাসা করছেন। দয়া করে আরও নির্দিষ্ট হন? আমি সাহায্য করতে পারি:\n- অ্যাকাউন্ট তথ্য এবং ব্যালেন্স তদন্ত\n- লেনদেনের ইতিহাস\n- অর্থ স্থানান্তর\n- ঋণ সম্পর্কিত তথ্য\n- কার্ড সেবা"
    },
    'or': {
        'greeting': "ନମସ୍କାର! ମୁଁ ଆପଣଙ୍କର ଭର୍ଚୁଆଲ ବ୍ୟାଙ୍କିଂ ସହାୟକ। ଆଜି ମୁଁ ଆପଣଙ୍କୁ କିପରି ସହାୟତା କରିପାରିବି?",
        'balance': "ଆପଣଙ୍କର ବର୍ତ୍ତମାନ ଖାତା ବ୍ୟାଲେନ୍ସ ଯାଞ୍ଚ କରିବା ପାଇଁ, ଦୟାକରି ଆପଣଙ୍କର ଖାତାରେ ଲଗଇନ କରନ୍ତୁ କିମ୍ବା ଆପଣଙ୍କର ବ୍ୟାଙ୍କିଂ ଆପ୍ ବ୍ୟବହାର କରନ୍ତୁ। ଆବଶ୍ୟକତା ପଡ଼ିଲେ, ମୁଁ ପ୍ରକ୍ରିୟା ମଧ୍ୟମେ ଆପଣଙ୍କୁ ଗାଇଡ କରିପାରିବି। ଆପଣ କ'ଣ କରିବାକୁ ଚାହୁଁଛନ୍ତି?",
        'transactions': "ଆପଣଙ୍କର ବ୍ୟାଙ୍କିଂ ଆପ୍ ବ୍ୟବହାର କରନ୍ତୁ କିମ୍ବା ଆପଣଙ୍କର ଖାତାରେ ଲଗଇନ କରନ୍ତୁ, ତେଣୁଆପଣଙ୍କର ବେବହୃତ ବୃତ୍ତାନୀ ସୂଚୀ ପୂରଣ କରନ୍ତୁ। ମୁଁ ଆପଣଙ୍କୁ ସହଯୋଗ କରିପାरିବି?",
        'transfer': "ମୁଁ ପଇସା ପଠେଇବା ସମସ୍ୟା ସହ ସହଯୋଗ କରିପାरିବି। ଆଗକୁ ବଢ଼ିବା ପାଇଁ, ଆପଣଙ୍କୁ ଆପଣଙ୍କର ବ୍ୟାଙ୍କିଂ ଆପ୍ କିମ୍ବା ଅନଲାଇନ ପୋର୍ଟାଲ ବ୍ୟବହାର କରିବାକୁ ପଡ଼ିବ। ଦୟାକରି କହନ୍ତୁ ଆପଣ କ'ଣ ପଠେଇବାକୁ ଚାହୁଁଛନ୍ତି?",
        'loans': "ଆମେ ବିଭିନ୍ନ ଋଣ ପ୍ରଦାନ କରୁଛୁ, ଯାହାରେ ବ୍ୟକ୍ତିଗତ ଋଣ, ଘର ଋଣ, ଏବଂ କାର ଋଣ ସମ୍ମିଳିତ। କୌଣସି ବିଶେଷ ଋଣ ପ୍ରକାର ବା ଯୋଗ୍ୟତା କ୍ରିଟେରିଆ ବିଷୟରେ ଆପଣ ଅଧିକ ଜାଣିବାକୁ ଚାହୁଁଛନ୍ତି?",
        'cards': "ଆପଣଙ୍କର କାର୍ଡ ସେବା, କ୍ରେଡିଟ ସୀମା ଏବଂ ଉପଲବ୍ଧ କାର୍ଡ ପ୍ରକାର ବିଷୟରେ ସୂଚନା ପାଇଁ, ଦୟାକରି ଆପଣଙ୍କର ବ୍ୟାଙ୍କିଂ ଆପ୍ ଯାଞ୍ଚ କରନ୍ତୁ କିମ୍ବା ଆମର କଷ୍ଟମର ସପୋର୍ଟ ଟିମକୁ ସମ୍ପର୍କ କରନ୍ତୁ। ମୁଁ ଆପଣଙ୍କୁ କିପରି ସହାୟତା କରିପାरିବି?",
        'default': "ମୁଁ ବୁଝିପାରିଛି ଯେ ଆପଣ ବ୍ୟାଙ୍କିଂ ସେବା ବିଷୟରେ ପ୍ରଶ୍ନ କରୁଛନ୍ତି। ଦୟାକରି ଅଧିକ ସୂଚନା ଦିଅନ୍ତୁ? ମୁଁ ସହାୟତା କରିପାରିବି:\n- ଖାତା ସୂଚନା ଏବଂ ବ୍ୟାଲେନ୍ସ ପ୍ରଶ୍ନ\n- ବେବହୃତ ବୃତ୍ତାନୀ\n- ପଇସା ପଠେଇବା\n- ଋଣ ସୂଚନା\n- କାର୍ଡ ସେବା"
    },
    'es': {
        'greeting': "¡Hola! Soy tu asistente de banca virtual. ¿Cómo puedo ayudarte hoy?",
        'balance': "Para verificar tu saldo de cuenta actual, inicia sesión en tu cuenta o usa tu aplicación bancaria. Si es necesario, puedo guiarte a través del proceso. ¿Qué más deseas hacer?",
        'transactions': "Puedes ver tu historial de transacciones a través de tu aplicación bancaria o iniciando sesión en tu cuenta en línea. ¿Puedo ayudarte en algo más?",
        'transfer': "Puedo ayudarte a guiarte con transferencias de dinero. Para continuar, deberás usar tu aplicación bancaria o portal en línea. Por favor, cuéntame qué deseas transferir.",
        'loans': "Ofrecemos varios productos de préstamo incluyendo préstamos personales, préstamos hipotecarios y préstamos para automóviles. ¿Te gustaría saber más sobre algún producto de préstamo específico o los criterios de elegibilidad?",
        'cards': "Para obtener información sobre tus servicios de tarjeta, límites de crédito y productos de tarjeta disponibles, consulta tu aplicación bancaria o ponte en contacto con nuestro equipo de atención al cliente. ¿Cómo puedo ayudarte?",
        'default': "Entiendo que estás preguntando sobre servicios bancarios. ¿Podrías ser más específico? Puedo ayudarte con:\n- Información de cuenta e investigación de saldo\n- Historial de transacciones\n- Transferencias de dinero\n- Información de préstamos\n- Servicios de tarjeta"
    },
    'fr': {
        'greeting': "Bonjour! Je suis votre assistant bancaire virtuel. Comment puis-je vous aider aujourd'hui?",
        'balance': "Pour vérifier votre solde de compte actuel, veuillez vous connecter à votre compte ou utiliser votre application bancaire. Si nécessaire, je peux vous guider à travers le processus. Que désirez-vous faire d'autre?",
        'transactions': "Vous pouvez consulter votre historique de transactions via votre application bancaire ou en vous connectant à votre compte en ligne. Puis-je vous aider autrement?",
        'transfer': "Je peux vous aider à vous guider dans les virements d'argent. Pour continuer, vous devrez utiliser votre application bancaire ou portail en ligne. Veuillez me dire ce que vous souhaitez transférer.",
        'loans': "Nous offrons plusieurs produits de prêt, notamment des prêts personnels, des prêts immobiliers et des prêts automobiles. Aimeriez-vous en savoir plus sur un produit de prêt spécifique ou les critères d'admissibilité?",
        'cards': "Pour obtenir des informations sur vos services de carte, limites de crédit et produits de carte disponibles, veuillez consulter votre application bancaire ou contacter notre équipe d'assistance clientèle. Comment puis-je vous aider?",
        'default': "Je comprends que vous posez des questions sur les services bancaires. Pouvez-vous être plus précis? Je peux vous aider avec:\n- Informations de compte et demandes de solde\n- Historique des transactions\n- Transferts d'argent\n- Informations sur les prêts\n- Services de carte"
    },
    'de': {
        'greeting': "Hallo! Ich bin Ihr virtueller Bankassistent. Wie kann ich Ihnen heute helfen?",
        'balance': "Um Ihren aktuellen Kontostand zu überprüfen, melden Sie sich bitte bei Ihrem Konto an oder verwenden Sie Ihre Banking-App. Falls erforderlich, kann ich Sie durch den Prozess führen. Was möchten Sie sonst noch tun?",
        'transactions': "Sie können Ihren Transaktionsverlauf über Ihre Banking-App oder durch Anmeldung bei Ihrem Online-Konto einsehen. Kann ich Ihnen sonst noch helfen?",
        'transfer': "Ich kann Ihnen dabei helfen, Geldtransfers durchzuführen. Um fortzufahren, müssen Sie Ihre Banking-App oder Ihr Online-Portal verwenden. Bitte teilen Sie mir mit, was Sie transferieren möchten.",
        'loans': "Wir bieten verschiedene Kreditprodukte an, darunter Privatkredite, Wohnungsbaudarlehen und Autokredite. Möchten Sie mehr über ein bestimmtes Kreditprodukt oder die Anspruchsvoraussetzungen erfahren?",
        'cards': "Für Informationen zu Ihren Kartendiensten, Kreditlimits und verfügbaren Kartenprodukten wenden Sie sich bitte an Ihre Banking-App oder kontaktieren Sie unser Kundensupport-Team. Wie kann ich Ihnen helfen?",
        'default': "Ich verstehe, dass Sie Fragen zu Bankdienstleistungen haben. Können Sie präziser sein? Ich kann Ihnen helfen mit:\n- Kontoinformationen und Saldoanfragen\n- Transaktionsverlauf\n- Geldtransfers\n- Kreditinformationen\n- Kartendienste"
    },
    'pt': {
        'greeting': "Olá! Sou seu assistente bancário virtual. Como posso ajudá-lo hoje?",
        'balance': "Para verificar seu saldo de conta atual, faça login em sua conta ou use seu aplicativo bancário. Se necessário, posso guiá-lo pelo processo. O que mais gostaria de fazer?",
        'transactions': "Você pode visualizar seu histórico de transações através de seu aplicativo bancário ou fazendo login em sua conta online. Posso ajudá-lo com mais alguma coisa?",
        'transfer': "Posso ajudá-lo a orientá-lo com transferências de dinheiro. Para prosseguir, você precisará usar seu aplicativo bancário ou portal online. Por favor, me diga o que deseja transferir.",
        'loans': "Oferecemos vários produtos de empréstimo, incluindo empréstimos pessoais, empréstimos imobiliários e empréstimos para automóveis. Gostaria de saber mais sobre um produto de empréstimo específico ou os critérios de elegibilidade?",
        'cards': "Para obter informações sobre seus serviços de cartão, limites de crédito e produtos de cartão disponíveis, consulte seu aplicativo bancário ou entre em contato com nossa equipe de suporte ao cliente. Como posso ajudá-lo?",
        'default': "Entendo que está fazendo perguntas sobre serviços bancários. Poderia ser mais específico? Posso ajudá-lo com:\n- Informações de conta e investigações de saldo\n- Histórico de transações\n- Transferências de dinheiro\n- Informações sobre empréstimos\n- Serviços de cartão"
    },
    'zh': {
        'greeting': "你好！我是您的虚拟银行助手。今天我能如何帮助您？",
        'balance': "要检查您当前的账户余额，请登录您的账户或使用您的银行应用程序。如果需要，我可以指导您完成流程。您还想做什么？",
        'transactions': "您可以通过您的银行应用程序或登录您的在线账户来查看您的交易历史。我还能帮您做些什么？",
        'transfer': "我可以帮助您指导如何进行转账。要继续，您需要使用您的银行应用程序或在线门户。请告诉我您想转账什么。",
        'loans': "我们提供多种贷款产品，包括个人贷款、住房贷款和汽车贷款。您想了解更多关于特定贷款产品或资格标准的信息吗？",
        'cards': "有关您的卡服务、信用额度和可用卡产品的信息，请查看您的银行应用程序或联系我们的客户支持团队。我能如何帮助您？",
        'default': "我理解您在询问有关银行服务的问题。您能更具体一些吗？我可以帮助您：\n- 账户信息和余额查询\n- 交易历史\n- 转账\n- 贷款信息\n- 卡服务"
    },
    'ja': {
        'greeting': "こんにちは！私はあなたのバーチャルバンキングアシスタントです。今日はどうお手伝いしましょうか？",
        'balance': "現在のアカウント残高を確認するには、アカウントにログインするか、バンキングアプリを使用してください。必要に応じて、プロセスをガイドすることができます。他に何がしたいですか？",
        'transactions': "バンキングアプリを使用するか、オンラインアカウントにログインして、取引履歴を表示できます。他にお手伝いできることはありますか？",
        'transfer': "送金に関するガイダンスをお手伝いすることができます。続行するには、バンキングアプリまたはオンラインポータルを使用する必要があります。何を転送したいかを教えてください。",
        'loans': "個人ローン、住宅ローン、自動車ローンなど、さまざまなローン商品を提供しています。特定のローン商品または適格基準についてもっと知りたいですか？",
        'cards': "カードサービス、クレジット限度額、利用可能なカード商品に関する情報については、バンキングアプリをご確認いただくか、カスタマーサポートチームにお問い合わせください。どのようにお手伝いしましょうか？",
        'default': "銀行サービスについてのお問い合わせですね。もっと具体的にしていただけますか？お手伝いできることは：\n- アカウント情報と残高照会\n- 取引履歴\n- 送金\n- ローン情報\n- カードサービス"
    },
    'ko': {
        'greeting': "안녕하세요! 저는 당신의 가상 은행 보조원입니다. 오늘 어떻게 도와드릴까요?",
        'balance': "현재 계정 잔액을 확인하려면 계정에 로그인하거나 뱅킹 앱을 사용하십시오. 필요하면 프로세스를 안내해드릴 수 있습니다. 다른 무엇을 하고 싶으신가요?",
        'transactions': "뱅킹 앱을 통해 또는 온라인 계정에 로그인하여 거래 내역을 볼 수 있습니다. 다른 도움이 필요하신가요?",
        'transfer': "송금에 대해 안내를 도와드릴 수 있습니다. 진행하려면 뱅킹 앱 또는 온라인 포털을 사용해야 합니다. 무엇을 송금하고 싶으신지 알려주세요.",
        'loans': "개인 대출, 주택 대출, 자동차 대출을 포함한 다양한 대출 상품을 제공합니다. 특정 대출 상품 또는 자격 기준에 대해 더 알고 싶으신가요?",
        'cards': "카드 서비스, 신용 한도 및 이용 가능한 카드 상품에 대한 정보는 뱅킹 앱을 확인하거나 고객 지원 팀에 문의하세요. 어떻게 도와드릴까요?",
        'default': "은행 서비스에 대해 문의하시는 것 같습니다. 더 구체적으로 말씀해주시겠어요? 도움을 드릴 수 있는 것들:\n- 계정 정보 및 잔액 조회\n- 거래 내역\n- 송금\n- 대출 정보\n- 카드 서비스"
    },
    'ar': {
        'greeting': "مرحبا! أنا مساعدك المصرفي الافتراضي. كيف يمكنني مساعدتك اليوم؟",
        'balance': "للتحقق من رصيد حسابك الحالي، يرجى تسجيل الدخول إلى حسابك أو استخدام تطبيق الخدمات المصرفية الخاص بك. إذا لزم الأمر، يمكنني إرشادك خلال العملية. ماذا تريد أن تفعل بعد ذلك؟",
        'transactions': "يمكنك عرض سجل المعاملات الخاص بك من خلال تطبيق الخدمات المصرفية أو بتسجيل الدخول إلى حسابك عبر الإنترنت. هل يمكنني مساعدتك في شيء آخر؟",
        'transfer': "يمكنني مساعدتك في توجيهك بشأن تحويلات الأموال. للمتابعة، ستحتاج إلى استخدام تطبيق الخدمات المصرفية أو البوابة الإلكترونية. يرجى إخباري بما تريد تحويله.",
        'loans': "نحن نقدم عدة منتجات قروض بما في ذلك القروض الشخصية والقروض العقارية وقروض السيارات. هل تريد معرفة المزيد عن منتج قرض معين أو معايير التأهيل؟",
        'cards': "للحصول على معلومات حول خدمات بطاقتك وحدود الائتمان والمنتجات المتاحة، يرجى التحقق من تطبيق الخدمات المصرفية أو الاتصال بفريق دعم العملاء لدينا. كيف يمكنني مساعدتك؟",
        'default': "أفهم أنك تسأل عن الخدمات المصرفية. هل يمكنك أن تكون أكثر تحديداً؟ يمكنني مساعدتك في:\n- معلومات الحساب واستفسارات الرصيد\n- سجل المعاملات\n- تحويلات الأموال\n- معلومات القروض\n- خدمات البطاقة"
    },
    'ru': {
        'greeting': "Привет! Я ваш виртуальный банковский помощник. Как я могу вам помочь сегодня?",
        'balance': "Чтобы проверить текущий баланс вашего счета, пожалуйста, войдите в свой счет или используйте мобильное приложение банка. При необходимости я могу помочь вам пройти через процесс. Что еще вы хотите сделать?",
        'transactions': "Вы можете просмотреть историю транзакций через мобильное приложение банка или войдя в свой онлайн-счет. Могу ли я помочь вам еще чем-то?",
        'transfer': "Я могу помочь вам с переводом денег. Для продолжения вам нужно использовать мобильное приложение банка или онлайн-портал. Пожалуйста, скажите мне, что вы хотите перевести.",
        'loans': "Мы предлагаем различные кредитные продукты, включая личные кредиты, ипотеку и автокредиты. Хотели бы вы узнать больше о конкретном кредитном продукте или критериях квалификации?",
        'cards': "Для получения информации о ваших карточных услугах, лимитах кредита и доступных карточных продуктах, пожалуйста, проверьте мобильное приложение банка или свяжитесь с нашей командой поддержки клиентов. Как я могу вам помочь?",
        'default': "Я понимаю, что вы спрашиваете о банковских услугах. Можете ли вы быть более конкретным? Я могу помочь вам:\n- Информация о счете и запросы баланса\n- История транзакций\n- Переводы денег\n- Информация о кредитах\n- Карточные услуги"
    }
}
