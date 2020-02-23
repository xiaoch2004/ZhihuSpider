config = {
         'API': {
             'host': 'https://www.zhihu.com',
             'answer': 'https://www.zhihu.com/api/v4/answers/{item_id}?include=data[*].voteup_count,content',
             'article': 'https://api.zhihu.com/articles/{item_id}',
             'question': 'https://www.zhihu.com/api/v4/questions/{item_id}/answers?include=data[*].voteup_count,content&limit={limit}&offset={offset}&sort_by={sort_by}',
             'column': 'https://zhuanlan.zhihu.com/api/columns/{item_id}/articles?include=data[*].voteup_count&limit={limit}&offset={offset}',
             'column_meta': 'https://www.zhihu.com/api/v4/columns/{item_id}?include=title,articles_count',
             'question_meta': 'https://www.zhihu.com/api/v4/questions/{item_id}?include=title',
             'answer_link': 'https://www.zhihu.com/question/{question_id}/answer/{answer_id}',
             'article_link': 'https://zhuanlan.zhihu.com/p/{article_id}',
             'author_homepage': 'https://www.zhihu.com/people/{user_id}',
             'user_answers': 'https://www.zhihu.com/api/v4/members/{item_id}/answers?include=data[*].content,voteup_count,created_time&limit={limit}&offset={offset}&sort_by={sort_by}',
             'user_articles': 'https://www.zhihu.com/api/v4/members/{item_id}/articles?include=data[*].content&offset={offset}&limit={limit}&sort_by={sort_by}',
             'user_meta': 'https://www.zhihu.com/api/v4/members/{item_id}?include=allow_message',
             'collection': 'https://www.zhihu.com/collection/{item_id}?page={page}',
             'collection_meta': 'https://api.zhihu.com/collections/{item_id}',
             'SORT_BY_VOT': 'voteups',
             'SORT_BY_DEF': 'default',
             'SORT_BY_DAT': 'created',
             'PLATFORM': 'desktop',
             },
         'ColumnManage': {
             'config_file': 'zhihu\\conf\\column_status',
             'title_reg': '"title":\\s*"(.+?)"',
             'totals_reg': '"articles_count":\\s*(\\d+)',
             },
         'Crawler': {
             'user-agent': {
                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
                 },
             },
         'QuestionManage': {
             'Chinese_reg': '[\\u4e00-\\u9fa5]',
             'img_reg': 'https?[^<>"_]_r.jpg',
             'title_reg': '"title":\\s*"(.+?)"',
             },
         'core': {
             'AVATAR_SIZE': 'l',
             'running': '正在获取文章 ID ...',
             'SLEEP': 5,
             'STYLE': 0,
             },
         'head': {
             'style': {
                 'styleCode': {
                     'code': '.highlight .c { color: #999999; font-style: italic }\n.highlight .err { color: #a61717;}\n.highlight .esc { color: #d0d0d0 }\n.highlight .g { color: #d0d0d0 }\n.highlight .k { color: #6ab825; font-weight: bold }\n.highlight .l { color: #d0d0d0 }\n.highlight .n { color: #d0d0d0 }\n.highlight .o { color: #d0d0d0 }\n.highlight .x { color: #d0d0d0 }\n.highlight .p { color: #d0d0d0 }\n.highlight .ch { color: #999999; font-style: italic }\n.highlight .cm { color: #999999; font-style: italic }\n.highlight .cp { color: #cd2828; font-weight: bold }\n.highlight .cpf { color: #999999; font-style: italic }\n.highlight .c1 { color: #999999; font-style: italic }\n.highlight .cs { color: #e50808; font-weight: bold;}\n.highlight .gd { color: #d22323 }\n.highlight .ge { color: #d0d0d0; font-style: italic }\n.highlight .gr { color: #d22323 }\n.highlight .gh { color: #ffffff; font-weight: bold }\n.highlight .gi { color: #589819 }\n.highlight .go { color: #cccccc }\n.highlight .gp { color: #aaaaaa }\n.highlight .gs { color: #d0d0d0; font-weight: bold }\n.highlight .gu { color: #ffffff;}\n.highlight .gt { color: #d22323 }\n.highlight .kc { color: #6ab825; font-weight: bold }\n.highlight .kd { color: #6ab825; font-weight: bold }\n.highlight .kn { color: #6ab825; font-weight: bold }\n.highlight .kp { color: #6ab825 }\n.highlight .kr { color: #6ab825; font-weight: bold }\n.highlight .kt { color: #6ab825; font-weight: bold }\n.highlight .ld { color: #d0d0d0 }\n.highlight .m { color: #3677a9 }\n.highlight .s { color: #ed9d13 }\n.highlight .na { color: #bbbbbb }\n.highlight .nb { color: #24909d }\n.highlight .nc { color: #447fcf;}\n.highlight .no { color: #40ffff }\n.highlight .nd { color: #ffa500 }\n.highlight .ni { color: #d0d0d0 }\n.highlight .ne { color: #bbbbbb }\n.highlight .nf { color: #447fcf }\n.highlight .nl { color: #d0d0d0 }\n.highlight .nn { color: #447fcf;}\n.highlight .nx { color: #d0d0d0 }\n.highlight .py { color: #d0d0d0 }\n.highlight .nt { color: #6ab825; font-weight: bold }\n.highlight .nv { color: #40ffff }\n.highlight .ow { color: #6ab825; font-weight: bold }\n.highlight .w { color: #666666 }\n.highlight .mb { color: #3677a9 }\n.highlight .mf { color: #3677a9 }\n.highlight .mh { color: #3677a9 }\n.highlight .mi { color: #3677a9 }\n.highlight .mo { color: #3677a9 }\n.highlight .sa { color: #ed9d13 }\n.highlight .sb { color: #ed9d13 }\n.highlight .sc { color: #ed9d13 }\n.highlight .dl { color: #ed9d13 }\n.highlight .sd { color: #ed9d13 }\n.highlight .s2 { color: #ed9d13 }\n.highlight .se { color: #ed9d13 }\n.highlight .sh { color: #ed9d13 }\n.highlight .si { color: #ed9d13 }\n.highlight .sx { color: #ffa500 }\n.highlight .sr { color: #ed9d13 }\n.highlight .s1 { color: #ed9d13 }\n.highlight .ss { color: #ed9d13 }\n.highlight .bp { color: #24909d }\n.highlight .fm { color: #447fcf }\n.highlight .vc { color: #40ffff }\n.highlight .vg { color: #40ffff }\n.highlight .vi { color: #40ffff }\n.highlight .vm { color: #40ffff }\n.highlight .il { color: #3677a9 }\n.highlight .hll { background-color: #404040 }\n.highlight {\n\tmargin: 40px 0;\n    background: #2f3640;\n    color: #fff;\n\tpadding: 20px 20px;\n\tfont-size: 16px;\n\toverflow: auto;\n\tborder-radius: 8px;\n}',
                     'file_name': 'styleCode',
                     'format_code': '.highlight .c{ color: #999999; font-style: italic}.highlight .err{ color: #a61717;}.highlight .esc{ color: #d0d0d0}.highlight .g{ color: #d0d0d0}.highlight .k{ color: #6ab825; font-weight: bold}.highlight .l{ color: #d0d0d0}.highlight .n{ color: #d0d0d0}.highlight .o{ color: #d0d0d0}.highlight .x{ color: #d0d0d0}.highlight .p{ color: #d0d0d0}.highlight .ch{ color: #999999; font-style: italic}.highlight .cm{ color: #999999; font-style: italic}.highlight .cp{ color: #cd2828; font-weight: bold}.highlight .cpf{ color: #999999; font-style: italic}.highlight .c1{ color: #999999; font-style: italic}.highlight .cs{ color: #e50808; font-weight: bold;}.highlight .gd{ color: #d22323}.highlight .ge{ color: #d0d0d0; font-style: italic}.highlight .gr{ color: #d22323}.highlight .gh{ color: #ffffff; font-weight: bold}.highlight .gi{ color: #589819}.highlight .go{ color: #cccccc}.highlight .gp{ color: #aaaaaa}.highlight .gs{ color: #d0d0d0; font-weight: bold}.highlight .gu{ color: #ffffff;}.highlight .gt{ color: #d22323}.highlight .kc{ color: #6ab825; font-weight: bold}.highlight .kd{ color: #6ab825; font-weight: bold}.highlight .kn{ color: #6ab825; font-weight: bold}.highlight .kp{ color: #6ab825}.highlight .kr{ color: #6ab825; font-weight: bold}.highlight .kt{ color: #6ab825; font-weight: bold}.highlight .ld{ color: #d0d0d0}.highlight .m{ color: #3677a9}.highlight .s{ color: #ed9d13}.highlight .na{ color: #bbbbbb}.highlight .nb{ color: #24909d}.highlight .nc{ color: #447fcf;}.highlight .no{ color: #40ffff}.highlight .nd{ color: #ffa500}.highlight .ni{ color: #d0d0d0}.highlight .ne{ color: #bbbbbb}.highlight .nf{ color: #447fcf}.highlight .nl{ color: #d0d0d0}.highlight .nn{ color: #447fcf;}.highlight .nx{ color: #d0d0d0}.highlight .py{ color: #d0d0d0}.highlight .nt{ color: #6ab825; font-weight: bold}.highlight .nv{ color: #40ffff}.highlight .ow{ color: #6ab825; font-weight: bold}.highlight .w{ color: #666666}.highlight .mb{ color: #3677a9}.highlight .mf{ color: #3677a9}.highlight .mh{ color: #3677a9}.highlight .mi{ color: #3677a9}.highlight .mo{ color: #3677a9}.highlight .sa{ color: #ed9d13}.highlight .sb{ color: #ed9d13}.highlight .sc{ color: #ed9d13}.highlight .dl{ color: #ed9d13}.highlight .sd{ color: #ed9d13}.highlight .s2{ color: #ed9d13}.highlight .se{ color: #ed9d13}.highlight .sh{ color: #ed9d13}.highlight .si{ color: #ed9d13}.highlight .sx{ color: #ffa500}.highlight .sr{ color: #ed9d13}.highlight .s1{ color: #ed9d13}.highlight .ss{ color: #ed9d13}.highlight .bp{ color: #24909d}.highlight .fm{ color: #447fcf}.highlight .vc{ color: #40ffff}.highlight .vg{ color: #40ffff}.highlight .vi{ color: #40ffff}.highlight .vm{ color: #40ffff}.highlight .il{ color: #3677a9}.highlight .hll{ background-color: #404040}.highlight{\tmargin: 40px 0;background: #2f3640;color: #fff;\tpadding: 20px 20px;\tfont-size: 16px;\toverflow: auto;\tborder-radius: 8px;}',
                     },
                 'styleMod': {
                     'code': '/*自定义的模块样式表*/\n\n\n.background-image {\n  text-align: center;\n  max-width: inherit;\n}\n.background-image img{\n  max-width: 100%;\n}\n/*video box*/\n.video {\n  max-width: inherit;\n  margin: 80px auto;\n}\n.video-cover {\n  max-width: inherit;\n  background-color: #141216;\n}\n.video img {\n  height: 400px;\n  display: block;\n  margin: 0 auto;\n}\n.video-tip {\n  border-radius: 0 0 8px 8px;\n  max-width: inherit;\n  height: 34px;\n  text-align: center;\n}\n/*header*/\n.header {\n  margin-bottom: 80px;\n}\n.title {\n  font-size: 36px;\n  margin-bottom: 80px;\n  text-align: center;\n  line-height: 42px;\n}\n.AuthorInfo,\n.Avatar {\n  border-radius: 5px;\n}\n.Popover {\n  width: 50px;\n  height: 50px;\n}\n.AuthorInfo {\n  width: 240px;\n  margin: auto;\n}\n.AuthorInfo-content {\n  position: relative;\n  left: 60px;\n  top: -50px;\n  line-height: 1em;\n  padding: 6px 0;\n}\n.AuthorInfo-name {\n  font-size: 28px;\n}\n.AuthorInfo-detail {\n  font-size: 16px;\n  margin-top: 8px;\n}\n.Popover,\n.AuthorInfo,\n.AuthorInfo-content,\n.AuthorInfo {\n  height: 50px;\n}\n\n/*LinkCard*/\n.LinkCard {\n  margin: 1em auto;\n  width: 390px !important;\n  border-radius: 12px;\n}\n\n.LinkCard-content {\n  position: relative;\n  display: -webkit-box;\n  display: -ms-flexbox;\n  display: flex;\n  -webkit-box-align: center;\n  -ms-flex-align: center;\n  align-items: center;\n  -webkit-box-pack: justify;\n  -ms-flex-pack: justify;\n  justify-content: space-between;\n  padding: 12px;\n  border-radius: inherit;\n  background-color: hsla(0, 0%, 96.5%, 0.88);\n}\n.LinkCard-text {\n  overflow: hidden;\n}\n.LinkCard-title {\n  display: -webkit-box;\n  -webkit-line-clamp: 2;\n  -webkit-box-orient: vertical;\n  overflow: hidden;\n  text-overflow: ellipsis;\n  max-height: 40px;\n  font-size: 16px;\n  font-weight: 500;\n  line-height: 1.25;\n  color: #1a1a1a;\n}\n.LinkCard-meta {\n  display: -webkit-box;\n  display: -ms-flexbox;\n  display: flex;\n  margin-top: 4px;\n  font-size: 14px;\n  line-height: 20px;\n  color: #999;\n  white-space: nowrap;\n}\n.LinkCard-imageCell {\n  margin-left: 8px;\n  border-radius: 6px;\n}\n.LinkCard-image {\n  display: block;\n  margin: 0 !important;\n  width: 60px;\n  height: 60px;\n  -o-object-fit: cover;\n  object-fit: cover;\n  border-radius: inherit;\n}\n.LinkCard-image--default {\n  display: -webkit-box;\n  display: -ms-flexbox;\n  display: flex;\n  -webkit-box-align: center;\n  -ms-flex-align: center;\n  align-items: center;\n  -webkit-box-pack: center;\n  -ms-flex-pack: center;\n  justify-content: center;\n  background-color: #ebebeb;\n  color: #d3d3d3;\n}\nsvg:not(:root) {\n  overflow: hidden;\n}\n\n.TipCard,\n.LinkCard {\n  position: relative;\n  display: block;\n  width: inherit;\n  -webkit-box-sizing: border-box;\n  box-sizing: border-box;\n  max-width: 100%;\n  overflow: hidden;\n  text-indent: 0 !important;\n}\n\n.TipCard,\n.LinkCard,\n.TipCard:hover,\n.LinkCard:hover {\n  text-decoration: none;\n  border: none !important;\n  color: inherit !important;\n}\n\n.TipCard-backdrop,\n.LinkCard-backdrop {\n  position: absolute;\n  top: 0;\n  left: 0;\n  right: 0;\n  bottom: 0;\n  background-repeat: no-repeat;\n  -webkit-filter: blur(20px);\n  filter: blur(20px);\n  background-size: cover;\n  background-position: 50%;\n}\n\n/* divide */\n.divide{\n    height: 30px;\n    max-width: 45em;\n    margin: 0 auto;\n}\n\n/* reference */\n.reference{\n  text-indent: 0;\n  font-size: 14px;\n}\n\n.reference tr:nth-child(2n){\n  background: white;\n}',
                     'file_name': 'styleMod',
                     'format_code': '.background-image{text-align: center;max-width: inherit;}.background-image img{max-width: 100%;}.video{max-width: inherit;margin: 80px auto;}.video-cover{max-width: inherit;background-color: #141216;}.video img{height: 400px;display: block;margin: 0 auto;}.video-tip{border-radius: 0 0 8px 8px;max-width: inherit;height: 34px;text-align: center;}.header{margin-bottom: 80px;}.title{font-size: 36px;margin-bottom: 80px;text-align: center;line-height: 42px;}.AuthorInfo,.Avatar{border-radius: 5px;}.Popover{width: 50px;height: 50px;}.AuthorInfo{width: 240px;margin: auto;}.AuthorInfo-content{position: relative;left: 60px;top: -50px;line-height: 1em;padding: 6px 0;}.AuthorInfo-name{font-size: 28px;}.AuthorInfo-detail{font-size: 16px;margin-top: 8px;}.Popover,.AuthorInfo,.AuthorInfo-content,.AuthorInfo{height: 50px;}.LinkCard{margin: 1em auto;width: 390px !important;border-radius: 12px;}.LinkCard-content{position: relative;display: -webkit-box;display: -ms-flexbox;display: flex;-webkit-box-align: center;-ms-flex-align: center;align-items: center;-webkit-box-pack: justify;-ms-flex-pack: justify;justify-content: space-between;padding: 12px;border-radius: inherit;background-color: hsla(0, 0%, 96.5%, 0.88);}.LinkCard-text{overflow: hidden;}.LinkCard-title{display: -webkit-box;-webkit-line-clamp: 2;-webkit-box-orient: vertical;overflow: hidden;text-overflow: ellipsis;max-height: 40px;font-size: 16px;font-weight: 500;line-height: 1.25;color: #1a1a1a;}.LinkCard-meta{display: -webkit-box;display: -ms-flexbox;display: flex;margin-top: 4px;font-size: 14px;line-height: 20px;color: #999;white-space: nowrap;}.LinkCard-imageCell{margin-left: 8px;border-radius: 6px;}.LinkCard-image{display: block;margin: 0 !important;width: 60px;height: 60px;-o-object-fit: cover;object-fit: cover;border-radius: inherit;}.LinkCard-image--default{display: -webkit-box;display: -ms-flexbox;display: flex;-webkit-box-align: center;-ms-flex-align: center;align-items: center;-webkit-box-pack: center;-ms-flex-pack: center;justify-content: center;background-color: #ebebeb;color: #d3d3d3;}svg:not(:root){overflow: hidden;}.TipCard,.LinkCard{position: relative;display: block;width: inherit;-webkit-box-sizing: border-box;box-sizing: border-box;max-width: 100%;overflow: hidden;text-indent: 0 !important;}.TipCard,.LinkCard,.TipCard:hover,.LinkCard:hover{text-decoration: none;border: none !important;color: inherit !important;}.TipCard-backdrop,.LinkCard-backdrop{position: absolute;top: 0;left: 0;right: 0;bottom: 0;background-repeat: no-repeat;-webkit-filter: blur(20px);filter: blur(20px);background-size: cover;background-position: 50%;}.divide{height: 30px;max-width: 45em;margin: 0 auto;}.reference{text-indent: 0;font-size: 14px;}.reference tr:nth-child(2n){background: white;}',
                     },
                 'styleText': {
                     'code': '*,\n::after,\n::before {\n  box-sizing: border-box;\n}\n\nbody { \n  font-size: 1.2rem;\n  line-height: 1.5em;\n  background-color: #f6f6f6;\n  font-family: "PT Serif", "Times New Roman", Times, serif, "Helvetica Neue", Helvetica, Arial, sans-serif;\n  color: rgb(31, 9, 9);\n}\n\n.article {\n  max-width: 50em;\n  margin: 0px auto;\n  padding: 6em;\n  background: #fff;\n  overflow: hidden;\n  border-radius: 2px;\n  -webkit-box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);\n  box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);\n  -webkit-box-sizing: border-box;\n  box-sizing: border-box;\n}\n\np {\n  margin-bottom: 1.5em;\n  line-height: inherit;\n}\n\np img[eeimg]{\n  display: inline-block;\n  margin: 0 3px;\n  max-width: 100%;\n  vertical-align: middle;\n}\n\np + ul,\np + ol {\n  margin-top: 0.5em;\n}\n\nblockquote {\n  margin: 0 2em;\n  background: #eee;\n  border-radius: 5px;\n  padding: 15px;\n  color: rgb(101, 101, 101);\n  font-style: italic;\n}\n\nblockquote p {\n  background: #eee;\n  border-radius: 5px;\n}\n\nblockquote p::before {\n  content: "\\201C";\n}\n\nblockquote p::after {\n  content: "\\201D";\n}\nblockquote ul,\nblockquote ol {\n  margin-left: 0px;\n}\nblockquote::before,\nblockquote::after,\nq::before,\nq::after {\n  content: none;\n}\nblockquote > :first-child,\nli > :first-child {\n  margin-top: 0px;\n}\nblockquote > :last-child {\n  margin-bottom: 0px;\n}\nblockquote,\nq {\n  quotes: none;\n}\n\na {\n  cursor: pointer;\n  text-decoration: none;\n  color: #3ac19f;\n}\n\na:hover,\na:active {\n  text-decoration: none;\n  color: #ff6188;\n  outline: 0px;\n}\na.url {\n  word-break: break-all;\n}\n\ntable tr th {\n  border-bottom: 0px;\n}\n\ntable {\n  border-collapse: collapse;\n  border-spacing: 0px;\n  margin-bottom: 1.5em;\n  font-size: 1em;\n  width: 100%;\n  overflow: auto;\n  break-inside: auto;\n  text-align: left;\n}\n\nheader,\nfooter {\n  font-family: "PT Serif", "Times New Roman", Times, serif;\n  color: rgb(31, 9, 9);\n}\nthead {\n  background-color: rgb(218, 218, 218);\n  display: table-header-group;\n}\n\nthead th,\ntfoot th {\n  padding: 0.25em 0.25em 0.25em 0.4em;\n  text-transform: uppercase;\n}\n\ntr {\n  break-inside: avoid;\n  break-after: auto;\n}\n\ntr:nth-child(2n) {\n  background: rgb(232, 231, 231);\n}\n\nth {\n  text-align: left;\n}\n\ntd {\n  vertical-align: top;\n  padding: 0.25em 0.25em 0.25em 0.4em;\n}\n\ntt {\n  font-size: 0.8em;\n  line-height: 1.7em;\n}\n\nol,\nul {\n  text-indent: 0;\n  position: relative;\n  list-style: none;\n  margin: 0px 0px 1.5em 1.5em;\n}\nol li {\n  list-style-type: decimal;\n  list-style-position: outside;\n}\n\nul li {\n  list-style-type: disc;\n  list-style-position: outside;\n}\n\nli div {\n  padding-top: 0px;\n}\n\nli {\n  margin: 0px;\n  margin-left: 2em;\n  position: relative;\n}\nli > figure:last-child {\n  margin-bottom: 0.5rem;\n}\n\nli > :first-child {\n  margin-top: 0px;\n}\n\nli > ul,\nli > ol {\n  margin-top: inherit;\n  margin-bottom: 0px;\n}\n\nli ol > li {\n  list-style-type: lower-alpha;\n}\n\nli li ol > li {\n  list-style-type: lower-roman;\n}\n\nkbd {\n  margin: 0px 0.1em;\n  padding: 0.1em 0.6em;\n  font-size: 0.8em;\n  color: rgb(36, 39, 41);\n  background: rgb(255, 255, 255);\n  border: 1px solid rgb(173, 179, 185);\n  border-radius: 3px;\n  box-shadow: rgba(12, 13, 14, 0.2) 0px 1px 0px,\n    rgb(255, 255, 255) 0px 0px 0px 2px inset;\n  white-space: nowrap;\n  vertical-align: middle;\n}\n\nsamp,\ntt {\n  font-family: var(--monospace);\n}\n\nhr {\n  border-bottom: 1px solid #d6d6d6;\n  margin-inline-start: 15%;\n  margin-inline-end: 15%;\n  margin-block-start: 5rem;\n  margin-block-end: 5rem;\n}\n\nu {\n  text-decoration: none;\n  border-bottom: 1px dashed #f40;\n}\n\nfigure {\n  margin: 2em auto;\n  max-width: 100%;\n  padding: 0px;\n  font-size: 1rem;\n  text-align: center;\n}\n\nfigure img {\n  display: block;\n  max-width: 60%;\n  margin: auto;\n}\n\nfigure figcaption {\n  padding: 0 1em;\n  font-size: 0.9rem;\n  color: #999;\n}\n\nfigure > table {\n  margin: 0px !important;\n}\n\ndiv.hr:focus {\n  cursor: none;\n}\n\na img,\nimg a {\n  cursor: pointer;\n}\n',
                     'file_name': 'styleText',
                     'format_code': '*,::after,::before{box-sizing: border-box;}body{font-size: 1.2rem;line-height: 1.5em;background-color: #f6f6f6;font-family: "PT Serif", "Times New Roman", Times, serif, "Helvetica Neue", Helvetica, Arial, sans-serif;color: rgb(31, 9, 9);}.article{max-width: 50em;margin: 0px auto;padding: 6em;background: #fff;overflow: hidden;border-radius: 2px;-webkit-box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);-webkit-box-sizing: border-box;box-sizing: border-box;}p{margin-bottom: 1.5em;line-height: inherit;}p img[eeimg]{display: inline-block;margin: 0 3px;max-width: 100%;vertical-align: middle;}p + ul,p + ol{margin-top: 0.5em;}blockquote{margin: 0 2em;background: #eee;border-radius: 5px;padding: 15px;color: rgb(101, 101, 101);font-style: italic;}blockquote p{background: #eee;border-radius: 5px;}blockquote p::before{content: "\\201C";}blockquote p::after{content: "\\201D";}blockquote ul,blockquote ol{margin-left: 0px;}blockquote::before,blockquote::after,q::before,q::after{content: none;}blockquote > :first-child,li > :first-child{margin-top: 0px;}blockquote > :last-child{margin-bottom: 0px;}blockquote,q{quotes: none;}a{cursor: pointer;text-decoration: none;color: #3ac19f;}a:hover,a:active{text-decoration: none;color: #ff6188;outline: 0px;}a.url{word-break: break-all;}table tr th{border-bottom: 0px;}table{border-collapse: collapse;border-spacing: 0px;margin-bottom: 1.5em;font-size: 1em;width: 100%;overflow: auto;break-inside: auto;text-align: left;}header,footer{font-family: "PT Serif", "Times New Roman", Times, serif;color: rgb(31, 9, 9);}thead{background-color: rgb(218, 218, 218);display: table-header-group;}thead th,tfoot th{padding: 0.25em 0.25em 0.25em 0.4em;text-transform: uppercase;}tr{break-inside: avoid;break-after: auto;}tr:nth-child(2n){background: rgb(232, 231, 231);}th{text-align: left;}td{vertical-align: top;padding: 0.25em 0.25em 0.25em 0.4em;}tt{font-size: 0.8em;line-height: 1.7em;}ol,ul{text-indent: 0;position: relative;list-style: none;margin: 0px 0px 1.5em 1.5em;}ol li{list-style-type: decimal;list-style-position: outside;}ul li{list-style-type: disc;list-style-position: outside;}li div{padding-top: 0px;}li{margin: 0px;margin-left: 2em;position: relative;}li > figure:last-child{margin-bottom: 0.5rem;}li > :first-child{margin-top: 0px;}li > ul,li > ol{margin-top: inherit;margin-bottom: 0px;}li ol > li{list-style-type: lower-alpha;}li li ol > li{list-style-type: lower-roman;}kbd{margin: 0px 0.1em;padding: 0.1em 0.6em;font-size: 0.8em;color: rgb(36, 39, 41);background: rgb(255, 255, 255);border: 1px solid rgb(173, 179, 185);border-radius: 3px;box-shadow: rgba(12, 13, 14, 0.2) 0px 1px 0px,rgb(255, 255, 255) 0px 0px 0px 2px inset;white-space: nowrap;vertical-align: middle;}samp,tt{font-family: var(--monospace);}hr{border-bottom: 1px solid #d6d6d6;margin-inline-start: 15%;margin-inline-end: 15%;margin-block-start: 5rem;margin-block-end: 5rem;}u{text-decoration: none;border-bottom: 1px dashed #f40;}figure{margin: 2em auto;max-width: 100%;padding: 0px;font-size: 1rem;text-align: center;}figure img{display: block;max-width: 60%;margin: auto;}figure figcaption{padding: 0 1em;font-size: 0.9rem;color: #999;}figure > table{margin: 0px !important;}div.hr:focus{cursor: none;}a img,img a{cursor: pointer;}',
                     },
                 },
             },
         'running': {
             'default_wh': '',
             },
         'tag': {
             'bgg': '<div class="background-image">\n    <img src="__#background-image#__" alt="background image">\n</div>\n',
             'header': '<div class="header">\n    <div class="title">\n        <a href="__#article-origin#__" target="_blank">\n            __#title#__\n        </a>\n    </div>\n    <a class="UserLink-link" target="_blank" href="__#user-link#__">\n        <div class="AuthorInfo">\n            <div class="Popover">\n                <img class="Avatar" width="50" height="50" src="__#user-avatar#__" alt="头像">\n            </div>\n            <div class="AuthorInfo-content">\n                <div class="AuthorInfo-name">\n                    <span>\n                        __#user-name#__\n                    </span>\n                </div>\n                <div class="AuthorInfo-detail">\n                    <span>\n                        __#created-date#__\n                    </span>\n                </div>\n            </div>\n        </div>\n    </a>\n</div>\n',
             'video': '<div class="video">\n    <a href="__#video-link#__" target="_blank">\n        <div class="video-cover">\n            <img src="__#video-cover#__" alt="video cover">\n        </div>\n        <div class="video-tip TipCard">\n            <span class="TipCard-backdrop" style="background-image:url(__#video-cover#__)">\n            </span>\n            <span style="font-size:18px;color:#222;line-height:34px;display:block;">\n                __#video-tip#__\n            </span>\n        </div>\n    </a>\n</div>\n',
             'lc_img': '<a target="_blank" href="__#link-card-url#__" class="LinkCard">\n    <span class="LinkCard-backdrop" style="background-image:url(__#link-card-image#__)">\n    </span>\n    <span class="LinkCard-content">\n        <span class="LinkCard-text">\n            <span class="LinkCard-title">\n                __#link-card-title#__\n            </span>\n            <span class="LinkCard-meta">\n                <span style="display:inline-flex;align-items:center">\n                    \u200b\n                    <svg class="Zi Zi--InsertLink" fill="currentColor" viewBox="0 0 24 24" width="17" height="17">\n                        <path d="M6.77 17.23c-.905-.904-.94-2.333-.08-3.193l3.059-3.06-1.192-1.19-3.059 3.058c-1.489 1.489-1.427 3.954.138 5.519s4.03 1.627 5.519.138l3.059-3.059-1.192-1.192-3.059 3.06c-.86.86-2.289.824-3.193-.08zm3.016-8.673l1.192 1.192 3.059-3.06c.86-.86 2.289-.824 3.193.08.905.905.94 2.334.08 3.194l-3.059 3.06 1.192 1.19 3.059-3.058c1.489-1.489 1.427-3.954-.138-5.519s-4.03-1.627-5.519-.138L9.786 8.557zm-1.023 6.68c.33.33.863.343 1.177.029l5.34-5.34c.314-.314.3-.846-.03-1.176-.33-.33-.862-.344-1.176-.03l-5.34 5.34c-.314.314-.3.846.03 1.177z" fill-rule="evenodd">\n                        </path>\n                    </svg>\n                </span>\n                __#domain#__\n            </span>\n        </span>\n        <span class="LinkCard-imageCell">\n            <img class="LinkCard-image" alt="图标" src="__#link-card-image#__">\n        </span>\n    </span>\n</a>\n',
             'lc_svg': '<a target="_blank" href="__#link-card-url#__" class="LinkCard">\n    <span class="LinkCard-content">\n        <span class="LinkCard-text">\n            <span class="LinkCard-title">\n                __#link-card-title#__\n            </span>\n            <span class="LinkCard-meta">\n                <span style="display:inline-flex;align-items:center">\n                    \u200b\n                    <svg fill="currentColor" viewBox="0 0 24 24" width="17" height="17">\n                        <path d="M6.77 17.23c-.905-.904-.94-2.333-.08-3.193l3.059-3.06-1.192-1.19-3.059 3.058c-1.489 1.489-1.427 3.954.138 5.519s4.03 1.627 5.519.138l3.059-3.059-1.192-1.192-3.059 3.06c-.86.86-2.289.824-3.193-.08zm3.016-8.673l1.192 1.192 3.059-3.06c.86-.86 2.289-.824 3.193.08.905.905.94 2.334.08 3.194l-3.059 3.06 1.192 1.19 3.059-3.058c1.489-1.489 1.427-3.954-.138-5.519s-4.03-1.627-5.519-.138L9.786 8.557zm-1.023 6.68c.33.33.863.343 1.177.029l5.34-5.34c.314-.314.3-.846-.03-1.176-.33-.33-.862-.344-1.176-.03l-5.34 5.34c-.314.314-.3.846.03 1.177z" fill-rule="evenodd">\n                        </path>\n                    </svg>\n                </span>\n                __#domain#__\n            </span>\n        </span>\n        <span class="LinkCard-imageCell">\n            <span class="LinkCard-image LinkCard-image--default">\n                <svg fill="currentColor" viewBox="0 0 24 24" width="32" height="32">\n                    <path d="M11.991 3C7.023 3 3 7.032 3 12s4.023 9 8.991 9C16.968 21 21 16.968 21 12s-4.032-9-9.009-9zm6.237 5.4h-2.655a14.084 14.084 0 0 0-1.242-3.204A7.227 7.227 0 0 1 18.228 8.4zM12 4.836A12.678 12.678 0 0 1 13.719 8.4h-3.438A12.678 12.678 0 0 1 12 4.836zM5.034 13.8A7.418 7.418 0 0 1 4.8 12c0-.621.09-1.224.234-1.8h3.042A14.864 14.864 0 0 0 7.95 12c0 .612.054 1.206.126 1.8H5.034zm.738 1.8h2.655a14.084 14.084 0 0 0 1.242 3.204A7.188 7.188 0 0 1 5.772 15.6zm2.655-7.2H5.772a7.188 7.188 0 0 1 3.897-3.204c-.54.999-.954 2.079-1.242 3.204zM12 19.164a12.678 12.678 0 0 1-1.719-3.564h3.438A12.678 12.678 0 0 1 12 19.164zm2.106-5.364H9.894A13.242 13.242 0 0 1 9.75 12c0-.612.063-1.215.144-1.8h4.212c.081.585.144 1.188.144 1.8 0 .612-.063 1.206-.144 1.8zm.225 5.004c.54-.999.954-2.079 1.242-3.204h2.655a7.227 7.227 0 0 1-3.897 3.204zm1.593-5.004c.072-.594.126-1.188.126-1.8 0-.612-.054-1.206-.126-1.8h3.042c.144.576.234 1.179.234 1.8s-.09 1.224-.234 1.8h-3.042z" fill-rule="evenodd">\n                    </path>\n                </svg>\n            </span>\n        </span>\n    </span>\n</a>\n',
             'ref_ind': '<sup id="ref-ind-__#index#__">\n    <a href="#ref-quo-__#index#__">\n        [__#index#__]\n    </a>\n</sup>\n',
             'quo': '<tr id="ref-quo-__#index#__">\n    <td>\n        <a href="#ref-ind-__#index#__">\n            [__#index#__]\n        </a>\n    </td>\n    <td>\n        <a href="__#ref-url#__" target="_blank">\n            __#ref-title#__\n        </a>\n    </td>\n</tr>\n',
             'header_simple': '<div class="header">\n    <div class="title">\n        <a href="__#article-origin#__" target="_blank">\n            __#title#__\n        </a>\n    </div>\n    <a class="UserLink-link" target="_blank" href="__#user-link#__">\n        <div class="AuthorInfo">\n            <div class="AuthorInfo-content">\n                <div class="AuthorInfo-name">\n                    <span>\n                        作者|__#user-name#__\n                    </span>\n                </div>\n            </div>\n        </div>\n    </a>\n</div>\n',
             },
         'Formatter': {
             'link_card_default_image': 'https://zhstatic.zhihu.com/assets/zhihu/editor/zhihu-card-default.svg',
             },
         }
