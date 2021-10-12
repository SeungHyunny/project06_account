import random
import wx
from home import home_CRUD

class PieChartPanel(wx.Panel):
        
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent )
        
    def SetData(self,data):
        self.data = data 
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        rows = home_CRUD.selectAll()
        totalRe = 0
        totalEx = 0
        for row in rows:
            if row[2] == '수입':
                totalRe += int(row[4])
            elif row[2] == '지출':
                totalEx += int(row[4])
        data = [totalRe,totalEx]
        # 중요 - 새로이 그린 내용으로 갱신 
        self.Refresh() #중요 
        
    def SetData2(self,data):
        self.data = data 
        self.Bind(wx.EVT_PAINT,self.OnPaint)
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
        # 중요 - 새로이 그린 내용으로 갱신 
        self.Refresh() #중요 
        
    def SetData3(self,data):
        self.data = data 
        self.Bind(wx.EVT_PAINT,self.OnPaint)
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
        data = [총급여,총용돈,총주거비,총식비,총교통비,총생필품,총취미,총기타]
        self.Refresh()

    def OnPaint(self,event):
        self.dc = wx.PaintDC(self)
        self.brush = wx.Brush("#ffffff") #칠하는 용도 
        self.dc.SetBackground(self.brush)
        self.dc.Clear()
        font = wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.dc.SetFont(font)
        total =0
        color = {}
        
        # 데이타 총량 산정
        for key in self.data:
            total += self.data[key]
        
        # 전체총량에 차지하는 각 데이타를 360도  각도로 환산하고, 파이챠트에 구분표시할 색상을 임의로 생성 
        for key in self.data:
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color[key] = (r,g,b)
            self.data[key] = int(self.data[key]/total*360)
        
        
        # 아래 글씨를 쓰기 위한 색상 지정  
        self.brush.SetColour(wx.Colour(0,0,0,1))
        
        # 브러쉬 지정 
        self.dc.SetBrush(self.brush)
        self.dc.DrawText("pie chart",400,17)
        
        #DrawEllipticArc(X, Y, WX, WY, ST, LT)
        # 원의 기준은 좌측 상단점(X,Y)
        # 가로폭, 세로폭(WX,WY)
        # 호의 시작 각도,끝나는 각도 (ST,LT)
        sum =0
        step= 60
        for key in self.data:
            # if len(str(self.data[key]))<=1:
            #     self.dc.DrawEllipticArc(50, 20, 300, 300, 0, 360)
            if self.data[key] != 0:
                r = color.get(key)[0]
                g = color.get(key)[1]
                b = color.get(key)[2]
                self.brush.SetColour(wx.Colour(r,g,b,1))
                self.dc.SetBrush(self.brush)
                self.dc.DrawEllipticArc(50, 20, 300, 300, sum, sum+self.data[key])
                self.dc.DrawRectangle(400, step, 50, 50)
                self.dc.DrawText(key,470,step)
                sum +=  self.data[key]
                step += 35
            
            else : pass
