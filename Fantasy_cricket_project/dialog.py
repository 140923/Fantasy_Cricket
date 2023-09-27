


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    import sqlite3
    Mydb = sqlite3.connect('FantasyCricket.db')
    curObj = Mydb.cursor()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 570)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 140, 511, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 200, 451, 231))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.players_list = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.players_list.setObjectName("players_list")
        self.horizontalLayout_2.addWidget(self.players_list)
        spacerItem = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.points_list = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.points_list.setObjectName("points_list")
        self.horizontalLayout_2.addWidget(self.points_list)
        self.calc_score = QtWidgets.QPushButton(Dialog)
        self.calc_score.setGeometry(QtCore.QRect(170, 450, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        self.calc_score.setFont(font)
        self.calc_score.setObjectName("calc_score")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 170, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Teamcombo = QtWidgets.QComboBox(Dialog)
        self.Teamcombo.setGeometry(QtCore.QRect(60, 100, 151, 22))
        self.Teamcombo.setToolTip("")
        self.Teamcombo.setObjectName("Teamcombo")
        self.Matchcombo = QtWidgets.QComboBox(Dialog)
        self.Matchcombo.setGeometry(QtCore.QRect(320, 100, 151, 22))
        self.Matchcombo.setObjectName("Matchcombo")
        self.Matchcombo.addItem("")
        self.Matchcombo.addItem("")
        self.Matchcombo.addItem("")
        self.score = QtWidgets.QLabel(Dialog)
        self.score.setGeometry(QtCore.QRect(190, 510, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setStyleSheet("color: rgb(61, 184, 8);\n"
"border-color: rgb(212, 29, 72);\n"
"border-width:2px;\n"
"border-style:solid;")
        self.score.setAlignment(QtCore.Qt.AlignCenter)
        self.score.setObjectName("score")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(330, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.fill_teamscombo()           
        self.calc_score.clicked.connect(self.calculateScore)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Evaluate the Performance of your Fantasy Team"))
        self.label_2.setText(_translate("Dialog", "Players"))
        self.calc_score.setText(_translate("Dialog", "Calculate Score"))
        self.label_3.setText(_translate("Dialog", "Points"))
        self.Matchcombo.setItemText(0, _translate("Dialog", "Match1"))
        self.Matchcombo.setItemText(1, _translate("Dialog", "Match2"))
        self.Matchcombo.setItemText(2, _translate("Dialog", "Match3"))
        self.score.setText(_translate("Dialog", "0"))
        self.label_5.setText(_translate("Dialog", "Select Team"))
        self.label_6.setText(_translate("Dialog", "Select Match"))

    #The combobox is filled with teamNames
    def fill_teamscombo(self):
        sql="SELECT name FROM teams;"
        try:
            Ui_Dialog.curObj.execute(sql)
            result=Ui_Dialog.curObj.fetchall()
            for i in result:
                self.Teamcombo.addItem(i[0])
        except:
            pass
        
    #To know which match is selected
    def get_match(self):
        matchName=self.Matchcombo.currentText()
        if matchName=="Match1":
            matchName="match"
        return matchName

    #The individual score with player name and total score of team is displayed    
    def calculateScore(self):
        teamName=self.Teamcombo.currentText()
        self.players_list.clear()
        self.points_list.clear()
        sql="SELECT player FROM teams WHERE name='"+teamName+"';"
        try:
            Ui_Dialog.curObj.execute(sql)
            result=Ui_Dialog.curObj.fetchone()
            players=result[0].split(",")
            teamScore=0
            for player in players:
                total_pts=0
                total_pts=self.batScore(player)+self.bwlScore(player)+self.fieldScore(player)
                teamScore+=total_pts
                self.players_list.addItem(player)
                self.points_list.addItem(str(total_pts))
            self.score.setText(str(teamScore))
        except:
            pass

    #The batting score is calculated   
    def batScore(self,player):
        match=self.get_match()
        bat_score=0
        sql="SELECT Scored,Faced,Fours,Sixes FROM '"+match+"'WHERE Player='"+player+"';"
        try:
            Ui_Dialog.curObj.execute(sql)
            batting_stats=Ui_Dialog.curObj.fetchone()
            scored=int(batting_stats[0])
            faced=int(batting_stats[1])
            fours=int(batting_stats[2])
            sixes=int(batting_stats[3])
            if faced:
                stk_rate=(scored/faced)*100
            else:
                stk_rate=0
            if scored>=100:         
                bat_score+=10            
            if scored>=50:
                bat_score+=5
            if 80<=stk_rate<=100:
                bat_score+=2
            if stk_rate>100:
                bat_score+=4
            bat_score+=fours
            bat_score+=(sixes*2)
            return bat_score
        except:
            pass

    #The bowling score is calculated
    def bwlScore(self,player):
        match=self.get_match()
        bwl_score=0
        sql="SELECT Bowled,Maiden,Given,Wkts FROM '"+match+"'WHERE Player='"+player+"';"
        try:
            Ui_Dialog.curObj.execute(sql)
            bowling_stats=Ui_Dialog.curObj.fetchone()
            bowled=int(bowling_stats[0])
            maiden=int(bowling_stats[1])
            given=int(bowling_stats[2])
            wkts=int(bowling_stats[3])
            if bowled:
                eco_rate=given/(bowled//6)
            else:
                eco_rate=0
            if 3.5<=eco_rate<=4.5:             
                bwl_score+=4
            if 2<=eco_rate<3.5:
                bwl_score+=7
            if 0<eco_rate<2:
                bwl_score+=10
            if wkts>=5:
                bwl_score+=10
            if 3<=wkts<=4:
                bwl_score+=5
            bwl_score+=(wkts*10)
            return bwl_score
        except:
            pass

    #The fielding score is calculated
    def fieldScore(self,player):
        match=self.get_match()
        field_score=0
        sql="SELECT Catches,Stumping,RO FROM '"+match+"'WHERE Player='"+player+"';"
        try:
            Ui_Dialog.curObj.execute(sql)
            fielding_stats=Ui_Dialog.curObj.fetchone()
            catches=int(fielding_stats[0])
            stumping=int(fielding_stats[1])
            ro=int(fielding_stats[2])
            field_score+=(catches*10)        
            field_score+=(stumping*10)
            field_score+=(ro*10)
            return field_score
        except:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())