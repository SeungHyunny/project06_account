'''
Created on 2021. 7. 27.
@author: pc374
'''
from home import home_CRUD


if __name__ == '__main__':
    
    #테이블만들기
    # home_CRUD.createTable()
    
    # # #자료 한개 입력하기
    # home_CRUD.insertData('2021-07-27','수입','급여','20000','월급')
    
    #
    # # #여러 자료를 동시에 입력하기
    # t_data = (
    #     ('ygs','유관순','1234','삼월하늘'),
    #     ('lss','이순신','1234','한산섬'),
    #     ('ysd','윤선도','1234','지국총')
    # )
    # sqliteCRUD.insertManyData(t_data)
    #
    # #전체data불러오기
    # sqliteCRUD.selectAll()
    #
    # #해당keydata불러오기
    # sqliteCRUD.select('hgd')
    #
    # #update
    # sqliteCRUD.update(('홍길동','5678','동번쩍 서번쩍','hgd'))
    # sqliteCRUD.select('hgd')
    #
    # #delete
    home_CRUD.delete(1)
    # sqliteCRUD.selectAll()