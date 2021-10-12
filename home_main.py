# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import sqlite3
import wx
import wx.xrc
from home import home_CRUD
from home.pie import PieChartPanel
import matplotlib.pyplot as plt


###########################################################################
## Class MyFrame1
###########################################################################
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"가계부", pos = wx.DefaultPosition, size = wx.Size( 1160,740 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour(wx.Colour(255,255,204))
        
        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"No", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        gbSizer2.Add( self.m_staticText10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txt_no = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        gbSizer2.Add( self.txt_no, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"날짜", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        gbSizer2.Add( self.m_staticText11, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txt_date = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_date, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"분류", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        gbSizer2.Add( self.m_staticText12, wx.GBPosition( 2, 0 ), wx.GBSpan( 2, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.radio_re = wx.RadioButton( self, wx.ID_ANY, u"수입", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        gbSizer2.Add( self.radio_re, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.radio_ex = wx.RadioButton( self, wx.ID_ANY, u"지출", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.radio_ex, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"항목", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        gbSizer2.Add( self.m_staticText13, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txt_contents = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_contents, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"금액", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        gbSizer2.Add( self.m_staticText14, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        com_titleChoices = ['급여','용돈','주거비','식비','교통비','생필품','취미','기타']
        self.com_title = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, com_titleChoices, 0 )
        gbSizer2.Add( self.com_title, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"내용", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        gbSizer2.Add( self.m_staticText15, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txt_price = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_price, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txt_show = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,200 ), wx.LC_REPORT|wx.BORDER_SUNKEN )
        self.txt_show.InsertColumn(0, 'No')
        self.txt_show.InsertColumn(1, '날짜')
        self.txt_show.InsertColumn(2, '분류')
        self.txt_show.InsertColumn(3, '항목')
        self.txt_show.InsertColumn(4, '금액')
        self.txt_show.InsertColumn(5, '내용')
        gbSizer2.Add( self.txt_show, wx.GBPosition( 0, 2 ), wx.GBSpan( 7, 10 ), wx.ALL|wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"총수입", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        bSizer6.Add( self.m_staticText16, 0, wx.ALL, 5 )
        
        self.txt_totalRe = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txt_totalRe, 0, wx.ALL, 5 )
        
        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"총지출", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        bSizer6.Add( self.m_staticText17, 0, wx.ALL, 5 )
        
        self.txt_totalEx = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txt_totalEx, 0, wx.ALL, 5 )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"INSERT", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button1, 0, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"UPDATE", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button2, 0, wx.ALL, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"DELETE", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"FIND", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button4, 0, wx.ALL, 5 )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"ALLDATA", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button5, 0, wx.ALL, 5 )
        
        self.m_button6 = wx.Button( self, wx.ID_ANY, u"CLEAR", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button6, 0, wx.ALL, 5 )
        
        gbSizer2.Add( bSizer6, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"기간", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        gbSizer2.Add( self.m_staticText16, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txt_dateF = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_dateF, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        gbSizer2.Add( self.m_staticText17, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.txt_dateL = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.txt_dateL, wx.GBPosition( 8, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.btn4 = wx.Button( self, wx.ID_ANY, u"그래프보기", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.btn4, wx.GBPosition( 8, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.btn1 = wx.Button( self, wx.ID_ANY, u"수입/지출 차트", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.btn1, wx.GBPosition( 8, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.btn2 = wx.Button( self, wx.ID_ANY, u"항목별 차트", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.btn2, wx.GBPosition( 8, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.btn3 = wx.Button( self, wx.ID_ANY, u"항목별 추이", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.btn3, wx.GBPosition( 8, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel = PieChartPanel(self)
        # self.panel = PieChartPanel1(self)
        self.panel.SetBackgroundColour(wx.Colour(255,255,153))
        
        gbSizer2.Add( self.panel, wx.GBPosition( 9, 0 ), wx.GBSpan( 20, 7 ), wx.EXPAND |wx.ALL, 5 )
        
        self.txt_Area = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,200 ), wx.HSCROLL|wx.TE_MULTILINE )
        self.txt_Area.SetBackgroundColour(wx.Colour(255,255,153))
        gbSizer2.Add( self.txt_Area, wx.GBPosition( 9, 7 ), wx.GBSpan( 20, 4 ), wx.EXPAND |wx.ALL, 5 )
        
        self.SetSizer( gbSizer2 )
        self.Layout()
        self.m_menubar2 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menubar2.Append( self.m_menu1, u"User" ) 
        
        self.m_menu2 = wx.Menu()
        self.m_menubar2.Append( self.m_menu2, u"Quit" ) 
        
        self.SetMenuBar( self.m_menubar2 )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnInsert )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnUpdate )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnDelete )
        self.m_button4.Bind( wx.EVT_BUTTON, self.OnFind )
        self.m_button5.Bind( wx.EVT_BUTTON, self.OnAlldata )
        self.m_button6.Bind( wx.EVT_BUTTON, self.OnClear )
        self.btn1.Bind( wx.EVT_BUTTON, self.Ongraph )
        self.btn2.Bind( wx.EVT_BUTTON, self.OnChart )
        self.btn3.Bind( wx.EVT_BUTTON, self.OnChart2 )
        self.btn4.Bind( wx.EVT_BUTTON, self.OnChart3 )
        self.txt_show.Bind( wx.EVT_LIST_ITEM_SELECTED, self.Onhandle )

    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnInsert( self, event ):
        date=self.txt_date.GetValue()
        if(self.radio_re.GetValue()):
            section='수입'
        elif(self.radio_ex.GetValue()):
            section='지출'
        title=self.com_title.GetValue()
        price=self.txt_price.GetValue()
        contents=self.txt_contents.GetValue()
        try:
            home_CRUD.insertData(date, section, title, price, contents)
            self.txt_Area.AppendText("입력성공!\n")
        except:
            print('예외발생')
            self.txt_Area.AppendText("예외발생\n")
        finally:
            print('입력성공')
        event.Skip()
    
    def OnUpdate( self, event ):
        date=self.txt_date.GetValue()
        if(self.radio_re.GetValue()):
            section='수입'
        elif(self.radio_ex.GetValue()):
            section='지출'
        title=self.com_title.GetValue()
        price=self.txt_price.GetValue()
        contents=self.txt_contents.GetValue()
        no=self.txt_no.GetValue()
        try:
            home_CRUD.update((date,section,title,price,contents,no))
            self.txt_Area.AppendText("수정성공!\n")
        except:
            print('예외발생!')
            self.txt_Area.AppendText("예외발생\n")
        finally:
            print('수정성공!')
        event.Skip()
    
    def OnDelete( self, event ):
        no=self.txt_no.GetValue()
        try:
            home_CRUD.delete(no)
            self.txt_Area.AppendText("삭제성공!\n")
        except:
            print('예외발생!')
            self.txt_Area.AppendText("예외발생\n")
        finally:
            print('삭제성공!')
        
        event.Skip()
    
    def OnFind( self, event ):
        date = self.txt_date.GetValue()
        rows = home_CRUD.select(date)
        key=0
        self.txt_show.DeleteAllItems()
        for data in rows:
            self.txt_show.InsertStringItem(key,str(data[0]))
            self.txt_show.SetStringItem(key,1,data[1])
            self.txt_show.SetStringItem(key,2,data[2])
            self.txt_show.SetStringItem(key,3,data[3])
            self.txt_show.SetStringItem(key,4,str(data[4]))
            self.txt_show.SetStringItem(key,5,data[5])
            key+=1
        self.txt_Area.AppendText("날짜로 데이터검색하기\n")
        event.Skip() 
    
    def OnAlldata( self, event ):
        self.txt_show.DeleteAllItems()
        rows=home_CRUD.selectAll()
        key=0
        totalRe = 0
        totalEx = 0
        for data in rows:
            self.txt_show.InsertStringItem(key,str(data[0]))
            self.txt_show.SetStringItem(key,1,data[1])
            self.txt_show.SetStringItem(key,2,data[2])
            self.txt_show.SetStringItem(key,3,data[3])
            self.txt_show.SetStringItem(key,4,str(data[4]))
            self.txt_show.SetStringItem(key,5,data[5])
            key+=1
            
        for data in rows:    
            if data[2] == '수입':
                totalRe += int(data[4])
            elif data[2] == '지출':
                totalEx += int(data[4])
            self.txt_totalRe.SetValue(str(totalRe))
            self.txt_totalEx.SetValue(str(totalEx))
        self.txt_Area.AppendText("전체데이터 보기\n")
        event.Skip()
    
    def OnClear( self, event ):
        self.txt_no.Clear()
        self.txt_date.Clear()
        self.radio_ex.SetValue(int(0))
        self.radio_re.SetValue(int(0))
        self.com_title.SetValue('')
        self.txt_price.Clear()
        self.txt_contents.Clear()
        self.txt_show.DeleteAllItems()
        self.txt_totalRe.Clear()
        self.txt_totalEx.Clear()
        self.txt_dateF.Clear()
        self.txt_dateL.Clear()
        self.panel.ClearBackground()
        self.txt_Area.AppendText("화면 지우기\n")
        event.Skip()
        
    def Onhandle( self, event ):
        num = event.GetIndex()
        no =self.txt_show.GetItem(num, col=0).GetText()
        date =self.txt_show.GetItem(num, col=1).GetText()
        section =self.txt_show.GetItem(num, col=2).GetText()
        title =self.txt_show.GetItem(num, col=3).GetText()
        price =self.txt_show.GetItem(num, col=4).GetText()
        contents =self.txt_show.GetItem(num, col=5).GetText()
        self.txt_no.SetValue(no)
        self.txt_date.SetValue(date)
        if section == '수입':
            self.radio_re.SetValue(1)
        else:
            section == '지출'
            self.radio_ex.SetValue(1)
        self.com_title.SetValue(title)
        self.txt_price.SetValue(price)
        self.txt_contents.SetValue(contents)
        self.txt_Area.AppendText("데이터 선택\n")
        event.Skip()  

    def Ongraph(self,event):
        rows = home_CRUD.selectAll()
        totalRe = 0
        totalEx = 0
        for row in rows:
            if row[2] == '수입':
                totalRe += int(row[4])
            elif row[2] == '지출':
                totalEx += int(row[4])
        self.panel.SetData({"수입":totalRe,"지출":totalEx})
        event.Skip()
        
    def OnChart(self,event):
        rows = home_CRUD.selectAll()
        총급여 = 0
        총용돈 = 0
        총주거비 = 0
        총식비 = 0
        총교통비 = 0
        총생필품 = 0
        총취미 = 0
        총기타 = 0
        for row in rows:
            if row[3] =='급여':
                총급여 += int(row[4])
            elif row[3] == '용돈':
                총용돈 += int(row[4])
            elif row[3] == '주거비':
                총주거비 += int(row[4])
            elif row[3] == '식비':
                총식비 += int(row[4])
            elif row[3] == '교통비':
                총교통비 += int(row[4])
            elif row[3] == '생필품':
                총생필품 += int(row[4])
            elif row[3] == '취미':
                총취미 += int(row[4])
            elif row[3] == '기타':
                총기타 += int(row[4])
        data = [총급여,총용돈,총주거비,총식비,총교통비,총생필품,총취미,총기타]
        labels = 'Salary','Allowance','Housing','Food','Traffic','Daily','Hobby','etc'
        colors = ['red','orange','yellow','green','blue','skyblue','purple','grey']
        plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90)
        plt.title('Pie chart of title')
        plt.show()
        event.Skip()
        
    def OnChart2(self,event):
        rows = home_CRUD.selectAll()
        총급여 = 0
        총용돈 = 0
        총주거비 = 0
        총식비 = 0
        총교통비 = 0
        총생필품 = 0
        총취미 = 0
        총기타 = 0
        for row in rows:
            if row[3] =='급여':
                총급여 += int(row[4])
            elif row[3] == '용돈':
                총용돈 += int(row[4])
            elif row[3] == '주거비':
                총주거비 += int(row[4])
            elif row[3] == '식비':
                총식비 += int(row[4])
            elif row[3] == '교통비':
                총교통비 += int(row[4])
            elif row[3] == '생필품':
                총생필품 += int(row[4])
            elif row[3] == '취미':
                총취미 += int(row[4])
            elif row[3] == '기타':
                총기타 += int(row[4])
        plt.title("Title bar graph")
        colors = ['red','orange','yellow','green','blue','skyblue','purple','grey']
        x_data=['Sal','All','Hou','Food','Tra','Dai','Hob','etc']
        y_data=[총급여,총용돈,총주거비,총식비,총교통비,총생필품,총취미,총기타]
        plt.bar(x_data,y_data, color=colors)
        plt.xlabel('Title')
        plt.ylabel('price')
        plt.show()
        self.txt_Area.AppendText("항목별 추이 확인\n")
        event.Skip()
    
    def OnChart3(self,event):
        dateF=self.txt_dateF.GetValue()
        dateL=self.txt_dateL.GetValue()
        rows = home_CRUD.selectDate(dateF, dateL)
        총급여 = 0
        총용돈 = 0
        총주거비 = 0
        총식비 = 0
        총교통비 = 0
        총생필품 = 0
        총취미 = 0
        총기타 = 0
        for row in rows:
            if row[3] =='급여':
                총급여 += int(row[4])
            elif row[3] == '용돈':
                총용돈 += int(row[4])
            elif row[3] == '주거비':
                총주거비 += int(row[4])
            elif row[3] == '식비':
                총식비 += int(row[4])
            elif row[3] == '교통비':
                총교통비 += int(row[4])
            elif row[3] == '생필품':
                총생필품 += int(row[4])
            elif row[3] == '취미':
                총취미 += int(row[4])
            elif row[3] == '기타':
                총기타 += int(row[4]) 
        self.panel.SetData({"급여":총급여,"용돈":총용돈,"주거비":총주거비,"식비":총식비,"교통비":총교통비,"생필품":총생필품,"취미":총취미,"기타":총기타})
        self.txt_Area.AppendText("해당 기간 항목차트 확인\n")
        event.Skip()

#######메인#########################################
if __name__ == '__main__':
    app=wx.App()
    frame = MyFrame1(parent=None)
    frame.Show()
    app.MainLoop()
    