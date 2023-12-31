import tkinter as tk
from tkinter import ttk, scrolledtext
import tkinter.font as tkFont
import pandas as pd
import codecs
from PIL import Image, ImageTk

class CollegeRecommendationGUI:
    def __init__(self, master):
        self.mbti_result = None
        self.master = master
        self.master.title("大學科系推薦與MBTI測驗") # 畫面標題
        self.master.geometry("1024x576") # 頁面大小

        self.create_widgets()
        
    
    def create_widgets(self):
        # MBTI Section
        self.mbti_frame = ttk.Frame(self.master)
        self.mbti_frame.pack(side=tk.LEFT, padx=20, pady=20)
      
        self.questions = [
            "1 你通常和哪種人相處得更好？\nA.現實的人\nB.想象力豐富的人\n",
            "2 在群體中，你比較偏好哪種方法？\nA.介紹他人\nB.由別人來介紹你\n",
            "3 你是哪種人？\nA.只要願意就能輕鬆地同幾乎任何人說個沒完\nB.只能在特定場合下或同特定的人才願意講許多話\n",
            "4 喜歡按日程表辦事？\nA.正合你意\nB.束縛了你\n",
            "5 作決定時，對於你來說更重要的是？\nA.考慮人們的感受和觀點\nB.權衡事實\n",
            "6 你更喜歡？\nA.務實且有豐富常識的人\nB.頭腦靈活的人\n",
            "7 你的個性比較像哪個?\nA.寬容\nB.堅定\n",
            "8 對於你新認識的人什麼時候能說出你的興趣所在？\nA.馬上就能\nB.只有當他們真正了解你之後才能\n",
            "9 多數時候，你傾向於？\nA.和他人在一起\nB.獨處\n",
            "10 當有一項特殊工作時，你會？\nA.在開始前精心組織策劃\nB.在工作進行中找出必要環節\n",
            "11 你更想要自己被認為是一個？\nA.善於動手的人\nB.善於創意的人\n",
            "12 當你和一群人在一起時，你會？\nA.參加大家的談話\nB.只同你熟知的人單獨談話\n",
            "13 你更傾向於？\nA.感性地做事\nB.依邏輯行事\n",
            "14 對於制定周末計劃，你覺得？\nA.有必要\nB.沒必要\n",
            "15 如果你是一位老師，你想要教哪一門課？\nA.涉及事實的課程\nB.涉及理論的課程\n",
            "16 你喜歡？\nA.事先安排好約會，聚會等\nB.只要時機恰當就無拘無束地做任何有趣的事\n",
            "17 當你某日想去某個地方，你會？\nA.計劃好將做的事情以及何時做\nB.什麼都不想就去\n",
            "18 你是哪種人?\nA.同情憐憫\nB.深謀遠慮\n",
            "19 你覺得通常別人要花費多久認識你？\nA.一小段時間來了解你\nB.很久來了解你\n",
            "20 你認為被稱為哪種人是更高的讚賞？\nA.感性的人\nB.一貫理性的人\n",
            "21 你更願意把哪種人作為朋友？\nA.腳踏實地的人\nB.常有新觀點的人\n",
            "22 你通常是？\nA.一個善於交際的人\nB.安靜緘默的人\n",
            "23 做很多人都會做的事情時，你喜歡？\nA.按慣例做\nB.按自己獨創的方式做\n",
            "24 往往，你是？\nA.情感駕馭理智\nB.理智駕馭情感\n",
            "25 日常工作中，你喜歡？\nA.通常先安排好工作並加以完成，以免壓力過大\nB.在時間緊迫的情況下爭分奪秒地工作\n",
            "26 當你為了消遣而閱讀時，你會怎麼做？\nA.喜歡作者確切地表達其意思\nB.欣賞奇特新穎的表達方式\n",
            "27 你願意在哪一個老闆（老師）手下工作（學習）？\nA.脾氣好，但前後不一致\nB.對人嚴厲，但有條理\n",
            "28 你更喜歡如何做多數事情？\nA.有計劃地\nB.即興時\n"
        ]
        self.answers = []
        self.current_question_index = 0

        # 使用 Pillow 加載和轉換圖片
        self.canvas = tk.Canvas(self.mbti_frame, width=1024, height=576)
        self.canvas.pack(fill="both", expand=True)

        self.pic=Image.open('mbti_bg.png')
        self.image = self.pic.resize((1024, 576))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.canvas.pack(fill="both", expand=True)

        # 在 Canvas 上放置背景圖片
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        # mbti題目
        self.question_text = self.canvas.create_text(100, 300, text=self.questions[self.current_question_index], 
                                                 width=380, fill="black", font=('jf open 粉圓 2.0', 18), anchor="w", justify="left")
        # A、B選項按鍵
        self.button_a = tk.Button(self.mbti_frame, text="A", command=lambda: self.answer_question("A"), width=10, height=2)
        self.button_a_window = self.canvas.create_window(180, 390, window=self.button_a)

        self.button_b = tk.Button(self.mbti_frame, text="B", command=lambda: self.answer_question("B"), width=10, height=2)
        self.button_b_window = self.canvas.create_window(380, 390, window=self.button_b)

    def create_widgets2(self):
        self.canvas.delete("all")
        self.mbti_frame.pack_forget()

        # Main container
        self.main_container = ttk.Frame(self.master)
        self.main_container.pack(side=tk.RIGHT, padx=20, pady=20)

        # College Recommendation Section
        self.college_frame = ttk.Frame(self.main_container)
        self.college_frame.pack(side=tk.LEFT, padx=20, pady=20)  # 將 college_frame 放在左邊

        self.label_college = tk.Label(self.college_frame, text="請輸入各科分數", font=('jf open 粉圓 2.0', 12))
        #self.label_college.pack(pady=10)

        # Create entry widgets for each subject
        self.entries_college = {}
        subjects_college = ['學測_國文', '學測_英文', '分科_數甲', '學測_數學A', '學測_數學B',
                            '學測_自然', '學測_社會', '分科_地理', '分科_歷史', '分科_公民',
                            '分科_物理', '分科_化學', '分科_生物']


        
        self.canvas = tk.Canvas(self.college_frame, width=1024, height=576)
        self.canvas.pack(fill="both", expand=True)

        self.pic=Image.open('result.png')
        self.image = self.pic.resize((1024, 576))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.canvas.pack(fill="both", expand=True)

        # 在 Canvas 上放置背景圖片
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        for i, subject in enumerate(subjects_college):
            frame = ttk.Frame(self.college_frame)
            label = ttk.Label(frame, text=subject, font=('jf open 粉圓 2.0', 12))
            label.pack(side="left")
            entry = ttk.Entry(frame, font=('jf open 粉圓 2.0', 12))
            entry.pack(side="left")
            y_offset=100
            y_offset = y_offset + i * 25
            self.canvas.create_window((200, y_offset), window=frame, anchor='nw')
            self.entries_college[subject] = entry


        #self.wi = self.canvas.create_window(10, 390, window=self.college_frame)

        self.wi = self.canvas.create_text(200, 80, text='請輸入各科分數:', 
                                                 width=150, fill="black", font=('jf open 粉圓 2.0', 12), anchor="w", justify="left")


        # Create submit button
        self.submit_button_college = tk.Button(self.college_frame, text="提交", command=self.submit_scores_college)
        #submit_button_college.pack(pady=10)
        self.button_a_window = self.canvas.create_window(325, 450, window=self.submit_button_college)

        # Result Frame (right)
        self.result_frame = ttk.Frame(self.college_frame)
        #result_frame.pack(side=tk.RIGHT, padx=20)
        self.a_window = self.canvas.create_window(700, 250, window=self.result_frame)

        # Create scrolled text widget for result
        self.result_text_college = scrolledtext.ScrolledText(self.result_frame, width=60, height=20, wrap=tk.WORD)
        self.result_text_college.pack(fill="both", expand=True)
        #self.b_window = self.canvas.create_window(180, 150, window=self.result_frame)
                                             


    def submit_scores_college(self):
        # Get user-input scores
        user_scores_college = {}

        for subject, entry in self.entries_college.items():
            input_text = entry.get()
            if input_text.strip():  # Check if the input is not empty or contains only whitespace
                try:
                    user_scores_college[subject] = float(input_text)
                except ValueError:
                    self.result_text_college.delete(1.0, tk.END)
                    self.result_text_college.insert(tk.END, f"Error: 不能將'{input_text}'轉換為數字。")
                    return
            else:
                self.result_text_college.delete(1.0, tk.END)
                self.result_text_college.insert(tk.END, f"Error: 請輸入 {subject} 分數。")
                return

        # Load department data
        try:
            with codecs.open('merged_file_new (1).csv', 'r', encoding='big5', errors='ignore') as file:
                df = pd.read_csv(file)
        except UnicodeDecodeError:
            # Handle if there is still an error
            self.result_text_college.delete(1.0, tk.END)
            self.result_text_college.insert(tk.END, "Error: Unable to decode with 'big5' encoding. Please check your file encoding.")
            return

        df = df.fillna(0)
        df = df.sort_values(by='普通生錄取分數', ascending=False)

        # Calculate total score (weighted)
        df['總分'] = sum(user_scores_college[subject] * df[subject] for subject in user_scores_college)

        df['普通生錄取分數'] = pd.to_numeric(df['普通生錄取分數'], errors='coerce')
        accepted_departments = df[(df['總分'] >= df['普通生錄取分數'] - 50) & (df['總分'] <= df['普通生錄取分數'] + 50)]

        # Regroup
        grouped_departments = accepted_departments.groupby('學群')

        # Assume you want to output departments for each target group
        target_groups = set(self.mbti_result)
        if self.mbti_result == "ISTJ":
            target_groups = ['財經學群', '工程學群', '管理學群', '法政學群']
        elif self.mbti_result == "ISFJ":
            target_groups = ['醫藥衛生學群', '生命科學學群', '生物資源學群', '社會與心理學群']
        elif self.mbti_result == 'INFJ':
            target_groups = ['社會與心理學群', '藝術學群', '建築與設計學群']
        elif self.mbti_result == 'INTJ':
            target_groups = ['資訊學群', '工程學群', '財經學群', '法政學群']
        elif self.mbti_result == 'ISTP':
            target_groups = ['資訊學群', '工程學群', '遊憩與運動學群']
        elif self.mbti_result == 'ISFP':
            target_groups = ['藝術學群', '建築與設計學群', '外語學群']
        elif self.mbti_result == 'INFP':
            target_groups = ['文史哲學群', '藝術學群', '社會與心理學群']
        elif self.mbti_result == 'INTP':
            target_groups = ['資訊學群', '工程學群', '數理化學群']
        elif self.mbti_result == 'ESTP':
            target_groups = ['遊憩與運動學群', '管理學群']
        elif self.mbti_result == 'ESFP':
            target_groups = ['大眾傳播學群', '藝術學群', '遊憩與運動學群']
        elif self.mbti_result == 'ENFP':
            target_groups = ['社會與心理學群', '藝術學群']
        elif self.mbti_result == 'ENTP':
            target_groups = ['管理學群', '財經學群', '法政學群']
        elif self.mbti_result == 'ESTJ':
            target_groups = ['工程學群', '財經學群', '管理學群']
        elif self.mbti_result == 'ESFJ':
            target_groups = ['醫藥衛生學群', '生命科學學群', '心理與社會學群', '教育學群', '外語學群']
        elif self.mbti_result == 'ENFJ':
            target_groups = ['教育學群', '心理與社會學群', '醫藥衛生學群']
        else:
            target_groups = ['管理學群', '法政學群', '外語學群']

        result_text = ""

        # Loop through each target group
        for target_group in target_groups:
            if target_group in grouped_departments.groups:
                target_departments = grouped_departments.get_group(target_group)
                result_text += f"\n以下是 {target_group} 中您可能可以考慮的科系：\n"
                result_text += target_departments[['校名', '系組名', '總分']].to_string(index=False, header=False) + "\n"
            else:
                result_text += f"\n沒有找到 {target_group} 相關的科系。\n"

        # Update result text widget
        self.result_text_college.delete(1.0, tk.END)  # Clear previous content
        self.result_text_college.insert(tk.END, result_text)

    def answer_question(self, answer):
        self.answers.append(answer)
        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            new_question = self.questions[self.current_question_index]
            self.canvas.itemconfig(self.question_text, text=new_question)
        else:
            result = self.calculate_result()
            result_text = f"您的 MBTI 结果是: {result}"
            if result == "ISTJ":
                recommand = "推薦：財經學群、工程學群、\n管理學群、法政學群"
            elif result == "ISFJ":
                recommand = '推薦：醫藥衛生學群、生命科學學群、\n生物資源學群、社會與心理學群'
            elif result == 'INFJ':
                recommand = '推薦：社會與心理學群、藝術學群、\n建築與設計學群'
            elif result == 'INTJ':
                recommand = '推薦：資訊學群、工程學群、\n財經學群、法政學群'
            elif result == 'ISTP':
                recommand = '推薦：資訊學群、工程學群、\n遊憩與運動學群'
            elif result == 'ISFP':
                recommand = '推薦：藝術學群、\n建築與設計學群、外語學群'
            elif result == 'INFP':
                recommand = '推薦：文史哲學群、藝術學群、\n社會與心理學群'
            elif result == 'INTP':
                recommand = '推薦：資訊學群、工程學群、\n數理化學群'
            elif result == 'ESTP':
                recommand = '推薦：遊憩與運動學群、管理學群'
            elif result == 'ESFP':
                recommand = '推薦：大眾傳播學群、藝術學群、\n遊憩與運動學群'
            elif result == 'ENFP':
                recommand = '推薦：社會與心理學群、藝術學群'
            elif result == 'ENTP':
                recommand = '推薦：管理學群、財經學群、\n法政學群'
            elif result == 'ESTJ':
                recommand = '推薦：工程學群、財經學群、\n管理學群'
            elif result == 'ESFJ':
                recommand = '推薦：醫藥衛生學群、生命科學學群、心理與社會學群、教育學群、\n外語學群'
            elif result == 'ENFJ':
                recommand = '推薦：教育學群、心理與社會學群、\n醫藥衛生學群'
            else:
                recommand = '推薦：管理學群、法政學群、外語學群'

            # Update result labels for MBTI
            self.canvas.delete(self.question_text)
            self.result = self.canvas.create_text(100, 270, text=result_text, 
                                                 width=380, fill="black", font=('jf open 粉圓 2.0', 18), anchor="w", justify="left")
            self.recon = self.canvas.create_text(100, 330, text=recommand, 
                                                 width=380, fill="black", font=('jf open 粉圓 2.0', 18), anchor="w", justify="left")
            
            self.next_page_button = tk.Button(self.mbti_frame, text="下一頁", command=self.create_widgets2)
            self.next_page_button_window = self.canvas.create_window(200, 450, window=self.next_page_button)
            self.button_a.destroy()
            self.button_b.destroy()

    def calculate_result(self):
        scoreE = 0
        scoreI = 0
        scoreS = 0
        scoreN = 0
        scoreT = 0
        scoreF = 0
        scoreJ = 0
        scoreP = 0

        for i, answer in enumerate(self.answers):
            if i in [21, 11, 1, 18, 8, 2, 7]:
                if answer == "A":
                    scoreE += 1
                else:
                    scoreI += 1
            elif i in [14, 0, 10, 5, 20, 25, 22]:
                if answer == "A":
                    scoreS += 1
                else:
                    scoreN += 1
            elif i in [23, 19, 4, 26, 17, 6, 12]:
                if answer == "A":
                    scoreF += 1
                else:
                    scoreT += 1
            else:
                if answer == "A":
                    scoreJ += 1
                else:
                    scoreP += 1

        # 判斷MBTI
        result = (
            "E" if scoreE > scoreI else "I") + (
            "S" if scoreS > scoreN else "N") + (
            "T" if scoreT > scoreF else "F") + (
            "J" if scoreJ > scoreP else "P"
        )
            
        self.mbti_result = result
        recommendation = self.generate_recommendation(result)

        return result
    
    def generate_recommendation(self, mbti_result):
        default_recommendation = '推薦：管理學群、法政學群、外語學群'

        recommendations = {
            'ISTJ': '推薦：財經學群、工程學群、管理學群、法政學群',
            "ISFJ": '推薦：醫藥衛生學群、生命科學學群、生物資源學群、社會與心理學群',
            'INFJ': '推薦：社會與心理學群、藝術學群、建築與設計學群',
            'INTJ': '推薦：資訊學群、工程學群、財經學群、法政學群',
            'ISTP': '推薦：資訊學群、工程學群、遊憩與運動學群',
            'ISFP': '推薦：藝術學群、建築與設計學群、外語學群',
            'INFP': '推薦：文史哲學群、藝術學群、社會與心理學群',
            'INTP': '推薦：資訊學群、工程學群、數理化學群',
            'ESTP': '推薦：遊憩與運動學群、管理學群',
            'ESFP': '推薦：大眾傳播學群、藝術學群、遊憩與運動學群',
            'ENFP': '推薦：社會與心理學群、藝術學群',
            'ENTP': '推薦：管理學群、財經學群、法政學群',
            'ESTJ': '推薦：工程學群、財經學群、管理學群',
            'ESFJ': '推薦：醫藥衛生學群、生命科學學群、心理與社會學群、教育學群、外語學群',
            'ENFJ': '推薦：教育學群、心理與社會學群、醫藥衛生學群',
        }

        # Add default recommendation to types not explicitly mentioned
        for mbti_type in ['ISTJ', "ISFJ", 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ENTP', 'ESTP', 'ESFP', 'ENFP', 'ESTJ', 'ESFJ', 'ENFJ']:
            recommendations.setdefault(mbti_type, default_recommendation)


        # Get the recommendation for the given MBTI result
        recommendation = recommendations.get(mbti_result[0])

        return recommendation

if __name__ == "__main__":
    root = tk.Tk()
    app = CollegeRecommendationGUI(root)
    root.mainloop()
